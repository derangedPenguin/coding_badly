import time

def find_em(num):
    #use set for faster write speed(?)
    vals = set()

    #skip over odd number if even
    skip_val = (num % 2 == 0)

    #stop at half and add self
    for i in range(1, num//2+1, 1+skip_val):
        if num % i == 0:
            vals.add(i)
    vals.add(num)
    
    return vals
def find_em_timed(num):
    start_time = time.perf_counter()
    #use set for faster write speed(?)
    vals = set()

    #skip over odd number if even
    skip_val = (num % 2 == 0)

    #stop at half and add self
    for i in range(1, num//2+1, 1+skip_val):
        if i % 100_000:
            if time.perf_counter() - start_time > 15:
                return 'Timeout'
        if num % i == 0:
            vals.add(i)
    vals.add(num)
    
    return vals

def formatted(num):
    start_time = time.perf_counter()
    if num > 1_000_000_000_000:
        factors = find_em_timed(num)
        took = '{:.20f}'.format(time.perf_counter() - start_time)
    else:
        factors = find_em(num)
        took = '{:.20f}'.format(time.perf_counter() - start_time)
    return factors, took

while True:
    # Get Number
    try:
        num = int(input('\nEnter an integer\n > '))
    except:
        print('\nPlease enter a valid integer')
        continue

    #find factors
    factors, operation_time = formatted(num=num)

    #format factors
    factors = [str(item) for item in sorted(factors)]

    #output
    print(f'Operation took {operation_time} seconds')
    print(f'\n the factors are {", ".join(factors)}')