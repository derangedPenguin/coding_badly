from time import perf_counter
from typing import Self

import json
import os

from scripts.TimeTracker import TimeTracker
from scripts.Mino import Mino

class MinoGenerator:

    time_tracker = TimeTracker()

    ADJACENT_OFFSETS = ((-1,0),(0,-1),(1,0),(0,1))

    MAX_RUNTIME_SECONDS = 30

    def __init__(self):
        ...

    ## Mino Generation
    @time_tracker.track_time
    def mino_grid_from_int(self, num:int, grid_size:int) -> Mino:
        '''
        takes :input num: and interprets bin(num) onto a square grid of size :input grid_size:
        '''
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
                grid[x][y] = bint_array[len(bint_array) - (x*grid_size+y) - 1] #read backwards & loop by grid size for x coord

        #create mino object
        return Mino(grid_size,
                    num,
                    grid)

    ## Evaluate Validity of Mino
    @time_tracker.track_time
    def get_active_neighbors(self, tiles:list[list[int]], x_y):
        x,y = x_y

        neighbors = set()

        for off_x, off_y in self.ADJACENT_OFFSETS:
            # if ( y+off_y not in range( 0, mino.size )) or ( x+off_x not in range( 0, mino.size )):
            #     continue
            if (x+off_x, y+off_y) in tiles:
                neighbors.add((x+off_x,y+off_y))
        
        return neighbors

    @time_tracker.track_time
    def is_valid_mino(self, mino:Mino, specify_num_tiles:int=0) -> bool:
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
        tiles_to_check = tiles_to_check.union(self.get_active_neighbors(active_tiles, current_tile))

        #sequentially check the neighbors of each tile based on previous tile
        while not len(active_tiles) == 0 and not len(tiles_to_check) == 0:
            # print(len(active_tiles), len(tiles_to_check) )
            current_tile = tiles_to_check.pop()
            active_tiles.remove(current_tile)
            tiles_to_check = tiles_to_check.union(self.get_active_neighbors(active_tiles, current_tile))
        
        return len(active_tiles) == 0

    def rotate_grid(self, grid:list) -> list:
        return list(list(i) for i in zip(*reversed(grid)))

    ## Compare for Duplicate Minos
    @time_tracker.track_time
    def minos_are_congruent(self, m1:Mino, m2:Mino) -> bool:
        #check they are same dimenstions
        if len(m1.grid[0]) + len(m1.grid) != len(m2.grid[0]) + len(m2.grid):
            return False
        
        #check if they are the same for any rotation
        m1_rotated = m1.grid
        for i in range(3):
            if m1_rotated == m2.grid:
                return True
            m1_rotated = self.rotate_grid(m1_rotated)
            # print(m1_rotated, '\n', m2.grid)
            
        return False
    
    def run_all_n_minos(self, n:int=4) -> list[Mino]:
        valid_minos_found = set()

        start = perf_counter()

        max_num = 2**(n*n)
        for i in range(2**(n*n)):
            if i % 100000 == 0:
                if perf_counter() - start > self.MAX_RUNTIME_SECONDS:
                    print(f'Reached max program runtime of {self.MAX_RUNTIME_SECONDS} seconds')
                    break
                print(f'generating minos... {i/max_num:.2%} complete')
            
            test_mino = self.mino_grid_from_int(i, n)
            test_mino.believed_valid = self.is_valid_mino(test_mino, n)

            if test_mino.believed_valid:
                test_mino.compress()
                valid_minos_found.add(test_mino)
        else:
            print(f'Completed in {perf_counter() - start} seconds')
        
        valid_minos_found = list(valid_minos_found)

        for base_mino in valid_minos_found:
            all_minos_copy = valid_minos_found.copy()
            all_minos_copy.remove(base_mino)
            for m2 in all_minos_copy:
                if self.minos_are_congruent(base_mino, m2):
                    valid_minos_found.remove(m2)
        
        valid_minos_found.sort(key=lambda a: a.origin_int)
        for mino in valid_minos_found:
            print(mino)
        
        print(f'minos found: {len(valid_minos_found)}')

        return valid_minos_found

    def run_particular_minos(self, ns:set[int], size:int):
        valid_minos_found = set()

        start = perf_counter()

        for i in ns:
            if i % 64 == 0:
                if perf_counter() - start > self.MAX_RUNTIME_SECONDS:
                    break
            
            test_mino = self.mino_grid_from_int(i, size)
            test_mino.believed_valid = self.is_valid_mino(test_mino, size)

            if test_mino.believed_valid:
                test_mino.compress()
                valid_minos_found.add(test_mino)
        
        valid_minos_found = list(valid_minos_found)

        for base_mino in valid_minos_found:
            minos_copy = valid_minos_found.copy()
            minos_copy.remove(base_mino)
            for m2 in minos_copy:
                copied = base_mino.copy()
                # copied.grid = rotate_grid(copied.grid)
                # print(base_mino.grid, copied.grid, '\n\n')
                if self.minos_are_congruent(base_mino, m2):
                    
                    valid_minos_found.remove(m2)
            
        # print('\n'.join(str(m) for m in sorted(valid_minos_found, key=lambda a: a.origin_int)))
        # print(f'nnumber of valid minos: {len(valid_minos_found)}/{2**(n*n)} possibilities')

    @time_tracker.track_time
    def gen_valid_mino_from_lowest_greater_int(self, n:int, start_int:int) -> Mino:
        '''takes an integer, uses mino_grid_from_int style function to create a mino from the lowest integer > n'''
        valid_mino_found = None
        origin_int = start_int
        while not valid_mino_found:
            ##-----------------Create Mino Grid-------------------
            bint_str = bin(origin_int)[2:]                      #make binary string
            bint_str = '0' * (n*n - len(bint_str)) + bint_str   #make n**2 digits
            bint_array = [int(i) for i in bint_str]             #make as list[int]
            if sum(bint_array) != n:
                origin_int += 1
                continue

            #setup empty grid
            grid = [
                [0 for _ in range(n)] for __ in range(n)
            ]

            #move bin data into grid
            for x in range(n):
                for y in range(n):
                    grid[x][y] = bint_array[len(bint_array) - (x*n+y) - 1] #read backwards & loop by grid size for x coord

            current_mino = Mino(n,
                                origin_int,
                                grid)
            
            if self.is_valid_mino(current_mino):
                valid_mino_found = current_mino


        #create mino object
        return valid_mino_found
    
    def find_all_minos(self, n:int) -> list[Mino]:
        start_time = perf_counter()
        n = 4
        i = 1
        minos_created = set()
        max_num = 2**(n*n)
        while i < max_num:
            print('hi')
            if i % 100000 == 0:
                if perf_counter() - start_time > self.MAX_RUNTIME_SECONDS:
                    print(f'Reached max program runtime of {self.MAX_RUNTIME_SECONDS} seconds')
                    break
                print(f'generating minos... {i/max_num:.2%} complete')


            this_mino = mino_gen.gen_valid_mino_from_lowest_greater_int(n, i)
            i = this_mino.origin_int + 1
            minos_created.add(Mino)


        else:
            print(f'Completed in {perf_counter() - start_time} seconds')

        minos_created = list(minos_created)

        for m1 in minos_created:
            all_minos_copy = minos_created.copy()
            all_minos_copy.remove(m1)
            for m2 in all_minos_copy:
                if self.minos_are_congruent(m1, m2):
                    minos_created.remove(m2)
        
        minos_created.sort(key=lambda a: a.origin_int)

        return minos_created

## Log Data
def log(minos):
    with open(f'logs/log{len(os.listdir('logs'))}.log','w') as file:
        for mino in minos:
            file.write(str(mino) + '\n')


if __name__ == "__main__":
    # helpful test cases tetra: 25120, 1632
    # valid Tetras: 1124, 1728, 3264, 4400, 25120, 34952, 50688

    mino_gen = MinoGenerator()

    # minos_created = mino_gen.run_all_n_minos(4)
    minos_created = mino_gen.find_all_minos(4)

    print(json.dumps(mino_gen.time_tracker.get_avgs(), indent=2))

    log(minos_created)


'''
Optimizations to Add:
- grid need only be size n-1, manually add the n*1 mino
- binary operation to only create integers with proper # of 1 digits


'''