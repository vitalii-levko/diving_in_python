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

## The Zen of Python

Create a Jupyter Notebook with a program that finds 3 most common words in _The Zen of Python_.

```Python
import this

zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
``` 

## Random10

Using Jupyter Notebook write a program that finds how many iterations were done for the function _random.randint(1, 10)_ to receive duplicate value.

```python
import random

new_number = random.randint(1, 10)
```

## Stringify

Within Jupyter Notebook write a function that takes a list of numbers and returns a list of corresponding string values.

For example, _stringify_list([1, 2, 3])_ should return _['1', '2', '3']_.

```python
def stringify_list(num_list):
    return None

print(stringify_list([1, 2, 3]))
```

## Logger

Create a decorator that takes a log file name as an argument and writes the result of a corresponding function to the specified log file.

For example

```python
@logger('log.txt')
def summator(num_list):
    return sum(num_list)

summator(range(7))

with open('log.txt', 'r') as f:
    print(f.read())
```
