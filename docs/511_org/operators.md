# GTFS Operators API

[API Docs](https://511.org/open-data/transit#accordion15549631041-panel)


## Example Request and Response

    GET http://api.511.org/transit/gtfsoperators?api_key=<API KEY>
    
    HTTP/1.1 200 OK
    Cache-Control: no-cache
    Cache-control: no-cache="set-cookie"
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Sat, 24 May 2025 20:12:53 GMT
    Expires: -1
    Pragma: no-cache
    RateLimit-Limit: 60
    RateLimit-Remaining: 59
    Server: Microsoft-IIS/10.0
    Set-Cookie: AWSELB=<COOKIE>;PATH=/;MAX-AGE=1
    Content-Length: 1046
    Connection: keep-alive
    
    [
        {
            "Id": "3D",
            "Name": "Tri Delta Transit",
            "LastGenerated": "5/16/2025 10:19:47 AM"
        },
        {
            "Id": "AC",
            "Name": "AC TRANSIT",
            "LastGenerated": "3/2/2025 12:29:30 AM"
        },
        {
            "Id": "AF",
            "Name": "Angel Island Tiburon Ferry",
            "LastGenerated": "4/26/2025 11:20:19 AM"
        },
        {
            "Id": "AM",
            "Name": "Capitol Corridor Joint Powers Authority",
            "LastGenerated": "5/16/2025 1:48:07 AM"
        },
        {
            "Id": "BA",
            "Name": "Bay Area Rapid Transit",
            "LastGenerated": "5/21/2025 10:34:26 AM"
        },
        {
            "Id": "CC",
            "Name": "County Connection",
            "LastGenerated": "1/2/2025 11:45:19 AM"
        },
        {
            "Id": "CE",
            "Name": "Altamont Corridor Express",
            "LastGenerated": "4/10/2025 3:12:04 PM"
        },
        {
            "Id": "CM",
            "Name": "Commute.org Shuttles",
            "LastGenerated": "4/8/2025 2:37:13 AM"
        },
        {
            "Id": "CT",
            "Name": "Caltrain",
            "LastGenerated": "4/24/2025 11:04:26 AM"
        },
        {
            "Id": "DE",
            "Name": "Dumbarton Express Consortium",
            "LastGenerated": "3/4/2025 12:47:28 PM"
        },
        {
            "Id": "EE",
            "Name": "Emery Express",
            "LastGenerated": "1/30/2025 11:16:12 AM"
        },
        {
            "Id": "EM",
            "Name": "Emery Go-Round",
            "LastGenerated": "1/30/2025 1:11:09 PM"
        },
        {
            "Id": "FS",
            "Name": "FAST",
            "LastGenerated": "5/8/2025 2:55:57 AM"
        },
        {
            "Id": "GF",
            "Name": "Golden Gate Ferry",
            "LastGenerated": "3/3/2025 11:23:25 AM"
        },
        {
            "Id": "GG",
            "Name": "Golden Gate Transit",
            "LastGenerated": "5/8/2025 10:55:52 AM"
        },
        {
            "Id": "GP",
            "Name": "San Francisco Recreation and Parks",
            "LastGenerated": "1/30/2025 11:18:09 AM"
        },
        {
            "Id": "MA",
            "Name": "Marin Transit",
            "LastGenerated": "4/25/2025 3:33:36 PM"
        },
        {
            "Id": "MB",
            "Name": "Mission Bay TMA",
            "LastGenerated": "3/24/2025 11:09:20 AM"
        },
        {
            "Id": "MC",
            "Name": "Mountain View Community Shuttle",
            "LastGenerated": "12/24/2024 12:48:38 AM"
        },
        {
            "Id": "MV",
            "Name": "MVgo",
            "LastGenerated": "2/20/2025 10:11:14 AM"
        },
        {
            "Id": "PE",
            "Name": "PETALUMA",
            "LastGenerated": "12/30/2024 8:47:00 AM"
        },
        {
            "Id": "PG",
            "Name": "Presidio Go",
            "LastGenerated": "1/8/2025 10:19:36 AM"
        },
        {
            "Id": "RG",
            "Name": "Regional GTFS",
            "LastGenerated": "5/24/2025 5:41:43 AM"
        },
        {
            "Id": "RV",
            "Name": "Rio Vista Delta Breeze",
            "LastGenerated": "2/13/2025 11:23:28 AM"
        },
        {
            "Id": "SA",
            "Name": "Sonoma Marin Area Rail Transit",
            "LastGenerated": "5/22/2025 2:27:55 AM"
        },
        {
            "Id": "SB",
            "Name": "San Francisco Bay Ferry",
            "LastGenerated": "5/1/2025 2:47:46 PM"
        },
        {
            "Id": "SC",
            "Name": "VTA",
            "LastGenerated": "4/21/2025 8:57:13 PM"
        },
        {
            "Id": "SF",
            "Name": "San Francisco Municipal Transportation Agency",
            "LastGenerated": "5/16/2025 1:38:37 AM"
        },
        {
            "Id": "SI",
            "Name": "San Francisco International Airport",
            "LastGenerated": "5/19/2025 3:54:20 PM"
        },
        {
            "Id": "SM",
            "Name": "SamTrans",
            "LastGenerated": "5/14/2025 3:10:06 PM"
        },
        {
            "Id": "SO",
            "Name": "Sonoma County Transit",
            "LastGenerated": "3/16/2025 1:56:44 PM"
        },
        {
            "Id": "SR",
            "Name": "SANTAROSA",
            "LastGenerated": "11/18/2024 7:40:40 AM"
        },
        {
            "Id": "SS",
            "Name": "City of South San Francisco",
            "LastGenerated": "2/1/2025 6:16:24 PM"
        },
        {
            "Id": "ST",
            "Name": "SolTrans",
            "LastGenerated": "5/23/2025 10:22:08 AM"
        },
        {
            "Id": "TF",
            "Name": "Treasure Island Ferry",
            "LastGenerated": "1/7/2025 2:24:43 PM"
        },
        {
            "Id": "UC",
            "Name": "Union City Transit",
            "LastGenerated": "11/26/2024 4:10:55 PM"
        },
        {
            "Id": "VC",
            "Name": "Vacaville City Coach",
            "LastGenerated": "4/10/2025 10:21:05 AM"
        },
        {
            "Id": "VN",
            "Name": "VINE Transit",
            "LastGenerated": "5/20/2025 11:27:46 AM"
        },
        {
            "Id": "WC",
            "Name": "WestCat (Western Contra Costa)",
            "LastGenerated": "4/18/2025 3:03:25 AM"
        },
        {
            "Id": "WH",
            "Name": "Livermore Amador Valley Transit Authority",
            "LastGenerated": "5/24/2025 10:44:39 AM"
        }
    ]
