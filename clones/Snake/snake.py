import pygame

class Snake:
    def __init__(self, game, start_len: int, start_pos: tuple, speed) -> None:
        self.game = game
        self.pieces = {i:{'pos':(start_pos[0]-i, start_pos[1])} for i in range(start_len)} # key is dist from head, 0 is head
        self.dir = (1,0) # x, y vector
        self.len = start_len # board units
        self.speed = 60 / speed # board units per frame

        self.timer = 0 # frames object has existed
        self.dist_along_tile = 0 # pixels head has moved across current tile
    
    def move(self, dir: list[int, int] | None = None) -> bool:
        """
        Moves the entire snake once in the snake's stored direction or the input direction if given.

        Returns True if the move results in collision with a wall or the snake itself.
        Does not move if collision is detected.
        """
        if dir is not None: # change snake dir if function recieves dir input
            self.dir = dir.copy()

        """CHECK COLLISION"""
        collided_self = False
        collided_board = False
        new_loc = self.pieces[0]['pos'][0] + self.dir[0], self.pieces[0]['pos'][1] + self.dir[1]
        if new_loc in [item['pos'] for item in self.pieces.values()]:
            collided_self = True
        if (new_loc[0] < 0 or new_loc[0] > self.game.board.width-1) or (new_loc[1] < 0 or new_loc[1] > self.game.board.height-1):
            collided_board = True

        if collided_self or collided_board:
            return True

        """MOVE"""
        #add new piece under caboose if snake length has increased
        if len(self.pieces) < self.len:
            self.pieces[len(self.pieces)] = self.pieces[len(self.pieces)-1].copy()

        #shuffle pieces forward from back to front
        for i in range(len(self.pieces)-1, 0, -1): 
            self.pieces[i]['pos'] = self.pieces[i-1]['pos']
        
        #move head in current direction
        self.pieces[0]['pos'] = self.pieces[0]['pos'][0] + self.dir[0], self.pieces[0]['pos'][1] + self.dir[1]

        return False

    def update(self):
        self.timer += 1

        can_move = True
        if self.timer % self.speed == 0:
            can_move = not self.move()

        if can_move:
            self.dist_along_tile = (self.dist_along_tile + (self.game.board.tile_width / self.speed)) % self.game.board.tile_width
    
    def get_piece_pos(self, piece_id: int, tile_width):
        piece = self.pieces[piece_id]
        if 0 == 0:
            #head
            tile_dist = self.dist_along_tile-1
            pos = (piece['pos'][0] * tile_width) + (tile_dist * self.dir[0]) + (tile_width / 2 * (not self.dir[0])), (piece['pos'][1] * tile_width) + (tile_dist * self.dir[1]) + (tile_width / 2 * (not self.dir[1]))
        elif piece_id == len(self.pieces):
            #tail
            pos = (piece['pos'][0] * tile_width) - (self.dist_along_tile * self.dir[0]), (piece['pos'][1] * tile_width) - (self.dist_along_tile * self.dir[1])
        else:
            #body
            pos = (piece['pos'][0] * tile_width) + (tile_width / 2), (piece['pos'][1] * tile_width) + (tile_width/2)
        return pos

    def render(self, surf, board):
        for dist, piece in reversed(self.pieces.items()):
            '''            screen_pos = ((piece['pos'][0] * board.tile_width) + board.tile_width/2), (piece['pos'][1] * board.tile_width) + board.tile_width/2
            if dist == 0:
                screen_pos = screen_pos[0] + (self.dist_along_tile * self.dir[0]), screen_pos[1] + (self.dist_along_tile * self.dir[1])
            '''

            screen_pos = self.get_piece_pos(dist, board.tile_width)

            size = (board.tile_width * max(((-1/(3*self.len) * dist) + 1)/2, 1/3))*5/3
            color = (0,0,max(255-((255/self.len)*dist), 0))

            #pygame.draw.circle(surf, color, screen_pos, size) # circle version
            #line version:
            pygame.draw.circle(surf, color, screen_pos, size/2)
            if dist == 0:
                continue
            next_pos = self.get_piece_pos(dist-1, board.tile_width)#(self.pieces[dist-1]['pos'][0] * board.tile_width) + board.tile_width/2, (self.pieces[dist-1]['pos'][1] * board.tile_width) + board.tile_width/2
            pygame.draw.line(surf, color, screen_pos, next_pos, int(size))
            
