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

        self.own_offsets = TETROMINOES[shape_id]

        self.left = self.own_offsets[0][0]
        self.top = self.own_offsets[0][1]
        self.right = self.own_offsets[-1][0]
        self.bottom = self.own_offsets[-1][0]

    def freeze(self):
        for offset in self.own_offsets:
            self.board[self.pos[1] + offset[1]][self.pos[0] + offset[0]] = self.shape_id

    def update(self):
        self.timer += 1

        down_collide = False

        for offset in self.own_offsets:
            if (self.board.tiles[self.pos[1] + offset[1]][self.pos[0] + offset[0]] != 0) or (self.pos[1] + offset[1] >= 20):
                down_collide = True
                break
        
        if not down_collide:
            self.pos[1] += (self.timer % FRAMERATE == 0)
        else:
            self.freeze()
            return True


    def render(self, surf):
        for offset in self.own_offsets:
            pos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
            surf.blit(self.game.assets[self.shape_id], (pos[0] * self.board.tile_size, pos[1] * self.board.tile_size))