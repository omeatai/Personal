# Udemy-Complete-Python-Developer-Course-ZTM

## [COURSE](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/)

<details>
  <summary>1. Introduction </summary>

# Python DataTypes

```pybs
int
float
bool
str
list
tuple
set
dict
```

# Operator Precedence

```py
print ((2013-3) ) + 2 ** 2

# ()
# **
# * /
# + -
```

# binary conversion

```py
print(bin(5))
print(int('0b101', 2))
```

### output:

```py
# 0b101
# 5
```

# augmented assignment operator

```py
some_value = 5
some_value += 2
print(some_value)
```

### output:

```py
# 7
```

# Type conversion

```py
a = str(100)
b = int(a)
c = type(b)
print(c)
```

### output:

```py
# <class 'int'>
```

# Escape Sequence

```py
weather = "It\'s \"kind of\" sunny!"
print(weather)
```

### output:

```py
# It's "kind of" sunny!
```

# Escape Sequence with tab and nextline

```py
weather = "\t It\'s \"kind of\" sunny \n Hope you have a good day!"
print(weather)
```

### output:

```py
#     It's "kind of" sunny
# Hope you have a good day!
```

</details>

<details>
  <summary>2. Python Strings </summary>

# formatted strings

```py
name = 'Johnny'
age = 55
print(f'hi {name}. You are {age} years old')
```

### output:

```py
# hi Johnny. You are 55 years old
```

# formatted strings with format method

```py
name = 'Johnny'
age = 55
print('Hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100))
```

### output:

```py
# Hi Sally. You are 100 years old.
```

# String Indexes

```py
selfish = 'me me me'
         # 01234567
print(selfish[7])
```

### output:

```py
# e
```

# String Indexes with start-stop-step

```py
selfish = '01234567'
         # 01234567
# [start:stop:stepover]
print(selfish[0:8:1])
```

### output:

```py
# 01234567
```

# String Indexes with reverse option

```py
selfish = '01234567'
         # 01234567
# [start:stop:stepover]
print(selfish[::-1])
```

### output:

```py
# 76543210
```

# String Method - Upper()

```py
quote = 'to be or not to be'
print(quote.upper())
```

### output:

```py
# TO BE OR NOT TO BE
```

# String Method - Capitalize()

```py
quote = 'to be or not to be'
print(quote.capitalize())
```

### output:

```py
# To be or not to be
```

# String Method - Lower()

```py
quote = 'to be or not to be'
print(quote.lower())
```

### output:

```py
# to be or not to be
```

# String Method - Find()

```py
quote = 'to be or not to be'
print(quote.find("not"))
```

### output:

```py
# 9
```

# String Method - Replace()

```py
quote = 'to be or not to be'
print(quote.replace("be", "me"))
```

### output:

```py
# to me or not to me
```

# Task 1 - Birth year

```py
birth_year = int(input('what year were you born? '))
age = 2023 - birth_year
print(f"Your age is {age} years.")
```

### output:

```py
# what year were you born? 1991
# Your age is 32 years.
```

# Task 2 - Password checker

```py
username = input("Enter your username: ")
password = input("Enter your password: ")
password_length = len(password)
print(f'{username.title()}, your password {password_length * "*"} is {password_length} letters long.')
```

### output:

```py
# Enter your username: ifeanyi
# Enter your password: secret
# Ifeanyi, your password ****** is 6 letters long.
```

</details>

<details>
  <summary>3. Python Lists </summary>

# Python List

```py
amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

print(amazon_cart)
```

### output:

```py
# ['notebooks', 'sunglasses', 'toys', 'grapes']
```

# List slicing

```py
amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

print(amazon_cart[0::2])
```

### output:

```py
# ['notebooks', 'toys']
```

# List mutability

```py
amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

amazon_cart[0] = 'laptop'
print(amazon_cart)
```

### output:

```py
# ['laptop', 'sunglasses', 'toys', 'grapes']
```

# Copy a List

```py
amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
# new_cart = amazon_cart.copy()
new_cart[0] = 'gum'

print(amazon_cart)
print(new_cart)
```

### output:

```py
# ['laptop', 'sunglasses', 'toys', 'grapes']
# ['gum', 'sunglasses', 'toys', 'grapes']
```

# List Matrix

```py
matrix = [
[1,5,1],
[0,1,0],
[1,0,1]
]

print(matrix[0][1])
```

### output:

```py
# 5
```

# List Methods - append()

```py
basket = [1,2,3,4,5]
basket.append(6)

print(basket)
```

### output:

```py
# [1, 2, 3, 4, 5, 6]
```

# List Methods - insert()

```py
basket = [1,2,3,4,5]
basket.insert(1, 100)

print(basket)
```

### output:

```py
# [1, 100, 2, 3, 4, 5]
```

# List Methods - extend()

```py
basket = [1,2,3,4,5]
basket.extend([90,91,92,93])

print(basket)
```

### output:

```py
# [1, 2, 3, 4, 5, 90, 91, 92, 93]
```

# List Methods - pop()

```py
basket = [1,2,3,4,5]
basket.pop()

print(basket)
```

### output:

```py
# [1, 2, 3, 4]
```

```py
basket = [1,2,3,4,5]
value_popped = basket.pop(2)

print(basket)
print(value_popped)
```

### output:

```py
# [1, 2, 4, 5]
# 3
```

# List Methods - remove()

```py
basket = [1,2,3,4,5]
basket.remove(4)

print(basket)
```

### output:

```py
# [1, 2, 3, 5]
```

# List Methods - clear()

```py
basket = [1,2,3,4,5]
basket.clear()

print(basket)
```

### output:

```py
# []
```

# List Methods - index()

```py
basket = ['a','b','c','d','e']
position = basket.index('c')

print(position)
```

### output:

```py
# 2
```

```py
basket = ['a','b','c','d','e']
position = basket.index('b', 0, 2)

print(position)
```

### output:

```py
# 1
```

# List Methods - 'in' keyword

```py
basket = ['a','b','c','d','e']

print('x' in basket)
```

### output:

```py
# False
```

# List Methods - count()

```py
basket = ['a','b','c','d','e', 'd']

print(basket.count('d'))
```

### output:

```py
# 2
```

# List Methods - sort()

```py
basket = ['a','b','c','d','e', 'd', 'a']
basket.sort()

print(basket)
```

### output:

```py
# ['a', 'a', 'b', 'c', 'd', 'd', 'e']
```

# List Methods - reverse()

```py
basket = ['a','b','c','d','e', 'd', 'a']
# basket = basket[::-1]
basket.reverse()

print(basket)
```

### output:

```py
# ['a', 'd', 'e', 'd', 'c', 'b', 'a']
```

# List Methods - sort() and reverse()

```py
basket = ['a','b','c','d','e', 'd', 'a']
basket.sort(key=None, reverse=True)

print(basket)
```

### output:

```py
# ['e', 'd', 'd', 'c', 'b', 'a', 'a']
```

# List Methods - sorted()

```py
basket = ['a','b','c','d','e', 'd', 'a']
new_basket = sorted(basket)

print(new_basket)
```

### output:

```py
# ['a', 'a', 'b', 'c', 'd', 'd', 'e']
```

# List Methods - sorted() and reverse()

```py
basket = ['a','b','c','d','e', 'd', 'a']
new_basket = sorted(basket, reverse=True)

print(new_basket)
```

### output:

```py
# ['e', 'd', 'd', 'c', 'b', 'a', 'a']
```

# List Methods - copy()

```py
basket = ['a','b','c','d','e', 'd', 'a']
new_basket = basket.copy()
# new_basket = basket[:]

print(new_basket)
```

### output:

```py
# ['a', 'b', 'c', 'd', 'e', 'd', 'a']
```

# List Methods - range()

```py
numbers = range(1,10)
number_list = list(numbers)

print(numbers)
print(number_list)
```

### output:

```py
# range(1, 10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# List Methods - join()

```py
words = ['hi','my','name','is','ifeanyi']
sentence = "-".join(words)

print(sentence)
```

### output:

```py
# hi-my-name-is-ifeanyi
```

# List unpacking

```py
a,b,c,_,*last_two = [1,2,3,4,5,6]

print(a)
print(b)
print(c)
print(last_two)
```

### output:

```py
# 1
# 2
# 3
# [5, 6]
```

</details>

<details>
  <summary>4. Python Dictionaries </summary>

# Dictionary

```py
dictionary = {
'a': [1,2,3],
'b': 'hello',
'x': True
}

my_list = [
{
  'a': [1,2,3],
  'b': 'hello',
  'x': True
},
{
  'a': [4,5,6],
  'b': 'hello',
  'x': True
}
]

print(dictionary['a'][1])
print(my_list[0]['a'])
```

### output:

```py
# 2
# [1, 2, 3]
```

# Dictionary Methods - get()

```py
user = {
'basket': [1,2,3],
'greet': 'hello'
}

print (user.get('age', 'Does not Exist!'))
```

### output:

```py
# Does not Exist!
```

# Dictionary Methods - dict()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

user2 = dict(name='John')
print(user2)
```

### output:

```py
# {'name': 'John'}
```

# Dictionary Methods - keys() and values()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

print('age' in user.keys())
print(20 in user.values())
```

### output:

```py
# True
# True
```

# Dictionary Methods - items()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

print(user.items())
for item in user.items():
  print(item)
```

### output:

```py
# dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
# ('basket', [1, 2, 3])
# ('greet', 'hello')
# ('age', 20)
```

# Dictionary Methods - clear()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

user.clear()
print(user)
```

### output:

```py
# {}
```

# Dictionary Methods - copy()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

user2 = user.copy()
print(user2)
```

### output:

```py
# {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
```

# Dictionary Methods - pop()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

removed_item = user.pop('age')

print(removed_item)
print(user)
```

### output:

```py
# 20
# {'basket': [1, 2, 3], 'greet': 'hello'}
```

# Dictionary Methods - popitem()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

removed_item = user.popitem()

print(removed_item)
print(user)
```

### output:

```py
# ('age', 20)
# {'basket': [1, 2, 3], 'greet': 'hello'}
```

# Dictionary Methods - update()

```py
user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

user.update({'age': 55})

print(user)
```

### output:

```py
# {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55}
```

</details>

<details>
  <summary>5. Python Tuples </summary>

# Tuple

```py
my_tuple = (1,2,3,4,5)

print(5 in my_tuple)
```

### output:

```py
# True
```

# Tuple - slicing

```py
my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]

print(new_tuple)

```

### output:

```py
# [2]
```

