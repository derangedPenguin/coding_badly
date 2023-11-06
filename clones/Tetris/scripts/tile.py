import random

FRAMERATE = 20

# each shape def must start with uppermost topmost tile, end with bottom right
TETROMINOES = {'I':((0,0),(1,0),(2,0),(3,0)),
               'O':((0,0),(1,0),(0,1),(1,1)),'T':((-1,0),(0,0),(1,0),(0,1)),
               'L':((0,0),(0,1),(0,2),(1,2)),'J':((1,0),(1,1),(1,2),(0,2)),
               'S':((0,0),(1,0),(0,1),(-1,1)),'Z':((0,0),(1,0),(1,1),(1,2))}



class FallingTile:
    def __init__(self, board, game, pos, shape_id, speed=1) -> None:
        self.pos = list(pos)
        self.board = board
        self.shape_id = shape_id #random.choice(tuple(TETROMINOES.keys()))
        self.game = game
        self.timers_active = {'main':True, 'left':False, 'right':False}
        self.timers = {'main':0, 'left':0, 'right':0}
        """time in frames since each timer started"""
        self.speed = speed
        self.speed_mod = 0

        self.own_offsets = TETROMINOES[self.shape_id]

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

    def shift(self, shift):
        if not self.shape_collide((self.pos[0]+shift, self.pos[1])):
            self.pos[0] += shift
    
    def timed_shift(self, shift):
        shift_dir = 'left' if shift == -1 else 'right'
        if self.timers[shift_dir] % (FRAMERATE / 4) == 0: #if current time aligns with allowed motion
            self.shift(shift)
    
    def start_timer(self, timer_name):
        self.timers_active[timer_name] = True
    
    def reset_timer(self, timer_name):
        self.timers_active[timer_name] = True
        self.timers[timer_name] = 0

    def update(self):
        for timer in self.timers:
            if self.timers_active[timer]:
                self.timers[timer] += 1

        down_collide = False

        down_collide = self.shape_collide((self.pos[0], self.pos[1]+1))
        
        if not down_collide:
            self.pos[1] += (self.timers['main'] % (FRAMERATE // (self.speed + self.speed_mod)) == 0) #adds 1 when time passed is multiple of framerate / tile speed mult
        else:
            self.freeze()
            return True

    def render(self, surf):
        for offset in self.own_offsets:
            pos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
            surf.blit(self.game.assets[self.shape_id], (pos[0] * self.board.tile_size, pos[1] * self.board.tile_size))