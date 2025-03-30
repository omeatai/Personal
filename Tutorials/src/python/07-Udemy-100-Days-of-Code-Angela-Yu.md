## UDEMY-100 DAYS OF CODE: THE COMPLETE PYTHON PRO BOOTCAMP FOR 2023 - ANGELA YU

###### [COURSE](https://www.udemy.com/course/100-days-of-code/)

<details>
  <summary>1. Introduction - Print Function </summary>

# Example 1:

```py
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello + input("What is your name?"))
```

```py
# What is your name? Bob
# Hello Bob
```

# Example 2:

```py
#This code prints the number of characters in a user's name.
print(len input ("What is your name?") ) )
```

```py
# What is your name? Bob
# 3
```

# Example 3:

```py
name = input("What is your name?")
print(name)
```

```py
# What is your name? Mark
# Mark
```

# Task 1:

```py
#1. Create a greeting for your program.
print("Welcome to the band name generator.")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of a pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
# https://band-name-generator-end.appbrewery.repl.run/
```

```py
# Welcome to the band name generator.
# Which city did you grow up in?
# Bristol
# What is the name of a pet?
# Rabbit
# Your band name could be  Bristol Rabbit
```

</details>

<details>
  <summary>2. Number Manipulation </summary>

# Example 1:

Rounding Numbers -

```py
print(round(8 / 3, 2))
```

```py
# 2.67
```

# Example 2:

Flooring Numbers -

```py
print(8 // 3)
```

```py
# 2
```

# Example 3:

```py
result = 4 / 2
result /= 2
print(result)
```

```py
# 1.0
```

# Example 4:

```py
score = 0
score += 1
print(score)
```

```py
# 1
```

</details>

<details>
  <summary>3. Using F Strings </summary>

# Example 1:

```py
score = 0
print("your score is " + str(score))
```

```py
score = 0
height = 1.8
isWinning = True
#f-String
print (f"your score is {score}")
```

```py
# your score is 0
```

# Example 2:

```py
score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

```py
# your score is 0, your height is 1.8, you are winning is True
```

# Example 3:

```py
age = input("What is your current age? ")

rem = (90 - int(age))
d =  rem * 365
w = rem * 52
m = rem * 12

print(f"You have {d} days, {w} weeks, and {m} months left.")
```

```py
# What is your current age? 35
# You have 20075 days, 2860 weeks, and 660 months left.
```

# Example 4:

Using the Format function -

```py
format(salesAmount, '.2f')
```

Using the Format Method:

```py
"{:.2f}".format(salesAmount)
```

# Task 1:

```py
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = (tip/100+1) * bill
bill_for_each_person = "{:.2f}".format(bill_with_tip/people)
print(f'Each person should pay: ${bill_for_each_person}.')
```

```py
# Welcome to the tip calculator!
# What was the total bill?
# $150.00
# How much tip would you like to give? 10, 12, or 15?
# 12
# How many people to split the bill?
# 5
# Each person should pay: $33.60.
```

</details>

<details>
  <summary>4. If Else Statements </summary>

# Example 1:

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
	print("You can ride the rollercoaster!")
else:
	print("Sorry, you have to grow taller before you can ride.")
```

```py
# Welcome to the rollercoaster!
# What is your height in cm? 180
# You can ride the rollercoaster!
```

# Example 2:

```py
number = int(input("Which number do you want to check? "))

if number%2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
```

```py
# Which number do you want to check? 51
# This is an odd number.
```

# Example 3:

Nested If/Else -

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age <= 18:
		print("Please pay $7.")
	else:
		print("Please pay $12.")
else:
	print("Sorry, you have to grow taller before you can ride.")
```

```py
# Welcome to the rollercoaster!
# What is your height in cm? 180
# You can ride the rollercoaster!
# What is your age? 19
# Please pay $12.
```

# Example 4:

Nested If/Elif/Else -

```py
if condition1:
  do A
elif condition2:
  do B
else:
  do this
```

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))

	if age < 12:
		print("Please pay $5.")
	elif age <= 18:
		print("Please pay $7.")
	else:
		print("Please pay $12.")
else:
	print("Sorry, you have to grow taller before you can ride.")
```

```py
# Welcome to the rollercoaster!
# What is your height in cm? 180
# You can ride the rollercoaster!
# What is your age? 11
# Please pay $5.
```

# Example 5:

```py
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

```

```py
# enter your height in m: 1.8034
# enter your weight in kg: 120
# Your BMI is 37, you are clinically obese.
```

# Example 6:

```py
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if not year % 100 == 0 or year % 100 == 0 and year % 400 == 0:
        print('Leap year.')
    else:
        print('Not leap year.')
else:
    print('Not leap year.')
```

```py
# Which year do you want to check? 2000
# Leap year.
```

# Example 7:

Multiple If statements -

```py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child tickets are $5.")
	elif age <= 18:
		bill = 7
		print("Youth tickets are $7.")
	else:
		bill = 12
		print("Adult tickets are $12.")

	wants_photo = input("Do you want a photo taken? Y or N. ")
	if wants_photo == "Y":
		bill += 3
	print(f"Your final bill is ${bill}.")
else:
	print("Sorry, you have to grow taller before you can ride.")
```

```py
# Welcome to the rollercoaster!
# What is your height in cm? 181
# You can ride the rollercoaster!
# What is your age? 22
# Adult tickets are $12.
# Do you want a photo taken? Y or N. Y
# Your final bill is $15.
```

# Example 8:

```py
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
pepperoni_bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
  pepperoni_bill = 3
else:
  bill += 25
  pepperoni_bill = 3

if add_pepperoni == "Y":
	if size == "S":
		bill += 2
	else:
		bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
```

```py
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M, or L S
# Do you want pepperoni? Y or N N
# Do you want extra cheese? Y or N Y
# Your final bill is: $16.
```

# Example 9:

```py
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = "true"
love = "love"
names = (name1 + name2).lower().strip()
true_count = 0
love_count = 0

for i in true:
    true_count += names.count(i)

for j in love:
    love_count += names.count(j)

love_score = int(f"{true_count}{love_count}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score =< 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
```

```py
# Welcome to the Love Calculator!
# What is your name?
# Kanye West
# What is their name?
# Kim Kardashian
# Your score is 42, you are alright together.
```

# Example 10:

```py
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

choice1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
	choice2=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
	if choice2 == "wait":
		choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?").lower()
		if choice3 == "red":
			print("It's a room full of fire. Game Over.")
		elif choice3 == "yellow":
			print("You found the treasure! You Win!")
		elif choice3 == "blue":
			print("You enter a room of beasts. Game Over.")
		else:
			print("You chose a door that doesn't exist. Game Over.")
	else:
		print("You got attacked by an angry trout. Game Over.")
else:
	print("You fell into a hole. Game Over.")
```

