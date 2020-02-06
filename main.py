import sys
import pygame as pg
from Expedition import *
from Menu import *
from Village import *
from MusicPlayer import *
from NamePrompt import *
from Score import *
from HSManager import *
from settings import *
from threading import Timer
import tkinter as tk

pg.init()
pg.display.set_caption("Breathless Town")
programIcon = pygame.image.load('images/airBottle.png')
pygame.display.set_icon(programIcon)

inGameTime = 0
gameTimer = False

def updateGameTimer():
    global inGameTime
    global gameTimer
    
    inGameTime += 1
    gameTimer = False

def updateTimers():
    global gameTimer

    if not village.timerAir:
        village.timerAir = True
        tAir = Timer(1.0, village.minusAir)
        tAir.start()
    if not village.timerPop:
        village.timerPop = True
        tPop = Timer(1.0, village.plusPopulation)
        tPop.start()
    if not village.timerGold:
        village.timerGold = True
        tGold = Timer(1.0, village.plusGold)
        tGold.start()
    if not gameTimer:
        gameTimer = True
        tGame = Timer(1.0, updateGameTimer)
        tGame.start()




namePrompt = NamePrompt()
playerName = namePrompt.getName()

hsManager = HSManager()
size = width, height = 1024, 768
screen = pg.display.set_mode(size)
fpsClock = pg.time.Clock()
village = Village(screen, 1024, 786)
musicPlayer = MusicPlayer()
menu = Menu(screen)
musicPlayer.playMenuMusic()
while True:
    fpsClock.tick(60)
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pygame.display.quit()
            sys.exit()
    
    if not menu.closed:
        menu.draw(hsManager.getStrings())
    else:
        village.setDifficulty(menu.difficulty)
        updateTimers()
        if village.inTheVillage:
            if village.win:
                hsManager.addScore(Score(1, inGameTime, playerName))
            if village.launchExpedition:
                musicPlayer.playExpeditionMusic()
                village.inTheVillage = False
                village.launchExpedition = False
                expedition = Expedition("map1", village.boots, village.airskill, menu.difficulty)
            else:

                village.draw()
        else:
            if expedition.inProgress:
                expedition.update()
                expedition.draw(screen)
            else:
                menu.drawDeath(expedition.win,expedition.time,expedition.moneyGained)
                pg.time.delay(150)
                musicPlayer.playMenuMusic()
                if expedition.win == True:
                    village.gold += expedition.moneyGained
                village.inTheVillage = True


    pg.display.update()