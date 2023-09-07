import pygame, time, json
import random as rand

"""
components: board display, wave function, collapsing
board object:
- holds state of each style
- also stores methods to make changes and get info on scale of entire board
- custom class, only used once to create 'game_board' object, in theory multiple can be created and run each time
tile class:
- tile object will be created for each coordinate (tile) on the board
- holds primarily information retrieval functions: list of surrounding tiles' states, etc.
- parent class for each tile type
tile subclasses:
- includes: void/null/empty, mountain, forest, beach, ocean
- 
"""
"""
a rule defines a specific interaction from one collapsed tile and any other non-collapsed tile which affects said tile's options
each rule is a dict {range:(x1,y1),(x2,y2) or point:(x,y), collapse:option or limit:(options) or rem:option(s)} or {'allrem':(options)}
"""
with open('colors.json','r') as file: 
    colors = json.loads(file.read())
with open('./wave_func_testing/version_3/rules.json','r') as file: 
    rules: dict = json.loads(file.read())['tile']
options = {'mountain':100,'forest':100,'beach':100,'ocean':100}
tile_colors = {'mountain':colors['brown'],'forest':colors['green'],'beach':colors['yellow'],'ocean':colors['blue'],'undefined':colors['white']}

class tile:
    def __init__(self) -> None:
        #self.state = 'super' # options: None (empty; err), 'super' (Superposition; all possible things available), 'inter' (interstate, between min and max options), 'collapsed' (only one potential remaining)
        self.options = options.copy()
        self.collapsed_state = 'undefined'
    
    def get_state(self):
        if self.options == options:
            return 'super'
        elif self.collapsed_state != 'undefined':
            return 'collapsed'
        else:
            return 'inter'
    
    def collapse(self,option):
        if option in self.options:
            self.collapsed_state = option
        else:
            return ValueError ('cannot collapse to impossible state')
        """if option != 'undefined':
            self.state = 'collapsed'
        else:
            self.state = 'super'"""
        
    def auto_collapse(self):
        self.collapse(self.options.keys()[0])
        
    def enact_rules(self,x,y): # both this and my rule definitions are horrid, i'll fix it later
        #sort
        tile_rules = rules.get(self.collapsed_state,{})
        allrems, points, ranges = [],[],[]
        for rule in tile_rules:
            if type_name := list(rule.keys())[0] == 'allrem':
                allrems.append(rule) 
            elif type_name == 'point':
                points.append(rule)
            else:
                ranges.append(rule)
        #enact
        for rule in allrems:
            for i in range(-1,2):
                for j in range(-1,2):
                    if i==0 and j==0:
                        continue
                    del game_board.data[x+i][y+1].options[rule.keys()[0]] #?!?! idek dude
        for rule in points:
            point = game_board.data[x+rule['point'][0]][y+rule['point'][1]]
            if operation := rule.keys[1] == 'remove':
                try:
                    del point.options[rule['remove']]
                except: pass
            else:
                pass
        for rule in ranges:
            x_range = range(rule['range'][0][0],rule['range'][1][0])
            y_range = range(rule['range'][0][1],rule['range'][1][1])
            for rel_x in x_range:
                for rel_y in y_range:
                    game_board.data[x+rel_x][y+rel_y].options[rule["promote"][0]] *= rule["promote"][1]

class board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.data = {x:{y:tile() for y in range(height)} for x in range(width)}
    
    def clear(self):
        self.data = {x:{y:tile() for y in range(self.height)} for x in range(self.width)}

def conf_to_range(val: int, max: int, min: int = 0):
    if val > max:
        result = max
    elif val < min:
        result = min
    else:
        result = val
    return result

def rand_collapse(tile: tile):
    val_dict = tile.options.copy()
    items = list(val_dict.keys())
    for i in val_dict:
        val_dict[i] //= 50
    result = []
    for i in items:
        for j in range(val_dict[i]):
            result.append(i)
    try:
        tile.collapse(rand.choice(result))
    except:
        print(tile.options)
    

#+-----------init---------------+
# --board init--
game_board = board(35,35)
tile_width = 12
border_width = 1
# --pygame init--
pygame.init()
screen = pygame.display.set_mode((game_board.width*(tile_width+border_width),game_board.height*(tile_width+border_width)))
clock = pygame.time.Clock()
dt = 0
running = True
mouse_down = False
drawing_state = 'mountain'

#+-----------sim loop-------------+
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_board.clear()
            if event.key == pygame.K_0:
                drawing_state = 'undefined'
            if event.key == pygame.K_1:
                drawing_state = 'mountain'
            if event.key == pygame.K_2:
                drawing_state = 'forest'
            if event.key == pygame.K_3:
                drawing_state = 'beach'
            if event.key == pygame.K_4:
                drawing_state = 'ocean'
            if event.key == pygame.K_SPACE:
                game_board.data[5][5].enact_rules(5,5)
    
    #board operations
    screen.fill(colors['black'])
    for x in range(game_board.width):
        for y in range(game_board.height):
            #draw
            pygame.draw.rect(screen,tile_colors[game_board.data[x][y].collapsed_state],pygame.rect.Rect(x*(tile_width+border_width),y*(tile_width+border_width),tile_width,tile_width))
            #basic collapse checks
            if len(point := game_board.data[x][y].options) == 1:
                point.auto_collapse()

    if mouse_down:
        pos = pygame.mouse.get_pos()
        pos = (pos[0]//(tile_width+border_width), pos[1]//(tile_width+border_width))
        pos = (conf_to_range(pos[0],game_board.width-1), conf_to_range(pos[1], game_board.height-1))
        if not keys[pygame.K_LALT]:
            game_board.data[pos[0]][pos[1]].collapse(drawing_state)
        else:
            rand_collapse(game_board.data[pos[0]][pos[1]])
            
    pygame.display.flip()
    dt = clock.tick()

pygame.quit()