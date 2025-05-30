# Lines (NeTEx) API

[API Docs](https://511.org/open-data/transit#accordion15549635844-panel)


## Example Request and Response

    GET http://api.511.org/transit/lines?api_key=<API KEY>&operator_id=SF
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 21:56:35 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 1396
    Connection: keep-alive
    
    [
        {
            "Id": "30X",
            "Name": "MARINA EXPRESS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "30X",
            "SiriLineRef": "30X",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "L",
            "Name": "TARAVAL",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "L",
            "SiriLineRef": "L",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "FBUS",
            "Name": "MARKET & WHARVES BUS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "FBUS",
            "SiriLineRef": "FBUS",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "25",
            "Name": "TREASURE ISLAND",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "25",
            "SiriLineRef": "25",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "27",
            "Name": "BRYANT",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "27",
            "SiriLineRef": "27",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "28",
            "Name": "19TH AVENUE",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "28",
            "SiriLineRef": "28",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "29",
            "Name": "SUNSET",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "29",
            "SiriLineRef": "29",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "14R",
            "Name": "MISSION RAPID",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "14R",
            "SiriLineRef": "14R",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "18",
            "Name": "46TH AVENUE",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "18",
            "SiriLineRef": "18",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "19",
            "Name": "POLK",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "19",
            "SiriLineRef": "19",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "714",
            "Name": "BART EARLY BIRD",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "714",
            "SiriLineRef": "714",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "1X",
            "Name": "CALIFORNIA EXPRESS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "1X",
            "SiriLineRef": "1X",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "23",
            "Name": "MONTEREY",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "23",
            "SiriLineRef": "23",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "90",
            "Name": "SAN BRUNO OWL",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "90",
            "SiriLineRef": "90",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "24",
            "Name": "DIVISADERO",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "24",
            "SiriLineRef": "24",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "22",
            "Name": "FILLMORE",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "22",
            "SiriLineRef": "22",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "33",
            "Name": "ASHBURY-18TH ST",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "33",
            "SiriLineRef": "33",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "12",
            "Name": "FOLSOM-PACIFIC",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "12",
            "SiriLineRef": "12",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "36",
            "Name": "TERESITA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "36",
            "SiriLineRef": "36",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "38R",
            "Name": "GEARY RAPID",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "38R",
            "SiriLineRef": "38R",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "14",
            "Name": "MISSION",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "14",
            "SiriLineRef": "14",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "2",
            "Name": "SUTTER",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "2",
            "SiriLineRef": "2",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "21",
            "Name": "HAYES",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "21",
            "SiriLineRef": "21",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "39",
            "Name": "COIT",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "39",
            "SiriLineRef": "39",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "58",
            "Name": "LAKE MERCED",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "58",
            "SiriLineRef": "58",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "37",
            "Name": "CORBETT",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "37",
            "SiriLineRef": "37",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "44",
            "Name": "O'SHAUGHNESSY",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "44",
            "SiriLineRef": "44",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "45",
            "Name": "UNION-STOCKTON",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "45",
            "SiriLineRef": "45",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "48",
            "Name": "QUINTARA-24TH STREET",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "48",
            "SiriLineRef": "48",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "43",
            "Name": "MASONIC",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "43",
            "SiriLineRef": "43",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "38",
            "Name": "GEARY",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "38",
            "SiriLineRef": "38",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "30",
            "Name": "STOCKTON",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "30",
            "SiriLineRef": "30",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "35",
            "Name": "EUREKA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "35",
            "SiriLineRef": "35",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "49",
            "Name": "VAN NESS-MISSION",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "49",
            "SiriLineRef": "49",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "5",
            "Name": "FULTON",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "5",
            "SiriLineRef": "5",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "31",
            "Name": "BALBOA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "31",
            "SiriLineRef": "31",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "57",
            "Name": "PARKMERCED",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "57",
            "SiriLineRef": "57",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "6",
            "Name": "HAIGHT-PARNASSUS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "6",
            "SiriLineRef": "6",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "56",
            "Name": "RUTLAND",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "56",
            "SiriLineRef": "56",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "5R",
            "Name": "FULTON RAPID",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "5R",
            "SiriLineRef": "5R",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "54",
            "Name": "FELTON",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "54",
            "SiriLineRef": "54",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "55",
            "Name": "DOGPATCH",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "55",
            "SiriLineRef": "55",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "1",
            "Name": "CALIFORNIA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "1",
            "SiriLineRef": "1",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "J",
            "Name": "CHURCH",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "J",
            "SiriLineRef": "J",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "KBUS",
            "Name": "INGLESIDE BUS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "KBUS",
            "SiriLineRef": "KBUS",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "N",
            "Name": "JUDAH",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "N",
            "SiriLineRef": "N",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "M",
            "Name": "OCEAN VIEW",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "M",
            "SiriLineRef": "M",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "8AX",
            "Name": "BAYSHORE A EXPRESS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "8AX",
            "SiriLineRef": "8AX",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "91",
            "Name": "3RD-19TH AVE OWL",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "91",
            "SiriLineRef": "91",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "LOWL",
            "Name": "OWL TARAVAL",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "LOWL",
            "SiriLineRef": "LOWL",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "7",
            "Name": "HAIGHT-NORIEGA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "7",
            "SiriLineRef": "7",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "8BX",
            "Name": "BAYSHORE B EXPRESS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "8BX",
            "SiriLineRef": "8BX",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "9R",
            "Name": "SAN BRUNO RAPID",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "9R",
            "SiriLineRef": "9R",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "CA",
            "Name": "CALIFORNIA STREET CABLE CAR",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "cableway",
            "PublicCode": "CA",
            "SiriLineRef": "CA",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "8",
            "Name": "BAYSHORE",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "8",
            "SiriLineRef": "8",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "66",
            "Name": "QUINTARA",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "66",
            "SiriLineRef": "66",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "15",
            "Name": "BAYVIEW HUNTERS POINT EXPRESS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "15",
            "SiriLineRef": "15",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "F",
            "Name": "MARKET & WHARVES",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "F",
            "SiriLineRef": "F",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "NBUS",
            "Name": "JUDAH BUS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "NBUS",
            "SiriLineRef": "NBUS",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "K",
            "Name": "INGLESIDE",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "K",
            "SiriLineRef": "K",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "67",
            "Name": "BERNAL HEIGHTS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "67",
            "SiriLineRef": "67",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "PM",
            "Name": "POWELL-MASON CABLE CAR",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "cableway",
            "PublicCode": "PM",
            "SiriLineRef": "PM",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "52",
            "Name": "EXCELSIOR",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "52",
            "SiriLineRef": "52",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "9",
            "Name": "SAN BRUNO",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "9",
            "SiriLineRef": "9",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "NOWL",
            "Name": "OWL JUDAH",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "NOWL",
            "SiriLineRef": "NOWL",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "PH",
            "Name": "POWELL-HYDE CABLE CAR",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "cableway",
            "PublicCode": "PH",
            "SiriLineRef": "PH",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "T",
            "Name": "THIRD",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "metro",
            "PublicCode": "T",
            "SiriLineRef": "T",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "TBUS",
            "Name": "THIRD BUS",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "TBUS",
            "SiriLineRef": "TBUS",
            "Monitored": true,
            "OperatorRef": "SF"
        },
        {
            "Id": "28R",
            "Name": "19TH AVENUE RAPID",
            "FromDate": "2025-05-15T00:00:00-07:00",
            "ToDate": "2025-06-20T23:59:00-07:00",
            "TransportMode": "bus",
            "PublicCode": "28R",
            "SiriLineRef": "28R",
            "Monitored": true,
            "OperatorRef": "SF"
        }
    ]