```py
# Welcome to Tresure Island.
# Your mission is to find the treasure.
# You're at a crossroad, where do you want to go? Type "left" or "right". left
# You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.wait
# You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?yellow
# You found the treasure! You Win!
```

# Example 11:

```py
import random

listofnum = [1, 2, 3, 4, 5]
# 1
print(random.choice(listofnum))

# 2
random.shuffle(listofnum)
print(listofnum)
```

```py
# 4
# [2, 1, 4, 5, 3]
```

# Example 12:

```py
import random

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

start = 'ON'

choices = ['left', 'right']
random_choice = random.choice(choices)
# print(random_choice)
choice = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'\n"
).lower().strip()
if choice == random_choice:
    print('Great Choice! Way to go. keep going forward....')
else:
    print('Fall into a Hole. Game Over.')
    start = 'OFF'

choices = ['swim', 'wait']
random_choice = random.choice(choices)
# print(random_choice)
if start == 'ON':
    choice = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
    ).lower().strip()

    if choice == random_choice:
        print('Great Choice! Way to go. keep going forward....')
    else:
        print('Attacked by Trout. Game Over.')
        start = 'OFF'

choices = ['red', 'yellow', 'blue']
random_choice = random.choice(choices)
# print(random_choice)
if start == 'ON':
    choice = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
    ).lower().strip()

    if choice == random_choice:
        print('Congratulations! You WON the challenge....')
    elif choice == "red":
        print('Burned by Fire. Game Over.')
    elif choice == "blue":
        print('Eaten by Beasts. Game Over.')
    else:
        print('Drowned by Water. Game Over.')
```

```py
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go? Type 'left' or 'right'
# left
# Great Choice! Way to go. keep going forward....
# You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.
# swim
# Great Choice! Way to go. keep going forward....
# You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
# yellow
# Congratulations! You WON the challenge....
```

</details>

<details>
  <summary>5. Importing Modules </summary>

# Example 1:

Import from a single module in same folder -

person.py:

```py
name = "Ben"
account_no = "113748919"
age = 21
```

main.py:

```py
from person import account_no

print(account_no)
```

```py
# 113748919
```

# Example 2:

Import from multiple modules in same folder -

person.py:

```py
name = "Ben"
account_no = "113748919"
age = 21
```

school.py:

```py
department = "Economics"
year = 2011
```

main.py:

```py
from person import account_no
from school import year

print(account_no)
print(year)

```

```py
# 113748919
# 2011
```

# Example 3:

Import from multiple modules in different folder -

host/init.py:

```py
__all__ = ["person", "school"]
```

host/person.py:

```py
name = "Ben"
account_no = "113748919"
age = 21
```

host/school.py:

```py
department = "Economics"
year = 2011
```

main.py:

```py
from host import *

print(person.account_no)
print(school.year)

```

```py
# 113748919
# 2011
```

</details>

<details>
  <summary>6. Generating Random Numbers </summary>

# Example 1:

```py
import random

#Random number between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

#Random number between 0 and 1
random_float = random.random()
print(random_float)
```

```py
# 4
# 0.35402952193969894
```

# Example 2:

Random number between 0 and 5:

```py
import random

#Random number between 1 and 10
random_integer = random.randint(1, 10)
# print(random_integer)

#Random number between 0 and 1
random_float = random.random()
# print(random_float)

#Random number between 0 and 5
for i in range(21):
    print(f"{i}: {format(round(random.random() * 5,2),'.2f')}")
```

```py
# 0: 2.61
# 1: 1.78
# 2: 1.57
# 3: 4.22
# 4: 0.43
# 5: 2.41
# 6: 2.86
# 7: 3.35
# 8: 4.37
# 9: 1.13
# 10: 0.60
# 11: 0.66
# 12: 3.54
# 13: 3.69
# 14: 2.81
# 15: 2.98
# 16: 3.79
# 17: 3.87
# 18: 3.01
# 19: 3.88
# 20: 0.95
```

# Example 3:

Select randomly from list of Choices:

```py
import random

print(random.choice(["Heads", "Tails"]))
```

```py
# Tails
```

# Example 4:

```py
import random

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
```

```py
# Heads
```

</details>

<details>
  <summary>7. Python Lists </summary>

# Example 1:

Get a List Item from the index Position -

```py
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(states_of_america[0])
```

```py
# Delaware
```

# Example 2:

Get an Item from the end of the list -

```py
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(states_of_america[-2])
```

```py
# Alaska
```

# Example 3:

Changing the value of an item in the List:

```py
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

states_of_america[1] = "Pencilvania"
print(states_of_america[1])
```

```py
# Pencilvania
```

# Example 4:

Adding Items to a List:

```py
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

states_of_america.append("Angelaland")
print(states_of_america[-1])
```

```py
# Angelaland
```

# Example 5:

Adding more than one item to the List:

```py
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

states_of_america.extend(["Angelaland", "Lagosland", "Hopeland"])
print(states_of_america[-5:])
```

```py
# ['Alaska', 'Hawaii', 'Angelaland', 'Lagosland', 'Hopeland']
```

# Example 6:

Randomly selecting items from a List:

```py
import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

person_to_pay = names[random.randint(0, len(names) - 1)]
print(f"{person_to_pay} is going to buy the meal today!")
```

```py
# Give me everybody's names, separated by a comma.
# James, John, Luke, Mary, Ashley, Dan
# Ashley is going to buy the meal today!
```

# Example 7:

```py
import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

person_to_pay = random.choice(names)
print(f"{person_to_pay} is going to buy the meal today!")
```

```py
# Give me everybody's names, separated by a comma.
# James, John, Luke, Mary, Ashley, Dan
# Ashley is going to buy the meal today!
```

# Example 8:

Nested Lists:

```py
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

```

```py
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
```

# Example 9:

```py
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? \n")

column_to_index = int(position[0]) - 1
row_to_index = int(position[1]) - 1
map[row_to_index][column_to_index] = "X"

print(f"{row1}\n{row2}\n{row3}")
```

```py
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', '⬜️️', '⬜️️']
# Where do you want to put the treasure?
# 23
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️️']
```

# Example 10:

RPS Game -

