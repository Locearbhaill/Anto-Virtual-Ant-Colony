#----------------------------#
#Third Year Project
#Last updated on or around 11/05/2019
#By Alex C & Liam ÓC
#----------------------------#



import pygame as pg  # pygame module used for the UI, prefix is pg
import random as r  # used a fair bit
from ui import *

r.seed()

#Messages => mostly used for debugging in terminal
messages = False     #turns on/off the msgs in terminal
deathmessages = False    #toggles death messages
fpsmessages = False #toggles fps messages

iterations = 0 #Used for keeping track of "iterations"
EnemySpawnFreq = 35 # every amount of loops for enemy to spawn eg enemy spawns every 35 loops of main


# FIELD
# field is the grouping food, obstacles, pheremones and the spawn
#
foodBlock = 70  # initial amount of food blocks
foodPerBlock = 50  # amount of food per block
foodLst = []  # like matrix except for food blocks
foodAmount = []  # keeps track of how much food each block has
obstacles = 3000  # number of obstacle on field
minSpawnDist = 25  # Minimum distance between spawns
initPheremone = 1.0  # going to be used later for pheremones
alpha = 3  # importance of feromone, higher means fermones have higher priority
beta = 3  # importance of inverse distance, higher means shorter paths found quicker, at the cost of
# lessening the importance of feromones and decreasing initial efficiency
antsOnFero = 100  # number of ants allowed on a single trail
localEvap = 0.0003  #increments pheromone by this amount
globEvap = 0.0005   #derements pheromone by this amount

antRePop = True # if true then ants will add ants to the colony in accordance with below variables.
antSpawnFreq = 10 #freqeuncy of spawning ants when food is found. 10 = 1 in 10 food creates an ant
antSpawnCounter = 9 #used for keeping track of ants to be added

drawing = True      #change this to enable/disable drawing of ants
evaporating = True  #??allows evaporation of pheremones??

# COLOURS
wht = (255, 255, 255)  # BACKGROUND COLOUR
blk = (0, 0, 0)  # ANT COLOUR
teal = (0, 88, 88)  # SUPERANT COLOUR
ylw = (255, 211, 0)  # SOLDIER COLOUR
btnylw = (240,210,0)    #SLOW SPEED BUTTON COLOUR
grn = (0, 255, 0)  # PHEREMONE COLOUR
btngrn = (10,200,10) # play btn colour
red = (200,10,10)   #stop btn colour
pnk = (148, 0, 211)  # ENEMY COLOUR
prpl = (178, 58, 238) #ENEMY SPAWN
brwn = (255, 255, 77)  # FOOD COLOUR
blu = (0, 0, 255)  # SPAWN COLOUR
gry = (128, 128, 128)  # OBSTACLE COLOUR

# ANTS
spawnX = 0  # X COORD FOR COLONY SPAWN
spawnY = 0  # Y COORD FOR COLONY SPAWN#
initAnts = 100  # initial number of ants
numLeet = 1  # this is the % of ants which will be leet
ants = []  # will be list of ant objects


matrix = []  # 100*100 matrix of everything static placed on field(food, spawns, obstacles)


# pygame stuff for the screen size
pg.init()   #needed to initialise PyGame
pg.display.set_caption("ANTO")  # title at the top of the window
screenScale = 7  # for pygame screen size ### has to be above the below line
screenheight = int(100 * screenScale)   #set height of PyGame window
screenwidth = int(143*screenScale)      #set width of PyGame window
screen = pg.display.set_mode([screenwidth, screenheight])  # sets screen size. DON'T MESS WTIH

clock = pg.time.Clock()     #needed for updating PyGame
fps = 60    #fps used in clock.tick() in main. runs simulation at 60 fps(unless it slows down)

#pygame text stuff
pg.font.init()  #for drawing text on the screen
screenfont = pg.font.SysFont("Terminal", 30)                #sets the font to "Terminal" + creates text object(a standard font included with win)
titlefont = pg.font.SysFont("Terminal",40)                  #sets title font as  " + creates text object
title = titlefont.render("ANTO",False,blk)                 #all of these
quittext = screenfont.render("Quit",False,blk)              #create text objects
anttext = screenfont.render("Ants:",False,blk)
enemytext = screenfont.render("Enemies:",False,blk)
soldiertext = screenfont.render("Soldiers:",False,blk)

