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
def textObjects( text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def textDisplay( msg, color, size, x, y):
    smallText = pygame.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjects(msg, smallText, color)
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)

def button(x, y, w, h, ic, ac, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(screen, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pg.quit()
                    quit()
                elif action == "exitExpedition":
                    # village.gold += expedition.gold()
                    return True
                elif action == "loseExpedition":
                    # village.gold += expedition.gold()
                    return True
        else:
            pg.draw.rect(screen, ic, (x, y, w, h))
            return False

        #######   



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
while run: 
    #village.lose or village.win
    # if ^ run = f alse
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

            Clicked = False
            see_through = pg.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
            see_through.fill((140, 140, 140, 200))
            screen.blit(see_through, (32,32))
            # Attend que l'utilisateur clique sur le bouton continuer
            while not Clicked:
                Clicked = button((SCREEN_WIDTH//2) - 125,(SCREEN_HEIGHT//2) + 100,250,70,green,bright_green,"loseExpedition")
                textDisplay("Return to town",black,20,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//2) + 100 + 35)
                pg.display.update()
                for event in pg.event.get():
                    if event.type == pg.QUIT: sys.exit()

        if expeditionClear:
            village.village = True
            joueur.rect.left = MAP_START_X
            joueur.rect.top = MAP_START_Y
            # Draw the transparent rect
            Clicked = False
            see_through = pg.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
            see_through.fill((140, 140, 140, 200))
            screen.blit(see_through, (32,32))
            # Attend que l'utilisateur clique sur le bouton continuer
            while not Clicked:
                Clicked = button((SCREEN_WIDTH//2) - 125,(SCREEN_HEIGHT//2) + 100,250,70,green,bright_green,"exitExpedition")
                textDisplay("Return to town",black,20,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//2) + 100 + 35)
                for event in pg.event.get():
                    if event.type == pg.QUIT: sys.exit()
                pg.display.update()




             
                        
