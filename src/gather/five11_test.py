from datetime import datetime, timezone

from .five11 import Five11


def test_params():
    api_key = '123456789'
    five11 = Five11(api_key)
    assert five11.params == {
        'api_key': '123456789',
        'agency': 'SF',
        'stopcode': 17166,
    }


def test_get_expected_arrival_time():
    visit = {
        'MonitoredVehicleJourney': {
            'MonitoredCall': {
                'ExpectedArrivalTime': '2025-05-24T22:18:21Z',
            }
        }
    }
    api_key = '123456789'
    five11 = Five11(api_key)

    arrival_time = five11._get_expected_arrival_time(visit)

    assert arrival_time == datetime(
        2025, 5, 24, 22, 18, 21, tzinfo=timezone.utc
    )


def test_get_expected_arrival_time_is_missing():
    visit = {
        'MonitoredVehicleJourney': {
            'MonitoredCall': {}
        }
    }
    api_key = '123456789'
    five11 = Five11(api_key)

    arrival_time = five11._get_expected_arrival_time(visit)

    assert arrival_time is None


def test_get_expected_arrival_time_is_unparsable():
    visit = {
        'MonitoredVehicleJourney': {
            'MonitoredCall': {
                'ExpectedArrivalTime': 'not an ISO 8601 date',
            }
        }
    }
    api_key = '123456789'
    five11 = Five11(api_key)

    arrival_time = five11._get_expected_arrival_time(visit)

    assert arrival_time is None


def test_get_expected_arrival_times():
    stop_monitoring_response = {
        'ServiceDelivery': {
            'StopMonitoringDelivery': {
                'MonitoredStopVisit': [
                    {
                        'MonitoredVehicleJourney': {
                            'MonitoredCall': {
                                'ExpectedArrivalTime': '2025-05-24T22:18:21Z',
                            }
                        }
                    },
                    {
                        'MonitoredVehicleJourney': {
                            'MonitoredCall': {
                                'ExpectedArrivalTime': '2025-05-24T22:22:28Z',
                            }
                        }
                    }
                ]
            }
        }

    }
    api_key = '123456789'
    five11 = Five11(api_key)

    arrival_times = five11._get_expected_arrival_times(stop_monitoring_response)

    assert arrival_times == [
        datetime(2025, 5, 24, 22, 18, 21, tzinfo=timezone.utc),
        datetime(2025, 5, 24, 22, 22, 28, tzinfo=timezone.utc),
    ]
