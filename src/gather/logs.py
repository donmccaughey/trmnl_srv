import json

from common.logs import LogStorage
from common.serialize import JSONDict
from datetime import datetime, timedelta, timezone


SKIP_MESSAGES = [
    'Failed to resolve hostname after 5 attempts, continuing...',
]


def get_log(trmnl_logs: LogStorage, skip_old: bool = True) -> JSONDict:
    log = {}

    log_files = trmnl_logs.files()
    if not log_files:
        return log

    most_recent = log_files[-1]
    with open(most_recent) as f:
        log_json = json.load(f)

    if is_old(log_json.get('creation_timestamp', 0)) and skip_old:
        return log

    log['created'] = log_json.get('created')

    device_status_stamp = log_json.get('device_status_stamp', {})
    log['volts'] = device_status_stamp.get('battery_voltage')

    if log_json.get('log_message') in SKIP_MESSAGES:
        return log

    log['id'] = log_json.get('log_id')
    log['message'] = log_json.get('log_message')

    return log


def is_old(
        timestamp: int,
        now_utc: datetime = datetime.now(timezone.utc)
) -> bool:
    timestamp_utc = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return now_utc - timestamp_utc > timedelta(hours=1)
