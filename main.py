import sys
import pygame as pg
from Expedition import *
from Menu import *
from Village import *
from settings import *
from threading import Timer

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

size = width, height = 1024, 768

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

village = Village(screen, 1024, 786)

startRect = pg.Rect(MAP_START_X - TAILLE_CASE, MAP_START_Y + (2 * TAILLE_CASE), 3 * TAILLE_CASE, TAILLE_CASE)

enemyHitboxList = []
running = True

menu = Menu(screen)

while running:
    fpsClock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    if not menu.closed:
        menu.draw()
    else:
        updateTimers()
        if village.inTheVillage:
            if village.launchExpedition:
                village.inTheVillage = False
                village.launchExpedition = False
                expedition = Expedition("map1")
            else:
                village.draw()
        else:
            if expedition.inProgress:
                expedition.update()
                expedition.draw(screen)
            else:
                menu.drawDeath()
                village.gold += expedition.moneyGained
                village.inTheVillage = True

    pg.display.update()