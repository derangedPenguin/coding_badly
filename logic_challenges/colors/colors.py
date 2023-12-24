import pygame
import random
import sys
import time

FPS = 60

COLS = {
    1:(255,255,255),
    10:(255,0,255),
    50:(0,0,255),
    100:(0,255,0),
    1000:(255,127,0),
    5000:(255,0,0),
    10_000:(0,0,0)
}
COL_COUNTER = {
    i:0 for i in COLS
}

def draw_text(text,pos,font_name='Helvetica',font_size=(16),color=(255,255,255)):
    font = pygame.font.SysFont(font_name,font_size)
    text_render = font.render(text,True,color)
    rect = text_render.get_rect()
    rect.center = (pos[0]+rect.width/2,pos[1])
    screen.blit(text_render,rect)

pygame.init()
screen = pygame.display.set_mode((480,480), flags=pygame.RESIZABLE, vsync=1)
clock = pygame.time.Clock()
screen_color = (255,255,255)
counter = 0
timer = 0
clicks = set()
stats = {
    i:{'count':0, 'chance':f'1:{10_000/i}'} for i in COLS
}

def run_chance(rigged=False):
    if not rigged:
        key = random.randint(0, 10_000)
        for num in COLS:
            if key <= num:
                COL_COUNTER[num] += 1
                return COLS[num]
        return (0,0,0)
    else:
        return COLS[1]

def clicked():
    global screen_color, counter, clicks
    screen_color = run_chance()
    counter += 1
    clicks.add(time.time())

while True:
    timer += 1
    screen.fill(screen_color)
    if timer % 10 == 0:
        clicked()
    #remove clicks greater than 3 seconds ago
    new_clicks = clicks.copy()
    for click_time in clicks:
        crnt = time.time()
        if crnt - click_time > 3:
            new_clicks.remove(click_time)
    clicks = new_clicks.copy()
    #get avg cps over past 3 seconds
    clicks_per_frame = len(clicks)/(3*FPS)

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(screen.get_width()*9/12, 0, screen.get_width()*3/12, screen.get_height()))

    #inverse screen color: (255-screen_color[0],255-screen_color[1],255-screen_color[2])
    draw_text(str(counter), (screen.get_width()*10/12, screen.get_height()/6), font_size=48, color=(0,0,0))
    draw_text(f'cps: ~{'{:.4}'.format(clicks_per_frame*60)}', (screen.get_width()*19/24, screen.get_height()*1/12), font_size=16, color=(0,0,0))

    for i, thing in enumerate(COL_COUNTER.items()):
        col_num, col_count = thing
        color = COLS[col_num]
        if color == (255,255,255):
            color = (200,200,200)
        draw_text(f'chance: {stats[col_num]['chance']} - count: {col_count}', (screen.get_width()*9/12, screen.get_height()/6 + (i+1)*50), font_size=32, color=color)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clicked()
    pygame.display.update()
    clock.tick(FPS)