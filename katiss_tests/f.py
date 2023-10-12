rooms, bottles = input().split(' ')

needed = 0

for room in range(int(rooms)):
    needed += int(input())
    
if needed <= int(bottles):
    print('Jebb')
else:
    print('Neibb')