'''dance'''
## Input
rows, cols = [int(i) for i in (input().split())]

map = [
    input() for i in range(rows)
]

moves = 1
for j in range(cols):
    if map[0][j] == '_':
        blank = True
        for i in range(1, rows):
            if map[i][j] == '$':
                blank = False
                break

        if blank == True:
            moves += 1

print(moves)
## Logic


## Output

