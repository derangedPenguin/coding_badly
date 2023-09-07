import pgzrun as pgz, random as rand, pygame, time

WIDTH = 1200
HEIGHT = 800
fullscreen = False
timer = 5.0

leftDown = False
rightDown = False
inPaddle = False
autoPlay = False
framerate = 0.1

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 3
ball.xVect = rand.randint(-3,3)
ball.yVect = -5
ball.speed = 10

paddle = Actor('paddle')
paddle.speed = 0
paddle.x = WIDTH / 2
paddle.y = HEIGHT * 5 / 6

def reset_ball():
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 3
    ball.xVect = rand.randint(-3,3)
    ball.yVect = -5
    ball.speed = 10

def win():
    global autoPlay, framerate
    reset_ball()
    autoPlay = True
    framerate = 0.05

# pgz game functions
def draw(): 
    screen.fill(color = (10,10,10))
    ball.draw()
    paddle.draw()
    if inPaddle:
        screen.blit('ball',(30,30))
    screen.draw.text(str(timer), center = (WIDTH * 13 / 16,HEIGHT / 16))

timeHold = 0
def update(dt):
    global timeHold, inPaddle, timer, framerate, leftDown, rightDown
    timeHold += dt
    if timeHold >= framerate:
        # the actual stuff

        #move ball
        if ball.xVect > 20: 
            ball.xVect = 20
        ball.y -= ball.yVect
        ball.x += ball.xVect

        #move paddle
        if autoPlay:
            if ball.x < paddle.x and abs(paddle.speed) <= 8:
                leftDown = True
                rightDown = False
            elif ball.x > paddle.x and abs(paddle.speed) <= 8:
                rightDown = True
                leftDown = False
            
        if rightDown and paddle.speed <= 8:
            paddle.speed += 2
        elif leftDown and paddle.speed >= -8:
            paddle.speed -= 2
        elif not rightDown and not rightDown:
            if paddle.speed < 0:
                paddle.speed += 2
            elif paddle.speed > 0:
                paddle.speed -= 2
        if paddle.width / 2 < paddle.x + paddle.speed < WIDTH - (paddle.width / 2):
            paddle.x += paddle.speed

        #collisions
        if ball.colliderect(paddle) and abs(ball.y - paddle.y) <= paddle.width / 2:
            ball.yVect *= -1
            ball.xVect = (ball.x - paddle.x) // 12
            #ball.xVect += (ball.x - paddle.x) // 4
        elif ball.x <= ball.width / 2 or ball.x >= WIDTH - ball.width / 2:
            ball.xVect *= -1
        elif ball.y <= ball.height / 2:
            ball.yVect *= -1
        elif ball.y >= HEIGHT - ball.width / 2:
            reset_ball()
        if abs(paddle.y - ball.y) <= paddle.height / 2 and abs(ball.x - paddle.x) <= paddle.width / 2:
            inPaddle = True
            if ball.x > paddle.x:
                ball.xVect -= 1
            elif ball.x < paddle.x:
                ball.xVect += 1
        elif inPaddle:
            ball.yVect = abs(ball.yVect)
            inPaddle = False
        if abs(ball.x - paddle.x) <= 5:
            if timer > 0:
                timer -= 0.1
            else:
                win()
        else:
            timer = 5



def on_key_down(key):
    global rightDown, leftDown
    if key == keys.D or key == keys.RIGHT:
        rightDown = True
    elif key == keys.A or key == keys.LEFT:
        leftDown = True
    elif key == keys.R:
        reset_ball()
    elif key == keys.W:
        win()
def on_key_up(key):
    global rightDown, leftDown
    if key == keys.D or key == keys.RIGHT:
        rightDown = False
    elif key == keys.A or key == keys.LEFT:
        leftDown = False
    
    
pgz.go()

# Extras and Archives

# potential for fullscreen
'''if key == keys.F:
        if fullscreen == False:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))'''

# direct controls for ball