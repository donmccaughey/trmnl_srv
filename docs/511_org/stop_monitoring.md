# Real-time Stop Monitoring (SIRI) API

[API Docs](https://511.org/open-data/transit#accordion15549635841-panel)


## Example Request and Response

    GET http://api.511.org/transit/StopMonitoring?api_key=<API KEY>&agency=SF&stopcode=17166
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 22:10:52 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 653
    Connection: keep-alive
    
    {
        "ServiceDelivery": {
            "ResponseTimestamp": "2025-05-24T22:10:52Z",
            "ProducerRef": "SF",
            "Status": true,
            "StopMonitoringDelivery": {
                "version": "1.4",
                "ResponseTimestamp": "2025-05-24T22:10:52Z",
                "Status": true,
                "MonitoredStopVisit": [
                    {
                        "RecordedAtTime": "2025-05-24T22:10:47Z",
                        "MonitoringRef": "17166",
                        "MonitoredVehicleJourney": {
                            "LineRef": "T",
                            "DirectionRef": "N",
                            "FramedVehicleJourneyRef": {
                                "DataFrameRef": "2025-05-24",
                                "DatedVehicleJourneyRef": "11740914_M12"
                            },
                            "PublishedLineName": "THIRD",
                            "OperatorRef": "SF",
                            "OriginRef": "17398",
                            "OriginName": "Bayshore Blvd & Sunnydale Ave",
                            "DestinationRef": "17876",
                            "DestinationName": "Chinatown - Rose Pak Station",
                            "Monitored": true,
                            "InCongestion": null,
                            "VehicleLocation": {
                                "Longitude": "-122.389191",
                                "Latitude": "37.7681046"
                            },
                            "Bearing": "345.0000000000",
                            "Occupancy": "seatsAvailable",
                            "VehicleRef": "2007",
                            "MonitoredCall": {
                                "StopPointRef": "17166",
                                "StopPointName": "4th St & King St",
                                "VehicleLocationAtStop": "",
                                "VehicleAtStop": "false",
                                "DestinationDisplay": "Chinatown",
                                "AimedArrivalTime": "2025-05-24T22:14:00Z",
                                "ExpectedArrivalTime": "2025-05-24T22:18:21Z",
                                "AimedDepartureTime": "2025-05-24T22:14:00Z",
                                "ExpectedDepartureTime": null,
                                "Distances": ""
                            }
                        }
                    },
                    {
                        "RecordedAtTime": "2025-05-24T22:10:47Z",
                        "MonitoringRef": "17166",
                        "MonitoredVehicleJourney": {
                            "LineRef": "T",
                            "DirectionRef": "N",
                            "FramedVehicleJourneyRef": {
                                "DataFrameRef": "2025-05-24",
                                "DatedVehicleJourneyRef": "11740915_M12"
                            },
                            "PublishedLineName": "THIRD",
                            "OperatorRef": "SF",
                            "OriginRef": "17398",
                            "OriginName": "Bayshore Blvd & Sunnydale Ave",
                            "DestinationRef": "17876",
                            "DestinationName": "Chinatown - Rose Pak Station",
                            "Monitored": true,
                            "InCongestion": null,
                            "VehicleLocation": {
                                "Longitude": "-122.388588",
                                "Latitude": "37.7607651"
                            },
                            "Bearing": "345.0000000000",
                            "Occupancy": "seatsAvailable",
                            "VehicleRef": "2016",
                            "MonitoredCall": {
                                "StopPointRef": "17166",
                                "StopPointName": "4th St & King St",
                                "VehicleLocationAtStop": "",
                                "VehicleAtStop": "false",
                                "DestinationDisplay": "Chinatown",
                                "AimedArrivalTime": "2025-05-24T22:26:00Z",
                                "ExpectedArrivalTime": "2025-05-24T22:22:28Z",
                                "AimedDepartureTime": "2025-05-24T22:26:00Z",
                                "ExpectedDepartureTime": null,
                                "Distances": ""
                            }
                        }
                    },
                    {
                        "RecordedAtTime": "2025-05-24T22:10:47Z",
                        "MonitoringRef": "17166",
                        "MonitoredVehicleJourney": {
                            "LineRef": "T",
                            "DirectionRef": "N",
                            "FramedVehicleJourneyRef": {
                                "DataFrameRef": "2025-05-24",
                                "DatedVehicleJourneyRef": "11740916_M12"
                            },
                            "PublishedLineName": "THIRD",
                            "OperatorRef": "SF",
                            "OriginRef": "17398",
                            "OriginName": "Bayshore Blvd & Sunnydale Ave",
                            "DestinationRef": "17876",
                            "DestinationName": "Chinatown - Rose Pak Station",
                            "Monitored": true,
                            "InCongestion": null,
                            "VehicleLocation": {
                                "Longitude": "-122.394287",
                                "Latitude": "37.7255173"
                            },
                            "Bearing": "15.0000000000",
                            "Occupancy": "seatsAvailable",
                            "VehicleRef": "2005",
                            "MonitoredCall": {
                                "StopPointRef": "17166",
                                "StopPointName": "4th St & King St",
                                "VehicleLocationAtStop": "",
                                "VehicleAtStop": "false",
                                "DestinationDisplay": "Chinatown",
                                "AimedArrivalTime": "2025-05-24T22:37:00Z",
                                "ExpectedArrivalTime": "2025-05-24T22:39:20Z",
                                "AimedDepartureTime": "2025-05-24T22:37:00Z",
                                "ExpectedDepartureTime": null,
                                "Distances": ""
                            }
                        }
                    }
                ]
            }
        }
    }
