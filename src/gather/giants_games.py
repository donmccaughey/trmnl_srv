from __future__ import annotations

import json

from common.serialize import Decodable, JSONDict, JSONList
from datetime import date, datetime, time
from importlib import resources
from typing import Self
from zoneinfo import ZoneInfo


class GiantsGame(Decodable):
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
        return [cls.decode(game_json) for game_json in schedule_json]

    def is_today(self, now: datetime) -> bool:
        now = now.astimezone(self.pacific_time)
        return now.date() == self.date

    @classmethod
    def decode(cls, encoded: JSONDict) -> Self:
        dt = datetime.strptime(encoded['date'], '%Y-%m-%d')
        date_only = dt.date()

        time_str = encoded['time']
        if time_str.endswith('PDT'):
            dt = datetime.strptime(time_str[:-4], '%I:%M %p')
            time_only = dt.time()
        else:
            time_only = None

        return cls(date_only, time_only, encoded['opponent'])
