import math

thing = 0.0

items = []

while True:
    thing = round(thing + 0.1, 1)
    if math.isclose(thing, round(thing)):
        items.append(thing)
    if thing >= 100:
        break

print(items)
print(len(items))