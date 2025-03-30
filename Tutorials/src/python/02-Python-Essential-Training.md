## +LinkedIn - Python Essential Training

## [COURSE](https://www.linkedin.com/learning/python-essential-training-18764650/getting-started-with-python?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false)

<details>
<summary>1. Install Jupyter Notebook </summary>

# Install Notebook

```py
pip install notebook
```

# Run Jupyter Notebook

```py
jupyter notebook
```

# #END</details>

<details>
<summary>2. Run Python </summary>

# Run Python

```py
python
```

```x
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

```py
>>> import this
```

```x
The Zen of Python, by Tim Peters

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
>>>
```

# #END</details>

<details>
<summary>3. Python Challenge - Factorial Challenge </summary>

# Python Challenge - Factorial Challenge

The factorial function gives the number of possible arrangements of a set of items of length "n"

For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 _ 3 _ 2 \* 1

5! = 5 _ 4 _ 3 _ 2 _ 1 = 120

6! = 6 _ 5 _ 4 _ 3 _ 2 \* 1 = 720

etc.

In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1

For the purposes of this exercise, factorials are only defined for positive integers (including 0)

# Solution 1 - Using While Loop

```py
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    i = 0
    f = 1
    while i < num:
        i = i + 1
        f = f * i

    return f


# return 120
print(factorial(5))

# return 720
print(factorial(6))

# return 1
print(factorial(0))

# return None
print(factorial(-2))

# return None
print(factorial(1.2))

# return None
print(factorial('spam spam spam spam spam spam'))
```

```x
120
720
1
None
None
None
```

# Solution 2 - Using Recursion

```py
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    return num * factorial(num - 1)


# return 120
print(factorial(5))

# return 720
print(factorial(6))

# return 1
print(factorial(0))

# return None
print(factorial(-2))

# return None
print(factorial(1.2))

# return None
print(factorial('spam spam spam spam spam spam'))
```

```x
120
720
1
None
None
None
```

# #END</details>

<details>
<summary>4. Ints and Floats </summary>

# Ints and Floats

### Dividing int with float

```py
20 / 4
```

```x
5.0
```

### Flooring int with float

```py
20 // 4
```

```x
5
```

### Adding int with float

```py
4 + 4.0
```

```x
8.0
```

### Multiplying int with float

```py
4 * 4.0
```

```x
16.0
```

### Exponentiating int with float

```py
4 ** 4.0
```

```x
256.0
```

### Converting float to int

```py
int(4 ** 4.0)
```

```x
256
```

```py
int(8.9)
```

```x
8
```

```py
int(8.99999999)
```

```x
8
```

```py
int(14/3)
```

```x
4
```

### Rounding floats

```py
14/3
# 4.666666666666667
round(14/3, 2)
```

```x
4.67
```

```py
1.2 - 1.0
# 0.19999999999999996
round(1.2 - 1.0, 2)
```

```x
0.2
```

# #END</details>

<details>
<summary>5. Using the Decimal Module for float Precision </summary>

# Using the Decimal Module for float Precision

### getcontext() attributes

```py
from decimal import Decimal, getcontext

getcontext()
```

```x
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1,
clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
```

### Set getcontext() precision

```py
from decimal import Decimal, getcontext

getcontext().prec=4
getcontext()
```

```x
Context(prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1,
clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
```

### Use Decimal function with precision

```py
from decimal import Decimal, getcontext

getcontext().prec=4
Decimal(1) / Decimal(3)
```

```x
0.3333
```

```py
getcontext().prec=2
Decimal(1) / Decimal(3)
```

```x
0.33
```

```py
Decimal(3.14)
```

```x
3.140000000000000124344978758017532527446746826171875
```

```py
Decimal('3.14')
```

```py
3.14
```

# #END</details>

<details>
<summary>6. Booleans </summary>

# Booleans

```py

```

# #END</details>
