import requests

from datetime import datetime, timezone

from serialize import JSONDict

class Five11:
    def __init__(self, api_key: str):
        self.headers = {
            'User-Agent': 'trmnl_srv (don@donm.cc)',
            'Accept': 'application/json',
        }

        self.api_key = api_key
        self.agency = 'SF'  # San Francisco MTA
        self.stop_code = 17166  # T Third, 4th & King, northbound
        self.stop_name = '4th and King'
        self.error = None

        self.stop_monitoring_response = {}
        self.stop_monitoring_url = f'http://api.511.org/transit/StopMonitoring'

        self.expected_arrival_times: list[datetime] = []

        self.updated = datetime.now(timezone.utc)

    @property
    def params(self) -> dict[str, str | int]:
        return {
            'api_key': self.api_key,
            'agency': self.agency,
            'stopcode': self.stop_code,
        }

    def get_stop_monitoring(self) -> bool:
        response = requests.get(
            self.stop_monitoring_url, headers=self.headers, params=self.params,
        )
        if response.status_code == 200:
            response.encoding = 'utf-8-sig'
            self.stop_monitoring_response = response.json()
            if service_delivery := self.stop_monitoring_response.get('ServiceDelivery'):
                if stop_monitoring_delivery := service_delivery.get('StopMonitoringDelivery'):
                    if monitored_stop_visit := stop_monitoring_delivery.get('MonitoredStopVisit'):
                        for visit in monitored_stop_visit:
                            if arrival_time := self._get_expected_arrival_time(visit):
                                self.expected_arrival_times.append(arrival_time)
            return True
        else:
            try:
                message = response.json()
            except requests.exceptions.JSONDecodeError:
                message = response.text or None

            self.error = {
                'timestamp': self.updated.isoformat(sep=' ', timespec='seconds'),
                'url': self.stop_monitoring_url,
                'status_code': response.status_code,
                'reason': response.reason,
                'message': message,
            }
            return False

    @staticmethod
    def _get_expected_arrival_times(stop_monitoring_response: JSONDict) -> list[datetime]:
        expected_arrival_times = []

        if service_delivery := stop_monitoring_response.get('ServiceDelivery'):
            if stop_monitoring_delivery := service_delivery.get('StopMonitoringDelivery'):
                if monitored_stop_visit := stop_monitoring_delivery.get('MonitoredStopVisit'):
                    for visit in monitored_stop_visit:
                        if arrival_time := Five11._get_expected_arrival_time(visit):
                            expected_arrival_times.append(arrival_time)

        return expected_arrival_times

    @staticmethod
    def _get_expected_arrival_time(monitored_stop_visit: JSONDict) -> datetime | None:
        if monitored_vehicle_journey := monitored_stop_visit.get('MonitoredVehicleJourney'):
            if monitored_call := monitored_vehicle_journey.get('MonitoredCall'):
                if expected_arrival_time := monitored_call.get('ExpectedArrivalTime'):
                    try:
                        return datetime.fromisoformat(expected_arrival_time)
                    except ValueError:
                        return None
        return None
