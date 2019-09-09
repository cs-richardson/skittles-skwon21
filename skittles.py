"""
skittles.py - San Kwon
This program asks the user to guess a random number between
0 and 1023 (inclusive) until the user is able to guess the
number correctly.
"""

import random
randomnum = random.randint(0, 1023)

print("There are anywhere from 0 to 1023 skittles in this machine.")
guess = int(input("Can your guess how many skittles are in here?: "))

while guess != randomnum:
    if guess < 0 or guess > 1023:
        print("The guess needs to be between 0 to 1023 inclusive!")
    elif guess < randomnum:
        print("There are more skittles than that!")
    elif guess > randomnum:
        print("There are less skittles than that!")
    guess = int(input("Try again!: "))
        
print("Your guess is correct! Your prize are these skittles!")
