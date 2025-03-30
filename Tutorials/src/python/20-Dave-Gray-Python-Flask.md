## +Dave Gray - Python-Flask

## [COURSE](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc)

<details>
<summary>1. Python Operators </summary>

# Python Operators

```py
# Assignment Operators
name = "Dave"
print(name)  # Dave

# Arithmetic Operators
a = 2 + 2
b = 4 - 2
c = 24 / 5
d = 24 // 5
e = round(24 / 5)
f = 24 % 5
g = 2 ** 5

print("a", a, "b", b, "c", c, "d", d, "e", e, "f", f, "g", g)
# a 4 b 2 c 4.8 d 4 e 5 f 4 g 32

meaning = 42
meaning += 1
print(meaning)  # 43
meaning -= 1
print(meaning)  # 42
meaning *= 10
print(meaning)  # 420
meaning /= 10
print(meaning)  # 42.0
meaning = round(meaning)
print(meaning)  # 42

# Comparison Operators
print(2 == 2)  # True
print(2 != 2)   # False
print(3 != 2)  # True
print(10 > 2)  # True
print(10 < 2)  # False
print(10 >= 10)  # True

if meaning > 10:
    print('Right on!')  # Right on!
else:
    print('Not today')

# Ternary Operator
print('Great!') if meaning > 10 else print('Not today')
# Great!

```

<img width="1136" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5a0fd9b7-aa1b-43a6-9f6b-93698862cb56">

# #END</details>

<details>
<summary>2. Data Type - String </summary>

# Data Type - String

[https://github.com/omeatai/src-python-flask-django/commit/786257d573dc94eea4ad0f451ed2a64fea47244c](https://github.com/omeatai/src-python-flask-django/commit/786257d573dc94eea4ad0f451ed2a64fea47244c)

```py
# String data type

# literal assignment
first = "Dave"
last = "Johnson"

print(first, type(first))  # Dave <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str))  # True

# constructor function
pizza = str("Pepperoni")
print(pizza, isinstance(pizza, str))  # Pepperoni True

# Concatenation
fullname = first + " " + last
fullname += "!"
print(fullname)  # Dave Johnson!

# Casting a number to a string
decade = str(1980)
print(decade, type(decade))  # 1980 <class 'str'>
statement = "I like rock music from the " + decade + "s."
print(statement)  # I like rock music from the 1980s.

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.   All good?
                    - Dave
'''
print(multiline)
# Hey, how are you?
#
# I was just checking in.   All good?
#                    - Dave

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this \\located?'
print(sentence)
# I'm back at work!	Hey!
#
# Where's this \located?

# String Methods
first = "Dave"
print(first)  # Dave
print(first.lower())  # dave
print(first.upper())  # DAVE

multiline = "hey, how are you?"
print(multiline)  # hey, how are you?
print(multiline.title())  # Hey, How Are You?
print(multiline.replace("hey", "Welcome"))  # Welcome, how are you?
print(len(multiline))  # 17
multiline += "                                        "
multiline = "                  " + multiline
print(len(multiline))  # 75
print(len(multiline.strip()))  # 17
print(len(multiline.lstrip()))  # 57
print(len(multiline.rstrip()))  # 35

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("Tea".ljust(16, ".") + "$1".rjust(4))

# ========MENU========
# Coffee..........  $1
# Muffin..........  $2
# Cheesecake......  $4
# Tea.............  $1

# string index values
first = "Dave"
print(first[1])  # a
print(first[-1])  # e
print(first[1:-1])  # av
print(first[1:])  # ave

# Some methods return boolean data
print(first.startswith("D"))  # True
print(first.endswith("Z"))  # False

```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3338cc92-727b-42ef-8921-afd7e43f0e67">

# #END</details>

<details>
<summary>3. Data Type - Boolean </summary>

# Data Type - Boolean

[https://github.com/omeatai/src-python-flask-django/commit/a379210ee24c5a461d223e4e642654c0fa30b462](https://github.com/omeatai/src-python-flask-django/commit/a379210ee24c5a461d223e4e642654c0fa30b462)

```py
# Boolean data type
x = bool(False)
my_value = True

print(type(x))  # <class 'bool'>
print(isinstance(my_value, bool))  # True
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/397f15c1-ae2c-4dd4-90b9-979c69046bb6">

# #END</details>

<details>
<summary>4. Data Type - Numeric </summary>

# Data Type - Numeric

[https://github.com/omeatai/src-python-flask-django/commit/1586574ec08840c3a77cb2b0d93d8667af4f9ed0](https://github.com/omeatai/src-python-flask-django/commit/1586574ec08840c3a77cb2b0d93d8667af4f9ed0)

```py
# Numeric data types
import math

# integer type
price = 100
best_price = int(80.001)
print(type(price))  # <class 'int'>
print(isinstance(best_price, int))  # True

# float type
gpa = 3.28
y = float(1)
print(type(gpa))  # <class 'float'>
print(isinstance(y, float))  # True

# complex type
comp_value = 5+3j
print(type(comp_value))  # <class 'complex'>
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0

# Built-in functions for numbers
gpa = 3.28
print(abs(gpa * -1))  # 3.28
print(round(gpa))  # 3
print(round(gpa, 1))  # 3.3
print(math.pi)  # 3.141592653589793
print(math.sqrt(64))  # 8.0
print(math.ceil(gpa))  # 4
print(math.floor(gpa))  # 3

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))  # <class 'int'>
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/28ca3892-458f-498f-b3c7-6cae9a153cd1">

