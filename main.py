import sys
import pygame as pg
from Player import *
from Camera import *
from Wall import *
from settings import *

pg.init()

size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

joueur = Player(1000, 1000, 64, 64)
mur1 = Wall(128, 128, 256, 64)
mur2 = Wall(128, 192, 64, 256)
camera = Camera()

collisionList = [mur1, mur2]

while 1:
    fpsClock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    joueur.update(pg.key.get_pressed(), collisionList)

    camera.draw(screen, joueur, collisionList)

    pg.display.update()