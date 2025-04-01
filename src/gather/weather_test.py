import pytest

from .weather import Weather


def test_weather_init():
    weather = Weather()

    assert 'User-Agent' in weather.headers
    assert 'Accept' in weather.headers

    assert weather.lat
    assert weather.lon
    assert weather.forecast_url == ''
    assert weather.period_name == ''
    assert weather.detailed_forecast == ''