# Tuple - unpacking

```py
my_tuple = (1,2,3,4,5,6,7)

a,b,c,_,*others = my_tuple

print(a)
print(b)
print(c)
print(others)
```

### output:

```py
# 1
# 2
# 3
# [5, 6, 7]
```

# Tuple Methods - count()

```py
my_tuple = (1,2,3,4,5,5,6,6,7)

print(my_tuple.count(5))
```

### output:

```py
# 2
```

# Tuple Methods - index()

```py
my_tuple = (1,2,3,4,5,5,6,6,7)

print(my_tuple.index(5))
```

### output:

```py
# 4
```

# Tuple Methods - len()

```py
my_tuple = (1,2,3,4,5,5,6,6,7)

print(len(my_tuple))
```

### output:

```py
# 9
```

</details>

<details>
  <summary>6. Python Sets </summary>

# Set

```py
my_set = {1, 2, 3, 4, 5, 100}

print(my_set)
```

### output:

```py
# {1, 2, 3, 4, 5, 100}
```

# Set Methods - add()

```py
my_set = {1, 2, 3, 4, 5, 100}
my_set.add(200)

print(my_set)
```

### output:

```py
# {1, 2, 3, 4, 5, 100, 200}
```

# Set Methods - copy()

```py
my_set = {1, 2, 3, 4, 5, 100}
new_set = my_set.copy()

print(new_set)
```

### output:

```py
# {1, 2, 3, 4, 5, 100}
```

# Set Methods - clear()

```py
my_set = {1, 2, 3, 4, 5, 100}
my_set.clear()

print(my_set)
```

### output:

```py
# set()
```

# Set Methods - difference()

```py
my_set = {1, 2, 3, 4, 5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
```

### output:

```py
# {1, 2, 3}
```

# Set Methods - discard()

```py
my_set = {1, 2, 3, 4, 5}
your_set = {4,5,6,7,8,9,10}

my_set.discard(5)
print(my_set)
```

### output:

```py
# {1, 2, 3, 4}
```

# Set Methods - difference_update()

```py
my_set = {1, 2, 3, 4, 5}
your_set = {4,5,6,7,8,9,10}

my_set.difference_update(your_set)
print(my_set)
```

### output:

```py
# {1, 2, 3}
```

# Set Methods - intersection()

```py
my_set = {1, 2, 3, 4, 5}
your_set = {4,5,6,7,8,9,10}

print(my_set.intersection(your_set))
print(my_set & your_set)
```

### output:

```py
# {4, 5}
# {4, 5}
```

# Set Methods - isdisjoint()

```py
my_set = {1, 2, 3}
your_set = {4,5,6,7,8,9,10}

print(my_set.isdisjoint(your_set))
```

### output:

```py
# True
```

# Set Methods - union()

```py
my_set = {1, 2, 3, 4, 5}
your_set = {4,5,6,7,8,9,10}

print(my_set.union(your_set))
print(my_set | your_set)
```

### output:

```py
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

# Set Methods - issubset()

```py
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.issubset(your_set))
```

### output:

```py
# True
```

# Set Methods - issuperset()

```py
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print(your_set.issuperset(my_set))
```

### output:

```py
# True
```

</details>

<details>
  <summary>7. Python Ternary Operator </summary>

# Using Ternary Operator

```py
# condition_if_true if condtion else condition_if_false

is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)
```

### output:

```py
# not allowed to message
```

</details>

<details>
  <summary>8. For Loops </summary>

# Using For Loops

```py
for item in (1,2,3,4,5):
  print (item)
```

### output:

```py
# 1
# 2
# 3
# 4
# 5
```

# Using Multiple For Loops

```py
for item in (1,2,3,4):
  for x in ['a', 'b', 'c']:
    print(item, x)
```

### output:

```py
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
```

</details>

<details>
  <summary>9. Dictionary Iterables </summary>

# Iterating over a dictionary:

```py
user = {
'name': 'Golem',
'age': 5006,
'can_swim': False
}

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)
```

### output:

```py
# ('name', 'Golem')
# ('age', 5006)
# ('can_swim', False)

# Golem
# 5006
# False

# name
# age
# can_swim
```

# Iterating via key and values:

```py
user = {
'name': 'Golem',
'age': 5006,
'can_swim': False
}

for key, value in user.items():
  print(key, value)
```

### output:

```py
# name Golem
# age 5006
# can_swim False
```

</details>

<details>
  <summary>10. Python Range </summary>

# Using Range:

```py
for number in range(0, 10):
  print(number)
```

### output:

```py
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

# Using Range with Step:

```py
for _ in range(0, 10, 2):
  print(_)
```

### output:

```py
# 0
# 2
# 4
# 6
# 8
```

# Using Inverse Range with Step:

```py
for _ in range(10, 0, -2):
  print(_)
```

### output:

```py
# 10
# 8
# 6
# 4
# 2
```

# Generating a List with Range:

```py
for _ in range(2):
  print(list(range(10)))
```

### output:

```py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</details>

<details>
  <summary>11. Python Enumerate </summary>

# Using Enumeration

```py
for i,char in enumerate('Helllooo'):
  print(i, char)
```

### output:

```py
# 0 H
# 1 e
# 2 l
# 3 l
# 4 l
# 5 o
# 6 o
# 7 o
```

</details>

<details>
  <summary>12. Python While Loop </summary>

# Using While Loops

```py
i = 0
while i < 10:
  print(i)
  i += 1
  # break
else:
  print('done with all the work')
```

### output:

```py
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# done with all the work
```

# Using While Loops with conditionals

```py
while True:
  response = input('say something: ')
  if (response == 'bye') :
    break
```

### output:

```py
# say something: Hi
# say something: hi
# say something: hello
# say something: hi
# say something: bye
```

# Task 1

### Solution 1

```py
#Exercise!
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,1,1,1,0,0],
[0,0,1,1,1,0,0]
]

for row in picture:
  res = ""
  for col in row:
    if col == 0:
      res += " "
    else:
      res += "*"
  print(res)
```

### output:

```py
#    *
#   ***
#  *****
# *******
#   ***
#   ***
```

### Solution 2

```py
#Exercise!
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,1,1,1,0,0],
[0,0,1,1,1,0,0]
]

for row in picture:
  for col in row:
    if col == 0:
      print(" ", end="")
    else:
      print("*", end="")
  print("", end="\n")
```

### output:

```py
#    *
#   ***
#  *****
# *******
#   ***
#   ***
```

# Task 2

### Exercise: Check for duplicates in list

```py
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)
```

### output:

```py
# ['b', 'n']
```

</details>

<details>
  <summary>13. Python Functions </summary>

# Creating functions

```py
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
  ]

def show_tree():
  for row in picture:
    for col in row:
      if col == 0:
        print(" ", end="")
      else:
        print("*", end="")
    print("")
  print("")

show_tree()
show_tree()
show_tree()
```

### output:

```py
#    *
#   ***
#  *****
# *******
#    *
#    *

#    *
#   ***
#  *****
# *******
#    *
#    *

#    *
#   ***
#  *****
# *******
#    *
#    *
```

# Parameters and Arguments

```py
#parameters
def say_hello(name, emoji):
  print(f'Hellllooooo {name} {emoji}!')

#arguments
say_hello('Ifeanyi', '😜')
say_hello('Dan', '😜')
say_hello('Emily', '😜')
```

### output:

```py
# Hellllooooo Ifeanyi 😜!
# Hellllooooo Dan 😜!
# Hellllooooo Emily 😜!
```

# Positional Arguments vs Keyword Arguments

```py
#parameters
def say_hello(name, emoji):
  print(f'Hellllooooo {name} {emoji}!')

# positional arguments
say_hello('Ifeanyi', '😜')
say_hello('Dan', '😜')
say_hello('Emily', '😜')

# keyword arguments
say_hello(name='Bibi', emoji='😜')
```

### output:

```py
# Hellllooooo Ifeanyi 😜!
# Hellllooooo Dan 😜!
# Hellllooooo Emily 😜!
# Hellllooooo Bibi 😜!
```

# Default parameters

```py
# Default parameters
def say_hello(name="Ben", emoji="😜"):
  print(f'Hellllooooo {name} {emoji}!')

# positional arguments
say_hello()
say_hello()
say_hello('Emily', '😜')

# keyword arguments
say_hello(name='Bibi', emoji='😜')
```

### output:

```py
# Hellllooooo Ben 😜!
# Hellllooooo Ben 😜!
# Hellllooooo Emily 😜!
# Hellllooooo Bibi 😜!
```

# Return Keyword

```py
def sum(num1, num2):
  return num1 + num2

# Should do one thing really well.
# Should return something.

total = sum(10,5)
print(sum(10, total))
```

### output:

```py
# 25
```

# Return Keyword 2

```py
def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func(num1, num2)

total = sum(10, 20)
print(total)
```

### output:

```py
# 30
```

# Docstrings

```py
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


test('!!!!')
```

### output:

```py
# !!!!
```

# Help Function

```py
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


help(test)
```

### output:

```py
# Help on function test in module __main__:

# test(a)
#     Info: this function tests and prints param a
```

# Docstring dunder method

```py
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


print(test.__doc__)
```

### output:

```py
#   Info: this function tests and prints param a
```

# \*args

```py
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5))
```

### output:

```py
# (1, 2, 3, 4, 5)
# 15
```

# \*\*kwargs

```py
def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs
```

### output:

```py
# 30
```

# Walrus Operator

```py
a = 'helloooooo0000'

if ((n := len(a)) > 10):
  print(f"too long {n} elements")
```

### output:

```py
# too long 14 elements
```

# Global Scope

```py
total = 0

def count():
    global total
    total += 1
    return total

print(count())
```

### output:

```py
# 1
```

# Non-local Scope

```py
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
```

### output:

```py
# inner: nonlocal
# outer: nonlocal
```

</details>

<details>
  <summary>14. Terminal Commands </summary>

# ls, pwd, cd, clear

```py
# bash$ ls
# Applications Google Drive Pictures
# Desktop Library Public
# Documents Movies
# Downloads Music

# bash$ pwd
# /Users/aneagoie

# bash$ cd Desktop
# bash$ ls
# untitled folder

# bash$ cd ..
# bash$ls
# Applications Google Drive Pictures
# Desktop Library Public
# Documents Movies
# Downloads Music

