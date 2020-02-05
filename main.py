import sys
import pygame as pg
from Player import *
from Camera import *
from Enemy import *
from Wall import *
from Map import *
from village import *
from settings import *
from threading import Timer

pg.init()

size = width, height = 1024, 768
dx = 0
dy = 0
black = 0, 0, 0

screen = pg.display.set_mode(size)

fpsClock = pg.time.Clock()

joueur = Player(MAP_START_X, MAP_START_Y, 64, 64)
enemies = []
enemies.append(Enemy((6.5 * TAILLE_CASE),(1.5 * TAILLE_CASE),(6 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
enemies.append(Enemy((9 * TAILLE_CASE),(5 * TAILLE_CASE),(24 * TAILLE_CASE),0,ENEMY_LOWDELAY,0))
enemies.append(Enemy((19 * TAILLE_CASE),(2 * TAILLE_CASE),(4 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
enemies.append(Enemy((30 * TAILLE_CASE),(2 * TAILLE_CASE),(6 * TAILLE_CASE),1,ENEMY_LOWDELAY,0))
enemies.append(Enemy((44 * TAILLE_CASE),(7 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,1))
enemies.append(Enemy((44 * TAILLE_CASE),(18 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,2))
enemies.append(Enemy((38 * TAILLE_CASE),(15 * TAILLE_CASE),(5 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))
enemies.append(Enemy((21 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,4))
enemies.append(Enemy((24 * TAILLE_CASE),(11 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,4))
enemies.append(Enemy((7 * TAILLE_CASE),(16 * TAILLE_CASE),(6 * TAILLE_CASE),0,ENEMY_HIGHDELAY,0))
enemies.append(Enemy((12 * TAILLE_CASE),(22 * TAILLE_CASE),(14 * TAILLE_CASE),0,ENEMY_LOWDELAY,0))
enemies.append(Enemy((1.5 * TAILLE_CASE),(18.5 * TAILLE_CASE),(8 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))
enemies.append(Enemy((29 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,3))
enemies.append(Enemy((23 * TAILLE_CASE),(30 * TAILLE_CASE),0,1,ENEMY_LOWDELAY,2))
enemies.append(Enemy((40 * TAILLE_CASE),(31 * TAILLE_CASE),(4 * TAILLE_CASE),0,ENEMY_HIGHDELAY,0))
enemies.append(Enemy((32 * TAILLE_CASE),(19 * TAILLE_CASE),(2 * TAILLE_CASE),1,ENEMY_HIGHDELAY,0))


startRect = pg.Rect(MAP_START_X - TAILLE_CASE,MAP_START_Y + (2 * TAILLE_CASE),3 * TAILLE_CASE,1 * TAILLE_CASE)
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
        expeditionClear = joueur.expeditionClear(startRect)

        camera.draw(screen, joueur, collisionList, enemyHitboxList)
        


        enemyHitboxList = []
        pg.display.update()

        if not alive:
            village.village = True
            joueur.rect.left = MAP_START_X
            joueur.rect.top = MAP_START_Y
        if expeditionClear:
            village.village = True
            joueur.rect.left = MAP_START_X
            joueur.rect.top = MAP_START_Y
            # Draw the transparent rect
            see_through = pg.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
            see_through.fill((140, 140, 140, 200))
            screen.blit(see_through, (32,32))
            # Attend que l'utilisateur clique sur le bouton continuer
            

             
                        
