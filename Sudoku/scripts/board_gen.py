import random

NUMS = [1,2,3,4,5,6,7,8,9]

TILES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

class MagicBoard:
    def __init__(self) -> None:
        self.board = [[0 for x in range(9)] for x in range(9)]

    def __getitem__(self, item):
        return self.board[item]
    def __setitem__(self, key, value):
        self.board[key] = value
    
    def get_column(self, index):
        return [row[index] for row in self.board]
    '''def get_box(self, coord):
        box_coord = (coord[0])//3, (coord[1])//3
        print(f'{coord} --- {box_coord}')
        box = [
            [self[x+(box_coord[0]*3)][y+(box_coord[1]*3)] for x in range(3)] for y in range(3)
        ]
        return box'''
    def get_box(self, coord):
        row, col = coord
        square=[]
        if row<3:
            if col<3:
                square=[self[i][0:3] for i in range(0,3)]
            elif col<6:
                square=[self[i][3:6] for i in range(0,3)]
            else:  
                square=[self[i][6:9] for i in range(0,3)]
        elif row<6:
            if col<3:
                square=[self[i][0:3] for i in range(3,6)]
            elif col<6:
                square=[self[i][3:6] for i in range(3,6)]
            else:  
                square=[self[i][6:9] for i in range(3,6)]
        else:
            if col<3:
                square=[self[i][0:3] for i in range(6,9)]
            elif col<6:
                square=[self[i][3:6] for i in range(6,9)]
            else:  
                square=[self[i][6:9] for i in range(6,9)]

        return square

    def is_val_in_row(self, val, row):
        return val in self[row]
    def is_val_in_column(self, val, column):
        return val in self.get_column(column)
    def is_val_in_box(self, val, coord):
        #return any((val in sublist for sublist in self.get_box(coord)))
        box = self.get_box(coord)
        return val in [box[0]+box[1]+box[2]]

    def is_board_full(self):
        return not any((0 in row for row in self.board))
    
    '''    def fill_board(self):
        for x, y in TILES:
            if self[x][y] != 0:
                continue

            available_nums = NUMS.copy()
            random.shuffle(available_nums)
            for chosen_val in available_nums:

                if (not self.is_val_in_box(chosen_val, (x,y)) 
                    and not self.is_val_in_column(chosen_val, y) 
                    and not self.is_val_in_row(chosen_val, x)):
                    self[x][y] = chosen_val'''
    def fill_board(self):
        for i in range(0,81):
            row=i//9
            col=i%9
            if grid[row][col]==0:
            shuffle(numberList)      
            for value in numberList:
                #Check that this value has not already be used on this row
                if not(value in grid[row]):
                #Check that this value has not already be used on this column
                if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                    #Identify which of the 9 squares we are working on
                    square=[]
                    if row<3:
                        if col<3:
                            square=[grid[i][0:3] for i in range(0,3)]
                        elif col<6:
                            square=[grid[i][3:6] for i in range(0,3)]
                        else:  
                            square=[grid[i][6:9] for i in range(0,3)]
                    elif row<6:
                        if col<3:
                            square=[grid[i][0:3] for i in range(3,6)]
                        elif col<6:
                            square=[grid[i][3:6] for i in range(3,6)]
                        else:  
                            square=[grid[i][6:9] for i in range(3,6)]
                    else:
                        if col<3:
                            square=[grid[i][0:3] for i in range(6,9)]
                        elif col<6:
                            square=[grid[i][3:6] for i in range(6,9)]
                        else:  
                            square=[grid[i][6:9] for i in range(6,9)]
                        #Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                        grid[row][col]=value
                        if is_grid_full(grid):
                            return True
                        else:
                            if fillGrid(grid):
                            return True
            break
        grid[row][col]=0
    
    def setup_board(self):
        """removes tiles randomly until board cannot be solved"""
        tiles = TILES.copy()
        random.shuffle(tiles)

        board_copy = self.board.copy()

        for x, y in tiles:
            original_tile = board_copy[x][y]
            board_copy[x][y] = ""
            if not self.solve_board(board_copy):
                board_copy[x][y] = original_tile

        self.board = board_copy.copy()
    
    def solve_board(self, board) -> list[list[int]] | bool:
        """attempts to solve input board, returns solved board if possible, else returns False"""
        return True