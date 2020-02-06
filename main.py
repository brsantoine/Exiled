import sys
import pygame as pg
from Expedition import *
from Menu import *
from Village import *
from MusicPlayer import *
from NamePrompt import *
from settings import *
from threading import Timer
import tkinter as tk

pg.init()

def updateTimers():
    if not village.timerAir:
        village.timerAir = True
        tAir = Timer(10.0, village.minusAir)
        tAir.start()
    if not village.timerPop:
        village.timerPop = True
        tPop = Timer(1.0, village.plusPopulation)
        tPop.start()
    if not village.timerGold:
        village.timerGold = True
        tGold = Timer(1.0, village.plusGold)
        tGold.start()


namePrompt = NamePrompt()
playerName = namePrompt.getName()

print(playerName)

size = width, height = 1024, 768
screen = pg.display.set_mode(size)
fpsClock = pg.time.Clock()
village = Village(screen, 1024, 786)
musicPlayer = MusicPlayer()
menu = Menu(screen)


while True:
    fpsClock.tick(60)
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pygame.display.quit()
            sys.exit()
    
    if not menu.closed:
        menu.draw()
    else:
        updateTimers()
        if village.inTheVillage:
            if village.launchExpedition:
                musicPlayer.playExpeditionMusic()
                village.inTheVillage = False
                village.launchExpedition = False
                expedition = Expedition("map1", village.boots, village.airskill)
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
                village.gold += expedition.moneyGained
                village.inTheVillage = True


    pg.display.update()