# #END</details>

<details>
<summary>5. User Input & Control Flow </summary>

# User Input & Control Flow

[https://github.com/omeatai/src-python-flask-django/commit/7493f2cdb60aad3ef4098079075f9d7e973dd24a](https://github.com/omeatai/src-python-flask-django/commit/7493f2cdb60aad3ef4098079075f9d7e973dd24a)

```py
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


player_choice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")  # "2"

player = int(player_choice)  # 2

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print(f"You chose {str(RPS(player)).replace("RPS.", "")}.")
# You chose PAPER.
print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.")
# Python chose ROCK.
print("")

result = (player, computer)

if result == (1, 3) or result == (2, 1) or result == (3, 2):
    print("🥳😜 Congrats! You win!  ") # 🥳😜 Congrats! You win!
elif player == computer:
    print("😎 It's a tie!")
else:
    print("😡 Python wins!")

# References:
# print(RPS(2))           # RPS.PAPER
# print(RPS.ROCK)         # RPS.ROCK
# print(RPS['ROCK'])      # RPS.ROCK
# print(RPS.ROCK.value)   # 1
# sys.exit()

# value = input("Please enter a your name: ")
# print(value)
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/81dcb299-16bc-4464-b192-0349a4bcbe7b">

# #END</details>

<details>
<summary>6. Python Lists </summary>

# Python Lists

[https://github.com/omeatai/src-python-flask-django/commit/7f68127e2a893544bf4bc3ea5913edc1d8f36a36](https://github.com/omeatai/src-python-flask-django/commit/7f68127e2a893544bf4bc3ea5913edc1d8f36a36)

```py
# Python Lists

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
empty_list = []

print("Dave" in users)  # True
print("Dave" in data)  # True
print("Dave" in empty_list)  # False
print("")

print(users[0])  # Dave
print(users[-2])  # John
print("")

# FInd index of value
print(users.index('Sara'))  # 2
print("")

# Slice from List
print(users[0:2])  # ['Dave', 'John']
print(users[1:])  # ['John', 'Sara']
print(users[-3:-1])  # ['Dave', 'John']
print(users[:])  # ['Dave', 'John', 'Sara']
print("")

# Find length of List
print(len(data))  # 3
print("")

# Append/Extend to List
users.append('Elsa')
print(users)  # ['Dave', 'John', 'Sara', 'Elsa']

users += ['Jason']
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']

users.extend(['Robert', 'Jimmy'])
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

data = ['Alex', 'Peter']
users.extend(data)
print(users)
# ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy', 'Alex', 'Peter']
print("")

# Insert to List
users = ['Fred', 'John']

users.insert(0, 'Bob')
print(users)  # ['Bob', 'Fred', 'John']

users[2:2] = ['Eddie', 'Alex', 'Bob', 'Stewart']
print(users)  # ['Bob', 'Fred', 'Eddie', 'Alex', 'Bob', 'Stewart', 'John']

users[2:4] = ['Robert', 'JPJ']
print(users)  # ['Bob', 'Fred', 'Robert', 'JPJ', 'Bob', 'Stewart', 'John']
print("")

# Remove from List
users.remove('Bob')
print(users)  # ['Fred', 'Robert', 'JPJ', 'Bob', 'Stewart', 'John']

popped = users.pop()
print(users)  # ['Fred', 'Robert', 'JPJ', 'Bob', 'Stewart']
print(popped)  # John

popped = users.pop(2)
print(users)  # ['Fred', 'Robert', 'Bob', 'Stewart']
print(popped)  # JPJ

del users[0]
print(users)  # ['Robert', 'Bob', 'Stewart']

# del data
data.clear()
print(data)  # []
print("")

# Sort List
users = ['Bob', 'Fred', 'John']
print(users)  # ['Bob', 'Fred', 'John']

users[1:2] = ['eddie']
print(users)  # ['Bob', 'eddie', 'John']

users.sort()
print(users)  # ['Bob', 'John', 'eddie']

users.sort(key=str.lower)
print(users)  # ['Bob', 'eddie', 'John']
print("")

nums = [4, 42, 78, 1, 5]
print(nums)  # [4, 42, 78, 1, 5]
nums.reverse()
print(nums)  # [5, 1, 78, 42, 4]

print(sorted(nums, reverse=True))  # [78, 42, 5, 4, 1]
print(nums)  # [5, 1, 78, 42, 4]

# nums.sort(reverse=True)
# print(nums)

# Copy List
nums = [4, 42, 78, 1, 5]
nums_copy1 = nums.copy()
print(nums_copy1)  # [4, 42, 78, 1, 5]

nums_copy2 = list(nums)
print(nums_copy2)  # [4, 42, 78, 1, 5]

nums_copy3 = nums[:]
print(nums_copy3)  # [4, 42, 78, 1, 5]

nums.sort()
print(nums)  # [1, 4, 5, 42, 78]
print(type(nums))  # <class 'list'>

my_list = list([1, "Neil", True])
print(my_list)  # [1, 'Neil', True]
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/78898673-cb21-4d34-96cf-290e38492d83">

# #END</details>

<details>
<summary>7. Python Tuples </summary>

# Python Tuples

[https://github.com/omeatai/src-python-flask-django/commit/f08b7725b409e7bb090a944e79f27d9397fb4a39](https://github.com/omeatai/src-python-flask-django/commit/f08b7725b409e7bb090a944e79f27d9397fb4a39)

```py
# Tuples

my_tuple = tuple(('Dave', 42, True))
print(my_tuple)  # ('Dave', 42, True)

another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)  # (1, 4, 2, 8, 2, 2)

print(type(my_tuple))  # <class 'tuple'>
print(type(another_tuple))  # <class 'tuple'>
print("")

new_list = list(my_tuple)
print(new_list)  # ['Dave', 42, True]
new_list.append('Neil')
print(new_list)  # ['Dave', 42, True, 'Neil']
new_tuple = tuple(new_list)
print(new_tuple)  # ('Dave', 42, True, 'Neil')
print("")

# unpacking Tuples
another_tuple = (1, 4, 2, 8, 2, 2)
print(another_tuple)  # (1, 4, 2, 8, 2, 2)
(one, *two, hey) = another_tuple
print(one)  # 1
print(two)  # [4, 2, 8, 2]
print(hey)  # 2
print(another_tuple.count(2))  # 3
```

<img width="1255" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3ded761d-8492-4465-8125-03199a64a77f">

# #END</details>

<details>
<summary>8. Python Dictionaries </summary>

# Python Dictionaries

[https://github.com/omeatai/src-python-flask-django/commit/dd597e8ea24bb80f983e060984a3871638c2c4df](https://github.com/omeatai/src-python-flask-django/commit/dd597e8ea24bb80f983e060984a3871638c2c4df)

```py
# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)  # {'vocals': 'Plant', 'guitar': 'Page'}
print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
print(type(band))  # <class 'dict'>
print(len(band))  # 2
print("")

# Access items
print(band["vocals"])  # Plant
print(band.get("guitar"))  # Page
print("")

# list all keys
print(band.keys())  # dict_keys(['vocals', 'guitar'])
# list all values
print(band.values())  # dict_values(['Plant', 'Page'])
# list of key/value pairs as tuples
print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
print("")

# verify a key exists
print("guitar" in band)  # True
print("triangle" in band)  # False
print("")

# Change and Add values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}
print("")

# Remove items
print(band.pop("bass"))  # JPJ
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
band["drums"] = "Borg"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Borg'}
print(band.popitem())  # ('drums', 'Borg')
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print("")

# Delete and clear
band["drums"] = "Bonham"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}
del band["drums"]
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
band2 = dict(vocals="Plant", guitar="Page")
print(band2)  # {'vocals': 'Plant', 'guitar': 'Page'}
band2.clear()
print(band2)  # {}
del band2
print("")

# Copy dictionaries
band2 = band.copy()
band2["drums"] = "Dave"
print(band)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print(band2)  # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}
band3 = dict(band)
print(band3)  # {'vocals': 'Coverdale', 'guitar': 'Page'}
print("")

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
# {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
print(band["member1"]["name"])  # Plant
print("")

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)  # {1, 2, 3, 4}
print(nums2)  # {1, 2, 3, 4}
print(type(nums))  # <class 'set'>
print(len(nums))  # 4
print("")

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}
print("")

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)  # {False, 1, 2, 3, 4}
print("")

# check if a value is in a set
# but you cannot refer to an element in the set with an index position or a key
print(2 in nums)  # True
print("")

# Add a new element to a set
nums.add(8)
print(nums)  # {False, 1, 2, 3, 4, 8}

# Add elements from one set to another
# you can use update with lists, tuples, and dictionaries, too.
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
my_new_set = one.union(two)
print(my_new_set)  # {1, 2, 3, 5, 6, 7}

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)  # {2, 3}

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)  # {1, 4}

```

<img width="1440" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/26921db4-bfe0-487b-a372-2538c494eb90">

# #END</details>

<details>
<summary>9. Python While & For Loops </summary>

# Python While & For Loops

[https://github.com/omeatai/src-python-flask-django/commit/c81b164f520097cb24a7e179f4e92c506f84ec1e](https://github.com/omeatai/src-python-flask-django/commit/c81b164f520097cb24a7e179f4e92c506f84ec1e)

```py
# while loop
value = 1
arr = []
while value <= 10:
    arr.append(value)
    value += 1
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while loop with break
value = 1
arr = []
while value <= 10:
    if value == 5:
        break
    arr.append(value)
    value += 1
print(arr)  # [1, 2, 3, 4]

# while loop with continue
value = 0
arr = []
while value <= 10:
    value += 1
    if value == 5:
        continue
    arr.append(value)
else:
    print("Value is now " + str(value))  # Value is now 11
print(arr)  # [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
print("")

# for loop on List
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)
# Dave
# Sara
# John

# for loop on String
y = ""
for x in "Mississippi":
    y += x
print(y)  # Mississippi

# for loop on List with break
names = ["Dave", "Sara", "John"]
for x in names:
    if x == "Sara":
        break
    print(x)  # Dave

# for loop on List with continue
names = ["Dave", "Sara", "John"]
for x in names:
    if x == "Sara":
        continue
    print(x)
print("")
# Dave
# John

# for loop in range
y = ""
for x in range(4):
    y += str(x)
print(y)  # 0123

# for loop in range with start/stop
y = ""
for x in range(2, 4):
    y += str(x)
print(y)
print("")  # 23

# for loop in range with start/stop/step
y = []
for x in range(5, 101, 5):
    y.append(x)
else:
    print("Glad that\'s over!")
print(y)
# Glad that's over!
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
print("")

# nested for loop
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
# Dave codes.
# Dave eats.
# Dave sleeps.
# Sara codes.
# Sara eats.
# Sara sleeps.
# John codes.
# John eats.
# John sleeps.

# for action in actions:
#     for name in names:
#         print(name + " " + action + ".")

```

<img width="1440" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/00f1a9e4-0010-4bfd-bcef-5cc6825ccb9c">

# #END</details>

<details>
<summary>10. Python Functions </summary>

# Python Functions

```py

```

```py

```

```py

```

```py

```

# #END</details>


