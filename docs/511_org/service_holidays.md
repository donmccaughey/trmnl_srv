# Service Holidays (NeTEx) API

[API Docs](https://511.org/open-data/transit#accordion155496358410-panel)


## Example Request and Response

    GET http://api.511.org/transit/holidays?api_key=<API KEY>&operator_id=SF
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 22:18:22 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 492
    Connection: keep-alive
    
    {
        "Content": {
            "ServiceCalendar": {
                "id": "SF",
                "FromDate": "2025-05-15",
                "ToDate": "2025-06-20"
            },
            "AvailabilityConditions": [
                {
                    "version": "any",
                    "id": "SF:2025-05-15",
                    "FromDate": "2025-05-15T00:00:00-07:00",
                    "ToDate": "2025-05-15T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-16",
                    "FromDate": "2025-05-16T00:00:00-07:00",
                    "ToDate": "2025-05-16T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-17",
                    "FromDate": "2025-05-17T00:00:00-07:00",
                    "ToDate": "2025-05-17T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-18",
                    "FromDate": "2025-05-18T00:00:00-07:00",
                    "ToDate": "2025-05-18T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-19",
                    "FromDate": "2025-05-19T00:00:00-07:00",
                    "ToDate": "2025-05-19T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-20",
                    "FromDate": "2025-05-20T00:00:00-07:00",
                    "ToDate": "2025-05-20T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-21",
                    "FromDate": "2025-05-21T00:00:00-07:00",
                    "ToDate": "2025-05-21T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-22",
                    "FromDate": "2025-05-22T00:00:00-07:00",
                    "ToDate": "2025-05-22T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-23",
                    "FromDate": "2025-05-23T00:00:00-07:00",
                    "ToDate": "2025-05-23T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-24",
                    "FromDate": "2025-05-24T00:00:00-07:00",
                    "ToDate": "2025-05-24T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-25",
                    "FromDate": "2025-05-25T00:00:00-07:00",
                    "ToDate": "2025-05-25T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-26",
                    "FromDate": "2025-05-26T00:00:00-07:00",
                    "ToDate": "2025-05-26T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-27",
                    "FromDate": "2025-05-27T00:00:00-07:00",
                    "ToDate": "2025-05-27T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-28",
                    "FromDate": "2025-05-28T00:00:00-07:00",
                    "ToDate": "2025-05-28T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-29",
                    "FromDate": "2025-05-29T00:00:00-07:00",
                    "ToDate": "2025-05-29T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-30",
                    "FromDate": "2025-05-30T00:00:00-07:00",
                    "ToDate": "2025-05-30T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-05-31",
                    "FromDate": "2025-05-31T00:00:00-07:00",
                    "ToDate": "2025-05-31T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-01",
                    "FromDate": "2025-06-01T00:00:00-07:00",
                    "ToDate": "2025-06-01T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-02",
                    "FromDate": "2025-06-02T00:00:00-07:00",
                    "ToDate": "2025-06-02T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-03",
                    "FromDate": "2025-06-03T00:00:00-07:00",
                    "ToDate": "2025-06-03T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-04",
                    "FromDate": "2025-06-04T00:00:00-07:00",
                    "ToDate": "2025-06-04T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-05",
                    "FromDate": "2025-06-05T00:00:00-07:00",
                    "ToDate": "2025-06-05T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-06",
                    "FromDate": "2025-06-06T00:00:00-07:00",
                    "ToDate": "2025-06-06T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-07",
                    "FromDate": "2025-06-07T00:00:00-07:00",
                    "ToDate": "2025-06-07T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-08",
                    "FromDate": "2025-06-08T00:00:00-07:00",
                    "ToDate": "2025-06-08T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-09",
                    "FromDate": "2025-06-09T00:00:00-07:00",
                    "ToDate": "2025-06-09T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-10",
                    "FromDate": "2025-06-10T00:00:00-07:00",
                    "ToDate": "2025-06-10T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-11",
                    "FromDate": "2025-06-11T00:00:00-07:00",
                    "ToDate": "2025-06-11T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-12",
                    "FromDate": "2025-06-12T00:00:00-07:00",
                    "ToDate": "2025-06-12T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-13",
                    "FromDate": "2025-06-13T00:00:00-07:00",
                    "ToDate": "2025-06-13T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-14",
                    "FromDate": "2025-06-14T00:00:00-07:00",
                    "ToDate": "2025-06-14T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-15",
                    "FromDate": "2025-06-15T00:00:00-07:00",
                    "ToDate": "2025-06-15T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-16",
                    "FromDate": "2025-06-16T00:00:00-07:00",
                    "ToDate": "2025-06-16T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-17",
                    "FromDate": "2025-06-17T00:00:00-07:00",
                    "ToDate": "2025-06-17T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-18",
                    "FromDate": "2025-06-18T00:00:00-07:00",
                    "ToDate": "2025-06-18T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-19",
                    "FromDate": "2025-06-19T00:00:00-07:00",
                    "ToDate": "2025-06-19T23:59:00-07:00"
                },
                {
                    "version": "any",
                    "id": "SF:2025-06-20",
                    "FromDate": "2025-06-20T00:00:00-07:00",
                    "ToDate": "2025-06-20T23:59:00-07:00"
                }
            ]
        }
    }