# bash$ clear
```

# root directory - cd /

```py
# bash$ cd /
# bash$ ls
# Applications
# Library
# Network
# System
# Users
# Volumes
# bin
# cores
# dev
# etc
# home
```

# user directory - cd ~

```py
# bash$ cd ~
# bash$ ls
# Applications Google Drive Pictures
# Desktop Library Public
```

# open folder

```py
# bash$ open .
```

# make directory

```py
# bash$ mkdir webapp
```

# create file

```py
# bash$ touch index.html
```

# open file

```py
# bash$ open index.html
```

# open file in Sublime Text

```py
# bash$ open -a "Sublime Text"
# bash$ open -a "Sublime Text" index.html
```

# rename file

```py
# bash$ mv index.html about.html
```

# delete file

```py
# bash$ rm about.html
```

# delete directory

```py
# bash$ rm -r webapp
```

# Audio Terminal

```py
# bash$ say Hello
```

</details>

+OBJECT ORIENTED PROGRAMMING

<details>
  <summary>15. Object Oriented Programming -  Creating Objects from a Class </summary>

# Creating Objects from a Class

```py
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

player1 = PlayerCharacter('Alex')
player2 = PlayerCharacter('Cindy')

print(player1)
print(player1.name)

print(player2)
print(player2.name)
```

### output:

```py
# <__main__.PlayerCharacter object at 0x7f7c49a88f70>
# Alex

# <__main__.PlayerCharacter object at 0x7f7c4e21ad00>
# Cindy
```

</details>

<details>
  <summary>16. Object Oriented Programming -  Class Object Attributes </summary>

# Class Object Attributes

```py
class PlayerCharacter:
    membership = "Student"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Alex', 30)
player2 = PlayerCharacter('Cindy', 24)

print(player1.name)
print(player1.age)
print(player1.membership)

print(player2.name)
print(player2.age)
print(player2.membership)
```

### output:

```py
# Alex
# 30
# Student

# Cindy
# 24
# Student
```

</details>

<details>
  <summary>17. Object Oriented Programming -  Using Class Object Attributes in Methods </summary>

# Using Class Object Attributes in Methods

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            #attributes
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}.')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.shout())
```

### output:

```py
# my name is Cindy.
# None
```

</details>

<details>
  <summary>18. Object Oriented Programming -  Instantiating default Attributes to users </summary>

# Instantiating default Attributes to users

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name="anonymous", age=0):
        if (age > 0):
            #attributes
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}.')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player2.shout())
```

### output:

```py
# my name is Tom.
# None
```

</details>

<details>
  <summary>19. Object Oriented Programming -  Class Method </summary>

# Class Method

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  #attributes
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Tom', 20)
print(PlayerCharacter.adding_things(2, 3))
```

### output:

```py
# 5
```

</details>

<details>
  <summary>20. Object Oriented Programming -  Instantiating a Class with Class Method </summary>

# Instantiating a Class with Class Method

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  #attributes
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Jimmy', num1 + num2)


# player1 = PlayerCharacter('Tom', 20)
player1 = PlayerCharacter.adding_things(2, 3)
print(player1)
print(player1.age)
```

### output:

```py
# <__main__.PlayerCharacter object at 0x7fd322061790>
# 5
```

</details>

<details>
  <summary>21. Object Oriented Programming -  Static Method </summary>

# Static Method

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  #attributes
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Jimmy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Bode', 34)
print(player1.adding_things2(3, 4))
```

### output:

```py
# 7
```

</details>

<details>
  <summary>22. Four (4) Pillars of OOP - Encapsulation </summary>

# Encapsulation

### Grouping Attributes and Methods into a unit to define an Object.

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  #attributes
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 30)
player1.speak()
```

### output:

```py
# my name is andrei, and I am 30 years old
```

</details>

<details>
  <summary>23. Four (4) Pillars of OOP - Abstraction </summary>

# Abstraction

### Hiding of Information and only making available what is necessary

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  #attributes
        self.age = age

    def speak(self):
        print(f'Hey! I\'m {self.name.title()}!')


player1 = PlayerCharacter('andrei', 30)
player1.speak()
```

### output:

```py
# Hey! I'm Andrei!
```

</details>

<details>
  <summary>24. Private Variables </summary>

# Private Variables

```py
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self._name = name  #attributes
        self._age = age

    def speak(self):
        print(f'Hey! I\'m {self._age} years old!')


player1 = PlayerCharacter('andrei', 30)
player1.speak()
```

### output:

```py
# Hey! I'm 30 years old!
```

</details>

<details>
  <summary>25. Four (4) Pillars of OOP - Inheritance </summary>

# Inheritance

### Allows new objects to take on the properties of existing objects.

```py
class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    pass

class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())
```

### output:

```py
# logged in
# None
```

</details>

<details>
  <summary>26. isinstance() </summary>

# isinstance()

```py
class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        pass

    def attack(self):
        pass


class Archer(User):
    def __init__(self, name, numarrows):
        pass

    def attack(self):
        pass


wizard1 = Wizard('Merlin', 60)
print(isinstance(wizard1, Wizard))
```

### output:

```py
# True
```

</details>

<details>
  <summary>27. Four (4) Pillars of OOP - Polymorphism </summary>

# Polymorphism

### Allows different forms of methods.

```py
class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Herculis', 30)


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
```

### output:

```py
# attacking with power of 60
# attacking with arrows: arrows left- 30
```

```py
class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#1 Add nother Cat
class Jonny(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#2 Create a list of all of the pets (create 3 cat instances from the above)
cat_1 = Simon('simon', 3)
cat_2 = Sally('sally', 4)
cat_3 = Jonny('jonny', 2)
my_cats = [cat_1, cat_2, cat_3]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()
```

### output:

```py
# simon is just walking around
# sally is just walking around
# jonny is just walking around
```

</details>

<details>
  <summary>28. User.__init__ vs super().__init__ </summary>

# User.**init** vs super().**init**

```py
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 60, 'mel@gmail.com')
archer1 = Archer('Herculis', 30, 'hec@gmail.com')
print(wizard1.email)
print(archer1.email)
```

### output:

```py
# mel@gmail.com
# hec@gmail.com
```

</details>

<details>
  <summary>29. Dir introspection </summary>

# dir introspection

```py
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 60, 'mel@gmail.com')
print(dir(wizard1))

```

### output:

```py
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
```

</details>

<details>
  <summary>30. Dunder Methods - Usage </summary>

# Dunder Methods Usage

```py
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
```

### output:

```py
# <__main__.Toy object at 0x7f01e9264850>
# <__main__.Toy object at 0x7f01e9264850>
```

</details>

<details>
  <summary>31. Dunder Methods - Altering Methods </summary>

# Altering Dunder Methods

```py
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {'name': 'Yoyo', 'has_pets': False}

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return "Yes??"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure.__len__())
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

```

### output:

```py
# red
# red
# 5
# 5
# Yes??
# Yoyo
```

</details>

<details>
  <summary>32. issubclass() </summary>

# issubclass

```py
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))

super_list1.append(5)
print(super_list1[0])

print(issubclass(SuperList, list))
```

### output:

```py
# 1000
# 5
# True
```

</details>

<details>
  <summary>32. Multiple Inheritance </summary>

# Multiple Inheritance

```py
class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)
print(hb1.arrows)
print(hb1.power)
hb1.sign_in()
```

### output:

```py
# 100
# 50
# logged in
```

</details>

<details>
  <summary>33. MRO - Method Resolution Order </summary>

# Method Resolution Order

```py
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())
# print(D.__mro__)
```

### output:

```py
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

</details>

+FUNCTIONAL PROGRAMMING

<details>
  <summary>34. Functional Programming - Pure Functions </summary>

# Pure Functions

### It always produces the same result or output for a given input

### It produces no side effects

```py
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

print(multiply_by2([1, 2, 3]))
```

### output:

```py
# [2, 4, 6]
```

</details>

<details>
  <summary>35. Functional Programming - map function </summary>

# map function

```py
def multiply_by2(item):
    return item * 2

my_new_list = list(map(multiply_by2, [1, 2, 3]))
print(my_new_list)
```

### output:

```py
# [2, 4, 6]
```

</details>

<details>
  <summary>36. Functional Programming - filter function </summary>

# filter function

```py
def check_odd(item):
    return item % 2 != 0

my_new_list = list(filter(check_odd, [1, 2, 3, 4, 5]))
print(my_new_list)
```

### output:

```py
# [1, 3, 5]
```

</details>

<details>
  <summary>37. Functional Programming - zip function </summary>

# zip function

```py
my_list = [1, 2, 3]
your_list = [10, 20, 30]

def check_odd(item):
    return item % 2 != 0

my_new_list = list(zip(my_list, your_list))
print(my_new_list)
```

### output:

```py
# [(1, 10), (2, 20), (3, 30)]
```

</details>

<details>
  <summary>38. Functional Programming - reduce function </summary>

# reduce function

```py
from functools import reduce

my_list = [1, 2, 3]

def add(total, item):
    return total + item

my_total = reduce(add, my_list, 10)
print(my_total)
```

### output:

```py
# 16
```

</details>

<details>
  <summary>38. Functional Programming - Task </summary>

# Solution 1

```py
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_names(item):
    return item.capitalize()


print(list(map(capitalize_names, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
zipped_list = list(zip(my_strings, my_numbers))
zipped_list.sort(key=lambda x: x[1], reverse=False)
print(zipped_list)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

pass_scores = list(filter(lambda x: x > 50, scores))
print(pass_scores)

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
combined_list = my_numbers + scores
total_sum = reduce(lambda total, item: total + item, combined_list)
print(total_sum)
```

### output:

```py
# ['Sisi', 'Bibi', 'Titi', 'Carla']
# [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]
# [73, 65, 76, 100, 88]
# 456
```

# Solution 2

```py
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))
```

### output:

```py
# ['SISI', 'BIBI', 'TITI', 'CARLA']
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# [73, 65, 76, 100, 88]
# 456
```

</details>

<details>
  <summary>39. Functional Programming - Lambda Expressions </summary>

# Lambda Expression

```py
#Multiply by 2
my_list = [1, 2, 3]

print(list(map(lambda x: x * 2, my_list)))

#Square
my_list = [5, 4, 3]

print(list(map(lambda x: x**2, my_list)))

#List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(sorted(a, key=lambda x: x[1], reverse=False))

a.sort(key=lambda x: x[1], reverse=False)
print(a)
```

### output:

```py
# [2, 4, 6]
# [25, 16, 9]
# [(10, -1), (0, 2), (4, 3), (9, 9)]
# [(10, -1), (0, 2), (4, 3), (9, 9)]
```

</details>

+COMPREHENSIONS

<details>
  <summary>40. List Comprehensions </summary>

# List Comprehension

```py
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 10)]
my_list3 = [num**2 for num in range(0, 10) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)

