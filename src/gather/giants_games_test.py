from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from .giants_games import GiantsGame


pacific_time = ZoneInfo('America/Los_Angeles')


def test_get_games():
    games = GiantsGame.get_games()
    assert len(games) == 101


def test_read_schedule():
    schedule = GiantsGame.read_schedule()
    assert isinstance(schedule, list)


def test_empty_time():
    schedule_json = [
        {
            'date': '2025-02-23',
            'time': '',
            'opponent': 'Cincinnati Reds',
        }
    ]
    games = GiantsGame.parse_games(schedule_json)
    assert len(games) == 1
    assert games[0].date == date(2025, 2, 23)
    assert games[0].time is None
    assert games[0].opponent == 'Cincinnati Reds'


def test_mountain_time():
    schedule_json = [
        {
            'date': '2025-02-12',
            'time': '1:05 pm MST',
            'opponent': "Pitchers' and Catchers' First Workout",
        }
    ]
    games = GiantsGame.parse_games(schedule_json)
    assert len(games) == 1
    assert games[0].date == date(2025, 2, 12)
    assert games[0].time is None
    assert games[0].opponent == "Pitchers' and Catchers' First Workout"


def test_pacific_time():
    schedule_json = [
        {
            'date': '2025-06-04',
            'time': '6:45 pm PDT',
            'opponent': 'San Diego Padres',
        }
    ]
    games = GiantsGame.parse_games(schedule_json)
    assert len(games) == 1
    assert games[0].date == date(2025, 6, 4)
    assert games[0].time == time(18, 45)
    assert games[0].opponent == 'San Diego Padres'


def test_is_today():
    schedule_json = [
        {
            'date': '2025-06-05',
            'time': '12:45 pm PDT',
            'opponent': 'San Diego Padres',
        },
        {
            'date': '2025-06-06',
            'time': '7:15 pm PDT',
            'opponent': 'Atlanta Braves',
        }
    ]
    now = datetime(
        2025, 6, 6,
        12, 0, tzinfo=pacific_time
    )

    games = GiantsGame.parse_games(schedule_json)
    assert len(games) == 2

    assert games[0].opponent == 'San Diego Padres'
    assert not games[0].is_today(now)

    assert games[1].opponent == 'Atlanta Braves'
    assert games[1].is_today(now)
