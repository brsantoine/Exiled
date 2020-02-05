import pygame as pg
from Wall import *
from Money import *
from Enemy import *
from settings import *
from random import randint

class Map:
    """Une classe qui correspond a un building"""
    def __init__(self, fileName):
        """Initialise la classe Building"""

        # self.img = pg.image.load("maps/" + fileName + ".png")

        self.wallList = []
        self.moneyList = []
        self.enemies = []
        self.playerSpawn = (0, 0)

        file = open("maps/" + fileName + ".map")

        notDone = True

        x = 0
        y = 0

        while notDone:

            line = file.readline()

            if not line:
                notDone = False
            else:
                for lettre in line:
                    if lettre == 'W':
                        self.wallList.append(Wall(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    if lettre == 'C':
                        self.moneyList.append(Money(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    if lettre == 'S':
                        self.playerSpawn = (64 * x, 64 * y)
                    x += 1
                
            y += 1
            x = 0

        file.close()

        nbInList = len(self.moneyList)
        moneyNb = randint((nbInList // 3) - (nbInList // 8), (nbInList // 3) + (nbInList // 8))

        index = 0

        indexesToDelete = []

        while index < nbInList:
            disappearanceProbability = randint(1, (nbInList))
            if disappearanceProbability > moneyNb:
                indexesToDelete.append(index)
            index += 1

        for indexToDelete in reversed(indexesToDelete):
            del self.moneyList[indexToDelete]

        self.enemies.append(Enemy((6.5 * TAILLE_CASE),(1.5 * TAILLE_CASE),(6 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
        self.enemies.append(Enemy((9 * TAILLE_CASE),(5 * TAILLE_CASE),(24 * TAILLE_CASE),0,ENEMY_LOWDELAY,0))
        self.enemies.append(Enemy((19 * TAILLE_CASE),(2 * TAILLE_CASE),(4 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
        self.enemies.append(Enemy((30 * TAILLE_CASE),(2 * TAILLE_CASE),(6 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
        self.enemies.append(Enemy((44 * TAILLE_CASE),(7 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,1))
        self.enemies.append(Enemy((44 * TAILLE_CASE),(18 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,2))
        self.enemies.append(Enemy((38 * TAILLE_CASE),(15 * TAILLE_CASE),(5 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))
        self.enemies.append(Enemy((21 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,4))
        self.enemies.append(Enemy((24 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,4))
        self.enemies.append(Enemy((7 * TAILLE_CASE),(16 * TAILLE_CASE),(6 * TAILLE_CASE),0,ENEMY_HIGHDELAY,0))
        self.enemies.append(Enemy((12 * TAILLE_CASE),(22 * TAILLE_CASE),(14 * TAILLE_CASE),0,ENEMY_LOWDELAY,0))
        self.enemies.append(Enemy((1.5 * TAILLE_CASE),(18.5 * TAILLE_CASE),(8 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))
        self.enemies.append(Enemy((29 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,3))
        self.enemies.append(Enemy((23 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,2))
        self.enemies.append(Enemy((40 * TAILLE_CASE),(31 * TAILLE_CASE),(4 * TAILLE_CASE),0,ENEMY_HIGHDELAY,0))
        self.enemies.append(Enemy((32 * TAILLE_CASE),(19 * TAILLE_CASE),(2 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))

    def update(self):
        enemyHitboxList = []

        for enemy in self.enemies:
            enemy.update()
            for hitbox in enemy.getHitbox() :
                enemyHitboxList.append(hitbox)

        return enemyHitboxList