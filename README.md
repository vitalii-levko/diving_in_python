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

## Draw Steps

Write a program that takes a number of steps as an argument and draws right aligned steps with _'#'_ symbol.

For example, _python3 draw_steps.py 4_ should print:

```javascript
   #
  ##
 ###
####
```

```python
import sys

num_steps = int(sys.argv[1])
```

## Quadratic Equation

Write a program that takes coefficients as arguments and finds the root(s) of the corresponding quadratic equation.

For example, _python3 quadratic_equation.py 1 -3 -4_ should print _4_ and _-1_.

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
```

## Median

Create a Jupyter Notebook with a program that generates random number list and finds the median of this list.

For example, the median of the list _numbers = [12, 13, 12, 15]_ is _12.5_.

```python
import random

numbers = []
```
