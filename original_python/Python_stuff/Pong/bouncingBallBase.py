import pgzrun as pgz, random as rand, pygame, time

WIDTH = 1200
HEIGHT = 800
fullscreen = False

leftDown = False
rightDown = False
autoPlay = False
framerate = 0.1
playerScore = 0
enemyScore = 0

ball = Actor('ball')
ball.x = WIDTH / 2
ball.y = HEIGHT / 2
ball.xVect = rand.randint(-3,3)
ball.yVect = 5 * rand.choice([1,-1])
ball.speed = 10

paddle = Actor('enemy_paddle')
paddle.speed = 0
paddle.x = WIDTH / 2
paddle.y = HEIGHT * 5 / 6

enemyPaddle = Actor('paddle')
enemyPaddle.speed = 0
enemyPaddle.x = WIDTH // 2
enemyPaddle.y = HEIGHT * 1 / 6

def reset_game():
    ball.x = WIDTH / 2
    ball.y = HEIGHT / 2
    ball.xVect = rand.randint(-3,3)
    ball.yVect = 5 * rand.choice([1, -1])
    ball.speed = 10

def win():
    global autoPlay, framerate
    reset_game()
    autoPlay = True
    framerate = 0.025
def exit_autoplay():
    global autoPlay, framerate
    reset_game()
    autoPlay = False
    framerate = 0.1

# pgz game functions
def draw(): 
    screen.fill(color = (10,10,10))
    ball.draw()
    paddle.draw()
    enemyPaddle.draw()
    screen.draw.text(str(enemyScore),center = (WIDTH * 11 / 12, HEIGHT / 2), color = (255,0,0), fontsize = 50)
    screen.draw.text(str(playerScore),center = (WIDTH * 1 / 12, HEIGHT / 2), color = (0,255,255), fontsize = 50)


timeHold = 0
def update(dt = framerate):
    global timeHold, framerate, leftDown, rightDown, playerScore, enemyScore
    timeHold += dt
    if timeHold >= framerate:
        # the actual stuff

        #move ball
        if ball.xVect > 20: 
            ball.xVect = 20
        ball.y -= ball.yVect
        ball.x += ball.xVect

        #paddles
        #move player paddle
        if not autoPlay:
            if rightDown and not leftDown and paddle.speed <= 8:
                paddle.speed += 2
            elif leftDown and not rightDown and paddle.speed >= -8:
                paddle.speed -= 2
            elif not rightDown and not rightDown:
                if paddle.speed < 0:
                    paddle.speed += 2
                elif paddle.speed > 0:
                    paddle.speed -= 2
            if paddle.width / 2 < paddle.x + paddle.speed < WIDTH - (paddle.width / 2):
                paddle.x += paddle.speed
        else: # auto play
            if ball.x < paddle.x - 8 and paddle.speed >= -8:
                paddle.speed -= 2
            elif ball.x > paddle.x + 8 and paddle.speed <= 8:
                paddle.speed += 2
            else:
                if paddle.speed < 0:
                    paddle.speed += 2
                elif paddle.speed > 0:
                    paddle.speed -= 2
            if paddle.width / 2 < paddle.x + paddle.speed < WIDTH - (paddle.width / 2):
                paddle.x += paddle.speed
        #enemy paddle
        if ball.yVect < 0: # while ball is moving away, follows more loosely, avoids edges
            if ball.x < enemyPaddle.x - (enemyPaddle.width * 1.5) and enemyPaddle.speed >= -8:
                enemyPaddle.speed -= 2
            elif ball.x > enemyPaddle.x + (enemyPaddle.width * 1.5) and enemyPaddle.speed <= 8:
                enemyPaddle.speed += 2
            if enemyPaddle.x < enemyPaddle.width and enemyPaddle.speed <= 8:
                enemyPaddle.speed += 2
            elif enemyPaddle.x > HEIGHT - enemyPaddle.width and enemyPaddle.speed >= -8:
                enemyPaddle.speed -= 2
        elif ball.x < enemyPaddle.x - (enemyPaddle.width / 2) + 2 and enemyPaddle.speed >= -8:
            enemyPaddle.speed -= 2
        elif ball.x > enemyPaddle.x + (enemyPaddle.width / 2) - 2 and enemyPaddle.speed <= 8:
            enemyPaddle.speed += 2
        elif abs(ball.x - enemyPaddle.x) <= 8:
            if ball.x < enemyPaddle.x and enemyPaddle.speed >= -8:
                enemyPaddle.speed -= 2
            elif ball.x > enemyPaddle.x and enemyPaddle.speed <= 8:
                enemyPaddle.speed += 2
        else:
            if enemyPaddle.speed < 0:
                enemyPaddle.speed += 2
            elif enemyPaddle.speed > 0:
                enemyPaddle.speed -= 2
        if enemyPaddle.width / 2 < enemyPaddle.x + enemyPaddle.speed < WIDTH - (enemyPaddle.width / 2):
            enemyPaddle.x += enemyPaddle.speed
            
        #collisions
        if ball.colliderect(paddle) and abs(ball.y - paddle.y) <= paddle.width / 2: # player paddle
            if ball.y < paddle.y - (paddle.height // 2):
                ball.yVect = abs(ball.yVect)
                ball.xVect = (ball.x - paddle.x) // 6 * (ball.yVect // 5)
            else:
                ball.xVect *= -1
                ball.xVect = (ball.x - paddle.x) // 6 * (ball.yVect // 5)
        elif ball.colliderect(enemyPaddle) and abs(ball.y - enemyPaddle.y) <= enemyPaddle.width / 2: # enemy paddle
            if ball.y < enemyPaddle.y + (enemyPaddle.height // 2) + (ball.y // 2):
                ball.yVect = abs(ball.yVect) * -1
                ball.xVect = (ball.x - enemyPaddle.x) // 6 * (ball.yVect // 5) * -1
            else:
                ball.xVect *= -1
                ball.xVect = (ball.x - enemyPaddle.x) // 6 * (ball.yVect // 5) * -1
        elif ball.y >= HEIGHT - ball.width / 2: # floor
            enemyScore += 1
            reset_game()
        elif ball.x <= ball.width / 2 or ball.x >= WIDTH - ball.width / 2: # left and right walls
            ball.xVect *= -1
        elif ball.y <= ball.height / 2: # ceiling
            playerScore += 1
            reset_game()
        
def on_key_down(key):
    global rightDown, leftDown
    if key == keys.D or key == keys.RIGHT:
        rightDown = True
    elif key == keys.A or key == keys.LEFT:
        leftDown = True
    elif key == keys.R:
        reset_game()
    elif key == keys.W:
        win()
    elif key == keys.S:
        exit_autoplay()
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

# != < >=