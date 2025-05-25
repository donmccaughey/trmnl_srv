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
        self.error = None

        self.points_response = {}
        self.points_url = f'https://api.weather.gov/points/{lat},{lon}'

        self.forecast_response = {}
        self.forecast_url = ''

        self.forecast_hourly_response = {}
        self.forecast_hourly_url = ''

        self.period_name = ''
        self.detailed_forecast = ''

        self.updated = datetime.now(timezone.utc)

    def get_points(self) -> bool:
        response = requests.get(self.points_url, headers=self.headers)
        if response.status_code == 200:
            self.points_response = response.json()
            self.forecast_url = self.points_response['forecast']
            self.forecast_hourly_url = self.points_response['forecastHourly']
            return True
        else:
            try:
                message = response.json()
            except requests.exceptions.JSONDecodeError:
                message = response.text or None

            self.error = {
                'timestamp': self.updated.isoformat(sep=' ', timespec='seconds'),
                'url': self.points_url,
                'status_code': response.status_code,
                'reason': response.reason,
                'message': message,
            }
            return False

    def get_forecast(self):
        response = requests.get(self.forecast_url, headers=self.headers)
        if response.status_code == 200:
            self.forecast_response = response.json()
            first_period = self.forecast_response['periods'][0]
            self.period_name = first_period['name']
            self.detailed_forecast = first_period['detailedForecast']
            self.updated = datetime.now(timezone.utc)
            return True
        else:
            try:
                message = response.json()
            except requests.exceptions.JSONDecodeError:
                message = response.text or '(no message)'

            self.error = {
                'timestamp': self.updated.isoformat(sep=' ', timespec='seconds'),
                'url': self.forecast_url,
                'status_code': response.status_code,
                'reason': response.reason,
                'message': message,
            }
            return False

    def get_forecast_hourly(self):
        response = requests.get(self.forecast_hourly_url, headers=self.headers)
        if response.status_code == 200:
            self.forecast_hourly_response = response.json()
            self.updated = datetime.now(timezone.utc)
            return True
        else:
            try:
                message = response.json()
            except requests.exceptions.JSONDecodeError:
                message = response.text or '(no message)'

            self.error = {
                'timestamp': self.updated.isoformat(sep=' ', timespec='seconds'),
                'url': self.forecast_url,
                'status_code': response.status_code,
                'reason': response.reason,
                'message': message,
            }
            return False
