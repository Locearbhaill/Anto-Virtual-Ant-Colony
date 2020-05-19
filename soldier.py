import random as r
from ui import matrix
initSoldiers = 20   #initial amount of soldiers
soldiers = []


# soldier colour is ylw
# spawn is same as colony spawn coords
class Soldier:
    """soldier class, will try to seek out and
    kill the enemies"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.targetX = 0
        self.targetY = 0
        self.targetMove = False
        self.id = r.randint(0, 50)

    def checkMove(self, newX, newY):
        #makes sure soldiers don't run through obstacles or go off the field
        if ((self.x + newX) in range(0,99)) and ((self.y + newY) in range(0,99)) and (matrix[self.x + newX][self.y + newY] != "obstacle"):
            return True
        else:
            return

    def move(self):
        #randomly selects a direction
        newX = r.randint(-1,1)
        newY = r.randint(-1,1)
        while not self.checkMove(newX,newY):
            newX = r.randint(-1,1)
            newY = r.randint(-1,1)
        self.x += newX
        self.y += newY

    def targMove(self):
        #used for moving towards enemies when found
        if self.targetX > self.x:
            self.x += 1
            if self.targetY > self.y:
                self.y += 1
            else:
                self.y -= 1
        else:
            self.x -= 1
            if self.targetY > self.y:
                self.y += 1
            else:
                self.y -=1
        if (self.x == self.targetX) and (self.y == self.targetY):
            self.targetMove = False


    def respawn(self): # not committed
        self.x = spawnX
        self.y = spawnY

    def target(self, stackOb):
        from enemy import enemies
        newX = stackOb.xpos()
        newY = stackOb.ypos()
        for enemy in enemies:
            if not (((enemy.x - self.x) ** 2) + (enemy.y - self.y) ** 2) ** 0.5 < 5:
                if (newX != self.targetX) and (newY != self.targetY):
                    self.targetX = newX
                    self.targetY = newY
                    self.targetMove = True
        else:
            self.targetX = enemy.x
            self.targetY = enemy.y
        self.targMove()



def soldiersInit():
    # func for initialising the soldiers
    from ui import spawnX, spawnY  # need to get the colony spawn coords
    for soldier in range(initSoldiers):
        soldiers.append(Soldier(spawnX, spawnY))