```py
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? \n")

print('You chose:')

player_choice = None

if choice == '0':
    print(rock)
    player_choice = "rock"
elif choice == '1':
    print(paper)
    player_choice = "paper"
elif choice == '2':
    print(scissors)
    player_choice = "scissors"
else:
    print('Wrong Input. Try Again!')

print('Computer chose:')

computer_choice = random.choice(["rock", "paper", "scissors"])

if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
elif computer_choice == "scissors":
    print(scissors)

if (player_choice == "rock" and computer_choice == "paper") or (
        player_choice == "paper"
        and computer_choice == "scissors") or (player_choice == "scissors"
                                               and computer_choice == "rock"):
    print('You Lose.')
elif (player_choice == "rock" and computer_choice == "scissors") or (
        player_choice == "paper"
        and computer_choice == "rock") or (player_choice == "scissors"
                                           and computer_choice == "paper"):
    print('You Won! Congrats!')
elif player_choice == None:
    print("")
else:
    print("It's a Tie!")

```

```py
# What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?
# 1
# You chose:

#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)

# Computer chose:

#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

# You Won! Congrats!
```

```py
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")

```

</details>

<details>
  <summary>8. Python For Loops </summary>

# Example 1:

Looping through Lists -

```py
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
	print(fruit)
```

```py
# Apple
# Peach
# Pear
```

# Example 2:

```py
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score=0
for i in student_scores:
    if i > highest_score:
        highest_score = i

print(f"The highest score in the class is: {highest_score}")
```

```py
# Input a list of student scores 10 20 30 40 70 80 40 30
# [10, 20, 30, 40, 70, 80, 40, 30]
# The highest score in the class is: 80
```

# Example 3:

```py
total = 0

for i in range(0,101,2):
    total += i
print(total)
```

```py
# 2550
```

# Example 4:

```py
total2 = 0

for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)
```

```py
# 2550
```

# Example 5:

```py
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

```py
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
```

# Example 6:

```py
#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(nr_letters):
    password += random.choice(letters)
for j in range(nr_symbols):
    password += random.choice(symbols)
for k in range(nr_numbers):
    password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = ""

while nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0:
    choice = random.randint(0, 2)
    if choice == 0 and nr_letters > 0:
        password2 += random.choice(letters)
        nr_letters -= 1
    elif choice == 1 and nr_symbols > 0:
        password2 += random.choice(symbols)
        nr_symbols -= 1
    elif choice == 2 and nr_numbers > 0:
        password2 += random.choice(numbers)
        nr_numbers -= 1

print(password2)

```

```py
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 3
# How many symbols would you like?
# 3
# How many numbers would you like?
# 3
# qJk##*130
# (z96P%T6)
```

# Example 7:

```py
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = []

for i in range(nr_letters):
    password2.append(random.choice(letters))
for j in range(nr_symbols):
    password2 += random.choice(symbols)
for k in range(nr_numbers):
    password2 += random.choice(numbers)

random.shuffle(password2)

mypassword = ""
for char in password2:
    mypassword += char
print(mypassword)
```

```py
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 3
# How many symbols would you like?
# 3
# How many numbers would you like?
# 3
# jgK*+*220
# e3g6*((m9
```

</details>

<details>
  <summary>9. Python Functions </summary>

# Example 1:

```py
def my_function():
  print("Hello")
  print("Bye")
my_function ()
```

```py
# Hello
# Bye
```

</details>

<details>
  <summary>10. Python While Loops </summary>

# Example 1:

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

step = 0
while step < 6:
    move()
    jump()
    step += 1
```

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
```

</details>

<details>
  <summary>11. Hangman </summary>

# Task 1:

```py
#Step 1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    print("Right" if letter == guess else "Wrong")
```

```py
# Guess a letter: a
# Right
# Right
# Wrong
# Wrong
# Wrong
# Right
# Wrong
# Wrong
```

# Task 2:

```py
#Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for index, letter in enumerate(chosen_word):
	if letter == guess:
			display[index] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

```

```py
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

word_length = len(chosen_word)
for position in range(word_length):
  letter = chosen_word [position]
  if letter == guess:
    display[position] = letter
```

```py
# Pssst, the solution is aardvark.
# ['_', '_', '_', '_', '_', '_', '_', '_']
# Guess a letter: a
# ['a', 'a', '_', '_', '_', 'a', '_', '_']
```

# Task 3:

```py
#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter
    print(display)

```

```py
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  #Check_guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
    if letter == guess:
      display[position] = letter

  print (display)

  if "_" not in display:
    end_of_game = True
    print("You win.")
```

```py
# ['b', 'a', 'b', 'o', 'o', '_']
# Guess a letter: n
# Current position: 0
#  Current letter: b
#  Guessed letter: n
# Current position: 1
#  Current letter: a
#  Guessed letter: n
# Current position: 2
#  Current letter: b
#  Guessed letter: n
# Current position: 3
#  Current letter: o
#  Guessed letter: n
# Current position: 4
#  Current letter: o
#  Guessed letter: n
# Current position: 5
#  Current letter: n
#  Guessed letter: n
# ['b', 'a', 'b', 'o', 'o', 'n']
```

# Task 4:

```py
#Step 4

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    found = False
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            found = True

    if found == False:
        lives -= 1
    else:
        found = False
    if lives == 0:
        print("You lose.")
        print(stages[lives])
        break

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

```

```py
#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
```

```py
# Pssst, the solution is baboon.
# Guess a letter: s
# _ _ _ _ _ _

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: s
# _ _ _ _ _ _

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# Guess a letter: s
# _ _ _ _ _ _

#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# Guess a letter: s
# _ _ _ _ _ _

#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========

# Guess a letter: s
# _ _ _ _ _ _

#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========

# Guess a letter: s
# You lose.

#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
```

# Task 5:

```py
#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
```

```py

#  _
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/
# Guess a letter: a
# a _ _ _ _ _

#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========

# Guess a letter: b
# You guessed b, that's not in the word. You lose a life.
# a _ _ _ _ _

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: e
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: o
# You guessed o, that's not in the word. You lose a life.
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# Guess a letter: l
# You guessed l, that's not in the word. You lose a life.
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# Guess a letter: m
# You guessed m, that's not in the word. You lose a life.
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========

# Guess a letter: c
# You guessed c, that's not in the word. You lose a life.
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========

# Guess a letter: f
# You guessed f, that's not in the word. You lose a life.
# You lose.
# a _ e _ _ e

#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========

```

</details>

<details>
  <summary>12. Caesar Cipher </summary>

# Example 1:

```py
# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Welcome")
    print("My Name is Ben.")
    print("How old are you?")

greet()
```

```py
# Welcome
# My Name is Ben.
# How old are you?
```

# Example 2:

```py
#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Mike")

