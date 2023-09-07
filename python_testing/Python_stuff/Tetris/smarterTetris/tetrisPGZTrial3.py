#Alex, it's too many pass statements
#losing rows with each obj reset, idunno y
import random
import pgzrun as pgz

pxStates = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#call internal coordinates as pxStates[y//20][x//20]
WIDTH = 400
HEIGHT = 600

timeHold = 0.0
downHeld = False

score = 0
blocksDropped = 0
pause = False

crntObj = Actor('square')
crntObj.x = 180
#define objects and the relative vectors from upper left block for other blocks in the shape and the spaces to check for collision, all indexes match
Objs = ['square','rect','stairLeft','stairRight','TShape','LLeft','LRight']
objVectors0 = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,1),(1,2)],[(1,0),(1,1),(0,1),(0,2)],[(1,0),(0,1),(1,1),(2,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,0),(1,0),(0,1),(0,2)]]
#for i in range(len(objVectors0)):
    #could try and make a constructor to create each new list, or just use multipliers where vectors applied and ditch the new lists, but ill start with hard-coding
objVectors90 = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(1,0),(2,0)],[(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(0,2),(1,1)],[(0,1),(1,1),(2,1),(2,0)],[(0,0),(1,0),(2,0),(2,1)]]
objVectors180 = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,1),(1,2)],[(1,0),(1,1),(0,1),(0,2)],[(0,0),(1,0),(2,0),(1,1)],[(0,0),(0,1),(0,2),(1,2)],[(1,0),(1,1),(1,2),(0,2)]]
objVectors270 = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(1,0),(2,0)],[(0,0),(1,0),(1,1),(2,1)],[(0,1),(1,0),(1,1),(1,2)],[(0,0),(1,0),(2,0),(0,1)],[(0,0),(0,1),(1,1),(2,1)]]
#colVectors = [[(0,2),(1,2)],[(0,5)],[(0,2),(1,3)]], archived, requires more hard coding but would allow for faster and more efficient collision

#create single index and use it to assign matching vectors and object type (square, T, etc.)
randIndex = random.randint(0,len(Objs)-1)
crntObj.objType = Objs[randIndex]
crntObj.vectors = objVectors0[randIndex]
#crntObj.colVectors = colVectors[randIndex]
rotation = 0

def resetObj():
    global randIndex, rotation, blocksDropped
    for i in range(len(crntObj.vectors)):
        pxStates[int(crntObj.y//20+(crntObj.vectors[i][1]))][int(crntObj.x//20+(crntObj.vectors[i][0]))] = 1
    crntObj.x = 180
    crntObj.y = 0
    randIndex = random.randint(0,len(Objs)-1)
    crntObj.objType = Objs[randIndex]
    crntObj.vectors = objVectors0[randIndex]
    #crntObj.colVectors = colVectors[randIndex]
    rotation = 0
    blocksDropped += 1

def rotateObj():
    global rotation, randIndex
    if rotation == 0:
        objVectors = objVectors90
        rotSet = 90
    elif rotation == 90:
        objVectors = objVectors180
        rotSet = 180
    elif rotation == 180:
        objVectors = objVectors270
        rotSet = 270
    elif rotation == 270:
        objVectors = objVectors0
        rotSet = 0
    for i in range(len(objVectors[randIndex])):
        #for all squares in object, if square(in real coords) is not outside window bounds, continue, else, dont do anything
        if crntObj.x-(crntObj.width*objVectors[randIndex][i][0]) > 0 and crntObj.x+(crntObj.width*objVectors[randIndex][i][0]) < WIDTH - crntObj.width:
            try:
                tempVal = 0
                for j in range(len(objVectors[randIndex])):
                    tempVal += pxStates[int(crntObj.y//20+objVectors[randIndex][j][1])][int(crntObj.x//20+objVectors[randIndex][j][0])]
                if tempVal == 0:
                    allowRotate = True
                else:
                    allowRotate = False
            except:
                allowRotate = False
        else:
            allowRotate = False
        if allowRotate:
            crntObj.vectors = objVectors[randIndex]
            rotation = rotSet

def update(dt):
    global timeHold, score, pause, blocksDropped
    if not pause:
        if timeHold+dt >= 0.25 - min(blocksDropped * 0.0005, 0.15): #limits framerate (in seconds)
            timeHold = 0 #reset for framerate limiter
            #colissions:
            for i in range(len(crntObj.vectors)):
                if crntObj.y//20+(crntObj.vectors[i][1]) == len(pxStates)-2 or pxStates[int(crntObj.y//20+(crntObj.vectors[i][1])+1)][int(crntObj.x//20+(crntObj.vectors[i][0]))] == 1:
                    resetObj()# why do i have to subtract two from this? ^
                #check for row completion:
                for j in range(len(pxStates)):
                    if pxStates[i] == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
                        score += 1
                        #drop higher rows
                        for j in range(i):
                            pxStates[i-j] = [x for x in pxStates[i-j-1]]
                        pxStates[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            crntObj.y += 20
            if downHeld:
                timeHold += (0.25 - (score * 0.005)) * 0.8
        else:
            timeHold += dt
    else:
        pass

def draw():
    global score
    screen.fill(color = (90,90,90))
    for i in range(len(crntObj.vectors)):
        screen.blit('square',(crntObj.x+(crntObj.width*crntObj.vectors[i][0]),crntObj.y+(crntObj.height*crntObj.vectors[i][1])))
    for i in range(len(pxStates)):
        for j in range(len(pxStates[1])):
            if pxStates[i][j] == 1:
                screen.blit('dead_brick',(j*20,i*20))
    screen.draw.text(str(score), center = (WIDTH/2,HEIGHT*0.1), color = (25,25,75), fontsize = 70)

def on_key_down(key):
    global downHeld, pause
    if key == keys.RIGHT or key == keys.D:
        for i in range(len(crntObj.vectors)):
            if crntObj.x+(crntObj.width*crntObj.vectors[i][0]) < WIDTH - crntObj.width:
                try:
                    tempVal = 0
                    for j in range(len(crntObj.vectors)):
                        tempVal += pxStates[int(crntObj.y//20+crntObj.vectors[j][1])][int(crntObj.x//20+1+crntObj.vectors[j][0])]
                    if tempVal == 0:
                        allowMove = True
                    else:
                        allowMove = False
                except:
                    allowMove = False
            else:
                allowMove = False
        if allowMove:
            crntObj.x += 20
    if key == keys.LEFT or key == keys.A:
        for i in range(len(crntObj.vectors)):
            if crntObj.x > 0:
                try:
                    tempVal = 0
                    for j in range(len(crntObj.vectors)):
                        tempVal += pxStates[int(crntObj.y//20+crntObj.vectors[j][1])][int(crntObj.x//20-1+crntObj.vectors[j][0])]
                    if tempVal == 0:
                        allowMove = True
                    else:
                        allowMove = False
                except:
                    allowMove = False
            else:
                allowMove = False
        if allowMove:
            crntObj.x -= 20
    if key == key.DOWN or key == keys.S:
        downHeld = True
    if key == keys.UP or key == keys.W:
        rotateObj()
    if key == keys.P:
        if not pause:
            pause = True
        else:
            pause = False
def on_key_up(key):
    global downHeld
    if key == keys.DOWN or key == keys.S:
        downHeld = False

pgz.go()