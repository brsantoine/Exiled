import pygame as pg
from Wall import *
from Exit import *
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
        self.exitList = []
        self.moneyList = []
        self.enemies = []
        self.playerSpawn = (0, 0)

        file = open("maps/" + fileName + ".map")

        readingMap = True

        x = 0
        y = 0

        while readingMap:

            line = file.readline()

            if not line:
                readingMap = False
            else:
                for lettre in line:
                    if lettre == 'W':
                        self.wallList.append(Wall(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    if lettre == 'E':
                        self.exitList.append(Exit(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    if lettre == 'C':
                        self.moneyList.append(Money(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    if lettre == 'S':
                        self.playerSpawn = (64 * x, 64 * y)
                    if lettre == '#':
                        readingMap = False
                    x += 1
                
            y += 1
            x = 0

        readingEnemies = True

        while readingEnemies:

            line = file.readline()

            if not line:
                readingEnemies = False
            else:
                enemy = line.split(" ; ")
                if enemy[4] == "LOW":
                    delay = ENEMY_LOWDELAY
                else:
                    delay = ENEMY_HIGHDELAY
                self.enemies.append(Enemy((float(enemy[0]) * TAILLE_CASE), (float(enemy[1]) * TAILLE_CASE), (float(enemy[2]) * TAILLE_CASE), float(enemy[3]), delay, float(enemy[5])))

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

    def update(self):
        enemyHitboxList = []

        for enemy in self.enemies:
            enemy.update()
            for hitbox in enemy.getHitbox() :
                enemyHitboxList.append(hitbox)

        return enemyHitboxList
