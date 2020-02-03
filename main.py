import sys
import pygame as pg
from Player import *
from Camera import *

pg.init()




size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()
mapBg = pg.image.load("tester.jpg")

joueur = Player(1000, 1000, 64, 64)
camera = Camera(mapBg)

collisionList = []

while 1:
    fpsClock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    joueur.update(pg.key.get_pressed(), collisionList)

    camera.draw(screen,joueur,collisionList)

    pg.display.update()