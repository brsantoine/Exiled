import sys
import pygame as pg
from Player import *
from Camera import *
from Enemy import *
from Wall import *
from Map import *
from village import *
from settings import *

pg.init()

size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

joueur = Player(384, 2240, 64, 64)
enemies = []
enemies.append(Enemy((6.5 * TAILLE_CASE),(1.5 * TAILLE_CASE),(6 * TAILLE_CASE),1,5,0))
enemies.append(Enemy((9 * TAILLE_CASE),(5 * TAILLE_CASE),(25 * TAILLE_CASE),0,5,0))
enemies.append(Enemy((19 * TAILLE_CASE),(2 * TAILLE_CASE),(5 * TAILLE_CASE),1,5,0))
enemies.append(Enemy((30 * TAILLE_CASE),(2 * TAILLE_CASE),(7 * TAILLE_CASE),1,5,0))
camera = Camera()

map1 = Map("map1", None)

collisionList = []
collisionList += map1.wallList
collisionList += enemies

village = village(screen, 1024, 786)

enemyHitboxList = []

run = True
while True:
    fpsClock.tick(60)

    if village.village:
        village.draw()
    else:

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        for enemy in enemies :
            enemy.update()
            for hitbox in enemy.getHitbox() :
                enemyHitboxList.append(hitbox)

        alive = joueur.update(pg.key.get_pressed(), collisionList,enemyHitboxList)

        camera.draw(screen, joueur, collisionList, enemyHitboxList)

        enemyHitboxList = []


        pg.display.update()

        if not alive:
            village.village = True
            joueur.rect.left = 384
            joueur.rect.top = 2240
