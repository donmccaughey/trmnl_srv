import requests

from datetime import datetime, timezone


LAT, LON = 37.7725, -122.3933


class Weather:
    def __init__(self, lat: float = LAT, lon: float = LON):
        self.headers = {
            'User-Agent': 'trmnl_srv (don@donm.cc)',
            'Accept': 'application/ld+json',
        }

        self.lat = lat
        self.lon = lon
        self.forecast_url = ''
        self.period_name = ''
        self.detailed_forecast = ''
        self.updated = datetime.now(timezone.utc)

    def get_points(self) -> bool:
        url = f'https://api.weather.gov/points/{self.lat},{self.lon}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            json_body = response.json()
            self.forecast_url = json_body['forecast']
            return True
        else:
            print(response.status_code)
            return False

    def get_forecast(self):
        response = requests.get(self.forecast_url, headers=self.headers)
        if response.status_code == 200:
            json_body = response.json()
            first_period = json_body['periods'][0]
            self.period_name = first_period['name']
            self.detailed_forecast = first_period['detailedForecast']
            self.updated = datetime.now(timezone.utc)
        else:
            print(response.status_code)
