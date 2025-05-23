from __future__ import annotations

import json

from datetime import date, datetime, time
from importlib import resources
from typing import Any
from zoneinfo import ZoneInfo


class GiantsGame:
    pacific_time = ZoneInfo('America/Los_Angeles')

    def __init__(self, game_date: date, game_time: time | None, opponent: str):
        self.date = game_date
        self.time = game_time
        self.opponent = opponent

    @classmethod
    def get_games(cls) -> list[GiantsGame]:
        schedule = cls.read_schedule()
        return cls.parse_games(schedule)

    @staticmethod
    def read_schedule() -> list[dict[str, Any]]:
        with resources.open_binary(__package__, 'giants-schedule.json') as f:
            return json.load(f)

    @classmethod
    def parse_games(cls, schedule_json: list[dict[str, Any]]) -> list[GiantsGame]:
        return [cls.__from_json(game_json) for game_json in schedule_json]

    def is_today(self, now: datetime) -> bool:
        now = now.astimezone(self.pacific_time)
        return now.date() == self.date

    @staticmethod
    def __from_json(object: dict[str, Any]) -> GiantsGame:
        dt = datetime.strptime(object['date'], '%Y-%m-%d')
        date_only = dt.date()

        time_str = object['time']
        if time_str.endswith('PDT'):
            dt = datetime.strptime(time_str[:-4], '%I:%M %p')
            time_only = dt.time()
        else:
            time_only = None
        return GiantsGame(date_only, time_only, object['opponent'])