```

### output:

```py
# ['h', 'e', 'l', 'l', 'o']
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 4, 16, 36, 64]
```

</details>

<details>
  <summary>41. Dictionary and Set Comprehensions </summary>

# Set Comprehension

```py
my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 10)}
my_list3 = {num**2 for num in range(0, 10) if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
```

### output:

```py
# {'e', 'l', 'h', 'o'}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# {0, 64, 4, 36, 16}
```

# Dictionary Comprehension

```py
simple_dict = {'a': 2, 'b': 3}
my_dict = {key: value**2 for key, value in simple_dict.items()}
my_dict2 = {num: num * 2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)

```

### output:

```py
# {'a': 4, 'b': 9}
# {1: 2, 2: 4, 3: 6}
```

# Task

```py
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(
    set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates)
```

### output:

```py
# ['n', 'b']
```

</details>

+PYTHON DECORATORS

<details>
  <summary>42. Python Decorators - Passing Functions as arguments</summary>

# Passing Functions as arguments

```py
def hello(func):
    func()

def greet():
    print('still here!')

a = hello(greet)

print(a)
```

### output:

```py
# still here!
# None
```

</details>

<details>
  <summary>43. Python Decorators - Higher Order Functions HOC</summary>

# Higher Order Functions HOC

```py
def greet(func):
  func()

def greet2():
  def func():
    return 5

  return func

```

</details>

<details>
  <summary>44. Python Decorators - Without and With @decorator </summary>

# Without @decorator

```py
def my_decorator(func):
    def wrap_func():
        print("Starting to Wrap function")
        print('-' * 30)
        func()
        print('-' * 30)
        print("Ending of Wrap function")

    return wrap_func

def hello():
    print('hellloooo')

hello2 = my_decorator(hello)
hello2()
```

### output:

```py
# Starting to Wrap function
# ------------------------------
# hellloooo
# ------------------------------
# Ending of Wrap function
```

# With @decorator

```py
def my_decorator(func):
    def wrap_func():
        print("Starting to Wrap function")
        print('-' * 30)
        func()
        print('-' * 30)
        print("Ending of Wrap function")

    return wrap_func

@my_decorator
def hello():
    print('hellloooo')

hello()
```

### output:

```py
# Starting to Wrap function
# ------------------------------
# hellloooo
# ------------------------------
# Ending of Wrap function
```

</details>

<details>
  <summary>45. Python Decorators - Passing *args and **kwargs parameters to @decorator </summary>

# passing arguments to @decorator

```py
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('-' * 30)
        func(*args, **kwargs)
        print('-' * 30)

    return wrap_func


@my_decorator
def hello(greeting, emoji='🙂'):
    print(greeting, emoji)


hello('Hiiii')
```

### output:

```py
# ------------------------------
# Hiiii 🙂
# ------------------------------
```

</details>

<details>
  <summary>51. Python Decorators - Time Performance Test </summary>

# Using Decorators for Time Performance testing

```py
#Decorator
from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"It took {format(t2-t1, '.3f')}s")
        return result

    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i * 5

long_time()
```

### output:

```py
# It took 0.196s
```

</details>

<details>
  <summary>52. Python Decorators - @authenticated decorator Task </summary>

# @authenticated decorator Task

### Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

```py
user1 = {
    'name': 'Sorna',
    'valid': True
    #changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper_func(*args, **kwargs):
        if args[0].get('valid'):
            return fn(*args, **kwargs)
        print('Unauthorised. access denied.')

    return wrapper_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

```

### output:

```py
# message has been sent
```

</details>

+ERROR HANDLING

<details>
  <summary>53. Error handling - Types </summary>

# Type Error

```py
print(1 + 'ade')
```

### output:

```py
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     print(1 + 'ade')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

# Syntax Error

```py
def hoooohooo()
  pass
```

### output:

```py
#   File "main.py", line 3
#     def hoooohooo()
#                   ^
# SyntaxError: invalid syntax
```

# Name Error

```py
def hoooohooo():
    1 + name

hoooohooo()
```

### output:

```py
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     hoooohooo()
#   File "main.py", line 2, in hoooohooo
#     1 + name
# NameError: name 'name' is not defined
```

# Index Error

```py
def hoooohooo():
    li = [1, 2, 3]
    li[5]

hoooohooo()
```

### output:

```py
# Traceback (most recent call last):
#   File "main.py", line 7, in <module>
#     hoooohooo()
#   File "main.py", line 4, in hoooohooo
#     li[5]
# IndexError: list index out of range
```

# Zero Division Error

```py
def hoooohooo() :
  5/0
hoooohooo()

```

### output:

```py
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     hoooohooo()
#   File "main.py", line 4, in hoooohooo
#     5/0
# ZeroDivisionError: division by zero
```

# Value Error

```py
age = int(input('what is your age? '))
print(age)
```

### output:

```py
# what is your age? dsfgsdgfsadg
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     age = int(input('what is your age? '))
# ValueError: invalid literal for int() with base 10: 'dsfgsdgfsadg'
```

</details>

<details>
  <summary>54. Error handling - Catching Exact Errors </summary>

# Catching Exact Errors

```py
while True:
  try:
    age = int(input('what is your age? '))
    print(10/age)
  except ZeroDivisionError:
    print('Zero is not allowed')
  except ValueError:
    print('please enter a number')
  else:
    print('thank you!')
    break
```

### output:

```py
# what is your age? 0
# Zero is not allowed
# what is your age? sdf
# please enter a number
# what is your age? 30
# 0.3333333333333333
# thank you!
```

</details>

<details>
  <summary>55. Error handling - Displaying Exact Errors </summary>

# Displaying Exact Errors

```py
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers')
        print(err)

print(sum(1, '2'))
```

### output:

```py
# please enter numbers
# unsupported operand type(s) for +: 'int' and 'str'
# None
```

</details>

<details>
  <summary>56. Error handling - Grouping Errors </summary>

# Grouping Errors

```py
def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        return f'oooops, {err}'

print(sum(1, '2'))
```

### output:

```py
# oooops, unsupported operand type(s) for +: 'int' and 'str'
```

</details>

<details>
  <summary>57. Error handling - Finally </summary>

# Finally

```py
while True:
    try:
        age = int(input('what is your age? '))
        10 / age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break
    finally:
        print('ok i am finally done')
```

### output:

```py
# what is your age? 0
# please enter age higher than 0
# ok i am finally done
# what is your age? asdfs
# please enter a number
# ok i am finally done
# what is your age? 40
# thank you!
# ok i am finally done
```

</details>

<details>
  <summary>58. Error handling - Raise Exception </summary>

# Raising Exception

```py
while True:
    try:
        age = int(input('what is your age? '))
        10 / age
        raise ValueError('hey! cut it out')
        # raise Exception('hey! cut it out')
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
    finally:
        print('ok i am finally done')
```

### output:

```py
# what is your age? 5
# ok i am finally done
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     raise ValueError('hey! cut it out')
# ValueError: hey! cut it out
```

</details>

+GENERATORS

<details>
  <summary>59. Generators - next and yield </summary>

# next and yield

```py
def gen_range(num):
    for i in range(num):
        yield i

g = gen_range(100)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

### output:

```py
# <generator object gen_range at 0x7fa947748f90>
# 0
# 1
# 2
# 3
```

</details>

<details>
  <summary>60. Generators - performance test </summary>

# Generator performance test

```py
from time import time


def performance(fn):
    def wrapper():
        f1 = time()
        fn()
        f2 = time()
        time_taken = format(f2 - f1, '.3f')
        print(f"It has taken {time_taken}secs to run.")

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5


long_time()
long_time2()

```

### output:

```py
# 1
# It has taken 2.389secs to run.
# 2
# It has taken 4.413secs to run.
```

</details>

<details>
  <summary>61. Generators - Iteration for For Loops </summary>

# Creating Iteration for For Loops

```py
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1, 2, 3])
```

### output:

```py
# <list_iterator object at 0x7f02bc19af70>
# 1
# <list_iterator object at 0x7f02bc19af70>
# 2
# <list_iterator object at 0x7f02bc19af70>
# 3
# <list_iterator object at 0x7f02bc19af70>
```

</details>

<details>
  <summary>61B. Generators - Iteration for Range </summary>

# Creating Iteration for Range

```py
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current == 0 and self.first != 0:
            MyGen.current = self.first
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(2, 10)
for i in gen:
    print(i)

```

### output:

```py
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

</details>

<details>
  <summary>61C. Generators - Fibonnacci sequence </summary>

# Creating Fibonnacci sequence

```py
def fib(num):
    current = 0
    next = 1
    for i in range(num + 1):
        yield current
        new_next = current + next
        current = next
        next = new_next

for x in fib(20):
    print(x)

```

### output:

```py
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
```

</details>

+PYTHON MODULES

<details>
  <summary>62. Modules in Python - Modules </summary>

# Importing modules

### main.py:

```py
import utility

print(utility.multiply(2, 4))
print(utility.divide(10, 5))
```

### utility.py:

```py
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
```

### output:

```py
# 8
# 2.0
```

</details>

<details>
  <summary>63. Modules in Python - Packages </summary>

# Using packages

### main.py:

```py
import utility
from shopping import shopping_cart

print(utility.multiply(2, 4))
print(utility.divide(10, 5))
print(shopping_cart)
print(shopping_cart.buy('Apple'))

```

### utility.py:

```py
def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

```

### shopping/**init**.py:

```py

```

### shopping/shopping_cart.py:

```py
def buy(item):
    cart = []
    cart.append(item)
    return cart

```

### output:

```py
# 8
# 2.0
# <module 'shopping.shopping_cart' from '/home/runner/decorators-1/shopping/shopping_cart.py'>
# ['Apple']
```

</details>

<details>
  <summary>64. Modules in Python - Simplifying imports of Packages, Modules and functions </summary>

# Simplifying imports

### main.py:

```py
from utility import multiply, divide
from shopping.mens.shopping_cart import buy

print(multiply(2, 4))
print(divide(10, 5))
print(buy('Apple'))

```

### utility.py:

```py
def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

```

### shopping/mens/shopping_cart.py:

```py
def buy(item):
    cart = []
    cart.append(item)
    return cart

```

### output:

```py
# 8
# 2.0
# ['Apple']
```

</details>

<details>
  <summary>65. Modules in Python - __name__ attribute </summary>

