square = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

nums = input('Enter first 4 sequence: ').split(' ')

square[0] = [int(nums[i]) for i in range(3)]
square[1][0] = int(nums[3])

magic_num = sum(square[0])

#-----------------------------

# column 1
square[2][0] = magic_num - (square[0][0] + square[1][0])

#column 2
square[1][1] = magic_num - square[2][0] - square[0][2]
square[2][1] = magic_num - square[0][1] - square[1][1]

#column 3
square[1][2] = magic_num - square[1][0] - square[1][1]
square[2][2] = magic_num - square[2][0] - square[2][1]

#check if magic
exit = False
for i in range(3):
    if sum(square[i]) != magic_num: exit = True
    if sum([square[j][i] for j in range(3)]) != magic_num: exit = True

if sum([square[i][i] for i in range(3)]) != magic_num: exit = True
if sum([square[0][2], square[1][1], square[2][0]]) != magic_num: exit = True

if not exit:
    print(square)
else:
    print('No magic square exists')