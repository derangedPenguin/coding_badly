import time
from math import sqrt

print('Welcome to Factor Finder!\n')

while True:
    # Get Number
    try:
        num = int(input('\nEnter an integer\n > '))
    except:
        print('\nPlease enter a valid integer')
        continue

    # Setup to Find Factors
    divisibleBy = []
    increment = 1
    if num % 2 != 0:
        increment = 2
    isNegative = 1
    if num < 0:
        isNegative = -1
    skipVal = int(sqrt(num) // 1) + 1
    
    #Find Factors
    startTime = time.time()
    for i in range(1 * isNegative,num//(skipVal+1)+1 * isNegative,increment * isNegative):
        if num % i == 0:
            divisibleBy.append(str(i))
    for i in range(1,skipVal):
        if num % i == 0:
            divisibleBy.append(str(num // i))
    divisibleBy.sort(key=int)
    operationTime = time.time() - startTime
    print('operation took',operationTime,'seconds')


    # Print
    if len(divisibleBy) > 2:
        print('\nYour number has',len(divisibleBy),'factors, including:',', '.join(divisibleBy))
    elif num == 0 or num == 1:
        print('\nYour number has only one factor')
    else:
        print('\nYour number is prime!')