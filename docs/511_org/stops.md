# Stops (NeTEx) API

[API Docs](https://511.org/open-data/transit#accordion15549635845-panel)


## Example Request and Response

    GET http://api.511.org/transit/stops?api_key=<API KEY>&operator_id=SF&line_id=T
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 22:01:29 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 1378
    Connection: keep-alive
    
    {
        "Contents": {
            "ResponseTimestamp": "2025-05-24T15:01:29-07:00",
            "dataObjects": {
                "id": "SF",
                "ScheduledStopPoint": [
                    {
                        "id": "17872",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "4th & Brannan Southbound",
                        "Location": {
                            "Longitude": "-122.396613",
                            "Latitude": "37.778341"
                        },
                        "Url": "https://www.sfmta.com/17872",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17397",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "4th St & King St",
                        "Location": {
                            "Longitude": "-122.393829",
                            "Latitude": "37.776135"
                        },
                        "Url": "https://www.sfmta.com/17397",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17166",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "4th St & King St",
                        "Location": {
                            "Longitude": "-122.393864",
                            "Latitude": "37.776278"
                        },
                        "Url": "https://www.sfmta.com/17166",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17399",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Bayshore Blvd & Areta Ave",
                        "Location": {
                            "Longitude": "-122.402339",
                            "Latitude": "37.712226"
                        },
                        "Url": "https://www.sfmta.com/17399",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17395",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Bayshore Blvd & Blanken Ave",
                        "Location": {
                            "Longitude": "-122.402316",
                            "Latitude": "37.712253"
                        },
                        "Url": "https://www.sfmta.com/17395",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17398",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Bayshore Blvd & Sunnydale Ave",
                        "Location": {
                            "Longitude": "-122.405044",
                            "Latitude": "37.708944"
                        },
                        "Url": "https://www.sfmta.com/17398",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17396",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Bayshore Blvd & Sunnydale Ave",
                        "Location": {
                            "Longitude": "-122.405113",
                            "Latitude": "37.70897"
                        },
                        "Url": "https://www.sfmta.com/17396",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17876",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Chinatown - Rose Pak Station",
                        "Location": {
                            "Longitude": "-122.408078",
                            "Latitude": "37.794807"
                        },
                        "Url": "https://www.sfmta.com/17876",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17879",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Fourth Street & Brannan Northbound",
                        "Location": {
                            "Longitude": "-122.39659",
                            "Latitude": "37.778403"
                        },
                        "Url": "https://www.sfmta.com/17879",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17362",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & 20th St",
                        "Location": {
                            "Longitude": "-122.388593",
                            "Latitude": "37.760367"
                        },
                        "Url": "https://www.sfmta.com/17362",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17355",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & 20th St",
                        "Location": {
                            "Longitude": "-122.388558",
                            "Latitude": "37.760518"
                        },
                        "Url": "https://www.sfmta.com/17355",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17363",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & 23rd St",
                        "Location": {
                            "Longitude": "-122.388047",
                            "Latitude": "37.755263"
                        },
                        "Url": "https://www.sfmta.com/17363",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17354",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & 23rd St",
                        "Location": {
                            "Longitude": "-122.388001",
                            "Latitude": "37.755414"
                        },
                        "Url": "https://www.sfmta.com/17354",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17343",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Carroll Ave",
                        "Location": {
                            "Longitude": "-122.394222",
                            "Latitude": "37.725491"
                        },
                        "Url": "https://www.sfmta.com/17343",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17344",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Carroll Ave",
                        "Location": {
                            "Longitude": "-122.394394",
                            "Latitude": "37.725241"
                        },
                        "Url": "https://www.sfmta.com/17344",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17352",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Evans Ave",
                        "Location": {
                            "Longitude": "-122.38792",
                            "Latitude": "37.742726"
                        },
                        "Url": "https://www.sfmta.com/17352",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17365",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Evans Ave",
                        "Location": {
                            "Longitude": "-122.388034",
                            "Latitude": "37.742727"
                        },
                        "Url": "https://www.sfmta.com/17365",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17342",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Gilman/Paul",
                        "Location": {
                            "Longitude": "-122.395782",
                            "Latitude": "37.722199"
                        },
                        "Url": "https://www.sfmta.com/17342",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17347",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Gilman/Paul",
                        "Location": {
                            "Longitude": "-122.39561",
                            "Latitude": "37.722449"
                        },
                        "Url": "https://www.sfmta.com/17347",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17390",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Hudson/Innes",
                        "Location": {
                            "Longitude": "-122.38893",
                            "Latitude": "37.739934"
                        },
                        "Url": "https://www.sfmta.com/17390",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17404",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Hudson/Innes",
                        "Location": {
                            "Longitude": "-122.388884",
                            "Latitude": "37.739916"
                        },
                        "Url": "https://www.sfmta.com/17404",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17403",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Kirkwood/La Salle",
                        "Location": {
                            "Longitude": "-122.389688",
                            "Latitude": "37.737641"
                        },
                        "Url": "https://www.sfmta.com/17403",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17391",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Kirkwood/La Salle",
                        "Location": {
                            "Longitude": "-122.389734",
                            "Latitude": "37.73765"
                        },
                        "Url": "https://www.sfmta.com/17391",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17394",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Le Conte Ave",
                        "Location": {
                            "Longitude": "-122.397697",
                            "Latitude": "37.71864"
                        },
                        "Url": "https://www.sfmta.com/17394",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17400",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Le Conte Ave",
                        "Location": {
                            "Longitude": "-122.397468",
                            "Latitude": "37.718809"
                        },
                        "Url": "https://www.sfmta.com/17400",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17353",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Marin St",
                        "Location": {
                            "Longitude": "-122.387445",
                            "Latitude": "37.748999"
                        },
                        "Url": "https://www.sfmta.com/17353",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17364",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Marin St",
                        "Location": {
                            "Longitude": "-122.387525",
                            "Latitude": "37.749097"
                        },
                        "Url": "https://www.sfmta.com/17364",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17359",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Mission Rock St",
                        "Location": {
                            "Longitude": "-122.389717",
                            "Latitude": "37.772832"
                        },
                        "Url": "https://www.sfmta.com/17359",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17358",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Mission Rock St",
                        "Location": {
                            "Longitude": "-122.389683",
                            "Latitude": "37.772984"
                        },
                        "Url": "https://www.sfmta.com/17358",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17402",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Oakdale/Palou",
                        "Location": {
                            "Longitude": "-122.390836",
                            "Latitude": "37.734358"
                        },
                        "Url": "https://www.sfmta.com/17402",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17392",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Oakdale/Palou",
                        "Location": {
                            "Longitude": "-122.390893",
                            "Latitude": "37.73435"
                        },
                        "Url": "https://www.sfmta.com/17392",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17393",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Revere/Shafter",
                        "Location": {
                            "Longitude": "-122.391605",
                            "Latitude": "37.732289"
                        },
                        "Url": "https://www.sfmta.com/17393",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17401",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street/Revere/Shafter",
                        "Location": {
                            "Longitude": "-122.391502",
                            "Latitude": "37.732262"
                        },
                        "Url": "https://www.sfmta.com/17401",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17346",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Williams Ave",
                        "Location": {
                            "Longitude": "-122.392684",
                            "Latitude": "37.729211"
                        },
                        "Url": "https://www.sfmta.com/17346",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17345",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Third Street & Williams Ave",
                        "Location": {
                            "Longitude": "-122.392604",
                            "Latitude": "37.729291"
                        },
                        "Url": "https://www.sfmta.com/17345",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17357",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Ucsf / Chase Center (16th St)",
                        "Location": {
                            "Longitude": "-122.389182",
                            "Latitude": "37.768504"
                        },
                        "Url": "https://www.sfmta.com/17357",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17360",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Ucsf / Chase Center (16th Street)",
                        "Location": {
                            "Longitude": "-122.389366",
                            "Latitude": "37.768237"
                        },
                        "Url": "https://www.sfmta.com/17360",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17356",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Ucsf Medical Center (Mariposa)",
                        "Location": {
                            "Longitude": "-122.388853",
                            "Latitude": "37.764391"
                        },
                        "Url": "https://www.sfmta.com/17356",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17361",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Ucsf Medical Center (Mariposa)",
                        "Location": {
                            "Longitude": "-122.388865",
                            "Latitude": "37.764239"
                        },
                        "Url": "https://www.sfmta.com/17361",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17877",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Union Square/Market St Station Northbound",
                        "Location": {
                            "Longitude": "-122.406477",
                            "Latitude": "37.787151"
                        },
                        "Url": "https://www.sfmta.com/17877",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17874",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Union Square/Market St Station Southbound",
                        "Location": {
                            "Longitude": "-122.406523",
                            "Latitude": "37.787133"
                        },
                        "Url": "https://www.sfmta.com/17874",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17878",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Yerba Buena/Moscone Station Northbound",
                        "Location": {
                            "Longitude": "-122.401551",
                            "Latitude": "37.782358"
                        },
                        "Url": "https://www.sfmta.com/17878",
                        "StopType": "onstreetBus"
                    },
                    {
                        "id": "17873",
                        "Extensions": {
                            "LocationType": null,
                            "PlatformCode": null,
                            "ParentStation": null,
                            "ValidBetween": {
                                "FromDate": "2025-05-15T00:00:00-07:00",
                                "ToDate": "2025-06-20T23:59:00-07:00"
                            }
                        },
                        "Name": "Yerba Buena/Moscone Station Southbound",
                        "Location": {
                            "Longitude": "-122.401551",
                            "Latitude": "37.782161"
                        },
                        "Url": "https://www.sfmta.com/17873",
                        "StopType": "onstreetBus"
                    }
                ]
            }
        }
    }
