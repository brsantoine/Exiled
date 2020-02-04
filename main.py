import sys
import pygame as pg
from Player import *
from Camera import *
from Wall import *
from Map import *
from settings import *

pg.init()

size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

player = Player(1000, 1000, 64, 64)
camera = Camera()

map1 = Map("map1", None)

collisionList = []
collisionList += map1.wallList

while 1:
    fpsClock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    player.update(pg.key.get_pressed(), collisionList)

    camera.draw(screen, player, collisionList)

    pg.display.update()