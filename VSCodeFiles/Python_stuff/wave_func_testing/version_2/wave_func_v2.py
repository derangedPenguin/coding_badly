import random as rand
import time, pygame

def clear_board(object):
    for x in range(object.width):
        object.data[x] = {y:empty for y in range(object.height)}

class board:
    def __init__(self,width,height,tile_size) -> None:
        self.width = width
        self.height= height
        self.tile_size = tile_size
        self.data = {}
        clear_board(self)
        

class tile:
    def __init__(self,color=(255,255,255),incompatible_list=None,favors=None) -> None:
        self.incompatible_list = incompatible_list
        self.favors = favors
        self.color = color

class mountain(tile):
    def __init__(self,  color=(255, 255, 255), incompatible_list=None, favors=None) -> None:
        super().__init__( color, incompatible_list, favors)
class forest(tile):
    def __init__(self,  color=(255, 255, 255), incompatible_list=None, favors=None) -> None:
        super().__init__( color, incompatible_list, favors)
class beach(tile):
    def __init__(self,  color=(255, 255, 255), incompatible_list=None, favors=None) -> None:
        super().__init__( color, incompatible_list, favors)
class ocean(tile):
    def __init__(self,  color=(255, 255, 255), incompatible_list=None, favors=None) -> None:
        super().__init__( color, incompatible_list, favors)
class empty(tile):
    def __init__(self,  color=(255, 255, 255), incompatible_list=None, favors=None) -> None:
        super().__init__( color, incompatible_list, favors)

mountain, forest, beach, ocean = tile((50,50,50)), tile((0,255,0)), tile((255,255,0)), tile((0,0,255))
mountain.incompatible_list, mountain.favors = [beach,ocean], forest
forest.incompatible_list, forest.favors = [ocean], forest
beach.incompatible_list, beach.favors = [mountain], ocean
ocean.incompatible_list, ocean.favors = [mountain,forest], ocean
empty = tile()
tiles = [mountain,forest,beach,ocean,empty]

game_board = board(75,75,8)

generations = 0

def build_prob_list(dict):
    items = list(dict.keys())
    result = []
    for i in dict:
        for j in range(dict[i]):
            result.append(i)
    return result


def get_adj_states(x,y,radius): 
    result = []
    for x in range(-1*radius,radius+1):
        for y in range(-1*radius,radius+1):
            if x==0 and y==0:
                continue
            try:
                result.append(game_board.data[x][y])
            except:
                result.append(empty)
    return result

def run_wave_func(game_board): #encases various wave functions, simplyfies other functions
    new_board = board(game_board.width,game_board.height,game_board.tile_size)
    for x in game_board.data:
        for y in game_board.data[x]:
            #time.sleep(0.01)
            terrain_v1(x,y,new_board)
            game_board.data = new_board.data

def terrain_v1(x,y,new_board):
    global generations
    generations += 1
    #gather data
    self_state = game_board.data[x][y]
    adj_states_data = {}
    for i in range(0,3): #constructs dict of each ring of adj states
        adj_states_data[i] = get_adj_states(x,y,i+1)
    # check if not empty, check if all surrounds are same, else follow rules
''' if not isinstance(self_state,empty):
new_board.data[x][y] == self_state
return'''
    

#+-----------------------------------DRAWING---------------------------------------+

#+--------------------setup----------------------+
# pygame setup
pygame.init()
screen = pygame.display.set_mode(((game_board.tile_size+1)*game_board.width,(game_board.tile_size+1)*game_board.height))
running = True
dt = 0
clock = pygame.time.Clock()
drawing_state = mountain
mouse_pressed = False
# colors
white = (255,255,255)
gray = (125,125,125)
black = (0,0,0)

def update_grid():
    #draw grid
    for x in range(game_board.width):
        for y in range(game_board.height):
            pygame.draw.rect(screen,game_board.data[x][y].color,pygame.rect.Rect(x*(game_board.tile_size+1),y*(game_board.tile_size+1),game_board.tile_size,game_board.tile_size))
    pygame.display.flip()

#+----------------Event Loop-------------------+
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                drawing_state = mountain
            if event.key == pygame.K_2:
                drawing_state = forest
            if event.key == pygame.K_3:
                drawing_state = beach
            if event.key == pygame.K_4:
                drawing_state = ocean
            if event.key == pygame.K_0:
                drawing_state = empty
            if event.key == pygame.K_SPACE:
                run_wave_func(game_board)
                print(generations)
            if event.key == pygame.K_r:
                clear_board(game_board)
    
    update_grid()

    #mouse drawing
    if mouse_pressed:
        pos = pygame.mouse.get_pos()
        pos = [pos[0]//(game_board.tile_size+1),pos[1]//(game_board.tile_size+1)]
        game_board.data[pos[0]][pos[1]] = drawing_state

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()