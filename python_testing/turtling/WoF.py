import random

'''
spin wheel for base money number

guess a letter
    get base money num * number of that letter in word to guess
    turn ends if guess no letter

if they win the round they get the money they've earned
'''

#spin wheel
WHEEL_OPTIONS = (1000,2000,3000,10000,"bankrupt","lose turn","trip to venice")

wheel_roll = random.choice(WHEEL_OPTIONS)

#make a guess
guess = input("Guess a letter in the phrase\n > ")

