#Takes a dictionary 'board' containg rows as dicts with each item containing an int to represent pixel state, and displays it
import pygame
#+----------------setup--------------+
import random as rand

class board:
    def __init__(self,width,height,mode='numeric') -> None:
        self.width = width
        self.height = height
        self.mode = mode
        self.data = {}
        for x in range(width): # can potentially be simplified
            self.data[x] = {y:0 for y in range(height)}
    def clear(self):
        for x in range(game_board.width): # can potentially be simplified
            game_board.data[x] = {y:0 for y in range(game_board.height)}

class tile:
    def __init__(self,type='dead') -> None:
        self.type = type
        self.possible = True
        self.prob = 1
        
        
#construct dict for coordinate plane, based on input dimensions
WIDTH = 160 #int(input('Width: '))
HEIGHT = 160 #int(input('Height: '))
cell_size = 3
game_board = board(width=WIDTH,height=HEIGHT)

for x in range(game_board.width): # can potentially be simplified
    game_board.data[x] = {y:0 for y in range(game_board.height)}

'''
steps:
- define ruleset - begins at basic, gets very more complicated very quick
- get applicable blocks
- choose from choices
'''

def get_adj_states(x,y,dist=1):
    result = []
    for i in range(-1*dist,dist+1):
        for j in range(-1*dist,dist+1):
            if i == 0 and j == 0:
                continue
            try:
                result.append(game_board.data[x+i][y+j])
            except:
                result.append(0)
    return result

def update_conway():
    new_board = {x:{} for x in range(game_board.height)}
    for row in game_board.data:
        for column in game_board.data[row]: # analysis section, conway's rules
            adj_states = get_adj_states(row,column)
            state = game_board.data[row][column]
            if sum(adj_states) == 3:
                result = 1
            elif sum(adj_states) == 2 and state == 1:
                result = 1
            else:
                result = 0
            new_board[row][column] = result
    for x in range(game_board.width): # can potentially be simplified
        game_board.data[x] = {y:new_board[x][y] for y in range(game_board.height)}

'''game of life but 3 states?:
just a 0.5 tile?
'''

def update_3_state():
    new_board = {x:{} for x in range(game_board.height)}
    for row in game_board.data:
        for column in game_board.data[row]: # analysis section, conway's rules
            adj_states = sum(get_adj_states(row,column))
            state = game_board.data[row][column]
            if state == 1:
                if adj_states < 2:
                    result = 0.5
                elif adj_states > 3:
                    result = 0
                else:
                    result = 1
            elif state == 0:
                if adj_states == 3 or adj_states == 2.5:
                    result = 1
                else:
                    result = 0
            elif state == 0.5:
                if adj_states == 2 or adj_states == 2.5:
                    result = 1
                elif state == 3:
                    result = 0.5
                else:
                    result = 0
            new_board[row][column] = result
    for x in range(game_board.width): # can potentially be simplified
        game_board.data[x] = {y:new_board[x][y] for y in range(game_board.height)}

def update_var_states(states_num=2): # archived, optical illusions with arg of 3
    new_board = {x:{} for x in range(game_board.height)}
    for row in game_board.data:
        for column in game_board.data[row]: # analysis section, conway's rules
            adj_states = sum(get_adj_states(row,column))
            state = game_board.data[row][column]
            for num in range(states_num):
                if adj_states < num*3+1 and adj_states > num*2:
                    result = min(1,num*2)
                elif adj_states == num*2:
                    result = state
                elif state == 0:
                    result = (states_num - 2) / (states_num - 1)
                else:
                    result = 0
            new_board[row][column] = result
    for x in range(game_board.width): # can potentially be simplified
        game_board.data[x] = {y:new_board[x][y] for y in range(game_board.height)}

'''
    thinking notes:
    - 4 options, mountain, forest, beach, ocean
    - starting at only adjacent cell tests
    - mountain can only be next to forest
    - forest can be next to mountain or beach
    - beach can be next to forest or ocean
    - ocean can only be next to beach
    - all can be next to selves
'''    

