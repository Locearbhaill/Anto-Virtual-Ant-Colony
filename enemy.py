import random as r
from ui import matrix


#ENEMIES

initEnemies = 5     #initial amount of enemies
enemymult = 1.0     #enemy multiplier(higher the number, the more that will spawn over time!)
enemies = [] #list of enemies

enemySpawnX = 0  # X COORD FOR ENEMY SPAWN
enemySpawnY = 0  # Y COORD FOR ENEMY SPAWN

def add_enemyAnts():
    enemies.append(Enemy(enemySpawnX, enemySpawnY))
    from ui import messages
    if messages:
        print("enemy spawned")


def getEnemySpawn():
    #func for getting enemy spawn(moved out of fieldInit!)
    from ui import spawnX, spawnY, minSpawnDist
    global enemySpawnX, enemySpawnY
    enemySpawnX = r.randint(0,99)
    enemySpawnY = r.randint(0,99)
    while not ((((enemySpawnX - spawnX) ** 2) + ((enemySpawnY - spawnY) ** 2)) ** .5) > minSpawnDist:
        # ensures enemy and regular spawn
        # is at least a minimum of 25 blocks away using distance formula
        enemySpawnX = r.randint(0, 99)
        enemySpawnY = r.randint(0, 99)

def enemyInit():
    for i in range(initEnemies):
        enemies.append(Enemy(enemySpawnX, enemySpawnY))


class Enemy():
    """docstring for Enemy."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = r.randint(0,50)

    def checkMove(self, newX, newY):
        if ((self.x + newX) in range(0,99)) and ((self.y + newY) in range(0,99)) and (matrix[self.x + newX][self.y + newY] != "obstacle"):
            return True
        else:
            return

    def move(self):
        newX = r.randint(-1,1)
        newY = r.randint(-1,1)
        while not self.checkMove(newX,newY):
            newX = r.randint(-1,1)
            newY = r.randint(-1,1)
        self.x += newX
        self.y += newY

    def respawn(self, enemySpawnX, enemySpawnY): # respawn for enemies
        self.x = enemySpawnX
        self.y = enemySpawnY
        from ui import deathmessages
        if deathmessages:
            print("Enemy ant", self.id, "died")

    def death(self, index):
        global enemies
        del enemies[index]