```

```py
# Hello Mike
# How do you do Mike?
```

# Example 3:

```py
#Functions with more than 1 input
def greet_with_inputs(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_inputs("Bob", "London")
```

```py
# Hello Bob
# What is it like in London?
```

# Example 4:

```py
#Functions with more than 1 input
def greet_with_inputs(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_inputs(location="London", name="Adam")
```

```py
# Hello Adam
# What is it like in London?
```

# Example 5:

```py
def paint_calc(height,width,cover):
    nums_of_cans = round(height*width/cover)
    print(f"You'll need {nums_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```

```py
import math

def paint_calc(height, width, cover):
  area = height*width
  num_of_cans = math.ceil(area / cover)
  print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```

```py
# Height of wall: 2
# Width of wall: 4
# You'll need 2 cans of paint.
```

# Example 6:

```py
def prime_checker(number):
    isPrime = True
    if number in {0, 1}:
        print("It's a prime number.")
        return
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    print(
        "It's not a prime number." if not isPrime else "It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
```

```py
# Check this number: 7
# It's a prime number.
```

# Example 7:

```py
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encryted_text = ""
    for letter in text:
        if letter not in alphabet:
            encryted_text += letter
        else:
            new_letter = ""
            index_pos = alphabet.index(letter)
            if (index_pos + 1 + shift) > 26:
                pos = (index_pos + 1 + shift) % 26
                new_letter = alphabet[pos - 1]
            else:
                new_letter = alphabet[index_pos + shift]
            encryted_text += new_letter
    print(f"The encoded text is {encryted_text}")

encrypt(text, shift)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

```

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.
  #e.g.
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)
```

```py
# Type 'encode' to encrypt, type 'decode' to decrypt:
# en
# Type your message:
# I love music
# Type the shift number:
# 5
# The encoded text is n qtaj rzxnh
```

# Example 8:

```py
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while not direction[0] in {"e", "d"}:
    print("You selected an Invalid option to encrypt or decrypt. Try again.")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


if direction[0] == "e":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
```

```py
# Type 'encode' to encrypt, type 'decode' to decrypt:
# d
# Type your message:
# lipps
# Type the shift number:
# 4
# The decoded text is hello
```

# Example 9:

```py
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(text_type, shift_amount, direction_type):
    if direction_type[0] == "e":
        cipher_text = ""
        for letter in text_type:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction_type[0] == "d":
        plain_text = ""
        for letter in text_type:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")
    else:
        print(
            "You selected an Invalid option to encrypt or decrypt. Try again.")


caesar(text_type=text, shift_amount=shift, direction_type=direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

```

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
```

```py
# Type 'encode' to encrypt, type 'decode' to decrypt:
# m
# Type your message:
# hello
# Type the shift number:
# 4
# You selected an Invalid option to encrypt or decrypt. Try again.

# Type 'encode' to encrypt, type 'decode' to decrypt:
# e
# Type your message:
# hello
# Type the shift number:
# 4
# The encoded text is lipps

# Type 'encode' to encrypt, type 'decode' to decrypt:
# d
# Type your message:
# lipps
# Type the shift number:
# 4
# The decoded text is hello
```

# Task 1:

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]

  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
```

Solved:

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
```

</details>

<details>
  <summary>13. Python Dictionaries and Nesting </summary>

# Example 1:

```py
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary.
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
```

```py
# An error in a program that prevents the program from running as expected.

# {
#   'Bug': 'An error in a program that prevents the program from running as expected.',
#   'Function': 'A piece of code that you can easily call over and over again.',
#   'Loop': 'The action of doing something over and over again.'
# }
```

# Example 2:

```py
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print (programming_dictionary)
```

```py
# {}
```

# Example 3:

```py
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
```

```py
# {
#   'Bug': 'A moth in your computer.',
#   'Function': 'A piece of code that you can easily call over and over again.'
# }
```

# Example 4:

```py
programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")
```

```py
# Bug: A moth in your computer.
# Function: A piece of code that you can easily call over and over again.
```

# Task 1:

```py
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
      student_grades[student] = "Outstanding"
    elif score > 80:
      student_grades[student] = "Exceeds Expectations"
    elif score > 70:
      student_grades[student] = "Acceptable"
    else:
      student_grades[student] = "Fail"

print(student_grades)
```

```py
# {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}
```

# Example 5:

Nested Dictionaries -

```py
#Nesting
{
  Key: [List],
  Key2:{Dict},
}

capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
```

# Example 6:

```py
#Nesting a List in a Dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 6
    }
}

print(travel_log["France"]["total_visits"])
```

```py
# 12
```

# Example 7:

```py
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

print(travel_log[0]["cities_visited"])
```

```py
# ['Paris', 'Lille', 'Dijon']
```

# Task 2:

```py
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

```

```py
# [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]
```

# Task 3:

```py
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bidders = {}
highest_bid = 0
highest_bidder = None
should_continue = True

while should_continue:
	print(logo)
	name = input("What is your name? ")
	bid = int(input("What is your bid price? $"))
	bidders[name] = bid
	ask_to_continue = input("Is there another bidder? Type 'y' or 'n'?\n")
	clear()
	if ask_to_continue.lower() == "n":
		for bidder in bidders:
			if bidders[bidder] > highest_bid:
				highest_bidder = bidder
				highest_bid = bidders[bidder]
				print({highest_bidder: highest_bid})
		should_continue = False
print(f"The highest bidder is {highest_bidder} at ${highest_bid}.")

```

```py
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

```

```py
# {'Ifeanyi': 100}
# {'James': 200}
# The highest bidder is James at $200.
```

</details>

<details>
  <summary>14. Functions with Outputs </summary>

# Example 1:

```py
#Functions with Outputs
def format_name(f_name, l_name):
    firstname = f_name.title()
    lastname = l_name.title()
    print(f"{firstname } {lastname}")

format_name("ifeanyi", "omeata")
```

```py
# Ifeanyi Omeata
```

# Example 2:

```py
#Functions with Outputs
def format_name(f_name, l_name):
    firstname = f_name.title()
    lastname = l_name.title()
    return f"{firstname } {lastname}"

name = format_name("ifeaNyi", "omeAta")
print(name)
```

```py
# Ifeanyi Omeata
```

# Example 3:

```py
#Functions with Outputs
def format_name(f_name, l_name):
	if not f_name or not l_name:
		return
	firstname = f_name.title()
	lastname = l_name.title()
	return f"{firstname } {lastname}"

first = input("What is your first name? ")
last = input("What is your last name? ")

name = format_name(first, last)
print(name)

```

```py
# What is your first name?
# What is your last name? omeatA
# None
```

# Example 4:

```py
#Functions with Outputs
def format_name(f_name, l_name):
	if not f_name or not l_name:
		return "You did not provide Inputs."
	firstname = f_name.title()
	lastname = l_name.title()
	return f"{firstname } {lastname}"

first = input("What is your first name? ")
last = input("What is your last name? ")

name = format_name(first, last)
print(name)
```

```py
# What is your first name? ifeANYI
# What is your last name?
# You did not provide Inputs.
```

# Task 1:

```py
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year."
      else:
        return "Not leap year."
    else:
      return "Leap year."
  else:
    return "Not leap year."

def days_in_month(selected_year, selected_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(selected_year) == "Leap year.":
      month_days[1] = 29
  return month_days[selected_month-1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

```py
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(selected_year, selected_month):
  if month > 12 or month < 1:
      return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(selected_year):
      return 29
  return month_days[selected_month-1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

```py
# Enter a year: 2000
# Enter a month: 2
# 29
```

# Example 5:

Using Doc Strings -

```py
#Return as an early exit
def format_name(f_name, l_name):
	"""Take a first and last name and format it to return the title case version of the name."""
	if not f_name or not l_name:
		return "You didn't provide valid inputs."
	formated_f_name = f_name.title()
	formated_l_name = l_name.title()
	return f"Result: {formated_f_name} {formated_l_name}"

first = input("What is your first name? ")
last = input("What is your last name? ")

name = format_name(first, last)
print(name)
```

```py
# What is your first name? ifeaNYI
# What is your last name? omeATA
# Result: Ifeanyi Omeata
```

# Example 6:

```py
#Calculator

#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
```

```py
# What's the first number?: 5
# +
# -
# *
# /
# Pick an operation from the line above: *
# What's the second number?: 6
# 5 * 6 = 30
```

# Example 7:

```py
#Calculator
#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = int(input("What's the first number?: "))
    repeat_task = False
    end_task = False

    while not end_task:
        for symbol in operations:
            print(symbol)
        operation_symbol = input(
            f"Pick {'another' if repeat_task else 'an'} operation: ")
        num2 = int(
            input(
                f"What's the {'next' if repeat_task else 'second'} number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculation = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: "
        )
        if continue_calculation == "n":
            end_task = True
            calculator()
        else:
            num1 = answer
            repeat_task = True

calculator()

```

```py
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

```

```py
# What's the first number?: 6
# +
# -
# *
# /
# Pick an operation: *
# What's the second number?: 5
# 6 * 5 = 30
# Type 'y' to continue calculating with 30, or type 'n' to exit.: y
# +
# -
# *
# /
# Pick another operation: /
# What's the next number?: 4
# 30 / 4 = 7.5
# Type 'y' to continue calculating with 7.5, or type 'n' to exit.: n
# What's the first number?:

```

</details>

<details>
  <summary>15. Blackjack Game </summary>

# Task 1:

```py
import random
from replit import clear

user_cards = []
computer_cards = []


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def give_card(person, num_of_times):
    for i in range(0, num_of_times):
        person.append(deal_card())


def calculate_score(person):
    if sum(person) == 21:
        return 0
    elif sum(person) > 21 and 11 in person:
        person.remove(11)
        person.append(1)
        return sum(person)
    else:
        return sum(person)


def get_user_result():
    print(
        f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}"
    )
    print(f"Computer's first card: {computer_cards[0]}")


def get_final_result():
    print(
        f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}"
    )
    print(
        f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}"
    )


def final(who_wins):
    get_final_result()
    if who_wins == "computer":
        print("Computer Wins! You Lose!")
    elif who_wins == "user":
        print("You Win!")
    print("Game Over!")


def compare(user_score, computer_score, computers_turn=False):
    if computer_score == 0 or user_score > 21:
        final("computer")
        return True
    elif user_score == 0 or computer_score > 21:
        final("user")
        return True
    elif computer_score > user_score and computer_score < 22 and computers_turn == True:
        final("computer")
        return True
    if computers_turn == False:
        get_user_result()


def play_again():
    start_again = input("Do you want to play again? 'y' or 'n': ")
    if start_again == 'y':
        user_cards.clear()
        computer_cards.clear()
        clear()
        start_game()


def start_game():
    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        print("Goodbye!")
        return

    give_card(user_cards, 2)
    give_card(computer_cards, 2)
    get_user_result()

    draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
    while not draw_again == "n":
        give_card(user_cards, 1)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if compare(user_score, computer_score):
            play_again()
            return
        draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if compare(user_score, computer_score, computers_turn=True):
            play_again()
            return
        give_card(computer_cards, 1)


start_game()

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

```

# Solution:

```py
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

```

```py
# Do you want to play a game of Blackjack? Type 'y' or 'n': y
# Your cards: [4, 7], current score: 11
# Computer's first card: 3
# Type 'y' to get another card, type 'n' to pass: y
# Your cards: [4, 7, 8], current score: 19
# Computer's first card: 3
# Type 'y' to get another card, type 'n' to pass: n
# Your final hand: [4, 7, 8], final score: 19
# Computer's final hand: [3, 7, 10], final score: 20
# Computer Wins! You Lose!
# Game Over!
# Do you want to play again? 'y' or 'n':
```

</details>

<details>
  <summary>16. Scope and Number Guessing Game </summary>

# Example 1:

```py
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

```py
# enemies inside function: 2
# enemies outside function: 1
```

# Example 2:

```py
################### Scope ####################

enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
```

```py
# enemies inside function: 2
# enemies outside function: 2
```

# Example 3:

```py
################### Scope ####################

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
```

```py
# enemies inside function: 1
# enemies outside function: 2
```

# Example 4:

```py
################### Scope ####################

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def get_socials():
    global TWITTER_HANDLE
    return TWITTER_HANDLE

print(get_socials())
```

```py
# @yu_angela
```

# Task 1:

```py
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

numbers = [i for i in range(1, 101)]
chosen_number = random.choice(numbers)

print(f"Pssst, the correct answer is {chosen_number}")

level = 0
lives = 0
guess = 0
end_game = False

while lives in {0, 200}:
    if lives == 0:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    else:
        print("Wrong Input! Please type 'easy' or 'hard' to make a selection.")
        level = input("Choose a difficulty: ")
    lives = 10 if level[0].lower() == 'e' else 5 if level[0].lower() == 'h' else 200

print(f"You have {lives} attempts remaining to guess the number.")


def clean_data(data):
    """Clean the guessed value to ensure it's a number between 1-100."""
    if not data.isdigit():
        print("Wrong Input! Value is not a number.")
    elif not int(data) in numbers:
        print("Number Boundary Error! Only Numbers between 1-100 are allowed.")
    else:
        return True

def is_correct(data):
  """Checks to see if the guessed value is accurate
    greater than data: print 'Too high'\n'Guess again.' --> None
    less than data: print 'Too low.'\n'Guess again.' --> None
    equals data: print 'You Win!' --> True
  """
  data = int(data)
  if data > chosen_number:
    print('Too high.\nGuess again.')
  elif data < chosen_number:
    print('Too low.\nGuess again.')
  else:
    print('You Win!')
    return True

while not end_game:
    guess_is_cleaned = False

    while not guess_is_cleaned:
        guess = input("Make a guess: ")
        if clean_data(guess):
            guess_is_cleaned = True

    if not is_correct(guess):
        lives-=1
        if not lives:
          print('Game Over. You Lose!')
          end_game = True
        else:
          print(f'You have {lives} attempts remaining to guess the number.')
    else:
        end_game = True


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
```

```py
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
```

```py

# <-- WELCOME TO -->
#   _  _            _                ___
#  | \| |_  _ _ __ | |__  ___ _ _   / __|__ _ _ __  ___
#  | .` | || | '  \| '_ \/ -_) '_| | (_ / _` | '  \/ -_)
#  |_|\_|\_,_|_|_|_|_.__/\___|_|    \___\__,_|_|_|_\___|
#
#
# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 1
# Choose a difficulty. Type 'easy' or 'hard': e
# You have 10 attempts remaining to guess the number.
# Make a guess: 56
# Too high.
# Guess again.
# You have 9 attempts remaining to guess the number.
# Make a guess: 1
# You Win!
```

</details>

<details>
  <summary>17. Higher-lower-final Game </summary>

# Task 1:

```py
import random
from replit import clear
from art import logo, vs
from game_data import data

current_score = 0
end_game = False
option_a = {}
option_b = {}
message = ""


def print_upper_logo():
    """Print the upper logo"""
    print(logo)


def print_lower_logo():
    """Print the lower logo"""
    print(vs)


def generate_option_data():
    """Generate an option with random data from game_data"""
    new_option = random.choice(data)
    while new_option == option_a or new_option == option_b:
        new_option = random.choice(data)
    return new_option


def display_option(option):
    print(
        f"{'Compare A' if option == option_a else 'Against B'}: {option['name']}, a {option['description']}, from {option['country']}."
    )


def ask_question():
    answer = input("Who has more followers? Type 'A' or 'B': ")
    return answer.upper()


def compare(opt_a, opt_b, selection):
    result = opt_a['follower_count'] > opt_b['follower_count']
    if result and selection == "B" or not result and selection == "A":
        print(f"Sorry, that's wrong. Final score: {current_score}")
        print(
            f"Option A: {opt_a['follower_count']}, Option B: {opt_b['follower_count']}"
        )
        print("Goodbye!")
    else:
        return True


#start
while not end_game:
    clear()
    #print upper logo
    print_upper_logo()
    if message:
        print(message)
    #print option_a
    #Eg. Compare A: Billie Eilish, a Musician, from United States.
    if current_score == 0:
        option_a = generate_option_data()
    else:
        option_a = option_b
    display_option(option_a)
    #print lower logo
    print_lower_logo()
    #print option_b
    #Eg. Against B: Vin Diesel, a Actor, from United States.
    option_b = generate_option_data()
    display_option(option_b)
    #Ask Question
    #Eg. Who has more followers? Type 'A' or 'B': a
    answer = ask_question()
    #If wrong, print Statement and End
    #Eg. Sorry, that's wrong. Final score: 0 <Current score>
    #If right, print Statement and Continue with next LOOP
    #Eg. You're right! Current score: 1.
    result = compare(option_a, option_b, answer)
    if result:
        current_score += 1
        message = f"You're right! Current score: {current_score}."
        print(
            f"Option A: {option_a['follower_count']}, Option B: {option_b['follower_count']}"
        )
    else:
        end_game = True

```

# Solution:

```py
from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

```

```py
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# Compare A: Instagram, a Social media platform, from United States.

#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)

# Against B: UEFA Champions League, a Club football competition, from Europe.
# Who has more followers? Type 'A' or 'B': a

#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# You're right! Current score: 1.
# Compare A: UEFA Champions League, a Club football competition, from Europe.

#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)

# Against B: NBA, a Club Basketball Competition, from United States.
# Who has more followers? Type 'A' or 'B': b
# Sorry, that's wrong. Final score: 1
# Option A: 58, Option B: 47
# Goodbye!
```

</details>

<details>
  <summary>18. Coffee Machine Code </summary>

# Task 1:

```py
from resources import MENU, resources


def get_report(total_cash):
    """Print report if the user types report"""
    water = f"Water: {resources['water']}ml\n"
    milk = f"Milk: {resources['milk']}ml\n"
    coffee = f"Coffee: {resources['coffee']}g\n"
    money = f"Money: ${total_cash}"
    return water + milk + coffee + money


def get_coin_amount():
    """Calculate the total sum of all the coins inserted"""
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


def is_sufficient(choice):
    """Check if the available resources are sufficient"""
    result = True
    for resource in MENU[choice]["ingredients"]:
        available_resource = resources[resource]
        needed_resource = MENU[choice]["ingredients"][resource]
        if available_resource < needed_resource:
            print(f"Sorry there is not enough {resource}.")
            result = False
    return result


def amount_to_pay(choice):
    """Calculate total amount to pay"""
    return MENU[choice]["cost"]


def make_drink(choice):
    """Use resources to make coffee and deposit cash"""
    for resource in MENU[choice]["ingredients"]:
        resources[resource] -= MENU[choice]["ingredients"][resource]
    return MENU[choice]["cost"]


def start_game():
    total_cash = 0

    while True:
        # TODO: 1. Ask - What would you like? (espresso/latte/cappuccino): latte
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Reply the user based on selection.
        if coffee_choice == "off":
            print("Turning Off...")
            return
        elif coffee_choice == "report":
            print(get_report(total_cash))
            continue
        elif not coffee_choice in {"espresso", "latte", "cappuccino"}:
            print("Wrong Input...Try Again!")
            continue

        # TODO: 3. Check if resources are sufficient
        if not is_sufficient(coffee_choice):
            print("Please select another option.")
            continue

        # TODO: 4. Calculate total amount to pay
        total_to_pay = amount_to_pay(coffee_choice)
        print(f"Total to pay: ${total_to_pay}.")

        # TODO: 5. Ask the user to insert coins and Calculate the coins amount
        total_amount = get_coin_amount()
        print(f"Amount Inserted: ${total_amount}")
        if total_amount < total_to_pay:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total_amount > total_to_pay:
            change = total_amount - total_to_pay
            print(f"Here is ${format(change,'.2f')} in change.")

        # TODO: 6. Make drink and reply user
        cash_added = make_drink(coffee_choice)
        total_cash += cash_added
        print(f"Here is your {coffee_choice} & Enjoy!")


start_game()

```

# Solution:

```py
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```

```py
# What would you like? (espresso/latte/cappuccino): report
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# What would you like? (espresso/latte/cappuccino): latte
# Total to pay: $2.5.
# Please insert coins.
# How many quarters?: 10
# How many dimes?: 5
# How many nickles?: 5
# How many pennies?: 5
# Amount Inserted: $3.3
# Here is $0.80 in change.
# Here is your latte & Enjoy!
# What would you like? (espresso/latte/cappuccino): report
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# What would you like? (espresso/latte/cappuccino): eafd
# Wrong Input...Try Again!
```

</details>

<details>
  <summary>19. Object Oriented Programming </summary>

# Example 1:

```py
from turtle import Turtle, Screen

tim = Turtle()
print(tim)
tim.shape("circle")
tim.color("black", "green")
tim.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```

```py
# <turtle.Turtle object at 0x1002ad290>
# 300
```

# Example 2:

```py
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)
```

```py
# +--------------+----------+
# | Pokemon Name |   Type   |
# +--------------+----------+
# |   Pikachu    | Electric |
# |   Squirtle   |  Water   |
# |  Charmander  |   Fire   |
# +--------------+----------+
```

# Example 3:

```py
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)
```

```py
# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electric |
# | Squirtle     | Water    |
# | Charmander   | Fire     |
# +--------------+----------+
```

# Task 1 -

main.py:

```py
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
mm = MoneyMachine()

while True:
    # TODO: 1. GET USER'S CHOICE
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. FIND OUT IF DRINK IS AVAILABLE
    menu = Menu()
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffee_maker.report()
        mm.report()
        continue
    elif not menu.find_drink(user_choice):
        continue
    item = menu.find_drink(user_choice)
    item_cost = item.cost
    # TODO: 3. FIND OUT IF RESOURCES ARE AVAILABLE TO MAKE THE DRINK
    is_sufficient = coffee_maker.is_resource_sufficient(item)
    if not is_sufficient:
        continue
    # TODO: 4. INSERT COINS INTO MACHINE TO MAKE PAYMENT AND CALCULATE
    result = mm.make_payment(item_cost)
    if not result:
        continue
    # TODO: 5. MAKE THE COFFEE
    coffee_maker.make_coffee(item)

```

coffee_maker.py:

```py
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

```

menu.py:

```py
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

```

money_machine.py:

```py
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

```

# Solution -

main.py:

```py
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)

