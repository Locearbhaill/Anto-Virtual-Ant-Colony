# FILE CONTAING THE ANT CLASS AND RELATED FUNCTIONS
import random as r
from ui import *


def add_Ants():#Everytime an ant finds food this is called to increase the size of the colony
    global antSpawnCounter
    antSpawnCounter += 1
    if antSpawnCounter % antSpawnFreq == 0:
        if antSpawnCounter % (antSpawnFreq * 15) == 0:
           ants.append(Ant(spawnX, spawnY, True))
           if messages:
               print("A super ant has been born")
        ants.append(Ant(spawnX, spawnY, False))
        if messages:
            print("An ant has been born!")


class Ant:
    global spawnX, spawnY
    antid = 0
    def __init__(self, x, y, leet):
        self.x = x
        self.y = y
        self.leet = leet
        self.putFeromone = False
        self.steps = 0
        self.tabooList = []
        self.tabooListIndex = 0
        self.id = Ant.antid
        Ant.antid += 1

    def turn(self):
        global initAnts, antSpawnCounter
        if not self.putFeromone:

            # create possible directions
            if (self.x == 0) and (self.y == 0):  # left top corner
                self.addPossibleTurns([2, 3, 4])
            if (self.x == 0) and (self.y == 99):  # left bottom corner
                self.addPossibleTurns([0, 1, 2])
            if (self.x == 99) and (self.y == 0):  # right top corner
                self.addPossibleTurns([4, 5, 6])
            if (self.x == 99) and (self.y == 99):  # right bottom corner
                self.addPossibleTurns([6, 7, 0])
            if (self.x == 0) and (self.y in range(1, 99)):  # left side somewhere (not corner)
                self.addPossibleTurns([0, 1, 2, 3, 4])
            if (self.x == 99) and (self.y in range(1, 99)):  # right side somewhere (not corner)
                self.addPossibleTurns([0, 4, 5, 6, 7])
            if (self.y == 0) and (self.x in range(1, 99)):  # top somewhere (not corner)
                self.addPossibleTurns([2, 3, 4, 5, 6])
            if (self.y == 99) and (self.x in range(1, 99)):  # bottom somewhere (not corner)
                self.addPossibleTurns([6, 7, 0, 1, 2])
            if (self.x in range(1, 99)) and (self.y in range(1, 99)):  # everywhere else apart from sides
                self.addPossibleTurns([0, 1, 2, 3, 4, 5, 6, 7])  # can move anywhere pretty much

            tmp = 0
            probs = []
            for i in self.possibleTurns:
                tmp += getInverseDistance(i) ** beta * self.figFeromone(i) ** alpha
            for i in self.possibleTurns:  # without second loop tmp changes and all ants mimick each other
                probs.append(getInverseDistance(i) ** beta * self.figFeromone(i) ** alpha / tmp)
            if not self.leet:
                probRange = []
                for i in range(0, len(probs)):
                    probRange.append(sumFirstElements(probs, i))
                newDir = self.selectDir(probRange)
            elif self.leet:
                newDir = self.selectDir(probs)
            self.move(newDir)

            if (matrix[self.x][self.y] == "food"):
                leetStr = ""
                if self.leet:
                    leetStr = "This is a Super Ant!"
                if messages:
                    print("Ant number", self.id, "found", "%#3d" % foodAmount[foodLst.index([self.x, self.y])], "Food at co-ordinates", self.x, self.y, "taking", "%#10f" % self.steps, "steps!", leetStr)
                if antRePop:
                    initAnts += 1
                    add_Ants()
                self.putFeromone = True

                if (foodPerBlock != 0):
                    foodAmount[foodLst.index([self.x, self.y])] -= 1
                    if foodAmount[foodLst.index([self.x, self.y])] == 0:
                        matrix[self.x][self.y] = initPheremone
                        self.putFeromone = False
                    if messages:
                        print("Food at co-ordinates", self.x, self.y, "Depleted but pheromone remains!")

        else:  # if putFeromone
            self.tabooListIndex += 1
            self.x = self.tabooList[-self.tabooListIndex][0]
            self.y = self.tabooList[-self.tabooListIndex][1]

            if type(matrix[self.x][self.y]) == type(0.0):
                newTau = (1 - localEvap) * matrix[self.x][self.y] + antsOnFero / self.steps
                matrix[self.x][self.y] = newTau

            if (matrix[self.x][self.y] == "spawn"):
                self.respawn()
        return

    def selectDir(self, probRange):
        if not self.leet:
            if (len(self.possibleTurns) > 0):
                rand = r.random()
                for i in range(len(probRange) - 1):
                    if (rand >= probRange[i]) and (rand < probRange[i + 1]):
                        return self.possibleTurns[i]
                if rand >= probRange[-1]:
                    return self.possibleTurns[-1]
            else:
                self.respawn()
        else:
            if len(self.possibleTurns) > 0:
                maxProb = max(probRange)
                maxIndeces = [i for i, j in enumerate(probRange) if j == maxProb]
                return self.possibleTurns[r.choice(maxIndeces)]
            else:
                self.respawn()

    def move(self, direc):
        if [self.x, self.y] not in self.tabooList:
            self.tabooList.append([self.x, self.y])  # add to sol list
        dx, dy = 0, 0

        if direc == 0:  # up
            dy = -1
        if direc == 1:  # up + right
            dy = -1
            dx = 1
        if direc == 2:  # right
            dx = 1
        if direc == 3:  # right + down
            dx = 1
            dy = 1
        if direc == 4:  # down
            dy = 1
        if direc == 5:  # down + left
            dy = 1
            dx = -1
        if direc == 6:  # left
            dx = -1
        if direc == 7:  # left + up
            dx = -1
            dy = -1

        self.x += dx
        self.y += dy

        if [self.x, self.y] not in self.tabooList:
            self.tabooList.append([self.x, self.y])

        if (dx * dy == 0):  # if straight move inc 1
            self.steps += 1
        else:
            self.steps += 2 ** .5  # if diagnol inc root 2

    def addPossibleTurns(self, arr):
        self.possibleTurns = []
        for i in arr:
            cur = self.tryMove(i)
            if not (cur in self.tabooList) and (cur[0] in range(0, 100)) and (cur[1] in range(0, 100)) and \
                    (matrix[cur[0]][cur[1]] != "obstacle"):
                self.possibleTurns.append(i)

    def tryMove(self, direc):  # going clockwise, 0 being up, 2 being right, 4 being down etc.
        if direc == 0:
            return [self.x, self.y - 1]  # up
        if direc == 1:
            return [self.x + 1, self.y - 1]  # right + up
        if direc == 2:
            return [self.x + 1, self.y]  # right
        if direc == 3:
            return [self.x + 1, self.y + 1]  # right + down
        if direc == 4:
            return [self.x, self.y + 1]  # down
        if direc == 5:
            return [self.x - 1, self.y + 1]  # left + down
        if direc == 6:
            return [self.x - 1, self.y]  # left
        if direc == 7:
            return [self.x - 1, self.y - 1]  # left + up

    def figFeromone(self, direc):
        fX = self.x
        fY = self.y

        if direc == 0:  # looking up
            fY = self.y - 1
        if direc == 1:  # looking up and right
            fY = self.y - 1
            fX = self.x + 1
        if direc == 2:  # looking right
            fX = self.x + 1
        if direc == 3:  # looking right and down
            fX = self.x + 1
            fY = self.y + 1
        if direc == 4:  # looking down
            fY = self.y + 1
        if direc == 5:  # looking down and left
            fX = self.x - 1
            fY = self.y + 1
        if direc == 6:  # looking left
            fX = self.x - 1
        if direc == 7:  # looking left and up
            fX = self.x - 1
            fY = self.y - 1

        if type(matrix[fX][fY]) == type(0.0):  # as in holds a fero value
            return matrix[fX][fY]
        else:
            return initPheremone * 10000

    def respawn(self):
        self.x = spawnX
        self.y = spawnY
        self.tabooList = []
        self.putFeromone = False
        self.tabooListIndex = 0
        self.steps = 0
        #print("Ant number", self.id, "got lost!")


    def death(self):
        """deletes ant from ants[] if they get killed by an enemy"""
        global ants
        ants.remove(self)



