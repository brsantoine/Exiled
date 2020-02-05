import sys
import pygame as pg
from Player import *
from Camera import *
from Enemy import *
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

joueur = Player(1000, 1000, 64, 64)
enemies = []
enemies.append(Enemy((6.5 * TAILLE_CASE),(1.5 * TAILLE_CASE),(6 * TAILLE_CASE),1,5,0))
enemies.append(Enemy((9 * TAILLE_CASE),(5 * TAILLE_CASE),(24 * TAILLE_CASE),0,5,0))
enemies.append(Enemy((19 * TAILLE_CASE),(2 * TAILLE_CASE),(4 * TAILLE_CASE),1,5,0))
enemies.append(Enemy((30 * TAILLE_CASE),(2 * TAILLE_CASE),(6 * TAILLE_CASE),1,5,0))
enemies.append(Enemy((44 * TAILLE_CASE),(7 * TAILLE_CASE),0,1,5,1))
enemies.append(Enemy((44 * TAILLE_CASE),(18 * TAILLE_CASE),0,1,5,2))
enemies.append(Enemy((38 * TAILLE_CASE),(15 * TAILLE_CASE),(5 * TAILLE_CASE),1,30,0))
enemies.append(Enemy((21 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,5,4))
enemies.append(Enemy((24 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,5,4))
enemies.append(Enemy((7 * TAILLE_CASE),(16 * TAILLE_CASE),(6 * TAILLE_CASE),0,30,0))
enemies.append(Enemy((12 * TAILLE_CASE),(22 * TAILLE_CASE),(14 * TAILLE_CASE),0,5,0))
enemies.append(Enemy((1.5 * TAILLE_CASE),(18.5 * TAILLE_CASE),(8 * TAILLE_CASE),1,30,0))
enemies.append(Enemy((29 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,1,3))
enemies.append(Enemy((23 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,1,2))
enemies.append(Enemy((44 * TAILLE_CASE),(31 * TAILLE_CASE),0,1,1,1))
enemies.append(Enemy((32 * TAILLE_CASE),(19 * TAILLE_CASE),(2 * TAILLE_CASE),1,30,0))



camera = Camera()

map1 = Map("map1", None)

collisionList = []
collisionList += map1.wallList
collisionList += enemies 

enemyHitboxList = []

run = True
while run:
    fpsClock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    for enemy in enemies :
        enemy.update()
        for hitbox in enemy.getHitbox() :
            enemyHitboxList.append(hitbox)

    run = joueur.update(pg.key.get_pressed(), collisionList,enemyHitboxList)

    camera.draw(screen, joueur, collisionList, enemyHitboxList)

    enemyHitboxList = []


    pg.display.update()
