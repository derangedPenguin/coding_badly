import time
from math import sqrt
import threading as thr

print('Welcome to Factor Finder!\n')

def func():
    global divisibleBy
    for i in range(1 * isNegative,num//(skipVal+1)+1 * isNegative,increment * isNegative):
        if num % i == 0:
            divisibleBy.add(str(i))
    for i in range(1,skipVal):
        if num % i == 0:
            divisibleBy.add(str(num // i))
    divisibleBy = sorted(divisibleBy, key=int)

while True:
    # Get Number
    try:
        num = int(input('\nEnter an integer\n > '))
    except:
        print('\nPlease enter a valid integer')
        continue

    # Setup to Find Factors
    divisibleBy = set()
    increment = 1
    if num % 2 != 0:
        increment = 2
    isNegative = 1
    if num < 0:
        isNegative = -1
    skipVal = int(sqrt(num) // 1) + 1
    
    #Find Factors
    finding = thr.Thread(target=func)
    start_time = time.time()
    finding.start()
    timeout = False
    while finding.is_alive():
        if time.time()-start_time>15:
            print("Operation surpassed time limit of 15 seconds\n")
            timeout = True
            break
    if timeout:
        continue
    operationTime = time.time() - start_time
    print('operation took',operationTime,'seconds')


    # Print
    if len(divisibleBy) > 2:
        print('\nYour number has',len(divisibleBy),'factors, including:',', '.join(divisibleBy))
    elif num == 0 or num == 1:
        print('\nYour number has only one factor')
    else:
        print('\nYour number is prime!')