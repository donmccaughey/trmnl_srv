from serialize import JSONDict
from textwrap import wrap

from .screen import Screen


def write_log_message(content: JSONDict, screen: Screen):
    log = content.get('log', {})
    volts = f"{log['volts']:.1f} v" if 'volts' in log else None
    if 'message' in log:
        message = f"Log {log.get('id')}: {log.get('message')} ({volts})"
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
    elif volts:
        screen.write_reverse(screen.cols - 1 - 1, screen.rows - 1, volts)