# **name** attribute

### main.py:

```py
from utility import multiply, divide
from shopping.mens.shopping_cart import buy

if __name__ == '__main__':
    print(multiply(2, 4))
    print(divide(9, 5))
    print(buy('Apple'))

```

</details>

<details>
  <summary>66. Modules in Python - Built-in Modules </summary>

# random

### main.py:

```py
import random

if __name__ == '__main__':
    print(random)
    print(random.random)
    print(random.random())
    print(random.randint(0, 10))
    print(random.choice(['apple', 'orange', 'banana']))

    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print(my_list)

    print(dir(random))

    help(random)
```

### output:

```py
# <module 'random' from '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py'>
# <built-in method random of Random object at 0x13a80fa20>
# 0.016844424862344165
# 5
# orange

# [4, 2, 5, 1, 3]

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# Help on module random:
#
# NAME
#     random - Random variable generators.
# ----------------------------------------------------------------
# ----------------------------------------------------------------

```

# sys.argv

### main.py:

```py
import sys

if __name__ == '__main__':
    print(sys)

    first = sys.argv[1]
    last = sys.argv[2]
    print(f'hiiiii! {first} {last}')
```

### output:

```py
# (venv) modules % python3 main.py Ifeanyi Omeata
# <module 'sys' (built-in)>
# hiiiii! Ifeanyi Omeata

```

</details>

<details>
  <summary>67. Modules in Python - Random Game task </summary>

# Solution

### main.py:

```py
import random
import sys

if __name__ == '__main__':

    first = int(sys.argv[1])
    last = int(sys.argv[2])
    random_choice = random.randint(first, last)
    print(random_choice)
    while True:
        try:
            guess = int(input(f'Guess a random number between {first} and {last}" '))
        except ValueError:
            print(f'Only numbers between {first} and {last} are allowed.')
            continue

        if first > guess < last:
            print('Value is not in range. Try again.')
        elif guess != random_choice:
            print('Wrong guess! Try again.')
        else:
            print(f'Correct! The Value is {random_choice}.')
            break
```

### output:

```py
# (venv) modules % python3 main.py 5 10
# 5
# Guess a random number between 5 and 10: 3
# Value is not in range. Try again.
# Guess a random number between 5 and 10: 7
# Wrong guess! Try again.
# Guess a random number between 5 and 10: 5
# Correct! The Value is 5.

```

</details>

<details>
  <summary>68. Modules in Python - Pyjokes </summary>

# Import Pyjokes

### main.py:

```py
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
```

### output:

```py
# How do you know whether a person is a Vim user? Don't worry, they'll tell you.
```

</details>

<details>
  <summary>69. Modules in Python - Counter in collections </summary>

# Counter

### main.py:

```py
from collections import Counter, defaultdict, OrderedDict

li = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7]
sentence = 'aa bbb cccc ddddd eeeeee'

print(Counter(li))
print(Counter(sentence))

```

### output:

```py
# Counter({2: 3, 7: 3, 1: 2, 3: 1, 4: 1, 5: 1, 6: 1})
# Counter({'e': 6, 'd': 5, ' ': 4, 'c': 4, 'b': 3, 'a': 2})
```

</details>

<details>
  <summary>70. Modules in Python - Defaultdict in collections </summary>

# Defaultdict

### main.py:

```py
from collections import Counter, defaultdict, OrderedDict

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])
```

### output:

```py
# 5
```

</details>

<details>
  <summary>71. Modules in Python - OrderedDict in collections </summary>

# OrderedDict

### main.py:

```py
from collections import Counter, defaultdict, OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

```

### output:

```py
# False
```

</details>

<details>
  <summary>72. Modules in Python - Datetime </summary>

# Datetime

### main.py:

```py
import datetime
import time

print(datetime.time())
print(datetime.time(5, 45, 2))
print(datetime.date.today())
print(time.time())
```

### output:

```py
# 00:00:00
# 05:45:02
# 2023-04-28
# 1682667595.1815803
```

</details>

<details>
  <summary>73. Modules in Python - Arrays </summary>

# Arrays

### main.py:

```py
from array import array

arr = array('i', [1, 2, 3])
print(arr[0])
```

### output:

```py
# 1
```

</details>

<details>
  <summary>74. Python Debugger - Breakpoint or Pdb </summary>

# Python Debugger Breakpoint or (pdb)

### main.py:

```py
import pdb


def add(num1, num2):
    # pdb.set_trace()
    breakpoint()
    return num1 + num2


add(4, 'hhkhads')
```

### output:

```py
# > /home/runner/decorators-1/main.py(6)add()
# -> return num1 + num2

# (Pdb) num1
# 4

# (Pdb) num2
# 'hhkhads'

# (Pdb) a
# num1 = 4
# num2 = 'hhkhads'

# (Pdb) help
# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where
#
# Miscellaneous help topics:
# ==========================
# exec  pdb

# (Pdb) w
#   /home/runner/decorators-1/main.py(9)<module>()
# -> add(4, 'hhkhads')
# > /home/runner/decorators-1/main.py(6)add()
# -> return num1 + num2

# (Pdb) clear

# (Pdb) num2 = 8

# (Pdb) step
# --Return--
# > /home/runner/decorators-1/main.py(6)add()->12
# -> return num1 + num2

# (Pdb) continue

```

</details>

+FILE I/O

<details>
  <summary>75. File I/O - Open, Close and Seek </summary>

# Open and Seek

### main.py:

```py
my_file = open('test.txt')

print(my_file)
print(my_file.read())
my_file.seek(0)
print(my_file.read())

my_file.close()
```

### output:

```py
# <_io.TextIOWrapper name='test.txt' mode='r' encoding='utf-8'>
# Hello, Welcome Home!
# :)
# Hello, Welcome Home!
# :)
```

### test.txt:

```txt
Hello, Welcome Home!
:)
```

</details>

<details>
  <summary>76. File I/O - Readline </summary>

# Readline

### main.py:

```py
my_file = open('test.txt')

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()
```

### output:

```py
# Hello, Welcome Home!
# :)
# How are you doing?
```

### test.txt:

```txt
Hello, Welcome Home!
:)
How are you doing?
Hope fine!
```

</details>

<details>
  <summary>77. File I/O - Readlines </summary>

# Readlines

### main.py:

```py
my_file = open('test.txt')

print(my_file.readlines())

my_file.close()
```

### output:

```py
# ['Hello, Welcome Home!\n', ':)\n', 'How are you doing?\n', 'Hope fine!']
```

### test.txt:

```txt
Hello, Welcome Home!
:)
How are you doing?
Hope fine!
```

</details>

<details>
  <summary>78. File I/O - With Context Manager </summary>

# With Context Manager

### main.py:

```py
with open('test.txt') as my_file:
    print(my_file.readlines())
    my_file.seek(0)
    print(my_file.readlines())
```

### output:

```py
# ['Hello, Welcome Home!\n', ':)\n', 'How are you doing?\n', 'Hope fine!']
# ['Hello, Welcome Home!\n', ':)\n', 'How are you doing?\n', 'Hope fine!']
```

### test.txt:

```txt
Hello, Welcome Home!
:)
How are you doing?
Hope fine!
```

</details>

<details>
  <summary>79. File I/O - Read File </summary>

# Read File

### main.py:

```py
with open('test.txt', mode="r") as my_file:
    print(my_file.readlines())
```

### output:

```py
# ['Hello, Welcome Home!\n', ':)\n', 'How are you doing?\n', 'Hope fine!']
```

### test.txt:

```txt
Hello, Welcome Home!
:)
How are you doing?
Hope fine!
```

</details>

<details>
  <summary>80. File I/O - Read and Write to File </summary>

# Read and Write to File

### main.py:

```py
with open('test.txt', mode="r+") as my_file:
    print(my_file.readlines())
    text = my_file.write('\nMy name is ken.')
    print(text)
```

```py
# ['Hello']
# 16
```

### test.txt:

```txt
Hello!
```

### output=test.txt:

```txt
Hello!
My name is ken.
```

</details>

<details>
  <summary>81. File I/O - Append to File </summary>

# Append to File

### main.py:

```py
with open('test.txt', mode="a") as my_file:
    text = my_file.write('\n:)')
    print(text)
```

```py
# 3
```

### test.txt:

```txt
Hello!
```

### output=test.txt:

```txt
Hello!
:)
```

</details>

<details>
  <summary>82. File I/O - Write to File </summary>

# Write to File

### main.py:

```py
with open('test.txt', mode="w") as my_file:
    text = my_file.write(':)')
    print(text)
```

```py
# 2
```

### test.txt:

```txt
Hello!
```

### output=test.txt:

```txt
:)
```

</details>

<details>
  <summary>83. File I/O - Pathlib </summary>

# Pathlib

### main.py:

```py
from pathlib import Path

p = r"/Users/ifeanyi/Desktop/SERVER/Cloud/modules/main.py"

print(1, Path(p).anchor)
print(2, Path(p).parent)
print(3, Path(p).name)
print(4, Path(p).stem)
print(5, Path(p).suffixes)
print(6, str(p))
```

### output:

```py
# 1 /
# 2 /Users/ifeanyi/Desktop/SERVER/Cloud/modules
# 3 main.py
# 4 main
# 5 ['.py']
# 6 /Users/ifeanyi/Desktop/SERVER/Cloud/modules/main.py
```

</details>

<details>
  <summary>84. File I/O - Try and Except </summary>

# Try and Except

### main.py:

```py
try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
```

### output:

```py
# file does not exist
#
# Traceback (most recent call last):
#   File "/Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/modules/main.py", line 7, in <module>
#     raise err
#   File "/Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/modules/main.py", line 3, in <module>
#     with open('sad.txt', mode='r') as my_file:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'sad.txt'
```

</details>

<details>
  <summary>85. File I/O - Translate Pypi </summary>

# Translate Pypi

```pybs
pip install translate
```

### main.py:

```py
from translate import Translator
translator = Translator(to_lang="fr")

try:
    with open("test.txt", mode="r") as my_file:
        note = my_file.read()
        print(f"English: {note}")
        translation = translator.translate(note)
        print(f"French: {translation}")
        with open('./test-fr.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print(f"Error. Check your file source.")
except Exception as err:
    print(f"Error: {err}")
```

### output:

```py
# English: Hello!, I am Alice.
# French: Bonjour, je suis Alice.
```

### test.txt:

```txt
Hello!, I am Alice.
```

### test-fr.txt:

```txt
Bonjour, je suis Alice.
```

