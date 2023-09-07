import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400,400)) 
clock = pygame.time.Clock()
running = True
dt = 0
entities = []

# game setup
def get_circle_rect(object):
    return pygame.Rect(object.pos[0]-object.radius,object.pos[1]-object.radius,object.radius*2,object.radius*2)

class ball:
    def __init__(self,pos,entity_type,vects=(0,0),radius=10,color=(0,0,0),grav_direction='down',coll_timer=0.05,enabled=True):
        self.pos = pygame.Vector2(pos)
        self.vects = pygame.Vector2(vects)
        self.radius = radius
        self.rect = get_circle_rect(self)
        self.color = color
        self.grav_direction = grav_direction
        self.grav_power = 1.0
        self.grav_enabled = True
        self.entity_type = entity_type
        self.coll_timer = coll_timer
        self.enabled = enabled

    def draw(self):
        if self.enabled:
            pygame.draw.circle(screen,self.color,self.pos,self.radius)

    def relative_motion(self,vects): # vects input is movement relative to own gravity, adjusts to match actual coordinate plane - changes motion vectors, not pos
        if self.grav_direction == 'right':
            vects = (vects[1] * -1,vects[0])
        elif self.grav_direction == 'left':
            vects = (vects[1],vects[0] * -1)
        elif self.grav_direction == 'up':
            vects = (vects[0] * -1,vects[1] * -1)
        self.vects.x -= vects[0] # same as motion in apply_physics, inverse to match stuff
        self.vects.y -= vects[1]
    
def apply_physics(object):
    global running
    if type(object) != ball:
        running = False
        print('tried to apply physics to invalid object')
    #motion, vertical then horizontal
    # if move goes below, land and bounce, same for above, else move
    if object.pos.y - object.vects.y * dt < object.radius:
        object.pos.y = object.radius
        object.vects.y *= -2/3
    elif object.pos.y - object.vects.y * dt > screen.get_height() - object.radius:
        object.pos.y = screen.get_height()-object.radius
        object.vects.y *= -2/3
    else:
        object.pos.y -= object.vects.y * dt

    if object.pos.x - object.vects.x * dt < object.radius:
        object.pos.x = object.radius
        object.vects.x *= -2/3
    elif object.pos.x - object.vects.x * dt > screen.get_width() - object.radius:
        object.pos.x = screen.get_width()-object.radius
        object.vects.x *= -2/3
    else:
        object.pos.x -= object.vects.x * dt
    #apply gravity
    object.relative_motion((0,20 * object.grav_power))
    '''if object.grav_direction == 'up' and object.grav_enabled:
        object.vects.y += 20 * object.grav_power
    elif object.grav_direction == 'down' and object.grav_enabled:
        object.vects.y -= 20 * object.grav_power
    elif object.grav_direction == 'right' and object.grav_enabled:
        object.vects.x += 20 * object.grav_power
    elif object.grav_direction == 'left' and object.grav_enabled:
        object.vects.x -= 20 * object.grav_power'''

def draw_text(text,pos,font_name='Helvetica',font_size=(16),color=(255,255,255)):
    font = pygame.font.SysFont(font_name,font_size)
    text_render = font.render(text,True,color)
    rect = text_render.get_rect()
    rect.center = (pos[0]+rect.width/2,pos[1])
    screen.blit(text_render,rect)
        
player = ball((screen.get_width() / 2, screen.get_height() / 2),radius=40,color=(100,100,150),entity_type='player')
enemy = ball((screen.get_width() / 2, screen.get_height() / 3),radius=40,color=(150,50,0),entity_type='enemy')
entities = [player,enemy]

while running:
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.grav_enabled:
                    player.grav_enabled = False
                else:
                    player.grav_enabled = True
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_e:
                enemy.enabled = False

    keys = pygame.key.get_pressed()
    
    #clear screen
    screen.fill((100,5,150))

    #draw
    player.draw()
    enemy.draw()
    '''if player.grav_direction == 'up':
        pygame.draw.lines(screen,(0,0,0),True,(screen.get_width()/2,screen.get_height()),(screen.get_width()/2,screen.get_height()/3))
    elif player.grav_direction == 'right':
        pygame.draw.lines(screen,(0,0,0),True,(screen.get_width()/2,screen.get_height()),(screen.get_width()*2/3,screen.get_height()/2))
    elif player.grav_direction == 'left':
        pygame.draw.lines(screen,(0,0,0),True,(screen.get_width()/2,screen.get_height()),(screen.get_width()/3,screen.get_height()/2))
    elif player.grav_direction == 'down':
        pygame.draw.lines(screen,(0,0,0),True,(screen.get_width()/2,screen.get_height()),(screen.get_width()/2,screen.get_height()*2/3))'''
    #draw_text('X vect:'+str(player.vects.x),(40,40))
    #draw_text('Y vect:'+str(player.vects.y),(40,80))

    #physics
    # motion, inverts direction to account for upper left origin
    for entity in entities:
        apply_physics(entity)
    player.rect, enemy.rect = get_circle_rect(player), get_circle_rect(enemy) #update rectangle

    # collision (screen edge collision included in motion)
    if pygame.sprite.collide_circle(player,enemy) and enemy.enabled:
        if player.coll_timer <= 0:
            player.coll_timer = 0.05
            if abs(player.pos.y - enemy.pos.y) < abs(player.pos.x - enemy.pos.x):
                player.vects.x *= -1
                player.vects.y *= 1
                enemy.vects.x *= -1
                enemy.vects.y *= 1
            else:
                player.vects.x *= 1
                player.vects.y *= -1
                enemy.vects.x *= 1
                enemy.vects.y *= -1
        else:
            player.coll_timer -= dt

    #get keys (gets pressed keys with event check, some controls split between here and event loop)
    if keys[pygame.K_w] and player.pos.y - player.vects.y * dt > 0:
        player.grav_direction, enemy.grav_direction = 'up', 'up'
    if keys[pygame.K_s]:
        player.grav_direction, enemy.grav_direction = 'down', 'down'
    if keys[pygame.K_a]:
        player.grav_direction, enemy.grav_direction = 'right', 'right'
    if keys[pygame.K_d]:
        player.grav_direction, enemy.grav_direction = 'left', 'left'
    if keys[pygame.K_r]:
        player.pos.x, player.pos.y = screen.get_width() / 2, screen.get_height() / 2
        player.vects.x, player.vects.y = 0, 0
        player.grav_direction = 'down'
    if keys[pygame.K_UP] and player.grav_power < 10:
        player.grav_power += 0.1
    if keys[pygame.K_DOWN] and player.grav_power > 0:
        player.grav_power -= 0.1

    #display the done things
    pygame.display.flip()

    #define framerate, keep physics framerate-independant
    dt = clock.tick(60) / 1000

pygame.quit()

# original physics
'''   # physics / gravity
    if player.pos.y - player.vects.y * dt > 0 and player.vects.y >= -1000 and grav_direction[0] == 'vertical':
        if player.vects.y >= 10:
            player.vects.y *= 0.9
        elif player.vects.y <= -10:
            player.vects.y *= 1.1
        elif player.vects.y != 0:
            player.vects.y -= 4
        else:
            player.vects.y -= 10
    elif player.pos.x - player.vects.x * dt > 0 and player.vects.x >= -1000 and grav_direction[0] == 'horizontal':
        if player.vects.x >= 10:
            player.vects.x *= 0.9
        elif player.vects.x <= -10:
            player.vects.x *= 1.1
        elif player.vects.x != 0:
            player.vects.x -= 4
        else:
            player.vects.y -= 10

    '''