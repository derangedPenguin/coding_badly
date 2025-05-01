## Input
curvatures = [int(input(f'Curvature {i}: ')) for i in range(5)]

from sys import exit

##Setup
# for val in curvatures:
#     if val < 0:


##Run

#create subsets
valid_subsets = []
for i in range(len(curvatures)):
    subset = curvatures.copy()
    subset.remove(curvatures[i])
    #ensure one negative is present
    if not any([j < 0 for j in subset]):
        continue

    #check
    if sum(subset)**2 == 2 * sum([k*k for k in subset]):
        valid_subsets.append((subset))

if len(valid_subsets) != 2:
    print('The circles CANNOT form an appolonian gasket')
    exit()

sum_2_circles = 0

curves_copy = curvatures.copy()
for i in range(4):
    curves_copy.remove(valid_subsets[0].pop(0))

sum_2_circles += curves_copy[0]

curves_copy = curvatures.copy()
for i in range(4):
    curves_copy.remove(valid_subsets[1].pop(0))

sum_2_circles += curves_copy[0]

if sum_2_circles == (sum(curvatures) - sum_2_circles)*2:
    print('the circles CAN form an apollonian gasket')
else: print('cannot')

