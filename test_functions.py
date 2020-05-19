#simple test functions used with PyTest to test very frequently used functions in ui.pu, ant.py and soldiers.py.
class TestFunctions(object):

    pause=False
    def test_getinversedistance(self):
        from ui import getInverseDistance
        a = [0,2,4,6]
        for n in a:
            assert getInverseDistance(n) == 1

    def test_sumFirstElements(self):
        from ui import sumFirstElements
        a = [1,2,3,4]
        end=2
        assert sumFirstElements(a,end) == 3

    def test_getSpawn(self):
        from ui import getSpawn, spawnX, spawnY
        getSpawn()
        assert (99 >= spawnX >= 0) and (99 >= spawnY >= 0)

    def test_addAnts(self):
        from ant import add_Ants, Ant
        from ui import antSpawnCounter, antSpawnFreq, spawnX, spawnY, ants
        add_Ants()
        assert len(ants)>0

    def test_soldiersInit(self):
        from soldier import soldiersInit, soldiers
        soldiersInit()
        assert len(soldiers)==20

    def test_antsInit(self):
        from ui import antsInit, ants, initAnts
        antsInit()
        assert len(ants)==initAnts+1

    def test_getEnemySpawn(self):
        from enemy import getEnemySpawn, enemySpawnX, enemySpawnY
        getEnemySpawn()
        assert (99 >= enemySpawnX >= 0) and (99 >= enemySpawnY >= 0)

    def test_enemyInit(self):
        from enemy import enemyInit, enemies, initEnemies
        enemyInit()
        assert len(enemies)==10

    def test_add_EnemyAnts(self):
        from enemy import add_enemyAnts, enemies, Enemy
        add_enemyAnts()
        assert len(enemies)==11

    def test_pauseFunc(self):
        from ui import pauseFunc
        pauseFunc()
        from ui import pause
        assert pause == True

    def test_slowFunc(self):
        from ui import slowFunc
        slowFunc()
        from ui import pause, fps
        assert (pause == False) and (fps == 15)

    def test_playFunc(self):
        from ui import playFunc
        playFunc()
        from ui import pause, fps
        assert (pause == False) and (fps == 60)

    def test_iter(self):
        from ui import iter
        iter()
        from ui import iterations
        assert iterations == 1
