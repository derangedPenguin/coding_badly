import random

from scripts.Board import Board

NUMS = [1,2,3,4,5,6,7,8,9]
NUMS_NON_ORDERED = set(NUMS)

TILES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

class MagicBoard:
    def __init__(self) -> None:
        self.board = Board()
    
    def fill_board(self):
        for row, col in TILES:
            grid = self.board
            numberList = NUMS.copy()

            if grid[row][col] == 0:
                random.shuffle(numberList)      
                for value in numberList:
                    #Check that this value can be at this spot
                    if self.board.is_val_valid_at_coord(value, (row, col)) :
                        grid[row][col]=value

                        if self.board.is_full():
                            return True
                        else:
                            if self.fill_board():
                                return True
                break
        grid[row][col] = 0
    
    def drain_board(self):
        """removes tiles randomly until board cannot be solved"""
        tiles = TILES.copy()
        random.shuffle(tiles)

        board_copy = self.board.copy()

        for x, y in tiles:
            original_tile = board_copy[x][y]
            board_copy[x][y] = 0
            if not self.solve_board(board_copy):
                board_copy[x][y] = original_tile

        return board_copy
    
    def solve_board(self, board: Board) -> list[list[int]] | bool:
        """
        IMPORTANT: Only feed a copy of the Board object, will solve in-place
        attempts to solve input board, returns solved board if possible, else returns False
        """
        initial_board = board.copy()

        solveable = True
        for y, row in enumerate(board):
            for x, value in enumerate(board):
                #If tile is empty
                if value not in NUMS:
                    possibilities = self.gen_possibilities_at((x,y), board)
                    if len(possibilities) > 1:
                        solveable = False
        return solveable
    
    @staticmethod
    def gen_possibilities_at(coord, board):
        val = board[coord[0]][coord[1]]
        if val in NUMS:
            return {val}

        possibilities = set()
        for i in NUMS_NON_ORDERED:
            if board.is_val_valid_at_coord(i, coord):
                possibilities.add(i)
        board.set_notes_at(possibilities, *coord)
        # print(possibilities)
        return possibilities

"""-------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------"""

class MagicBoard2:
    def __init__(self) -> None:
        self.board = Board()
    
    def drain_board(self):
        """removes tiles randomly until board cannot be solved"""
        tiles = TILES.copy()
        random.shuffle(tiles)

        board_copy = self.board.copy()

        for x, y in tiles:
            original_tile = board_copy[x][y]

            board_copy[x][y] = 0
            if not self.solve_board(board_copy):
                ...
                board_copy[x][y] = original_tile

        return board_copy
    
    def solve_board(self, initial_board: Board) -> list[list[int]] | bool:
        board = initial_board.copy()

        solveable = True

        # while not board.is_full():
        for y, row in enumerate(board):
            for x, value in enumerate(board):
                #If tile is empty
                if value not in NUMS:

                    possibilities = self.gen_possibilities_at((x,y), board)

                    if len(possibilities) == 1:
                        # print(possibilities)
                        board[x][y] = possibilities.pop()
                        # print(board[x][y],'\n')
                    else:
                        return False
        # print('hi')
        return True
    
    @staticmethod
    def gen_possibilities_at(coord, board):
        val = board[coord[0]][coord[1]]
        if val in NUMS:
            return {val}

        possibilities = set()
        for i in NUMS_NON_ORDERED:
            if board.is_val_valid_at_coord(i, coord):
                possibilities.add(i)

        # board.set_notes_at(possibilities, *coord)
        return possibilities