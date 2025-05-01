'''tour de france'''
## Input
num_front_sprockets, num_rear_sprockets = [int(i) for i in (input().split())]

f_gears = [int(i) for i in (input().split())]
r_gears = [int(i) for i in (input().split())]

_ = input()

drive_ratios = []

## Logic
for i in f_gears:
    for j in r_gears:
        drive_ratios.append(j/i)

drive_ratios.sort(reverse=True)
max = 0
for r in range(len(drive_ratios)):
    if r == len(drive_ratios)-1:
        break
    if max < (drive_ratios[r] / drive_ratios[r+1]):
        max = drive_ratios[r] / drive_ratios[r+1]


## Output
print(round(max, 2))
