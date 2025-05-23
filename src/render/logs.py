import json

from datetime import datetime, timedelta, timezone
from pathlib import Path
from textwrap import wrap

from .screen import Screen


SKIPPED_MESSAGES = [
    'Failed to resolve hostname after 5 attempts, continuing...',
]


def is_log_file(path: Path) -> bool:
    return (
        path.is_file()
        and path.suffix == '.json'
    )


def list_log_files(web_root: Path) -> list[Path]:
    logs_dir = web_root / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)
    return [
        path for path in sorted(logs_dir.iterdir())
        if is_log_file(path)
    ]


def write_log_message(log_file: Path, screen: Screen, skip_old: bool = True):
    with open(log_file) as f:
        log_json = json.load(f)

    creation_timestamp = log_json['creation_timestamp']
    creation_utc = datetime.fromtimestamp(
        creation_timestamp, tz=timezone.utc
    )
    now_utc = datetime.now(timezone.utc)

    if skip_old and (now_utc - creation_utc > timedelta(hours=1)):
        return

    device_status_stamp = log_json.get('device_status_stamp')
    if device_status_stamp:
        battery_voltage = device_status_stamp.get('battery_voltage')
        log_volts = f'{battery_voltage:.1f} v'
    else:
        log_volts = ''

    if log_json['log_message'] in SKIPPED_MESSAGES:
        if log_volts:
            screen.write_reverse(screen.cols - 1 - 1, screen.rows - 1, log_volts)
        return

    log_id = log_json['log_id']
    log_message = log_json['log_message']
    message = f'Log {log_id}: {log_message} ({log_volts})'
    if len(message) > screen.cols - 2:
        message_lines = wrap(
            message,
            width=screen.cols - 2,
            break_long_words=True,
            break_on_hyphens=True,
            fix_sentence_endings=True,
        )
        row = screen.rows - len(message_lines)
        for j, line in enumerate(message_lines):
            screen.write(1, row + j, line)
    else:
        screen.write(1, screen.rows - 1, message)
