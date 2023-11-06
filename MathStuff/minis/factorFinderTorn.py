import time

from math import sqrt

import threading as thr

from os import system

'''COLORS = {
    'default':
}

def colored(string, color):
    return 
'''

def func():
    divisibleBy = set()

    for i in range(1,num//(skipVal+1)+1,increment):
        if num % i == 0:
            divisibleBy.add(str(i))

    for i in range(1,skipVal):
        if num % i == 0:
            divisibleBy.add(str(num // i))
    return sorted(divisibleBy, key=int)

system('clear')
print('Welcome to Factor Finder!\n')

while True:
    # Get Number
    try:
        num = abs(int(input('\nEnter an integer\n > ')))
    except:
        print('\nPlease enter a valid integer')
        continue

    # Setup to Find Factors
    increment = 1
    if num % 2 != 0:
        increment = 2
    skipVal = int(sqrt(num) // 1) + 1
    
    #Find Factors
    finding = thr.Thread(target=func)
    start_time = time.perf_counter()
    finding.start()
    timeout = False
    while finding.is_alive():
        if time.perf_counter() - start_time > 15:
            print(time.perf_counter(), start_time)
            print("Operation surpassed time limit of 15 seconds\n")
            timeout = True
            break
    if timeout:
        continue
    operationTime = '{:.20f}'.format(time.perf_counter() - start_time)
    print(f'operation took {operationTime} seconds with multithreading')

    start_time = time.perf_counter()
    divisibleBy = func()
    operationTime = '{:.20f}'.format(time.perf_counter() - start_time)
    print(f'operation took {operationTime} seconds without multithreading')


    # Print
    if len(divisibleBy) > 2:
        print(f'\nYour number has {len(divisibleBy)} factors, including: {", ".join(divisibleBy)}')
    elif num == 0 or num == 1:
        print('\nYour number has only one factor')
    else:
        print('\nYour number is prime!')