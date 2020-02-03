import sys
import pygame as pg
from Player import *

pg.init()

size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

joueur = Player(50, 50, 32, 64)

collisionList = []

while 1:
    fpsClock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    joueur.update(pg.key.get_pressed(), collisionList)

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, 10000, 10000))
    joueur.draw(screen)

    pg.display.update()