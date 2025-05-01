'''TAI'''
## Input
num_samples = int(input())
points = []
for i in range(num_samples):
    points.append([float(i) for i in (input().split())]) # time, value

## Logic
area = 0
for i, point in enumerate(points):
    if i+1 == len(points): break

    point2 = points[i+1]

    area += 1/2 * (point2[0] - point[0]) * (point[1] + point2[1])

## Output
print(area / 1000)