def pygameTextInit():
    #initialisese the counter text
    from enemy import enemies       #used for getting no. of enemies
    from soldier import soldiers    #used for getting no. of soldiers
    antcounttext = screenfont.render(str(len(ants)),False,blk)
    enemycounttext = screenfont.render(str(len(enemies)),False,blk)
    soldiercounttext = screenfont.render(str(len(soldiers)),False,blk)

# Stack to keep track of death locations
class DeathStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def xpos(self):
        if self.isEmpty() != True:
            return self.items[len(self.items) - 2]

    def ypos(self):
        if self.isEmpty() != True:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

antDeathStack = DeathStack()    #Initialises death stack

def getSpawn():
    #func for getting spawn(moved out of fieldInit!)
    global spawnX, spawnY
    spawnX = r.randint(0,99)
    spawnY = r.randint(0,99)

# Initialises everything on the field, namely; food, obstacles and the spawn.
def fieldInit():
    from enemy import getEnemySpawn
    for i in range(100):
        matrix.append([])
        for j in range(100):
            matrix[i].append(initPheremone)  # set the pheremone for every spot to just 1.0
    # set a random spawn
    getSpawn()
    matrix[spawnX][spawnY] = "spawn"  # puts the spawn in random matrix position x y
    #set random enemy spawn
    getEnemySpawn()
    from enemy import enemySpawnX, enemySpawnY
    matrix[enemySpawnX][enemySpawnY] = "enemySpawn"  # puts enemy spawn in random matrix postion xy
    # randomly place food blocks on field
    for i in range(foodBlock):
        foodX = r.randint(0, 98)
        foodY = r.randint(0, 98)
        foodLst.append([foodX, foodY])
        foodAmount.append(foodPerBlock)
        matrix[foodX][foodY] = "food"  # puts a "food" in matrix position x y

    # randomly place obstacles on field
    for i in range(obstacles):
        obstacleX = r.randint(0, 99)
        obstacleY = r.randint(0, 99)
        if matrix[obstacleX][obstacleY] != "spawn" and matrix[obstacleX][obstacleY] != "enemySpawn" and matrix[obstacleX][obstacleY] != "food":
                matrix[obstacleX][obstacleY] = "obstacle"  # puts an obstacle in matrix position x y
        else:
            continue


# func for actually drawing the squares on the screen
# (except for background which is done in "drawField()")
def draw(colour, x, y):
    square = pg.Surface((screenScale, screenScale))  # size of the small squares on screen
    square.fill(colour)  # fills squares with colour
    screen.blit(square, (x * screenScale, y * screenScale))  # blit is used in pygame for drawing
    return (x * screenScale, y * screenScale)


# draws everything on the field, except for ants.
def drawField():
    screen.fill(wht)  # basically sets background to white
    for i in range(100):  # iterate through x coords
        for j in range(100):  # iterate through y coords
            if matrix[i][j] == "spawn":
                draw(blu, i, j)  # draws the spawn
            elif matrix[i][j] == "enemySpawn":
                draw(prpl, i, j)
            elif matrix[i][j] == "food":
                draw(brwn, i, j)  # draws the food
            elif matrix[i][j] == "obstacle":
                draw(gry, i, j)  # draws obstacles
            else:
                phereGray = 255 - (matrix[i][j] - initPheremone) * 1.5  # higher means deeper color
                phereGreen = 2 * phereGray
                if phereGray > 255:
                    phereGray = 255
                if phereGray < 0:
                    phereGray = 0
                if phereGreen > 255:
                    phereGreen = 255
                if phereGreen < 50:
                    phereGreen = 50
                draw((phereGray, phereGreen, phereGray), i, j)  # draw rgb using calculated value for phere

def updateAntCountText():
    #updates the counter of ants in the sidebar
    global antcounttext
    antcounttext = screenfont.render(str(len(ants)),False,blk)

def updateEnemyCountText():
    #updates the counter of enemies in the sidebar
    from enemy import enemies
    global enemycounttext
    enemycounttext = screenfont.render(str(len(enemies)),False,blk)

def updateSoldierCountText():
    #updates the counter of soldiers in the sidebar
    from soldier import soldiers
    global soldiercounttext
    soldiercounttext = screenfont.render(str(len(soldiers)),False,blk)

#X + Y coords and width + height of the buttons
stopX = 102*screenScale
slowX = 115.5*screenScale
playX = 129*screenScale
buttonY = 85*screenScale
buttonwidth = 12*screenScale
buttonheight = 7*screenScale

