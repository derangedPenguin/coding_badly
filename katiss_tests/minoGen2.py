from time import perf_counter

class mino:
    def __init__(self, size:int, origin_int:int=0, data:list[list[int]]|None=None) -> None:
        self.origin_int = origin_int
        self.size = size

        if data is None:
            self.grid = [
                [0 for _ in range(size)] for __ in range(size)
            ]
        else:
            self.grid = data

        self.believed_valid = True
    
    def __str__(self) -> str:
        output = '----------------------------------------\n'
        for x, row in enumerate(self.grid):
            for val in row:
                output += '[-]' if val else ' - '
            if x == 0:
                output += f'   Origin Num: {self.origin_int}'
            elif x == 1:
                output += f'   Believed Valid: {self.believed_valid}'
            if x != self.size-1:
                output += '\n'
        return output

def mino_from_int(num:int, grid_size:int) -> mino:
    bint_str = bin(num)[2:]                                             #make binary string
    bint_str = '0' * (grid_size*grid_size - len(bint_str)) + bint_str   #make n**2 digits
    bint_array = [int(i) for i in bint_str]                             #make as list[int]
    # print(sum(bint_array))

    #setup empty grid
    grid = [
        [0 for _ in range(grid_size)] for __ in range(grid_size)
    ]

    #move bin data into grid
    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] = bint_array[len(bint_array) - (x*grid_size+y) - 1] #read backwards, idk

    #create mino object
    return mino(grid_size,
                num,
                grid)

ADJACENT_OFFSETS = ((-1,0),(0,-1),(1,0),(0,1))
def get_active_neighbors(tiles:list[list[int]], x_y):
    x,y = x_y

    neighbors = set()

    for off_x, off_y in ADJACENT_OFFSETS:
        # if ( y+off_y not in range( 0, mino.size )) or ( x+off_x not in range( 0, mino.size )):
        #     continue
        if (x+off_x, y+off_y) in tiles:
            neighbors.add((x+off_x,y+off_y))
    
    return neighbors


def is_valid_mino(mino:mino, specify_num_tiles:int=0) -> bool:
    ## Check has correct num of tiles
    if specify_num_tiles:
        if sum([int(i) for i in bin(mino.origin_int)[2:]]) != specify_num_tiles:
            return False
        
    ## Check all tiles are connected
    #establish all tiles
    active_tiles = set()
    for x, row in enumerate(mino.grid):
        for y, val in enumerate(row):
            if val:
                active_tiles.add((x,y))
    
    #setup current tile & queue
    current_tile = active_tiles.pop()

    tiles_to_check = set()
    tiles_to_check = tiles_to_check.union(get_active_neighbors(active_tiles, current_tile))

    #sequentially check the neighbors of each tile based on previous tile
    while not len(active_tiles) == 0 and not len(tiles_to_check) == 0:
        # print(len(active_tiles), len(tiles_to_check) )
        current_tile = tiles_to_check.pop()
        active_tiles.remove(current_tile)
        tiles_to_check = tiles_to_check.union(get_active_neighbors(active_tiles, current_tile))
    
    return len(active_tiles) == 0


valid_minos_found = 0

start = perf_counter()

n = 5

for i in range(2**(n*n)):
    if i % 64 == 0:
        if perf_counter() - start > 300:
            break
    
    test_mino = mino_from_int(i, n)
    test_mino.believed_valid = is_valid_mino(test_mino, n)

    if test_mino.believed_valid:
        valid_minos_found += 1
        print(test_mino)
    
print(valid_minos_found)