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
programIcon = pg.image.load('images/airBottle.png')
pg.display.set_icon(programIcon)

sound_cashing = pg.mixer.Sound('sounds/cashing.ogg')

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
        tPop = Timer(10.0, village.plusPopulation)
        tPop.start()
    if not village.timerGold:
        village.timerGold = True
        tGold = Timer(1.0, village.plusGold)
        tGold.start()
    if not gameTimer:
        gameTimer = True
        tGame = Timer(1.0, updateGameTimer)
        tGame.start()


def endVillage():
    global village
    hsManager.addScore(Score(1, inGameTime, playerName))
    village.drawDeath(inGameTime)
    village = Village(screen, 1024, 786)
    musicPlayer.playMenuMusic()
    menu.closed = False

namePrompt = NamePrompt()
playerName = namePrompt.getName()

hsManager = HSManager()
size = width, height = 1024, 768
screen = pg.display.set_mode(size)
fpsClock = pg.time.Clock()
global village
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
        inGameTime = 0
    else:
        village.setDifficulty(menu.difficulty)
        updateTimers()
        if village.inTheVillage:
            if village.win:
                endVillage()
            if village.lose:
                endVillage()
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
                if expedition.win == True:
                    sound_cashing.play()
                    village.gold += expedition.moneyGained
                pg.time.delay(150)
                musicPlayer.playMenuMusic()
                
                village.inTheVillage = True


    pg.display.update()