```

```py
# What would you like? (espresso/latte/cappuccino): report
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# What would you like? (espresso/latte/cappuccino): latte
# Please insert coins.
# How many quarters?: 14
# How many dimes?: 5
# How many nickles?: 5
# How many pennies?: 5
# Here is $1.8 in change.
# Here is your latte ☕️. Enjoy!
# What would you like? (espresso/latte/cappuccino): report
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# What would you like? (espresso/latte/cappuccino): latte
# Sorry there is not enough water.
# Sorry there is not enough milk.
# What would you like? (espresso/latte/cappuccino): off
```

</details>

<details>
  <summary>20. The Quiz OOP Project </summary>

# Example 1:

```py
class Car:
    def __init__(self):
        self.color = "blue"
        self.weight = 200
        self.speed = 380

    def move(self, steps, direction):
        return f"Car has moved {steps} steps to the {direction}."

    def honk(self):
        return "HONK! HONK!"


car = Car()
print(car.weight)
print(car.move(30, "right"))
print(car.honk())
```

```py
# 200
# Car has moved 30 steps to the right.
# HONK! HONK!
```

# Example 2:

```py
class User:
    pass

user_1 = User()
user_1.id = "001"
user_1.username = "ifeanyi"
user_1.lastname = "omeata"

user_2 = User()
user_2.id = "002"
user_2.username = "jack"
user_2.lastname = "buddy"