def world_gen_v101():
    board_full = False
    while not board_full:
        #test for any empty slots in board, break for loop and continue if loop finishes naturally
        full_test = True
        for x in game_board.data:
            for y in game_board.data[x]:
                if game_board.data[x][y] == 0:
                    full_test = False
        board_full = full_test
        #actual func:
        game_board.mode = 'biomes'
        new_board = {x:{} for x in range(game_board.height)}
        for row in game_board.data:
            for column in game_board.data[x]:
                adj_states = get_adj_states(row,column)
                options = [1,2,3,4]
                state = game_board.data[row][column]
                if state != 0 or sum(adj_states) == 0:
                    new_board[row][column] = state
                    continue
                if 1 in adj_states:
                    options.remove(3)
                    options.remove(4)
                    options.append(2)
                elif 2 in adj_states:
                    options.remove(4)
                if 4 in adj_states:
                    options.remove(1)
                    options.remove(2)
                    options.append(4)
                elif 3 in adj_states:
                    options.remove(1) 
                if options == []: options.append(5)
                new_board[row][column] = rand.choice(options)
        game_board.data = new_board

#+---------------------------------running---------------------------------+
#pygame setup
pygame.init()
screen = pygame.display.set_mode((game_board.width*(cell_size+1),game_board.height*(cell_size+1)))
running = True
mouse_clicked = False
analysis_running = False
analysis_paused = False
dt = 0
clock = pygame.time.Clock()
hold_time = 0
gens = 0
rate = 0.1
# colors
white = (255,255,255)
gray = (125,125,125)
black = (0,0,0)
purple = (50,0,125)

def get_state_color(x,y):
    state = game_board.data[x][y]
    if game_board.mode == 'numeric':
        return (255-255*state,255-255*state,255-255*state)
    else:
        if state == 1:
            return (50,50,50)
        elif state == 2:
            return (0,175,25)
        elif state == 3:
            return (200,200,0)
        elif state == 4:
            return (0,0,255)
        elif state == 5:
            return(255,0,0)
        else:
            return white


def draw_text(text,pos,font_name='Helvetica',font_size=(16),color=(255,255,255)):
    font = pygame.font.SysFont(font_name,font_size)
    text_render = font.render(text,True,color)
    rect = text_render.get_rect()
    rect.center = (pos[0]+rect.width/2,pos[1])
    screen.blit(text_render,rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            analysis_paused = True
            pos = pygame.mouse.get_pos()
            hold_time = 0
            try:
                if game_board.data[pos[0]//(cell_size+1)][pos[1]//(cell_size+1)] == 0:
                    mode = 'enable'
                else:
                    mode = 'disable'
            except:
                pass
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False
            analysis_paused = False
        if event.type == pygame.K_UP:
            rate += 0.2
        if event.type == pygame.K_DOWN and rate > 0.2:
            rate -= 0.2
        #if event.type == pygame.K_SPACE:
            #print('space pressed')
            #analysis_running = True
    #clear screen
    screen.fill(black)

    for x in range(game_board.width):
        for y in range(game_board.height):
            pygame.draw.rect(screen,get_state_color(x,y),pygame.rect.Rect(x*(cell_size+1),y*(cell_size+1),cell_size,cell_size))

    if mouse_clicked:
        pos = pygame.mouse.get_pos()
        if mode == 'enable':
            game_board.data[pos[0]//(cell_size+1)][pos[1]//(cell_size+1)] = 1
        else:
            game_board.data[pos[0]//(cell_size+1)][pos[1]//(cell_size+1)] = 0

    if analysis_running and not analysis_paused:
        hold_time += dt
        if hold_time > rate:
            hold_time = 0
            gens += 1
            #time.sleep(dt)
            world_gen_v101()

    #get pressed state of keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        analysis_running = True
    if keys[pygame.K_p]:
        analysis_running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_r]:
        game_board.clear()

    #update screen & clock
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()