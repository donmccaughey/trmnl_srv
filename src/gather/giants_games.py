from __future__ import annotations

import json

from datetime import date, datetime, time
from importlib import resources
from serialize import JSONDict, JSONList
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
    def read_schedule() -> JSONList:
        filename = 'giants-schedule.json'
        with resources.files().joinpath(filename).open('rb') as f:
            return json.load(f)

    @classmethod
    def parse_games(cls, schedule_json: JSONList) -> list[GiantsGame]:
        return [cls.__from_json(game_json) for game_json in schedule_json]

    def is_today(self, now: datetime) -> bool:
        now = now.astimezone(self.pacific_time)
        return now.date() == self.date

    @staticmethod
    def __from_json(game_json: JSONDict) -> GiantsGame:
        dt = datetime.strptime(game_json['date'], '%Y-%m-%d')
        date_only = dt.date()

        time_str = game_json['time']
        if time_str.endswith('PDT'):
            dt = datetime.strptime(time_str[:-4], '%I:%M %p')
            time_only = dt.time()
        else:
            time_only = None
        return GiantsGame(date_only, time_only, game_json['opponent'])