print(user_1.username)
print(user_2.username)
```

```py
# ifeanyi
# jack
```

# Example 3:

```py
class User:
    def __init__(self, user_id, username, lastname):
        self.id = user_id
        self.username = username
        self.lastname = lastname


user_1 = User("001", "ifeanyi", "omeata")
user_2 = User("002", "jack", "buddy")

print(user_1.lastname)
print(user_2.lastname)
```

```py
# omeata
# buddy
```

# Example 4:

```py
class User:
    def __init__(self, user_id, username, lastname):
        self.id = user_id
        self.username = username
        self.lastname = lastname
        self.followers = 0


user_1 = User("001", "ifeanyi", "omeata")
user_2 = User("002", "jack", "buddy")

print(user_1.lastname)
print(user_1.followers)
```

```py
# omeata
# 0
```

# Example 5:

```py
class User:
    def __init__(self, user_id, username, lastname):
        self.id = user_id
        self.username = username
        self.lastname = lastname
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "ifeanyi", "omeata")
user_2 = User("002", "jack", "buddy")

user_1.follow(user_2)
print(user_1.username)
print(user_1.followers)
print(user_1.following)
print(user_2.username)
print(user_2.followers)
print(user_2.following)
```

```py
# ifeanyi
# 0
# 1
# jack
# 1
# 0
```

# Example 6:

```py
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question = Question("What is the largest country in the world?", "Russia")
print(question.text)
print(question.answer)
```

```py
# What is the largest country in the world?
# Russia
```

# Example 7:

```py
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    instance = Question(text=question_text, answer=question_answer)
    question_bank.append(instance)

