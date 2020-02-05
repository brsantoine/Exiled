import pygame as pg

from Map import *
from Camera import *
from Player import *

class Expedition:
    def __init__(self, mapFileName):
        self.moneyGained = 0
        self.map = Map(mapFileName)
        self.camera = Camera()
        self.inProgress = True

        self.player = Player(self.map.playerSpawn, 64, 64)

        self.collisionList = []
        self.collisionList += self.map.wallList
        self.collisionList += self.map.enemies

        self.enemyHitboxList = []

    def update(self):
        self.enemyHitboxList = self.map.update()
        self.player.update(pg.key.get_pressed(), self.collisionList)
        
        if self.player.rect.collidelist(self.map.exitList) != -1:
            self.inProgress = False

        if self.player.rect.collidelist(self.enemyHitboxList) != -1:
            self.inProgress = False

        moneyIndex = 0
        while moneyIndex < len(self.map.moneyList):
            if self.map.moneyList[moneyIndex].rect.colliderect(self.player.rect):
                self.moneyGained += randint(40, 60)
                del self.map.moneyList[moneyIndex]
            moneyIndex += 1
                

        if self.player.rect.collidelist(self.enemyHitboxList) != -1:
            self.inProgress = False

    def draw(self, screen):
        self.displayList = []
        self.displayList += self.map.wallList
        self.displayList += self.map.exitList
        self.displayList += self.map.moneyList
        self.displayList += self.map.enemies
        self.camera.draw(screen, self.player, self.displayList, self.enemyHitboxList)