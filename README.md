# diving in python

## Geolocation Request

Create a new environment. Activate it and install module _requests_. Write a function to get location info in json format.

For example, _python geolocation_request.py_ might return:

```javascript
{
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "region": "CA",
  "regionName": "California",
  "city": "San Francisco",
  "zip": "94105",
  "lat": "37.7898",
  "lon": "-122.3942",
  "timezone": "America\/Los_Angeles",
  "isp": "Wikimedia Foundation",
  "org": "Wikimedia Foundation",
  "as": "AS14907 Wikimedia US network",
  "query": "208.80.152.201"
}
```

```python
import pprint

def get_location_info():
    return None

if __name__ == "__main__":
    pprint.pprint(get_location_info())
```

## Digit Sum

Create a module _solution.py_ that takes a string argument and summarize digits in it.

For example, _python3 solution.py 873_ should print _18_.

```python
import sys

digit_string = sys.argv[1]

```
