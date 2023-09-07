import random
import pgzrun as pgz

pixelStates = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
WIDTH = 400
HEIGHT = 600

timeHold = 0.0
downHeld = False

score = 0

oneStates = ['square']
twoStates = ['rect','stairLeft','stairRight']
fourStates = ['leftL','rightL','Tshape']
Objs = ['square','rect','stairLeft']
objVectors = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,1),(1,2)]]
colVectors = [[(0,2),(1,2)],[(0,5)],[(0,2),(1,3)]]
brickHeights = [2,4,3]
#each list in objVectors matches to the object of the same index in Objs
crntObj = Actor('square')
crntObj.x = 180
randIndex = random.randint(0,len(Objs)-1)
crntObj.objType = Objs[randIndex]
crntObj.vectors = objVectors[randIndex]
crntObj.colVectors = colVectors[randIndex]
crntObj.brickHeight = brickHeights[randIndex]
rotation = 0

def getLowerBlocks():
    if crntObj.objType in oneStates:
        if crntObj.objType == 'square':
            return int(pixelStates[int((crntObj.y//20)+2)][int(crntObj.x//20)]) + int(pixelStates[int((crntObj.y//20)+2)][int((crntObj.x//20)+1)])
    elif crntObj.objType in twoStates:
        if crntObj.objType == 'rect':
            return pixelStates[int(crntObj.y//20+4)][int(crntObj.x//20)]
        elif crntObj.objType == 'stairL':
            return int(pixelStates[int((crntObj.y//20)+2)][int(crntObj.x//20)]) + int(pixelStates[int((crntObj.y//20)+3)][int(crntObj.x//20+1)])

def setFilledCoords():
        if crntObj.objType == 'square':
            crntObj.fills = [(crntObj.x,crntObj.y),(crntObj.x+crntObj.width,crntObj.y),(crntObj.x+crntObj.width,crntObj.y+crntObj.height),(crntObj.x,crntObj.y+crntObj.height)]
        elif crntObj.objType == 'rect':
            crntObj.fills = [(crntObj.x,crntObj.y),(crntObj.x,crntObj.y+(crntObj.height)),(crntObj.x,crntObj.y+(crntObj.height*2)),(crntObj.x,crntObj.y+(crntObj.height*3))]
        elif crntObj.objType == 'stairL':
            crntObj.fills = [(crntObj.x,crntObj.y),(crntObj.x,crntObj.y+(crntObj.height)),(crntObj.x+crntObj.width,crntObj.y+(crntObj.height)),(crntObj.x+crntObj.width,crntObj.y+(crntObj.height*2))]

def getFilledCoords():
    tempList = []
    for i in range(len(crntObj.vectors)):
        tempList.append(crntObj.y + (crntObj.height * crntObj.vectors[i][1]))
    print(tempList)
    return (tempList)

def resetObj():
    for i in range(len(crntObj.fills)):
        pixelStates[int(crntObj.fills[i][1])//20][int(crntObj.fills[i][0])//20] = 1
    crntObj.x = 180
    crntObj.y = 0
    randIndex = random.randint(0,len(Objs)-1)
    crntObj.objType = Objs[randIndex]
    crntObj.vectors = objVectors[randIndex]
    crntObj.colVectors = colVectors[randIndex]

def update(dt):
    global timeHold, score
    if timeHold + dt >= 0.1:
        timeHold = 0
        #Collisions (kinda) crntObj.x//20+crntObj.colVectors[x][1] / max(crntObj.y + (crntObj.height * crntObj.vectors[0][1],))
        if max(getFilledCoords()) >= HEIGHT - crntObj.height: #check for floor
            resetObj()
        for i in range(len(crntObj.colVectors)-1):
            if pixelStates[int((crntObj.y//20)+crntObj.colVectors[i][1])][int((crntObj.x//20)+crntObj.colVectors[i][0])] >= 1: #check for dead block
                resetObj()
        #check rows
        for i in range(len(pixelStates)):
            if pixelStates[i] == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
                pixelStates[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                score += 1
                #drop higher rows
                for j in range(i):
                    pixelStates[i-j] = pixelStates[i-j-1]

        #not collisions
        crntObj.y += 20
        if downHeld and crntObj.y <= HEIGHT - (crntObj.height*4) and (pixelStates[int(crntObj.y//20+2)][int(crntObj.x//20)] == 0 and pixelStates[int(crntObj.y//20+2)][int(crntObj.x//20+1)] == 0):
            crntObj.y += 20
        setFilledCoords()
    else:
        timeHold += dt


def draw():
    screen.fill(color = (50,50,50))
    makeObj()
    for y in range(len(pixelStates)):
        for x in range(len(pixelStates[1])):
            if pixelStates[y][x] == 1:
                screen.blit('dead_brick',(x*20,y*20))
    screen.draw.text(str(score),center = (WIDTH/2,20), color = (255,0,0))

def makeObj():
    for i in range(len(crntObj.vectors)):
        screen.blit('square',(crntObj.x+(crntObj.width*crntObj.vectors[i][0]),crntObj.y+(crntObj.height*crntObj.vectors[i][1])))
        
def on_key_down(key):
    global downHeld
    if key == keys.RIGHT:
        if crntObj.x <= 17*20 and (pixelStates[int(crntObj.y//20)][int(crntObj.x//20+2)] == 0 and pixelStates[int(crntObj.y//20+1)][int(crntObj.x//20+2)] == 0):
            crntObj.x += 20
    if key == keys.LEFT:
        if crntObj.x > 0 and (pixelStates[int(crntObj.y//20)][int(crntObj.x//20-1)] == 0 and pixelStates[int(crntObj.y//20+1)][int(crntObj.x//20-1)] == 0):
            crntObj.x -= 20
    if key == keys.DOWN:
        downHeld = True
    if key == keys.UP:
        pass
def on_key_up(key):
    global downHeld
    if key == keys.DOWN:
        downHeld = False
        
setFilledCoords()
pgz.go()