</details>

+REGULAR EXPRESSIONS

<details>
  <summary>86. Regular Expressions - Search </summary>

# Search

### main.py:

```py
import re

string = 'search inside of this text please!'

print('th' in string)

a = re.search('th', string)
print(a)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

```

### output:

```py
# True

# <re.Match object; span=(17, 19), match='th'>
# (17, 19)
# 17
# 19
# th
```

</details>

<details>
  <summary>87. Regular Expressions - Compile </summary>

# Compile

### main.py:

```py
import re

pattern = re.compile('th')

string = 'search inside of this text please!'
string2 = 'search the boy went to the school.'

a = pattern.search(string)
b = pattern.search(string2)

print(a)
print(b)
```

### output:

```py
# <re.Match object; span=(17, 19), match='th'>
# <re.Match object; span=(7, 9), match='th'>
```

</details>

<details>
  <summary>88. Regular Expressions - Findall </summary>

# Findall

### main.py:

```py
import re

pattern = re.compile('th')

string = 'search inside of this text please!'
string2 = 'search the boy went to the school.'

a = pattern.findall(string)
b = pattern.findall(string2)

print(a)
print(b)
```

### output:

```py
# ['th']
# ['th', 'th']
```

</details>

<details>
  <summary>89. Regular Expressions - Fullmatch </summary>

# Fullmatch

### main.py:

```py
import re

pattern = re.compile('the boy')

string = 'the boy'
string2 = 'search the boy went to the school.'

a = pattern.fullmatch(string)
b = pattern.fullmatch(string2)

print(a)
print(b)

```

### output:

```py
# <re.Match object; span=(0, 7), match='the boy'>
# None
```

</details>

<details>
  <summary>90. Regular Expressions - Match </summary>

# Match

### main.py:

```py
import re

pattern = re.compile('the boy')

string = 'the boy'
string2 = 'the boy went to the school.'

a = pattern.match(string)
b = pattern.match(string2)

print(a)
print(b)
```

### output:

```py
# <re.Match object; span=(0, 7), match='the boy'>
# <re.Match object; span=(0, 7), match='the boy'>
```

</details>

<details>
  <summary>91. Regular Expressions - Summary </summary>

# Summary

### main.py:

```py
# abc…	          Letters
# 123…	          Digits
# \d	            Any Digit
# \D	            Any Non-digit character
# .	              Any Character
# \.	            Period
# [abc]	          Only a, b, or c
# [^abc]	        Not a, b, nor c
# [a-z]	          Characters a to z
# [0-9]	          Numbers 0 to 9
# \w	            Any Alphanumeric character
# \W	            Any Non-alphanumeric character
# {m}	            m Repetitions
# {m,n}	          m to n Repetitions
# *	              Zero or more repetitions
# +	              One or more repetitions
# ?	              Optional character
# \s	            Any Whitespace
# \S	            Any Non-whitespace character
# ^…$	            Starts and ends
# (…)	            Capture Group
# (a(bc))	        Capture Sub-group
# (.*)	          Capture all
# (abc|def)	      Matches abc or def

# []	  A set of characters =	"[a-m]"
# \	    Signals a special sequence (can also be used to escape special characters) =	"\d"
# .	    Any character (except newline character) = "he..o"
# ^	    Starts with	= "^hello"
# $	    Ends with	= "planet$"
# *	    Zero or more occurrences	= "he.*o"
# +	    One or more occurrences	= "he.+o"
# ?	    Zero or one occurrences	= "he.?o"
# {}	  Exactly the specified number of occurrences	= "he.{2}o"
# |	    Either or	= "falls|stays"
# ()	  Capture and group

```

</details>

<details>
  <summary>92. Regular Expressions - Email Validation Task </summary>

# Email Validation

```py
# ^[\w_.+-]+@\w+\.[\w.-]+$
# ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
```

### main.py:

```py
import re

pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

string = 'admin@gmail.com'
string2 = 'the boy went to the school.'

a = pattern.match(string)
b = pattern.match(string2)

print(a)
print(b)

```

### output:

```py
# <re.Match object; span=(0, 15), match='admin@gmail.com'>
# None
```

</details>

<details>
  <summary>93. Regular Expressions - Password Validation Task </summary>

# Password Validation

```py
# ^[a-zA-Z0-9$%#@]{8,}[\d]$
```

### main.py:

```py
# At least 8 char long
#contain any sort letters, numbers $%#@

import re

pattern = re.compile(r'^[a-zA-Z0-9$%#@]{8,}[\d]$')

string = 'pass123#@$$3'
string2 = 'adsadf--!zkdfn'

a = pattern.match(string)
b = pattern.match(string2)

print(a)
print(b)

```

### output:

```py
# <re.Match object; span=(0, 12), match='pass123#@$$3'>
# None
```

</details>

+UNITTEST

<details>
  <summary>94. Unittest - Unittest Methods </summary>

# Unittest Methods

```py
# Method	                            Checks that
# assertEqual(a, b)	                  a == b
# assertNotEqual(a, b)	              a != b
# assertTrue(x)	                      bool(x) is True
# assertFalse(x)	                    bool(x) is False
# assertIs(a, b)	                    a is b
# assertIsNot(a, b)	                  a is not b
# assertIsNone(x)	                    x is None
# assertIsNotNone(x)	                x is not None
# assertIn(a, b)	                    a in b
# assertNotIn(a, b)                   a not in b
# assertIsInstance(a, b)	            isinstance(a, b)
# assertNotIsInstance(a, b)	          not isinstance(a, b)

# assertAlmostEqual(a, b)	              round(a-b, 7) == 0
# assertNotAlmostEqual(a, b)	          round(a-b, 7) != 0
# assertGreater(a, b)	                  a > b
# assertGreaterEqual(a, b)	            a >= b
# assertLess(a, b)	                    a < b
# assertLessEqual(a, b)	                a <= b
# assertRegex(s, r)	                    r.search(s)
# assertNotRegex(s, r)	                not r.search(s)
# assertCountEqual(a, b)	              a and b have the same elements in the same number, regardless of their order.

```

</details>

</details>

<details>
  <summary>95. Unittest - assertEqual() </summary>

# assertEqual()

### main.py:

```py
def do_stuff(num):
    return num + 5

print(do_stuff(10))
```

### test.py:

```py
import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()


```

### output:

```py
# ~/decorators-1$ python test.py
# 15
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
```

</details>

<details>
  <summary>96. Unittest - assertIsInstance() </summary>

# assertIsInstance()

### main.py:

```py
def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err

print(do_stuff(10))

```

### test.py:

```py
import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

if __name__ == '__main__':
    unittest.main()


```

### output:

```py
# ~/decorators-1$ python test.py
# 15
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
```

</details>

<details>
  <summary>97. Unittest - assertIsNone() </summary>

# assertIsNone()

### main.py:

```py
def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return None
    except ValueError as err:
        return err

print(do_stuff(10))
```

### test.py:

```py
import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()


```

### output:

```py
# ~/decorators-1$ python test.py
# 15
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK
```

</details>

<details>
  <summary>98. Unittest - Run all Tests </summary>

# Run all Tests Together

```pybs
python -m unittest
```

```py
# ~/decorators-1$ python3 -m unittest
# 15
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK
```

</details>

<details>
  <summary>99. Unittest - Verbose </summary>

# Get more details with verbose

```pybs
python -m unittest -v
```

```py
# ~/decorators-1$ python3 -m unittest -v
# 15
# test_do_stuff (test.TestMain) ... ok
# test_do_stuff2 (test.TestMain) ... ok
# test_do_stuff3 (test.TestMain) ... ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK
```

</details>

<details>
  <summary>100. Unittest - Docstrings/Comments </summary>

# Docstrings/Comments

### main.py:

```py
def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return None
    except ValueError as err:
        return err


print(do_stuff(10))
```

### test.py:

```py
import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        """Test 1 for do_stuff"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """Test 2 for do_stuff"""
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        """Test 3 for do_stuff"""
        test_param = None
        result = main.do_stuff(test_param)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
```

### output:

```py
# ~/decorators-1$ python3 -m unittest -v
# 15
# test_do_stuff (test.TestMain)
# Test 1 for do_stuff ... ok
# test_do_stuff2 (test.TestMain)
# Test 2 for do_stuff ... ok
# test_do_stuff3 (test.TestMain)
# Test 3 for do_stuff ... ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.050s

# OK
```

</details>

<details>
  <summary>101. Unittest - SetUp </summary>

# SetUp

### main.py:

```py
def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return None
    except ValueError as err:
        return err

print(do_stuff(10))

```

### test.py:

```py
import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.myValues = (10, 'shkshks', None)
        print('about to test the function')

    def test_do_stuff(self):
        """Test 1 for do_stuff"""
        test_param = self.myValues[0]
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """Test 2 for do_stuff"""
        test_param = self.myValues[1]
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        """Test 3 for do_stuff"""
        test_param = self.myValues[2]
        result = main.do_stuff(test_param)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

```

### output:

```py
# ~/decorators-1$ python3 -m unittest -v
# 15
# test_do_stuff (test.TestMain)
# Test 1 for do_stuff ... about to test the function
# ok
# test_do_stuff2 (test.TestMain)
# Test 2 for do_stuff ... about to test the function
# ok
# test_do_stuff3 (test.TestMain)
# Test 3 for do_stuff ... about to test the function
# ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK
```

</details>

<details>
  <summary>102. Unittest - TearDown </summary>

# TearDown

### main.py:

```py
def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return None
    except ValueError as err:
        return err

print(do_stuff(10))

```

### test.py:

```py
import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.myValues = (10, 'shkshks', None)
        print('about to test the function')

    def test_do_stuff(self):
        """Test 1 for do_stuff"""
        test_param = self.myValues[0]
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """Test 2 for do_stuff"""
        test_param = self.myValues[1]
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        """Test 3 for do_stuff"""
        test_param = self.myValues[2]
        result = main.do_stuff(test_param)
        self.assertIsNone(result)

    def tearDown(self):
        print("Cleaning Up...")

if __name__ == '__main__':
    unittest.main()

```

### output:

```py
# ~/decorators-1$ python3 -m unittest -v
# 15
# test_do_stuff (test.TestMain)
# Test 1 for do_stuff ... about to test the function
# Cleaning Up...
# ok
# test_do_stuff2 (test.TestMain)
# Test 2 for do_stuff ... about to test the function
# Cleaning Up...
# ok
# test_do_stuff3 (test.TestMain)
# Test 3 for do_stuff ... about to test the function
# Cleaning Up...
# ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK
```

