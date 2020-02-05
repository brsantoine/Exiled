import sys
import pygame as pg
from Player import *
from Camera import *
from Enemy import *
from Expedition import *
from Wall import *
from Money import *
from village import *
from settings import *
from threading import Timer

pg.init()

size = width, height = 1024, 768

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

village = village(screen, 1024, 786)

run = True
while True:
    fpsClock.tick(60)

    if not village.timerAir:
        village.timerAir = True
        tAir = Timer(10.0, village.minusAir)
        tAir.start()
    if not village.timerPop:
        village.timerPop = True
        tPop = Timer(1.0, village.plusPopulation)
        tPop.start()


    if village.village:
        village.draw()
        
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
    else:

        expedition = Expedition("map1")

        while expedition.inProgress:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            expedition.update()

            expedition.draw(screen)

            pg.display.update()

        if not expedition.inProgress:
            village.village = True

