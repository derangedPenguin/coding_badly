from json import dumps

NUMS = [1,2,3,4,5,6,7,8,9]

NUMS_NON_ORDERED = set(NUMS)

class Board:
    def __init__(self) -> None:
        self.board = [[0 for x in range(9)] for y in range(9)]
        self.notes = [[set() for x in range(9)] for y in range(9)]
    
    def __getitem__(self, item):
        return self.board[item]
    def __setitem__(self, key, value):
        self.board[key] = value
    
    def __str__(self):
        return dumps(self.board, indent=2)
    
    def copy(self):
        copy = Board()
        copy.board = self.board.copy()
        copy.notes = self.notes.copy()
        return copy
    
    def get_row(self, index):
        return self.board[index]
    def get_column(self, index):
        return [row[index] for row in self.board]
    def get_box(self, coord):
        box_coord = self.get_box_coord(coord)
        # print('\n',self.board.__str__())
        # box = [[0,0,0],[0,0,0],[0,0,0]]
        # for x in range(3):
        #     for y in range(3):
        #         try:
        #             box[x][y] = self[x+(box_coord[0]*3)][y+(box_coord[1]*3)]
        #         except IndexError as err:
        #             print(coord, box_coord)
        #             print(self.board[x], y)
        #             print(self.is_full())
        #             raise err
        box = [
            [self[x+(box_coord[0]*3)][y+(box_coord[1]*3)] for x in range(3)] for y in range(3)
        ]
        return box
    def get_box_coord(self, coord):
        return (coord[0])//3, (coord[1])//3

    def is_val_in_row(self, val, row):
        return val in self[row]
    def is_val_in_column(self, val, column):
        return val in self.get_column(column)
    def is_val_in_box(self, val, coord):
        box = self.get_box(coord)
        return val in box[0]+box[1]+box[2]

    def is_val_valid_at_coord(self, val, coord):
        return (not self.is_val_in_row(val, coord[0])
                and not (self.is_val_in_column(val, coord[1]))
                and not (self.is_val_in_box(val, coord))
                )
    def is_val_valid_at_coord_in_place(self, val, coord, debug=False):
        valid = True

        row:list = self.get_row(coord[0]).copy()
        if debug:print(row, end=' - ')
        row.pop(coord[1])
        if debug:print(row)
        if val in row:
            # print('row', end=' - ')
            valid = False

        column = self.get_column(coord[1]).copy()
        column.pop(coord[0])
        if val in row:
            # print('row', end=' - ')
            valid = False

        box = self.get_box(coord).copy()
        box[coord[0]%3].pop(coord[1]%3)
        if val in row:
            # print('row', end='\n')
            valid = False
        
        return valid

        # return (not val in row
        #         and not val in column
        #         and not val in box[0]+box[1]+box[2]
        #         )

    def is_full(self):
        return not any((0 in row for row in self.board))

    def set_tile(self, value, coord):
        self[coord[0]][coord[1]] = value
    
    def get_notes_at(self, x, y):
        return self.notes[x][y]
    def set_notes_at(self, vals:set, x, y):
        self.notes[x][y] = vals

    def set_note(self, val, coord):
        #toggles the val param in the given notes set at that coord
        if val in self.get_notes_at(*coord):
            self.notes[coord[0]][coord[1]].remove(val)
        else:
            self.notes[coord[0]][coord[1]].add(val)
        
