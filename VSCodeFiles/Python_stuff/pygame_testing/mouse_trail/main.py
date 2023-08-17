import pygame, json

pygame.init()
running = True
dt = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((350,350))
with open('colors.json','r') as file: colors = json.loads(file.read())

val = 1000

mp_dict = dict({i:(0,0) for i in range(val+1)})
time_held = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(mp_dict)
    
    screen.fill(colors['black'])
    time_held += dt
    if time_held >= 0.1:
        time_held = 0
        for i in range(val,-1,-1):
            mp_dict[i+1] = mp_dict[i]
    mp_dict[0] = pygame.mouse.get_pos()

    for i in range(len(mp_dict)):
        #dist_ratio = max(0.1*i/(val/2),1)
        #pygame.draw.circle(screen,(0,255,255,1/dist_ratio),mp_dict[i],10/dist_ratio)
        try:
            pygame.draw.line(screen,colors['cyan'],mp_dict[i],mp_dict[i-1],min(i,5))
        except: pass

    pygame.display.flip()
    dt = clock.tick()

pygame.quit