def drawSide():
    #function for drawing the sidebar
    #ie. everything that's not on the field
    """
    Use loops to draw and upated everything on sidebar?
    """
    pg.draw.line(screen, blk,(100*screenScale,0),(100*screenScale,100*screenScale))             #draws line separating field from sidebar
    pg.draw.rect(screen, red,(stopX,buttonY,buttonwidth,buttonheight))     #draws stop btn
    pg.draw.rect(screen, btnylw,(slowX,buttonY,buttonwidth,buttonheight))     #draws slow btn
    pg.draw.rect(screen, btngrn,(playX,buttonY,buttonwidth,buttonheight))  #draws play button
    screen.blit(title,(110*screenScale,10*screenScale))             #draws "ANTO" at top of sidebar
    screen.blit(quittext,(117*screenScale,95*screenScale))          #draws "QUIT" at bottom of sidebar
    screen.blit(anttext,(110*screenScale, 60*screenScale))          #draws "Ants:" in sidebar
    screen.blit(soldiertext,(110*screenScale,65*screenScale))       #draws "Soldier:" in sidebar
    screen.blit(enemytext,(110*screenScale,70*screenScale))         #draws "Enemies:" in sidebar
    updateAntCountText()
    updateEnemyCountText()
    updateSoldierCountText()
    screen.blit(antcounttext,(125*screenScale, 60*screenScale))     #draws the ant counter in sidebar
    screen.blit(soldiercounttext,(125*screenScale,65*screenScale))  #draws soldier counter in sidebar
    screen.blit(enemycounttext,(125*screenScale, 70*screenScale))   #draws the enemy counter in sidebar

def pauseFunc():
    #pauses the simulation
    global pause
    pause = True
    if messages:
        print("paused!")
def slowFunc():
    #runs simulation at quarter speed
    global pause, fps
    pause = False
    fps = 15
    if messages:
        print("setting to slow speed!")
def playFunc():
    #runs simulation at full speed
    global pause, fps
    pause = False
    fps = 60
    if messages:
        print("back to 60 fps!")

def buttons(posx,posy):
    #func to decide which button is clicked and calls the respective button func
    #does by crudely checking if mouse is in btn coords when it is clicked!
    click = pg.mouse.get_pressed()
    #click[0] is mouse1
    #click[1] is mouse2
    if (stopX+buttonwidth > posx > stopX) and (buttonY+buttonheight > posy > buttonY):
        if (click[0] ==1 and not pause) :
            pauseFunc()
        else:
            pass
    elif (slowX+buttonwidth > posx > slowX) and (buttonY+buttonheight > posy > buttonY):
        if (click[0] ==1 and pause) or (click[0] ==1 and not pause):
            slowFunc()
        else:
            pass
    elif (playX+buttonwidth > posx > playX) and (buttonY+buttonheight > posy > buttonY):
        if (click[0] ==1 and pause) or (click[0] and fps != 60):
            playFunc()
        else:
            pass
    elif (117*screenScale+30 > posx > 117*screenScale) and (95*screenScale+15 > posy > 95*screenScale):
        print("quitting!")
        pg.quit()
        quit()
    else:
        pass
# ------------------------------------ANT DRAWING AND CREATION-----------------------------------------
def antsInit():
    from ant import Ant
    num2Bpromoted = int(numLeet / 100 * initAnts)  # no. of leet ants

    for i in range(initAnts):
        ants.append(Ant(spawnX, spawnY, False))  # add to list

    while (num2Bpromoted > 0):  # while there exists ants to be promoted
        chosenLeet = r.choice(ants)  # promote some!
        if not chosenLeet.leet:
            chosenLeet.leet = True
            num2Bpromoted -= 1
            if messages:
                print("Ant Number", "%#10d" % chosenLeet.id, "has been promoted. Good job 'lil buddy!")

def sumFirstElements(arr, end):  # sums first elements of array renamed from summy
    tmp = 0
    if end >= len(arr):
        end = len(arr) - 1
    for i in range(0, end):
        tmp += arr[i]
    return tmp

def getInverseDistance(dir):
    if (dir == 0) or (dir == 2) or (dir == 4) or (dir == 6):
        return 1.0  # straight line dist is 1
    else:
        return float(1 / 2 ** .5)  # Diagonal distance with root 2

