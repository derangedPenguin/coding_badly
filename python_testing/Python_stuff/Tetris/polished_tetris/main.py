import pygame
import random as rand
#from pygame.sprite import _Group

pygame.init()
running = True
screen = pygame.display.set_mode((500,650))
current_screen = 'main_menu'
score = 0
board = [[0 for i in range(30)] for i in range(20)]

tile_images = {1:'dead_brick.png',2:'square.png'}

tetrominoes = {'I':((0,0),(1,0),(2,0),(3,0)),
               'O':((0,0),(1,0),(0,1),(1,1)),'T':((-1,0),(0,0),(1,0),(0,1)),
               'L':((0,0),(0,1),(0,2),(1,2)),'J':((1,0),(1,1),(1,2),(0,2)),
               'S':((0,0),(1,0),(0,1),(-1,1)),'Z':((0,0),(1,0),(1,1),(1,2))}
ttm_colors = {'I':'light_blue','O':'yellow','T':'purple','L':'orange','J':'blue','S':'green','Z':'red'}

class falling_ttm(pygame.sprite.Sprite):
    def __init__(self, shape: str, color = (0,0,0)) -> None:
        super().__init__()
        self.rel_points = tetrominoes[shape]
        self.color = color

current_ttm = falling_ttm('I')

def rect_from_center(height: int, width: int, pos: tuple):
    return pygame.rect.Rect(pos[0]-(width/2),pos[1]-(height/2),width,height)

def draw_text(text: str,pos: tuple,font_name='Yu Gothic Regular',font_size=(16),color=(255,255,255)):
    font = pygame.font.SysFont(font_name,font_size)
    text_render = font.render(text,True,color)
    rect = text_render.get_rect()
    rect.center = pos
    screen.blit(text_render,rect)

start_button = rect_from_center(40,80,(screen.get_width()/2,screen.get_height()*3/5))

def pause():
    global current_screen
    #pygame.draw.rect(screen,(0,0,0,0.1),pygame.rect.Rect(0,0,screen.get_width(),screen.get_height()))
    current_screen = 'paused'

def update_menu():
    global current_screen
    screen.fill((0,0,0))
    draw_text('Tetris',(screen.get_width()/2,screen.get_height()/5),font_size=32)
    draw_text('Start',(screen.get_width()/2,screen.get_height()*3/5))
    if pygame.MOUSEBUTTONDOWN and start_button.collidepoint(pygame.mouse.get_pos()):
        current_screen = 'game_active'

def update_game():
    screen.fill((0,0,0))
    draw_text(str(score),(screen.get_width()/2,screen.get_height()/8),font_size=32)
    pygame.draw.rect(screen,(255,255,255), pygame.rect.Rect(49,0,402,601))
    for x in range(len(board)):
        for y in range(len(board[x])):
            if status := board[x][y] != 0:
                screen.blit(pygame.image.load('Tetris/images/'+tile_images[status]),(x*20+50,y*20))
            else:
                pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(x*20+50,y*20,20,20))
    #falling ttm managing
    

def init_game():
    global score, board, current_ttm
    score = 0
    board = [[0 for i in range(30)] for i in range(20)]
    current_ttm = falling_ttm(shape=rand.choice(list(tetrominoes.keys())))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if current_screen == 'paused':
                if event.key in [pygame.K_p, pygame.K_SPACE]:
                    current_screen = 'game_active'
            if current_screen == 'game_active':
                if event.key == pygame.K_p:
                    pause()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == 'paused':
                current_screen = 'game_active'
    
    match current_screen:
        case 'main_menu':
            update_menu()
        case 'game_active':
            update_game()
        case 'paused':
            pass
    
    pygame.display.flip()

pygame.quit()