# reselpy_randomizer

A simple utility module for providing random data.

The purpose of this project is twofold. The first purpose is to provide me with a structured way to learn Python. The second purpose is make a modest contribution to those programmers that might need a utility for generating random data.

The **reselpy_randomizer** provides a set of methods that generate random data. The data generated by the reselpy_randomizer are:

* First Name
* Last Name
* Email
* US City, according to city, state, postal code and lat/long, URL for map
* Integer
* Float
* String of random length, with random characters
* Phrase poopulate with random words

# Examples

The follow sections provide a listing of each method with examples

## Import statement

```python
from randomizer.randomizer import Randomizer
```

## Randomizer.get_random_first_name()

Gets a random name from a list of 5000 common first names

**Example**
```python
 str = Randomizer.get_random_first_name()
 ```
**returns** `'Britt'`


## Randomizer.get_random_last_name()

Gets a random name from a list of 5000 common last names

**Example**
```python
str = Randomizer.get_random_last_name()
 ```
**returns** `'Hoppin'`



## Randomizer.get_random_email(first_name, last_name)

**Example**
```python
 first_name = Randomizer.get_random_first_name()
 last_ name = Randomizer.get_random_last_name()
 email = Randomizer.get_random_email(first_name, last_name)
  ```
**returns** `'Alta.Jann@keyed.tv'`


## Randomizer.get_random_city()

Gets a random city according to the United States Postal Service Zip Code direcctory

**Example**
```python
city = Randomizer.get_random_city()
 ```

**returns**

 ```javascript
  {
    'postalcode': '10006',
    'city': 'New York', 
    'state': 'NY', 
    'longitude': '40.71',
    'latitude': '-73.99'
  }
```

## Randomizer.get_random_int(min, max)

**Example**
```python
min = 1
max = 100
int = Randomizer.get_random_int(min, max)
 ```
**returns** `99`


## Randomizer.get_random_float(min, max)

**Example**
```python
min = 1.25
max = 87.0124
flt = Randomizer.get_random_float(min, max)
 ```
**returns** `51.80303608846783`


## Randomizer.get_random_string(max_length)

**Example**
```python
string_length = 20
str = Randomizer.get_random_string(string_length)
 ```
**returns** `'gF&77Q*$No!M2tB@#8*O'`



## Randomizer.get_random_phrase(number_of_words)

**Example**
```python
number_of_words = 12
phrase = Randomizer.get_random_phrase(number_of_words)
 ```

**returns**

`'capsheaf millenarist levoversion yawnful dvandva extradition Feramorz decameral begut gallowglass octacolic daggerlike'`