def drawAnts():
    # func for drawing ants on each iteration of main
    for lilguy in ants:
        lilguy.turn()
        if not lilguy.leet:
            if drawing:
                draw(blk, lilguy.x, lilguy.y)  # regular lil dudes
        else:
            if drawing:
                draw(teal, lilguy.x, lilguy.y)  # leet dudes


def drawSoldiers():
    # func for drawing soldiers on each iteration of main
    from soldier import soldiers
    for soldier in soldiers:
        if soldier.targetMove:
            soldier.targMove()
        else:
            soldier.move()
        if drawing:
            draw(ylw, soldier.x, soldier.y)


def drawEnemies():
    # func for drawing enemies on each iteration of main
    from enemy import enemies
    for enemy in enemies:  # imports "enemies" from enemy.py
        enemy.move()  # move() is in enemies(as of 22/02 only simple movement)
        if drawing:
            draw(pnk, enemy.x, enemy.y)  # uses draw func in this file#


def placeFood(posx, posy):
    # Called to manually place food with left click
    global foodBlock, matrix
    posx = round(posx / screenScale)
    posy = round(posy / screenScale)
    foodBlock += 1
    foodLst.append([posx, posy])  # Unelegant way for directly adding food
    foodAmount.append(foodPerBlock)  # Unelegant way for directly adding food
    matrix[posx][posy] = "food"  # Unelegant way for directly adding food
    draw(brwn, posx, posy)  # Color, x, y
    if messages:
        print("Placed food at:", posx, posy)
    return

def deathCheck():  # Used for checking if an ant should die
    from enemy import enemies
    from soldier import soldiers, Soldier
    enemylocations = set((enemy.x,enemy.y) for enemy in enemies)
    overlaps = [ant for ant in ants if (ant.x,ant.y) in enemylocations]
    for overlap in overlaps:
        antDeathStack.push(overlap.x)
        antDeathStack.push(overlap.y)
        list(map(lambda Soldier:Soldier.target(antDeathStack),soldiers))
        overlap.death()
        if deathmessages:
            print("Enemy killed ant", overlap.id)
    #soldierlocations = set((soldier.x,soldier.y) for soldier in soldiers)
    #print(enemylocations.intersection(soldierlocations))
    #list(map(lambda enemy:enemy.death(),enemylocations.intersection(soldierlocations)))
    for soldier in soldiers:
        for index, enemy in enumerate(enemies):
            if soldier.x == enemy.x and soldier.y == enemy.y:
                if deathmessages:
                    print("soldier", soldier.id, "has killed enemy ", enemy.id, "Good job lilguy!")
                enemy.death(index)  #calls enemy death func


def evaporator():
    for x in range(100):
        for y in range(100):
            if type(matrix[x][y]) == (type(0.0)):
                matrix[x][y] = matrix[x][y] * (1-globEvap)

def foodGone(): #doesn't work
    if foodBlock > 0:
        for i in foodLst:
            if len(i) > 0:
                return False
        return True
    else:
        return False



def iter():
    from enemy import add_enemyAnts
    global iterations
    iterations += 1
    if iterations % EnemySpawnFreq == 0:
        add_enemyAnts()


def main():
    from enemy import enemyInit
    from soldier import soldiersInit
    pygameTextInit()
    fieldInit()  # initialise the field
    antsInit()  # initialise the ants
    soldiersInit()  # initialise the soldiers
    enemyInit()  # Initialise the enemies
    global initAnts, matrix, alive
    # Keeps running until quit(x is clicked or esc pressed)
    while alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                alive = False
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                posx, posy = pg.mouse.get_pos()
                if posx > 100*screenScale:
                    buttons(posx,posy)
                else:
                    placeFood(posx, posy)
                pass

            elif event.type == pg.K_ESCAPE:  # good idea, doesnt work :(
                alive = False
        drawField()  # update the field
        drawSide()
        drawAnts()  # update ants
        drawSoldiers()  # update soldiers
        drawEnemies()  # update enemies
        deathCheck()  # checks for dead ants
        iter()
        if evaporating:
            evaporator()
        pg.display.flip()  # used for pygame(updates screen)
        clock.tick(fps)  # used in pygame
        if fpsmessages:
            print(fps)
        if foodGone(): #doesn't work
            print("all food is gone! ")
            alive = False
        if pause:
            while pause:
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        posx,posy = pg.mouse.get_pos()
                        buttons(posx,posy)
                    else:
                        pass
    print("there were ", initAnts, "in the colony. Good job lilguys! ")
    pg.quit()

alive = True
pause = False
main()
