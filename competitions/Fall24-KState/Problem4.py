## Inputs
num = int(input('first: '))
sequence = input('sequence: ')

## Setup
sum = 0

## Run
for i, char in enumerate(sequence):
    if char == sequence[(i+1)%num]:
        sum += int(char)

## Output
print(sum)
