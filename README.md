# Diving in Python

## Basic Types and Constructs
## Code Organization and Environment

### Geolocation Request

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

### Digit Sum

Create a module _solution.py_ that takes a string argument and summarize digits in it.

For example, _python3 solution.py 873_ should print _18_.

```python
import sys

digit_string = sys.argv[1]

```

### Draw Steps

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

### Quadratic Equation

Write a program that takes coefficients as arguments and finds the root(s) of the corresponding quadratic equation.

For example, _python3 quadratic_equation.py 1 -3 -4_ should print _4_ and _-1_.

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
```

## Collections
## Functions

### Median

Create a Jupyter Notebook with a program that generates random number list and finds the median of this list.

For example, the median of the list _numbers = [12, 13, 12, 15]_ is _12.5_.

```python
import random

numbers = []
```

### The Zen of Python

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

### Random10

Using Jupyter Notebook write a program that finds how many iterations were done for the function _random.randint(1, 10)_ to receive duplicate value.

```python
import random

new_number = random.randint(1, 10)
```

### Stringify

Within Jupyter Notebook write a function that takes a list of numbers and returns a list of corresponding string values.

For example, _stringify_list([1, 2, 3])_ should return _['1', '2', '3']_.

```python
def stringify_list(num_list):
    return None

print(stringify_list([1, 2, 3]))
```

### Logger

Create a decorator that takes a log file name as an argument and writes the result of a corresponding function to the specified log file.

For example _summator(range(7)_ should output result _21_ to the file _'log.txt'_.

```python
@logger('log.txt')
def summator(num_list):
    return sum(num_list)

summator(range(7))

with open('log.txt', 'r') as f:
    print(f.read())
```

### Fibonacci Numbers

Create a program that takes a number as an argument and prints all the Fibonacci numbers till the given one.

For example _python3 fibonacci.py 42_ should print _1, 1, 2, 3, 5, 8, 13, 21, 34_.

```python
import sys

pass
```

### Key-Value Storage

Using _argparse_ and _json_ modules create a program that takes key and value as arguments and stores them in a temporary file or takes only key and prints already stored value(s).

E.g. _sotrage.py --key key_name --val value_ should store corresponding pair in JSON format in the file. And _storage.py --key key_name_ should print either a value(s) from the file or _None_ if not exists.

```python
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    pass
```

### To JSON

Within Jupyter Notebook write a decorator _to_json_ that could be used with different fucntions to convert their return value to JSON format.

E.g. _get_data()_ should return '{"data": 42}'.

```python
@to_json
def get_data():
    return {
        'data': 42
    }

get_data()  # returns '{"data": 42}'
```

## Classes and Objects

### Weather Forecast

Create a program that prints a weather forecast for the specified city for the next 10 days.

E.g. _python3 forecast.py kyiv_ should print:

```javascript
[{'date': datetime.datetime(2018, 10, 12, 0, 0), 'high_temp': '17'},
 {'date': datetime.datetime(2018, 10, 13, 0, 0), 'high_temp': '15'},
...
 {'date': datetime.datetime(2018, 10, 21, 0, 0), 'high_temp': '15'}]
```

```python
import pprint

pprint.pprint(forecast)
```

## Work with Errors

### File Reader

Create a module _solution.py_ with the class _FileReader_ inside. Class initializer should take a path to the file on the hard disk as an argument.

Class _FileReader_ should have the _read_ method that returns file's content as a string. When exception _IOError_ occurs this method should return an empty string.

```python
reader = FileReader("example.txt")
print(reader.read())
```

### Cars

Create a program that reads the file 'cars.csv' and creates a list of corresponding objects.

```python
import csv

class CarBase:
    def _init__(self, brand, photo_file_name, carrying):
        pass

    def get_photo_file_ext(self):
        pass

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass

    def get_body_volume(self):
        pass

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass

def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            print(row)

    return car_list
```

## Special Class Methods

### File Interface

Create the _File_ interface that:

* should be initialized with the absolute path
```python
obj = File('/tmp/file.txt')
```
* has the _write_ method
```python
obj.write('line\n')
```
* supports add operation creating new File object and file which contains content of both files 
```python
first = File('/tmp/first')
second = File('/tmp/second')

new_obj = first + second
```
* supports iteration protocol returning file by lines
```python
for line in File('/tmp/file.txt'):
    ...
```
* returns the path when printing it
```python
obj = File('/tmp/file.txt')

print(obj)
'/tmp/file.txt'
```

## The Mechanism of the Classes

### Commission Descriptor

Write the descriptor _Value_ that should be used within _Account_ class. When the _amount_ attribute is being setting the commission should be subtracted appropriately.

```python
class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print(new.account.amount) # 90
```
