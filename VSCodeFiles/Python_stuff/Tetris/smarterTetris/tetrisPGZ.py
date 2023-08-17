import os, random, time, pgzrun

'''column is x, row is y, first location in coords is row, second is column'''
coords = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
objCoord = [9,0]
timeHold = 0.0

WIDTH = 400
HEIGHT = 600

downHeld = False

crntObj = Actor('square')
crntObj.x = 180
crntObj.y = 0

def makeSquare(column,row):
    coords[column-1][row] = 0
    coords[column-1][row+1] = 0
    coords[column][row] = 1
    coords[column][row+1] = 1
    coords[column+1][row] = 1
    coords[column+1][row+1] = 1

def update(dt):
    global objCoord, coords, timeHold
    if downHeld:
        crntObj.y += 20
    if timeHold + dt >= 0.25:
      timeHold = 0.0
      if crntObj.y//20 <= 28:
        makeSquare(int(crntObj.x//20),int(crntObj.y//20))
        crntObj.y += 20
      else:
        resetObj()
    else:
        timeHold += dt   

def getStateResult(x,y): #returns what image to blit depending on state of the internal (non pgz) coord, returns empty string for nothing
    state = coords[x][y]
    if state == 0:
        return ''
    elif state == 1:
        return 'square'
    elif state == 2:
        return 'dead_brick'

def draw():
    global crntObj, objCoord
    screen.fill('black')
    for y in range(len(coords)):
        for x in range(len(coords[1])):
            try: #blits image to screen, does nothing for nothing
                screen.blit(getStateResult(x,y), (x*20,y*20))
            except:
                pass


def on_key_down(key): #pgz keystroke func, used for all controls
    global downHeld
    if key == keys.RIGHT:
        if crntObj.y <= 17*20:
            crntObj.y += 20
    elif key == keys.LEFT:
        if crntObj.y > 0:
            crntObj.y -= 20
    elif key == keys.DOWN:
        downHeld = True

def on_key_up(key):
    global downHeld
    if key == keys.DOWN:
        downHeld = False

def resetObj():
    crntObj.x = 180
    crntObj.y = 0
    makeSquare(int(crntObj.x//20),int(crntObj.y//20))

pgzrun.go()