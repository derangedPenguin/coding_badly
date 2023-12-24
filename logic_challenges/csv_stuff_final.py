import csv

import os

with open('pokemon.csv', encoding='utf8', errors='ignore', newline='') as file:
    data = list(csv.reader(file))

    table_data = {}

    for i, category in enumerate(data[0]):
        table_data[category] = [data[x][i] for x in range(1, len(data))]

OPTIONS = ['find an average (further choice)', 'what pokemon has the longest name?', 'what pokemon has the lowest catch rate?', 'what is the most common ability?']

AVG_OPTIONS = {'weight':'weight_kg', 'speed':'speed', 'special defense':'sp_defense', 'special attack':'sp_attack', 'hit points':'hp', 'height':'height_m', 'defense':'defense', 'catch rate':'capture_rate', 'base stat total':'base_total'}

def weird_to_float(item):
    """for handling inconsistnecies in how numbers are recorded in the file"""
    if item == '':
        return 0
    return float(item)

def weird_to_list(item: str):
    """for converting written lists in strings to python lists"""
    item = item.strip('"[]')
    as_list = [i.strip("'") for i in item.split(', ')]
    return as_list


def display_options():
    """print the primary menu and handle chosen options"""
    os.system('clear')
    print('Options:')
    for i, option in enumerate(OPTIONS):
        print(f'  {i+1}. {option}')

    choice = int(input('\nEnter the number of your choice\n > '))
    response = handle_choice(choice)
    print('\n',response)

def handle_choice(choice):
    """handles each specific option to calculate, returns the full formatted strign to be printed to the user"""
    match choice:
        case 1:
            """
            calculates the average for a chosen stat across all pokemon by first displaying options of averagable stats 
            then dividing the sum of chosen list by it's length
            """
            while True:
                for i, option in enumerate(AVG_OPTIONS):
                    print(f'  {i+1}. {option}')
                try:
                    choice2 = int(input('\nWhat option would you like to find the average of?\n > ')) - 1
                    choice2 = AVG_OPTIONS[list(AVG_OPTIONS.keys())[choice2]]
                except:
                    print('Please enter a valid option')
                    continue
                result = sum([weird_to_float(i) for i in table_data[choice2]])/len(table_data[choice2])
                return f'the average {choice2} is {result}'
                    
        case 2:
            """
            finds the longest name by finding the max of the name list with len as the key
            """
            name = max(table_data['name'], key=len)
            return f'the longest name is {name} with {len(name)} characters'
        case 3:
            """
            finds the lowest catch rate by finding the min of the catch rate list with a key of int
            """
            rate = min(table_data['capture_rate'], key=int)
            return f'the pokemon with the lowest catch rate is {table_data['name'][table_data['capture_rate'].index(rate)]} with a catch rate of {rate}'
        case 4:
            """
            finds the most common ability by creating a dict containing each ability and its number of occurences, then finds the ability with the largest value
            """
            abilities = {}
            for mon_abilities in [weird_to_list(item) for item in table_data['abilities']]:
                for ability in mon_abilities:
                    if ability in abilities:
                        abilities[ability] += 1
                    else:
                        abilities[ability] = 1
            
            biggest = ('name', 0)
            for ability, num in abilities.items():
                if num > biggest[1]:
                    biggest = (ability, num)
            return f'the most common ability is {biggest[0]} with {biggest[1]} occurences'
        case _:
            return 'Please choose a valid option'

while True:
    """main loop to allow multiple actions to be chosen in one run"""
    display_options()
    if input("\nContinue? ('y'/'n')\n > ") == 'n':
        break