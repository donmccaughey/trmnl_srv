from common.serialize import JSONDict
from datetime import time

from .screen import Screen


def write_giants_games_today(content: JSONDict, screen: Screen):
    if content['giants_games_today']:
        game_times = [
            time.fromisoformat(game_time).strftime('%I:%M %p')
            for game_time in content['giants_games_today']
        ]
        when = ','.join(game_times)
        message = f'Giants game today at {when}.'
        screen.write(1, 10, message)
    else:
        screen.write(1, 10, 'No Giants game today.')
