from typing import Self

class Mino:
    def __init__(self, size:int, origin_int:int=0, data:list[list[int]]|None=None) -> None:
        self.origin_int = origin_int
        self.size = size

        if data is None:
            self.grid = [
                [0 for _ in range(size)] for __ in range(size)
            ]
        else:
            self.grid = data

        self.compressed = False
    
    def __str__(self) -> str:
        output = '----------------------------------------\n'
        for x, row in enumerate(self.grid):
            for val in row:
                output += '[-]' if val else ' - '
            if x == 0:
                output += f'\tOrigin Num: {self.origin_int}'
            # elif x == 1:
            #     output += f'   Believed Valid: {self.believed_valid}'
            if x != self.size-1:
                output += '\n'
        return output

    def __hash__(self):
        return (self.origin_int, self.compressed).__hash__()
    
    def copy(self) -> Self:
        return Mino(self.size, self.origin_int, self.grid)

    def compress(self):
        '''remove all empty rows & columns to reduce size of mino storage array'''
        ## Whole Rows
        for i in range(len(self.grid)-1, -1, -1):
            if sum(self.grid[i]) == 0:
                # print('deleting')
                # self.grid.remove(row)
                del self.grid[i]
        
        ## Columns
        # end of columns
        highest_y = 0
        for row in self.grid:
            for y in range(len(row)-1, -1, -1):
                if row[y]:
                    highest_y = max(y+1, highest_y)
                    break
        
        if highest_y < len(self.grid[0]):
            for row in self.grid:
                # print('deleting')
                del row[highest_y:]
        #beginning of columns
        lowest_y = len(self.grid[0])
        for row in self.grid:
            for y in range(len(row)):
                if row[y]:
                    lowest_y = min(y, lowest_y)
                    break
        
        if lowest_y > 0:
            for row in self.grid:
                # print('deleting')
                del row[:lowest_y]

        # print(highest_y, lowest_y)

        self.compressed = True