print(question_bank)
```

```py
# [<question_model.Question object at 0x1047b91d0>, <question_model.Question object at 0x1047b9190>, <question_model.Question object at 0x1047b9290>, <question_model.Question object at 0x1047b9510>, <question_model.Question object at 0x1047b9210>, <question_model.Question object at 0x1047b9810>, <question_model.Question object at 0x1047b9850>, <question_model.Question object at 0x1047b9890>, <question_model.Question object at 0x1047b98d0>, <question_model.Question object at 0x1047b9610>, <question_model.Question object at 0x1047b9910>, <question_model.Question object at 0x1047b9950>]
```

# Task 1 -

main.py:

```py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    instance = Question(text=question_text, answer=question_answer)
    question_bank.append(instance)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your Final Score is: {quiz.score} out of {quiz.question_number}.")

```

quiz_brain.py:

```py
class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = question_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        quiz_length = len(self.questions_list)
        return self.question_number < quiz_length

    def check_answer(self, answer, current_answer):
        if answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Oops! You got it Wrong!")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

```

question_model:

```py
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

```

data.py:

```py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to "
             "take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a "
             "state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

```

```py
# Q.1: A slug's blood is green. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 1/1

# Q.2: The loudest animal is the African Elephant. (True/False)?: False
# You got it right!
# The correct answer was: False
# Your current score is 2/2

# Q.3: Approximately one quarter of human bones are in the feet. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 3/3

# Q.4: The total surface area of a human lungs is the size of a football pitch. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 4/4

# Q.5: In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 5/5

