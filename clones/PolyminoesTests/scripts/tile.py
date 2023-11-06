FRAMERATE = 20

# each shape def must start with uppermost topmost tile, end with bottom right
TETROMINOES = {
    1: ((0,0),(0,1),(0,2),(0,3))
}

class FallingTile:
    def __init__(self, board, game, pos, shape_id) -> None:
        self.pos = list(pos)
        self.board = board
        self.shape_id = shape_id
        self.game = game
        self.timer = 0
        """time in frames that tile has existed"""

        self.own_offsets = TETROMINOES[shape_id]

        #stuff for overall rect collision with more complex shapes
        self.left = self.own_offsets[0][0]
        self.top = self.own_offsets[0][1]
        self.right = self.own_offsets[-1][0]
        self.bottom = self.own_offsets[-1][0]

    def freeze(self):
        for offset in self.own_offsets:
            self.board[self.pos[1] + offset[1]][self.pos[0] + offset[0]] = self.shape_id
    
    def shape_collide(self, pos) -> bool:
        try:
            for offset in self.own_offsets:
                if self.board.tiles[pos[1]+offset[1]][pos[0]+offset[0]] != 0:
                    return True
        except KeyError:
            return True
        return False

    def shift(self, shift: tuple):
        if not self.shape_collide((self.pos[0]+shift[0], self.pos[1]+shift[1])):
            self.pos[0] += shift[0]
            self.pos[1] += shift[1]

    def update(self):

        self.timer += 1

        '''down_collide = False

        down_collide = self.shape_collide((self.pos[0], self.pos[1]+1))
        
        if not down_collide:
            self.pos[1] += (self.timer % FRAMERATE == 0) #adds 1 when time passed is multiple of framerate (60fps)
        else:
            self.freeze()
            return True'''


    def render(self, surf):
        for offset in self.own_offsets:
            pos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
            surf.blit(self.game.assets[self.shape_id], (pos[0] * self.board.tile_size, pos[1] * self.board.tile_size))