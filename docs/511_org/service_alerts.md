# GTFS Realtime Service Alerts API

[API Docs](https://511.org/open-data/transit#accordion15549631045-panel)


## Example Request and Response


    GET http://api.511.org/transit/servicealerts?api_key=<API KEY>&agency=SF&format=json
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 21:44:25 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 2282
    Connection: keep-alive
    
    {
        "Header": {
            "GtfsRealtimeVersion": "1.0",
            "incrementality": 0,
            "Timestamp": 1748123066
        },
        "Entities": [
            {
                "Id": "884787690",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1748119560,
                            "End": 1748205960
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "",
                            "Trip": null
                        }
                    ],
                    "Url": {
                        "Translations": [
                            {
                                "Text": "https://511.org/alerts/transit/disruptions",
                                "Language": "en"
                            }
                        ]
                    },
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "- Inbound K-Ingleside Line Delayed at Ocean and Dorado",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "SF Muni reports inbound K-Ingleside Line delayed at Ocean and Dorado, due to mechanical problems.",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8704",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747292400,
                            "End": 1750057199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15578"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "49",
                            "Trip": null,
                            "StopId": "15578"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board at Randall",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board at Randall",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8459",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1745305200,
                            "End": 1761721199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "7",
                            "Trip": null,
                            "StopId": "15649"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "7 STOP TEMP. MOVED Board at Market & 7th transit island",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "7 STOP TEMP. MOVED Board at Market & 7th transit island",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_7826",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1741248000,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "8",
                            "Trip": null,
                            "StopId": "18114"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8",
                            "Trip": null,
                            "StopId": "18115"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8BX",
                            "Trip": null,
                            "StopId": "18114"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8BX",
                            "Trip": null,
                            "StopId": "18115"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "8, 8BX STOP TEMP. CLOSED Board at Hahn & Sunnydale",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "8, 8BX STOP TEMP. CLOSED Board at Hahn & Sunnydale",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_7827",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1741248000,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "8",
                            "Trip": null,
                            "StopId": "16346"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8",
                            "Trip": null,
                            "StopId": "16343"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8",
                            "Trip": null,
                            "StopId": "16345"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8BX",
                            "Trip": null,
                            "StopId": "16346"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8BX",
                            "Trip": null,
                            "StopId": "16343"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "8BX",
                            "Trip": null,
                            "StopId": "16345"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "8, 8BX STOP TEMP. CLOSED Board at Geneva & Santos",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "8, 8BX STOP TEMP. CLOSED Board at Geneva & Santos",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_7701",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1735200000,
                            "End": 1754031599
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15623"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14 STOP TEMP. MOVED Board at Mission/Beale OR Steuart/Mission. ",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14 STOP TEMP. MOVED Board at Mission/Beale OR Steuart/Mission. ",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8982",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747983600,
                            "End": 1748674799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "5",
                            "Trip": null,
                            "StopId": "14236"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "21",
                            "Trip": null,
                            "StopId": "14236"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "33",
                            "Trip": null,
                            "StopId": "14236"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "5, 21, 33 STOP TEMP. MOVED Board west at Fulton & Parsons",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "5, 21, 33 STOP TEMP. MOVED Board west at Fulton & Parsons",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8991",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1748070000,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17398"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17399"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17400"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17347"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17343"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17345"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17401"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17402"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17403"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17404"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17352"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17353"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17354"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17355"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17356"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17357"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17358"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17166"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17879"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17878"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17877"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17876"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17876"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17874"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17873"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17872"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17397"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17359"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17360"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17361"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17362"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17363"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17364"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17365"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17390"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17391"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17392"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17393"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17346"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17344"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17342"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17394"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17395"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "T",
                            "Trip": null,
                            "StopId": "17396"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "Chinatown Rose Pak Station    Right Street Elevator\t  Out of Service",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "Chinatown Rose Pak Station    Right Street Elevator\t  Out of Service",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_7715",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1740816000,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "12",
                            "Trip": null,
                            "StopId": "16882"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "12",
                            "Trip": null,
                            "StopId": "16882"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "12 STOP TEMP. MOVED Board 280-feet south of existing stop",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "12 STOP TEMP. MOVED Board 280-feet south of existing stop",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8618",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1746514800,
                            "End": 1749279599
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "12",
                            "Trip": null,
                            "StopId": "17024"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "12 STOP TEMP. MOVED Board at Folsom/3rd (boarding island)",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "12 STOP TEMP. MOVED Board at Folsom/3rd (boarding island)",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8875",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747983600,
                            "End": 1748156399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "37",
                            "Trip": null,
                            "StopId": "13314"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "37 STOP TEMP. MOVED Board on other side of Diamond",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "37 STOP TEMP. MOVED Board on other side of Diamond",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8882",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747551600,
                            "End": 1756796399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15602"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "14R",
                            "Trip": null,
                            "StopId": "15602"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14, 14R STOP TEMP. CLOSED Board at Mission & Naglee",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14, 14R STOP TEMP. CLOSED Board at Mission & Naglee",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8759",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747292400,
                            "End": 1750057199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15597"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15596"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "49",
                            "Trip": null,
                            "StopId": "15597"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "49",
                            "Trip": null,
                            "StopId": "15596"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board at Richland",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board at Richland",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8120",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1742972400,
                            "End": 1748761199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "12",
                            "Trip": null,
                            "StopId": "14664"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "27",
                            "Trip": null,
                            "StopId": "14664"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "12, 27 STOP TEMP. CLOSED Board at 10th",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "12, 27 STOP TEMP. CLOSED Board at 10th",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_7998",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1742194800,
                            "End": 1748761199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "45",
                            "Trip": null,
                            "StopId": "16748"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "45 STOP TEMP. CLOSED Board at Laguna",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "45 STOP TEMP. CLOSED Board at Laguna",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8771",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747292400,
                            "End": 1748674799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "35",
                            "Trip": null,
                            "StopId": "14389"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "36",
                            "Trip": null,
                            "StopId": "14389"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "52",
                            "Trip": null,
                            "StopId": "14389"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "35, 36, & 52 STOP TEMP. MOVED Board: Diamond & Kern",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "35, 36, & 52 STOP TEMP. MOVED Board: Diamond & Kern",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8145",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1743404400,
                            "End": 1748674799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "27",
                            "Trip": null,
                            "StopId": "18048"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "27 STOP TEMP. MOVED Board on other side of Turk",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "27 STOP TEMP. MOVED Board on other side of Turk",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8146",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1743404400,
                            "End": 1748674799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "12",
                            "Trip": null,
                            "StopId": "14665"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "27",
                            "Trip": null,
                            "StopId": "14665"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "12, 27 STOP TEMP. MOVED Board at 12th & Folsom",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "12, 27 STOP TEMP. MOVED Board at 12th & Folsom",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8542",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1746082800,
                            "End": 1750143599
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "1",
                            "Trip": null,
                            "StopId": "14023"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "1",
                            "Trip": null,
                            "StopId": "14020"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "1 DTR STOP CLOSED Board at Hyde or Taylor",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "1 DTR STOP CLOSED Board at Hyde or Taylor",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8163",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1740038400,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16346"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16344"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16345"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16575"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16568"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16565"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16339"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16346"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16344"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "14809"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "14895"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16385"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16388"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16383"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16386"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16570"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16584"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17297"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13793"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16352"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17899"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16362"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16355"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16364"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13778"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17886"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16038"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16119"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16026"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13238"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13244"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15652"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15651"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15650"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15647"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15645"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15643"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15640"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15685"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17264"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16475"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15335"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15335"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15657"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15639"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15678"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15694"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15655"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15695"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15656"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15676"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15680"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13245"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13239"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16027"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16037"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16039"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17888"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13779"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16365"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16357"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16358"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16371"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13772"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "13783"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16569"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16583"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16576"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16571"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16387"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16382"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16389"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16384"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "17127"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "14808"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "14899"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16345"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16340"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16566"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16567"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16574"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "9/9R STOP MOVED Board at Geneva & Santos",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "9/9R STOP MOVED Board at Geneva & Santos",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8164",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1740038400,
                            "End": 1767254399
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16568"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16565"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16339"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16340"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16566"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "16567"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16568"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16565"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16339"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16340"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16566"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "16567"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "9/9R STOP MOVED Board at Sunnydale & Western Access Road",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "9/9R STOP MOVED Board at Sunnydale & Western Access Road",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8932",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747638000,
                            "End": 1748242799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "Trip": null
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "Carnaval on Sunday. Muni reroutes details at sfmta.com/carnaval",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "Carnaval on Sunday. Muni reroutes details at sfmta.com/carnaval",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8165",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1737100800,
                            "End": 1756623599
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "2",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "6",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "9R",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "NOWL",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "KBUS",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "NBUS",
                            "Trip": null,
                            "StopId": "15658"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "LOWL",
                            "Trip": null,
                            "StopId": "15658"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "STOP TEMP. MOVED Board at Market & Main transit island",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "STOP TEMP. MOVED Board at Market & Main transit island",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8431",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1744959600,
                            "End": 1748242799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "5",
                            "Trip": null,
                            "StopId": "14737"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "5R",
                            "Trip": null,
                            "StopId": "14737"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "5/5R STOP TEMP. MOVED Board midblock btwn 9th & 10th",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "5/5R STOP TEMP. MOVED Board midblock btwn 9th & 10th",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8432",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1744959600,
                            "End": 1748242799
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "5",
                            "Trip": null,
                            "StopId": "14736"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "5R",
                            "Trip": null,
                            "StopId": "14736"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "5/5R STOP TEMP. MOVED Board at Fulton & 11th",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "5/5R STOP TEMP. MOVED Board at Fulton & 11th",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8699",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747292400,
                            "End": 1750057199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15613"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "49",
                            "Trip": null,
                            "StopId": "15613"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "14R",
                            "Trip": null,
                            "StopId": "15613"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14, 14R, 49 STOP TEMP. MOVED Board btwn Murray & Crescent",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14, 14R, 49 STOP TEMP. MOVED Board btwn Murray & Crescent",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            },
            {
                "Id": "SF_8700",
                "TripUpdate": null,
                "Vehicle": null,
                "Alert": {
                    "ActivePeriods": [
                        {
                            "Start": 1747292400,
                            "End": 1750057199
                        }
                    ],
                    "InformedEntities": [
                        {
                            "AgencyId": "SF",
                            "RouteId": "14",
                            "Trip": null,
                            "StopId": "15577"
                        },
                        {
                            "AgencyId": "SF",
                            "RouteId": "49",
                            "Trip": null,
                            "StopId": "15577"
                        }
                    ],
                    "Url": null,
                    "HeaderText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board btwn Appleton & Santa Maria",
                                "Language": "en"
                            }
                        ]
                    },
                    "DescriptionText": {
                        "Translations": [
                            {
                                "Text": "14, 49 STOP TEMP. MOVED Board btwn Appleton & Santa Maria",
                                "Language": "en"
                            }
                        ]
                    },
                    "TtsHeaderText": null,
                    "TtsDescriptionText": null
                }
            }
        ]
    }