# Q.6: In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral. (True/False)?: Flase
# Oops! You got it Wrong!
# The correct answer was: False
# Your current score is 5/6

# Q.7: It is illegal to pee in the Ocean in Portugal. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 6/7

# Q.8: You can lead a cow down stairs but not up stairs. (True/False)?: False
# You got it right!
# The correct answer was: False
# Your current score is 7/8

# Q.9: Google was originally called 'Backrub'. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 8/9

# Q.10: Buzz Aldrin's mother's maiden name was 'Moon'. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 9/10

# Q.11: No piece of square dry paper can be folded in half more than 7 times. (True/False)?: 'False
# Oops! You got it Wrong!
# The correct answer was: False
# Your current score is 9/11

# Q.12: A few ounces of chocolate can to kill a small dog. (True/False)?: True
# You got it right!
# The correct answer was: True
# Your current score is 10/12

# You have completed the Quiz.
# Your Final Score is: 10 out of 12.

# Process finished with exit code 0

```

</details>

<details>
  <summary>21. Turtle Graphics </summary>

# Example 1 - Draw a Square

```py
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
for _ in range(4):
    tim.forward(200)
    tim.right(90)


screen = Screen()
screen.exitonclick()
```

# Example 2 - Draw a Dashed Line

```py
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
```

# Example 3 - Draw from Square to Decagon

```py
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

for i in range(4, 11):
    angle = 360/i
    tim.color(random.choice(colours))
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
```

# Example 4 - Using RGB Colors

```py
import random
import turtle
turtle.colormode(255)

tim = turtle.Turtle()
tim.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()

```

# Example 5: Draw a Spinograph

```py
import random
import turtle
turtle.colormode(255)

tim = turtle.Turtle()
tim.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tim.pensize(2)
tim.speed("fastest")


def draw_spinograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


draw_spinograph(1)

screen = turtle.Screen()
screen.exitonclick()

```

# Example 6: Draw a Hirst Painting using Colorgram pypi

```py
import random
import turtle
import colorgram
from PIL import Image, ImageDraw


turtle.colormode(255)

myImage = Image.open("image.jpeg");
# myImage.show();
num_of_colors = 10
colors = colorgram.extract(myImage, num_of_colors)

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    color = random.choice(colors)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    return r, g, b


def move_to_next_line(nums):
    tim.up()
    tim.setheading(270)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(30 * nums)
    tim.setheading(0)
    tim.down()


def create_hirst(nums):
    for _ in range(nums):
        for _ in range(nums):
            tim.color(random_color())
            tim.begin_fill()
            tim.circle(10)
            tim.end_fill()
            tim.up()
            tim.forward(30)
            tim.down()
        move_to_next_line(nums)


create_hirst(num_of_colors)

screen = turtle.Screen()
screen.exitonclick()

```

# Solution:

```py
import random
import turtle
import colorgram

turtle.colormode(255)

num_of_colors = 10
colors = colorgram.extract("image.jpeg", num_of_colors)

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    color = random.choice(colors)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    return r, g, b


sides = 10
number_of_dots = sides**2
tim.up()
tim.hideturtle()
tim.setheading(180)
tim.forward(200)
tim.setheading(270)
tim.forward(200)
tim.setheading(0)
for dot_count in range(1, number_of_dots+1):
    tim.down()
    tim.dot(20, random_color())
    tim.up()
    tim.forward(40)
    if dot_count % sides == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(40*sides)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

```

</details>

<details>
  <summary>22. Turtle Event Listeners </summary>

# Directional Events

```py
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")


def move_up():
    tim.setheading(90)
    tim.forward(10)


def move_down():
    tim.setheading(270)
    tim.forward(10)


def move_right():
    tim.setheading(0)
    tim.forward(10)


def move_left():
    tim.setheading(180)
    tim.forward(10)


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)
screen.exitonclick()

```

# Make an Etch-a-Sketch App

```py
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

```

# The Turtle Race

```py
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
winner = ""
end_game = False
turtles = []

start = -100
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.speed("fast")
    tim.penup()
    tim.goto(x=-230, y=-start)
    start += 40
    turtles.append(tim)

while not end_game:
    count = 0
    for turtle in turtles:
        current = turtle.xcor()
        rand_num = random.choice([10,20,30])
        new_pos = current + rand_num
        turtle.setx(230 if new_pos >= 230 else new_pos)
        if not winner and turtle.xcor() >= 230:
            winner = turtle.color()
        if turtle.xcor() >= 230:
            count += 1
    if count == len(colors):
        end_game = True

if winner[0] == user_bet:
    print("Congratulations! You Won!")
else:
    print("Sorry, You lost!")
    print(f"{winner[0].title()} Won!")

screen.listen()
# screen.onkey(key="c", fun=clear)
screen.exitonclick()

```

```py
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

```

```py
# You've won! The green turtle is the winner!
```

</details>

<details>
  <summary>23. Snake Game 1 </summary>

# Procedual Setup

```py
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for cord in starting_pos:
    block = Turtle(shape="square")
    block.penup()
    block.color("white")
    block.goto(cord)
    snake.append(block)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    for num in range(len(snake)-1, 0, -1):
        new_x = snake[num - 1].xcor()
        new_y = snake[num - 1].ycor()
        snake[num].goto(new_x, new_y)
    snake[0].forward(20)


screen.exitonclick()

```

# Object Oriented Programming Setup

main.py:

```py
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

screen.exitonclick()

```

snake.py:

```py
from turtle import Turtle
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for cord in START:
            block = Turtle(shape="square")
            block.penup()
            block.color("white")
            block.goto(cord)
            self.snake.append(block)

    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[num - 1].xcor()
            new_y = self.snake[num - 1].ycor()
            self.snake[num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

```

</details>

<details>
  <summary>24. Snake Game 2 - Class Inheritance </summary>

# Example 1:

```py
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("It's a Fish!")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
```

```py
# moving in water.
# Inhale, exhale.
# It's a Fish!
# 2
```

# Task 1 -

main.py:

```py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()

```

scoreboard.py:

```py
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.width(30)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.show_score()

```

food.py:

```py
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

```

snake.py:

```py
from turtle import Turtle
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START:
            self.add_block(position)

    def add_block(self, position):
        block = Turtle(shape="square") if self.segments else Turtle(shape="turtle")
        block.color("white" if self.segments else "green")
        block.penup()
        block.goto(position)
        self.segments.append(block)

    def extend(self):
        self.add_block(self.segments[-1].position())

    # def create_snake(self):
    #     for cord in START:
    #         block = Turtle(shape="square")
    #         block.penup()
    #         block.color("white")
    #         block.goto(cord)
    #         self.snake.append(block)

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

```

</details>

<details>
  <summary>25. Ping Pong Game </summary>

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


</details>
