import os

def grab_backwards(i:int, collection):
    try:
        return collection[len(collection)-i]
    except IndexError:
        # print('hi')
        return '0'
        

class mino:

    ADJECENT_OFFSETS = [
        (-1,0), (0,-1), (1,0), (0,1)
    ]

    def __init__(self, size:int):
        self.size = size
        self.blocks = [
            [0 for i in range(size)] for i in range(size)
        ]
    
    def print(self):
        for row in self.blocks:
            for block in row:
                # print(block, end='')
                print('[-]' if block else ' - ', end='')
            print()
    
    def next_mino(self, start_val:int, block_count:int|None=None) -> int:
        approved_mino = False
        while not approved_mino:
            ##Generate representative bint
            # if n % 2 == 0:
            #     n += 1
            #     continue

            bint = bin(start_val)[2:]
            bint_array = [int(i) for i in bint]

            if block_count is not None and sum(bint_array) != block_count:
                start_val += 1
                continue

            mino_grid = [
                [0 for i in range(self.size)] for i in range(self.size)
            ]

            if self.test_for_mino(mino_grid):
                approved_mino = True
        self.blocks = mino_grid
        return start_val
    
    def set_blocks_from_int(self, n:int):
        bint = bin(n)[2:]
        bint = '0'*((self.size*self.size) - len(bint)) + bint
        bint = [int(bint[i]) for i in range(len(bint))]
        # print(n, bint, len(bint))
        for x in range(self.size):
            for y in range(self.size):
                self.blocks[x][y] = bint[len(bint)-((x*4)+(y*1))-1]
        # l = len(bint)
        # self.blocks = [
        #    [ grab_backwards(i+j, bint) for i in range(self.size)] for j in range(self.size)
        # ]

    def get_adjacent_tiles(self, x_y, mino_grid:list[list[bool]]|None=None):
        if mino_grid is None: mino_grid = self.blocks

        adj_tiles = []
        for off_x, off_y in self.ADJECENT_OFFSETS:
            try:
                adj_tiles.append(mino_grid[off_x+x_y[0]][off_y+x_y[1]])
            except:
                adj_tiles.append(0)
        return adj_tiles
    
    def test_for_mino(self, mino_grid:list[list[bool]]|None=None):
        if mino_grid is None: mino_grid = self.blocks

        for x in range(len(mino_grid)):
            for y in range(len(mino_grid[0])):
                if not sum(self.get_adjacent_tiles((x,y))) > 0:
                    return False
        return True

    def progression(self):
        n = 4
        m = n
        og_value = 15 # in binary is 1111
        value = og_value
        not_finished = True
        while not_finished:
            value = value + 2**n - 2**(n-1)
            print(value)
            n-=1
            if n == 1:
                n = m+1
                m = n
            if n > 10:
                not_finished = False
        
    def progression2(self):
        # stuff = []
        for n in range(16):
            base = 2**n
            for i in range(n-1):
                print(bin(base-(2**i)+(2**i+1)))

test = mino(4)
for i in range(2**8):
    test.set_blocks_from_int(i)
    if test.test_for_mino():
        test.print()


# test = mino(4)
# test.print()
# i = 0
# while i < 2**16:
#     i = test.next_mino(i, 4)
#     print(i)
#     test.print()
    