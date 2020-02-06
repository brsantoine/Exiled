import pygame as pg
import os
from random import randint
from Map import *
from Camera import *
from Player import *
from AirBall import *
from threading import Timer

class Expedition:
    def __init__(self, mapFileName, boots, airSkill):
        self.moneyGained = 0

        mapList = []

        for map in os.listdir("maps"):
            mapList.append(map)

        randomMap = randint(0, len(mapList) - 1)

        self.map = Map("maps/" + mapList[randomMap])
        self.camera = Camera()
        self.inProgress = True

        self.player = Player(self.map.playerSpawn, 64, 64)

        self.collisionList = []
        self.collisionList += self.map.wallList
        self.collisionList += self.map.enemies

        self.enemyHitboxList = []
        self.airballs = []
        if airSkill == True:
            self.player.gotAirSkill()
        if boots == True:
            self.player.gotBoots()
        self.win = True
        self.timerExped = False
        self.time = 0


    def update(self):
        self.enemyHitboxList = self.map.update()
        keys = pg.key.get_pressed()
        self.player.update(keys, self.collisionList, self.map.width, self.map.height)
        airball = self.player.AirBall(keys)
        if airball != False:
            self.airballs.append(airball)

        for airball in self.airballs:
            if airball.update(keys,self.map.wallList+self.map.exitList,self.map.enemies) == False:
                self.airballs.remove(airball)
                del airball

        if self.player.rect.collidelist(self.map.exitList) != -1:
            self.inProgress = False

        if self.player.rect.collidelist(self.enemyHitboxList) != -1:
            self.inProgress = False
            self.win = False

        if not self.timerExped:
            self.timerExped = True
            t = Timer(1, self.updateTime)
            t.start()

        moneyIndex = 0
        while moneyIndex < len(self.map.moneyList):
            if self.map.moneyList[moneyIndex].rect.colliderect(self.player.rect):
                self.moneyGained += randint(MIN_GOLD_PER_CASH, MAX_GOLD_PER_CASH)
                del self.map.moneyList[moneyIndex]
            moneyIndex += 1
    def updateTime(self):
        self.timerExped = False
        self.time += 1

    def draw(self, screen):
        self.displayList = []
        self.displayList += self.map.wallList
        self.displayList += self.map.grassList
        self.displayList += self.map.exitList
        self.displayList += self.map.moneyList
        self.displayList += self.map.enemies
        self.displayList += self.airballs
        self.camera.draw(screen, self.player, self.displayList, self.enemyHitboxList, self.map.width, self.map.height)