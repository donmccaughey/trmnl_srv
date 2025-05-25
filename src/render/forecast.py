from serialize import JSONDict
from textwrap import wrap

from .screen import Screen


def write_forecast(content: JSONDict, screen: Screen):
    if 'error' in content['forecast']:
        screen.write(1, 4, 'Weather:')

        status_code = content['forecast']['error']['status_code']
        reason = content['forecast']['error']['reason']
        screen.write(1, 5, f'    {status_code} {reason}')
    else:
        period = content['forecast']['period_name']
        forecast_title = f'Weather {period}:'
        screen.write(1, 4, forecast_title)

        details = content['forecast']['detailed_forecast']
        detail_lines = wrap(
            details,
            width=screen.cols - 2,
            initial_indent='    ',
            break_long_words=True,
            break_on_hyphens=True,
            fix_sentence_endings=True,
        )
        row = 5
        for j, line in enumerate(detail_lines):
            screen.write(1, row + j, line)
