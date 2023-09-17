## 10x Genomics Platform Engineering Technical Coding Prompt

Create a web service that converts a CSV file into an API that exposes JSON.

Download and run docker image:
```
docker pull cqhecode/10x
docker run -p 80:9090 -d cqhecode/10x
```

>GET localhost:80/query?date=2012-09-20
```
{
    "result": [
        {
            "date": "Thu, 20 Sep 2012 00:00:00 GMT",
            "precipitation": 0.0,
            "temp_max": 19.4,
            "temp_min": 10.0,
            "weather": "drizzle",
            "wind": 2.5
        }
    ]
}
```

> GET localhost:80/query?type=rain&limit=10
```
{
    "result": [
        {
            "date": "Mon, 02 Jan 2012 00:00:00 GMT",
            "precipitation": 10.9,
            "temp_max": 10.6,
            "temp_min": 2.8,
            "weather": "rain",
            "wind": 4.5
        },
        {
            "date": "Tue, 03 Jan 2012 00:00:00 GMT",
            "precipitation": 0.8,
            "temp_max": 11.7,
            "temp_min": 7.2,
            "weather": "rain",
            "wind": 2.3
        },
        {
            "date": "Wed, 04 Jan 2012 00:00:00 GMT",
            "precipitation": 20.3,
            "temp_max": 12.2,
            "temp_min": 5.6,
            "weather": "rain",
            "wind": 4.7
        },
        {
            "date": "Thu, 05 Jan 2012 00:00:00 GMT",
            "precipitation": 1.3,
            "temp_max": 8.9,
            "temp_min": 2.8,
            "weather": "rain",
            "wind": 6.1
        },
        {
            "date": "Fri, 06 Jan 2012 00:00:00 GMT",
            "precipitation": 2.5,
            "temp_max": 4.4,
            "temp_min": 2.2,
            "weather": "rain",
            "wind": 2.2
        },
        {
            "date": "Sat, 07 Jan 2012 00:00:00 GMT",
            "precipitation": 0.0,
            "temp_max": 7.2,
            "temp_min": 2.8,
            "weather": "rain",
            "wind": 2.3
        },
        {
            "date": "Mon, 09 Jan 2012 00:00:00 GMT",
            "precipitation": 4.3,
            "temp_max": 9.4,
            "temp_min": 5.0,
            "weather": "rain",
            "wind": 3.4
        },
        {
            "date": "Tue, 10 Jan 2012 00:00:00 GMT",
            "precipitation": 1.0,
            "temp_max": 6.1,
            "temp_min": 0.6,
            "weather": "rain",
            "wind": 3.4
        }
    ]
}
```