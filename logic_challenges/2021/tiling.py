# rules: - Within any row or column there must be the same number of red bricks and tan bricks
#        - No row or column can have three consecutive bricks of the same color

def analyze(rolumn: list):
    failed = False
    if not rolumn.count('T') == rolumn.count('R'):
        failed = True
        #print('unequal count')
    if 'TTT' in str(rolumn) or 'RRR' in str(rolumn):
        failed = True
        #print('mroe than 3 consec')
    return failed

side_length = int(input('Enter number of rows and columns: '))

tiles = [] #[input()[i:i+4]  for i in range(side_length)]

for i in range(side_length):
    tiles.append(list(input()))
#print(tiles)

grid_succeeds = True

for row in tiles:
    if analyze(row): # if it failed
        grid_succeeds = False
        #print(f'failed on row {tiles.index(row)}')
        break

for i, row in enumerate(tiles):
    column = []
    for column_num in range(side_length):
        column.append(row[column_num])
    if analyze(column): # if it failed
        grid_succeeds = False
        #print(f'failed on column {column_num}')
        break

print(grid_succeeds)
    
