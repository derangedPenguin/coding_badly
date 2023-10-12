import timeit

def BizzFuzz(line1):
    vars = [int(i) for i in line1.split(' ')]
    vars = tuple(vars)
    count = 0
    for i in range(vars[0], vars[1]+1):
        if i % vars[2] == 0 and i % vars[3] == 0:
            count += 1
    print(count)

BizzFuzz('11 121 ')