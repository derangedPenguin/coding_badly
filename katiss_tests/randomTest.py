import random as rand
from math import sqrt

cases = 100000000

sum_avg = sum([rand.random()+rand.random() for i in range(cases)]) / cases

root_avg = sum([sqrt(rand.random()) for i in range(cases)]) / cases

print(sum_avg, root_avg)