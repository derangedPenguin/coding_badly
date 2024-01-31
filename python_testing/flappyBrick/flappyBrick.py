#SETUP PYGAME ZERO
import pgzrun, random

#SCREEN
WIDTH = 400
HEIGHT = 600

#SETUP SCORE
score = 0

#SETUP BRICK
brick = Actor("brick")
brick.x = 90
brick.y = 250
setattr(brick, 'velocity', 1.5)

#SETUP WALLS
wall_top = Actor('wall-top')
wall_bottom = Actor('wall-bottom')
gap = 200

wall_top.x = WIDTH + wall_top.width
wall_top.y = 0
wall_bottom.x = WIDTH + wall_top.width
wall_bottom.y = wall_top.height + gap

#SETUP BACKGROUND
def setRandCoords(actor):
  actor.y = random.randint(0, HEIGHT)
  actor.x = random.randint(0, WIDTH)

cloud1 = Actor('cloud1')
cloud2 = Actor('cloud2')
cloud3 = Actor('cloud3')
cloud4 = Actor('cloud4')
cloud5 = Actor('cloud5')
clouds = [cloud1,cloud2,cloud3,cloud4,cloud5]

for i in range(len(clouds)):
  setRandCoords(clouds[i])
  setattr(clouds[i], 'speed', random.uniform(0.25,3))
  clouds[i].width = 272 * random.uniform(0.25,1)
  clouds[i].height = 136 * (clouds[i].width / 272)

#BUTTON PRESSES
def on_mouse_down():
  if brick.velocity - 12.5 > -12.6:
    brick.velocity = brick.velocity - 12.5
  else:
    brick.velocity = -12.5

#DRAW STUFF TO SCREEN
def draw():
  global score
  screen.fill("lightblue")
  for i in range(len(clouds)):
    clouds[i].draw()
  brick.draw()
  wall_top.draw()
  wall_bottom.draw()
  screen.draw.text(str(score), (WIDTH / 2, 30), color=(255,0,255), fontsize = 50)
  screen.draw.text(str(brick.y), (WIDTH / 2, 60))

#EACH CYCLE THROUGH THE LOOP
def update():
  global score, gap
  brick.y += brick.velocity
  if brick.velocity < 5:
    brick.velocity = brick.velocity + 0.5
  wall_top.x -= 1 + (score/20)
  wall_bottom.x -= 1 + (score/20)
  for i in range(len(clouds)):

    clouds[i].x -= clouds[i].speed
  if score < 50:
    gap = (1 - (score/100)) * 200

  

  #COLLISIONS
  if brick.colliderect(wall_top) or brick.colliderect(wall_bottom):
    score += 1
    reset()
  if brick.y > 600 - (brick.height/2):
    reset()
  if brick.y < brick.height / 2:
    brick.velocity = 1
  if wall_top.x < 0 - wall_top.width:
    score += 1
    reset_walls()
  for i in range(len(clouds)):
    if clouds[i].x <= 0 - clouds[i].width:
      reset_cloud(clouds[i])
  
#RESET
def reset():
  global score
  score = 0
  brick.y = 250
  wall_top.x = WIDTH + wall_top.width
  wall_bottom.x = WIDTH + wall_bottom.width
def reset_walls():
  wall_top.x = WIDTH + wall_top.width
  wall_bottom.x = WIDTH + wall_bottom.width
  wall_top.y = random.randint(-50,50)
  wall_bottom.y = wall_top.y + wall_top.height + gap
def reset_cloud(cloud):
  cloud.y = random.randint(0,HEIGHT)
  cloud.x = WIDTH + (2 * cloud.width)
  #cloud.width = 272 * random.uniform(0.25,1)
  #cloud.height = 136 * (cloud.width / 272)
  cloud.inflate(2,2)
  cloud.speed = random.uniform(0.25,3)

#RUN PYGAME ZERO
pgzrun.go()