</details>

<details>
  <summary>103. Unittest - Test Guess Number Game Task </summary>

# Test Game Task

### main.py:

```py
import random


def generate_number():
    return random.randint(1, 10)


def check_number(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
        else:
            print("Wrong Number, Try Again!")
    else:
        print('hey bozo, I said 1~10')


def start_game():
    answer = generate_number()
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if check_number(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue


if __name__ == '__main__':
    start_game()

```

### test.py:

```py
import unittest
import main


class TestGame(unittest.TestCase):
    def setUp(self):
        print('\nTesting the function.')

    def test_generate_number_is_working(self):
        """Test for generate_number is working"""
        result = main.generate_number()
        self.assertTrue(0 < result < 11)
        self.assertIn(result, range(1, 11))

    def test_check_number_correct_guess(self):
        """Test for check_number for correct guess"""
        result = main.check_number(5, 5)
        self.assertTrue(result)
        self.assertIsNotNone(result)

    def test_check_number_wrong_guess(self):
        """Test for check_number for wrong guess"""
        result = main.check_number(5, 10)
        self.assertFalse(result)
        self.assertIsNone(result)

    def test_check_number_off_limit(self):
        """Test for check_number for off limit guess"""
        result = main.check_number(11, 10)
        self.assertFalse(result)
        self.assertIsNone(result)

    def tearDown(self):
        print("Ending Test. Cleaning Up...\n")


if __name__ == '__main__':
    unittest.main()

```

### output:

```py
# ~/decorators-1$ python test.py -v
# test_check_number_correct_guess (__main__.TestGame)
# Test for check_number for correct guess ...
# Testing the function.
# you are a genius!
# Ending Test. Cleaning Up...

# ok
# test_check_number_off_limit (__main__.TestGame)
# Test for check_number for off limit guess ...
# Testing the function.
# hey bozo, I said 1~10
# Ending Test. Cleaning Up...

# ok
# test_check_number_wrong_guess (__main__.TestGame)
# Test for check_number for wrong guess ...
# Testing the function.
# Wrong Number, Try Again!
# Ending Test. Cleaning Up...

# ok
# test_generate_number_is_working (__main__.TestGame)
# Test for generate_number is working ...
# Testing the function.
# Ending Test. Cleaning Up...

# ok

# ----------------------------------------------------------------------
# Ran 4 tests in 0.004s

# OK
```

</details>

+PYTHON IMAGES

<details>
  <summary>104. Python Images - Pillow </summary>

# Install Pillow

```pybs
pip install Pillow
```

# Get Image Properties with Pillow

### main.py:

```py
from PIL import Image

im = Image.open("./Pokemon_images/pikachu.jpeg")

print(1, im)
print(2, im.format)
print(3, im.size)
print(4, im.mode)
```

### output:

```py
# 1 <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x104901710>
# 2 JPEG
# 3 (640, 640)
# 4 RGB
```

</details>

<details>
  <summary>105. Python Image FIltering with Pillow - BLUR </summary>

# BLUR

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.filter(ImageFilter.BLUR)
filtered_img.save("./Pokemon_images/blur.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235739279-a5a40352-2831-439c-b484-d5c10e17e9a0.png)
![](https://user-images.githubusercontent.com/32337103/235739359-b3bcba3d-68a1-4623-9a49-38e847c3472c.png)

</details>

<details>
  <summary>106. Python Image FIltering with Pillow - SMOOTH </summary>

# SMOOTH

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.filter(ImageFilter.SMOOTH)
filtered_img.save("./Pokemon_images/smooth.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235739465-bc67243f-2ed3-4831-91a1-770831157801.png)
![](https://user-images.githubusercontent.com/32337103/235739530-d90d9447-5f31-4a24-85a7-794b12062337.png)

</details>

<details>
  <summary>107. Python Image FIltering with Pillow - SHARPEN </summary>

# SHARPEN

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.filter(ImageFilter.SHARPEN)
filtered_img.save("./Pokemon_images/sharpen.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235740264-e74ff84d-ea47-41d0-bef0-206d4e255a02.png)
![](https://user-images.githubusercontent.com/32337103/235740315-82b9ea25-70be-4971-a660-ab4ec606ada2.png)

</details>

<details>
  <summary>108. Python Image FIltering with Pillow - Convert to Grayscale Image </summary>

# Convert to Grayscale Image

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.convert('L')
filtered_img.save("./Pokemon_images/gray.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235741619-1aecb9fd-4b3b-4f30-9bef-d1d2d2e251bb.png)
![](https://user-images.githubusercontent.com/32337103/235741926-984dc7f4-64b8-4ab7-b339-32e7a4ed0039.png)

</details>

<details>
  <summary>109. Python Image FIltering with Pillow - SHOW </summary>

# SHOW

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.convert('L')
filtered_img.save("./Pokemon_images/gray.png", "png")
filtered_img.show()
```

![](https://user-images.githubusercontent.com/32337103/235744263-21bd0a0e-af86-40c0-a508-a4015ca0aafc.png)
![](https://user-images.githubusercontent.com/32337103/235744467-2ea5b215-6b6d-49f8-9ab6-44e15aacb3bf.png)

</details>

<details>
  <summary>110. Python Image FIltering with Pillow - ROTATE </summary>

# ROTATE

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.convert('L')
rotated = filtered_img.rotate(90)
rotated.save("./Pokemon_images/rotated.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235746188-36cf6451-2c97-4da2-a408-06fda3467fff.png)
![](https://user-images.githubusercontent.com/32337103/235746259-4bd564d3-00ed-4216-8f1d-167ce6d2c505.png)

</details>

<details>
  <summary>111. Python Image FIltering with Pillow - RESIZE </summary>

# RESIZE

### main.py:

```py
from PIL import Image, ImageFilter

im = Image.open("./Pokemon_images/pikachu.jpeg")

filtered_img = im.convert('L')
resize = filtered_img.resize((300, 300))
resize.save("./Pokemon_images/resize.png", "png")
```

![](https://user-images.githubusercontent.com/32337103/235747283-f818da60-721e-4926-aa7b-5f9aee8a50a8.png)
![](https://user-images.githubusercontent.com/32337103/235747322-00ddd4c7-9b50-415c-8f2f-eaff12b6494a.png)

</details>

<details>
  <summary>112. Python Image FIltering with Pillow - CROP </summary>

# CROP

### main.py:

```py
from turtle import width

from PIL import Image, ImageFilter

with Image.open("./Pokemon_images/pikachu.jpeg") as im:

    # The crop method from the Image module takes four coordinates as input.
    # The right can also be represented as (left+width)
    # and lower can be represented as (upper+height).
    (left, upper, right, lower) = (0, 0, 150, 300)

    filtered_img = im.convert('L')
    resized_img = filtered_img.resize((300, 300))
    cropped_img = resized_img.crop((left, upper, right, lower))
    cropped_img.save("./Pokemon_images/cropped.png", "png")

```

![](https://user-images.githubusercontent.com/32337103/235752540-db474aa2-9f54-4842-b9cc-164a9e60472c.png)
![](https://user-images.githubusercontent.com/32337103/235752575-222a28de-231d-47e0-826c-fe54e6162680.png)

</details>

<details>
  <summary>113. Python Image FIltering with Pillow - THUMBNAIL </summary>

# THUMBNAIL

### main.py:

```py
from PIL import Image, ImageFilter

with Image.open("./Pokemon_images/pikachu.jpeg") as im:

    filtered_img = im.convert('L')
    filtered_img.thumbnail((300, 300))
    filtered_img.save("./Pokemon_images/thumbnail.png", "png")

```

![](https://user-images.githubusercontent.com/32337103/235758429-254c1761-827a-444c-b0f9-d34ebd5a5eee.png)
![](https://user-images.githubusercontent.com/32337103/235758474-55b0d83d-84ce-4370-bd3b-54c68d9ed86e.png)

</details>

<details>
  <summary>114. Python Image FIltering with Pillow - Convert Image Format Task </summary>

# Convert Image Format Task

### main.py:

```py
import os
import sys
from pathlib import Path
from PIL import Image

if __name__ == '__main__':
    first = sys.argv[1]
    second = sys.argv[2]

    # Get parent directory
    print('File name : ', os.path.basename(__file__))
    print('Directory Name: ', os.path.dirname(os.path.realpath(__file__)))
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Get path for the first (old) directory
    dir_path_search = os.path.join(dir_path, first)
    print('Directory Search Path : ', dir_path_search)

    # create list of files and directories in the first (old) directory
    dir_list = os.listdir(dir_path_search)
    print('Found Files/Folders: ', dir_list)

    # check if the second (new) directory exists
    new_dir_path = os.path.join(dir_path, second)
    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)

    for file in dir_list:
        file_name = Path(file).stem
        # file_name = os.path.splitext(file)[0]
        old_file_path = os.path.join(dir_path_search, file)
        new_file_path_no_ext = os.path.join(new_dir_path, file_name)
        with Image.open(old_file_path) as im:
            img = im.convert('RGB')
            img.save(f"{new_file_path_no_ext}.png")

```

### output:

```py
# (venv) ifeanyi@Ifeanyis modules % python main.py Pokedex Pokedex_PNG
# File name :  main.py
# Directory Name:  /Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/modules
# Directory Search Path :  /Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/modules/Pokedex
# Found Files/Folders:  ['squirtle.jpeg', 'charmander.jpeg', 'bulbasaur.jpeg', 'pikachu.jpeg']

```

![](https://user-images.githubusercontent.com/32337103/235792392-673acde8-8da1-41fc-aafb-f3a07a735301.png)

</details>

+PYTHON PDF

<details>
  <summary>115. Python PDF - Different Versions </summary>

# Different Versions

### What you will see with version 1.26:

```pybs
pip install PyPDF2==1.26
```

```py
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
	 
for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)
 
with open('watermarked_output.pdf', 'wb') as file:
  output.write(file)
```

### What you will see with latest version:

```pybs
pip install PyPDF2
```

```py
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()
 
for i in range(len(template.pages)):
  page = template.pages[i]
  page.merge_page(watermark.pages[0])
  output.add_page(page)
 
with open('watermarked.pdf', 'wb') as file:
  output.write(file)
```

</details>

<details>
  <summary>116. Python PDF - PyPDF2 numPages </summary>

# Install pyPDF2 library

```pybs
pip install PyPDF2==1.26
```

# numPages

### main.py:

```py
import PyPDF2

with open('pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
```

### output:

```py
# 1
```

![](https://user-images.githubusercontent.com/32337103/236008313-e0e6e067-1557-4fe1-8b9f-66a4d5521785.png)

</details>

<details>
  <summary>117. Python PDF - PyPDF2 getPage() </summary>

# getPage()

### main.py:

```py
import PyPDF2

with open('pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getPage(0))
```

### output:

```py
# {'/Type': '/Page', '/Parent': IndirectObject(4, 0), '/Resources': IndirectObject(11, 0),
#'/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I':
#<PyPDF2.generic.BooleanObject object at 0x102ca0890>}, '/Contents': IndirectObject(2, 0)}

```

![](https://user-images.githubusercontent.com/32337103/236010253-64ccee89-e4bc-4e33-8064-1a4e5a75d1dc.png)

</details>

<details>
  <summary>118. Python PDF - PyPDF2 Rotate File </summary>

# Rotate File

### main.py:

```py
import PyPDF2

with open('pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdf/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
```

![](https://user-images.githubusercontent.com/32337103/236123037-fde5b063-17bb-4f08-92e4-992f612411dd.png)
![](https://user-images.githubusercontent.com/32337103/236123125-f228fadc-416a-4c1b-9ce8-cde998fb9806.png)

</details>

<details>
  <summary>119. Python PDF - PyPDF2 Merge Files </summary>

# Merge Files

### main.py:

```py
import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('pdf/super.pdf')

pdf_combiner(inputs)

```

![](https://user-images.githubusercontent.com/32337103/236124927-e847da7b-0861-4d2e-862f-66abf64b6509.png)
![](https://user-images.githubusercontent.com/32337103/236124993-7e75cb08-d908-4e21-8ca4-35caac06bb1e.png)

</details>

<details>
  <summary>120. Python PDF - PyPDF2 Watermark Files </summary>

# Watermark Files

### main.py:

```py
import PyPDF2

template = PyPDF2.PdfFileReader(open('pdf/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('pdf/watermarked_output.pdf', 'wb') as file:
    output.write(file)
```

![](https://user-images.githubusercontent.com/32337103/236154895-410e25a6-2f7a-40e1-b8a3-f2b3dde59fe3.png)
![](https://user-images.githubusercontent.com/32337103/236162181-acc71180-e078-40a6-b398-0878db6723fe.png)

</details>

+PYTHON EMAILS

<details>
  <summary>121. Python Emails - Send an Email </summary>

# Send an Email

### main.py:

```py
import smtplib
from email.message import EmailMessage

HOST = "smtp.gmail.com"
PORT = 465
EMAIL_ADDRESS = 'test.omeatai@gmail.com'
EMAIL_PASSWORD = 'gabeggupikasip'
EMAIL_FROM = 'Test Email'
EMAIL_TO = 'cokava3776@larland.com'
YOUR_SUBJECT = 'You won 1,000,000 dollars!'
YOUR_MESSAGE = "I am a Python Master! \n\nI just won $1,000,000 😀."

email = EmailMessage()
email['from'] = EMAIL_FROM
email['to'] = EMAIL_TO
email['subject'] = YOUR_SUBJECT
email.set_content(YOUR_MESSAGE)

# FOR GMAIL:
with smtplib.SMTP_SSL(HOST, PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(email)
    # smtp.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_TO, msg=YOUR_MESSAGE)
    print('all good boss..')

# NOT GMAIL:
# with smtplib.SMTP(host=HOST, port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(email)
#     print('all good boss..')

```

![](https://user-images.githubusercontent.com/32337103/236231546-52df2b6f-eec4-40b4-8662-e9e8718e8e22.png)
![](https://user-images.githubusercontent.com/32337103/236231921-1b70ea09-82e7-41d9-a070-670981d9c242.png)

</details>

<details>
  <summary>122. Python Emails - Send Email with html Template </summary>

# Send Email with html Template

### main.py:

```py
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_text = Template(Path('index.html').read_text())

HOST = "smtp.gmail.com"
PORT = 465
EMAIL_ADDRESS = 'test.omeatai@gmail.com'
EMAIL_PASSWORD = 'gabeggupikasip'
EMAIL_FROM = 'Test Email'
EMAIL_TO = 'cokava3776@larland.com'
YOUR_SUBJECT = 'You won 1,000,000 dollars!'
YOUR_MESSAGE = "I am a Python Master! \n\nI just won $1,000,000 😀."

email = EmailMessage()
email['from'] = EMAIL_FROM
email['to'] = EMAIL_TO
email['subject'] = YOUR_SUBJECT
# email.set_content(YOUR_MESSAGE)
email.set_content(html_text.substitute({'name': 'TinTin'}), 'html')

# FOR GMAIL:
with smtplib.SMTP_SSL(HOST, PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(email)
    print('all good boss..')

```

### index.html:

```html
<!DOCTYPE html>
<html>
  <head> </head>
  <body>
    You just won so much money $name.
  </body>
</html>
```

![](https://user-images.githubusercontent.com/32337103/236250275-d95c9e56-1670-47ee-9088-868dc040d79b.png)
![](https://user-images.githubusercontent.com/32337103/236250471-c9b8ed15-e84b-412a-8ca4-7c1b15a3a8f6.png)

</details>

+PASSWORD CHECKER

<details>
  <summary>123. Password Checker - Password API </summary>

# Install requests

```pybs
pip install requests
```

# Hashing Passwords

![](https://user-images.githubusercontent.com/32337103/236257849-26d71dec-db27-40df-8129-0bd08f29d1cd.png)

# Get Password range from API

### main.py:

```py
import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)

print(res)
print(res.status_code)
```

### output:

```py
# <Response [200]>
# 200
```

![](https://user-images.githubusercontent.com/32337103/236335891-3e3fd2e3-a60e-417f-a064-10e684e73653.png)

</details>

<details>
  <summary>123. Password Checker - Encoding Password with SHA1 Hashing </summary>

# Encoding Password with SHA1 Hashing

### main.py:

```py
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def pwned_api_check(password):
    encoded_password = password.encode('utf-8')
    sha1_hash_object = hashlib.sha1(encoded_password)
    sha1password = sha1_hash_object.hexdigest().upper()
    print(encoded_password)
    print(sha1_hash_object)
    print(sha1password)
    return sha1password

pwned_api_check("password123")

```

### output:

```py
# b'password123'
# <sha1 _hashlib.HASH object @ 0x104d4c710>
# CBFDAC6008F9CAB4083784CBD1874F76618D2A97
```

![](https://user-images.githubusercontent.com/32337103/236337903-2a63f4b3-6233-44eb-a54d-4a4491302f2f.png)

</details>

<details>
  <summary>124. Password Checker - Get similar Passwords from API  </summary>

# Get similar Passwords from API

### main.py:

```py
import hashlib

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    pass


def pwned_api_check(password):
    encoded_password = password.encode('utf-8')
    sha1_hash_object = hashlib.sha1(encoded_password)
    sha1password = sha1_hash_object.hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    text_response = response.text
    return first5_char, tail, sha1password, response, text_response


sha1_head, sha1_tail, sha1pass, resp, hash_passwords = pwned_api_check("password123")
print(sha1_head)
print(sha1_tail)
print(sha1pass)
print(resp)
print(hash_passwords)

```

### output:

```py
# CBFDA
# C6008F9CAB4083784CBD1874F76618D2A97
# CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# <Response [200]>
# 00791BB54CC9122C70C1156FD97134EB83E:3
# 008CDEBE10E31BF09C9BD20CBCC2C9CEDA3:2
# 00BD64FF4BE8674BC4C85CE380856184F9C:1
# 014BD2A0B6A9CE1553A4E1F48F57A88B40A:1
# 018976509BD8782F7B991A1B559150A504B:1
# 0195EA9FE8111E4BF79C5E3062AC43B48E7:1
# 01CA8E858E0AF42EC10F950BE58D9BC2548:1
# 01D17A3DCD8311E9FE4B9E5DC719861E431:1
# --------------------------------------------
```

![](https://user-images.githubusercontent.com/32337103/236342158-585128bf-6f49-4256-8b43-99af38d0e9d2.png)

</details>

<details>
  <summary>125. Password Checker - Separating Passwords from Counts </summary>

# Separating Passwords from Counts

### main.py:

```py
import hashlib

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    print(hashes)
    for h, count in hashes:
        print(h, count)


def pwned_api_check(password):
    encoded_password = password.encode('utf-8')
    sha1_hash_object = hashlib.sha1(encoded_password)
    sha1password = sha1_hash_object.hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    text_response = response.text
    return first5_char, tail, sha1password, response


sha1_head, sha1_tail, sha1pass, resp = pwned_api_check("password123")

get_password_leaks_count(resp, sha1_tail)

```

### output:

```py
# <generator object get_password_leaks_count.<locals>.<genexpr> at 0x104084900>
# 00791BB54CC9122C70C1156FD97134EB83E 3
# 008CDEBE10E31BF09C9BD20CBCC2C9CEDA3 2
# 00BD64FF4BE8674BC4C85CE380856184F9C 1
# 014BD2A0B6A9CE1553A4E1F48F57A88B40A 1
# 018976509BD8782F7B991A1B559150A504B 1
# 0195EA9FE8111E4BF79C5E3062AC43B48E7 1
# 01CA8E858E0AF42EC10F950BE58D9BC2548 1
# 01D17A3DCD8311E9FE4B9E5DC719861E431 1
# 01D6E29A6B4937A3291AC026BE40D97A345 1
# 02F089AA64C104FF24007DC566F85BE1E3D 1
```

![](https://user-images.githubusercontent.com/32337103/236345022-ebad5274-179e-4cd1-9f9a-c26e173c7c44.png)

</details>

<details>
  <summary>126. Password Checker - Get Password Leaks Count </summary>

# Get Password Leaks Count

### main.py:

```py
import hashlib
import sys
import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    encoded_password = password.encode('utf-8')
    sha1_hash_object = hashlib.sha1(encoded_password)
    sha1password = sha1_hash_object.hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

```

### output:

```py
# (venv) modules % python main.py hello iloveu password123# this#is#my#password#
# hello was found 264691 times... you should probably change your password!
# iloveu was found 313982 times... you should probably change your password!
# password123# was found 385 times... you should probably change your password!
# this#is#my#password# was NOT found. Carry on!
# done!

```

![](https://user-images.githubusercontent.com/32337103/236487375-a198c995-438c-4ea3-9453-5b097b8d4429.png)


```py

```

```py

```

```py

```

```py

</details>
