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
    smallText = pg.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjects(msg, smallText, color)
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)

def button(x, y, w, h, ic, ac, action=None):
        global mainMenu
        global difficultyMenu
        global creditsScreen
        global playing
        global helpMenu
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(screen, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "quit":
                    sys.exit()
                elif action == "exitExpedition":
                    # village.gold += expedition.gold()
                    return True
                    pygame.time.delay(150)
                elif action == "loseExpedition":
                    # village.gold += expedition.gold()
                    return True
                    pygame.time.delay(150)
                elif action == "Play":
                    mainMenu = False
                    difficultyMenu = True
                    pygame.time.delay(150)
                elif action == "Help":
                    mainMenu = False
                    helpMenu = True
                    pygame.time.delay(150)
                elif action == "Credits":
                    mainMenu = False
                    creditsScreen = True
                    pygame.time.delay(150)
                elif action == "easy":
                    difficultyMenu = False
                    playing = True
                    pygame.time.delay(150)
                elif action == "normal":
                    difficultyMenu = False
                    playing = True
                    pygame.time.delay(150)
                elif action == "hard":
                    difficultyMenu = False
                    playing = True
                    pygame.time.delay(150)

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
running = True

x = 400
y = 220
buttonWidth = 224
buttonHeight = 80
y2 = y+(buttonHeight+32)
y3 = y+(buttonHeight+32)*2
y4 = y+(buttonHeight+32)*3

global mainMenu
global difficultyMenu
global creditsScreen
global playing
global helpMenu
mainMenu = True
difficultyMenu = False
creditsScreen = False
playing = False
helpMenu = False

while running:
   
    fpsClock.tick(60)
    for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

    screen.fill(white)
    if mainMenu:
        textDisplay("Menu", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
        # Button play
        button(x, y, buttonWidth, buttonHeight, green, bright_green, "Play")
        textDisplay("Play", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )
        # Button help
        button(x, y2, buttonWidth, buttonHeight, green, bright_green,"Help")
        textDisplay("Help", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )
        # Button Credits
        button(x, y3, buttonWidth, buttonHeight, green, bright_green,"Credits")
        textDisplay("Credits", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )
        # Button quit
        button(x, y4, buttonWidth, buttonHeight, green, bright_green,"quit")
        textDisplay("Quit", black, 20, (x+(buttonWidth/2)), (y4+(buttonHeight/3)) )
    elif helpMenu:
        pass
    elif creditsScreen:
        pass
    elif difficultyMenu:
        textDisplay("Difficulty", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
        # Button easy
        button(x, y, buttonWidth, buttonHeight, green, bright_green, "easy")
        textDisplay("Easy", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )
        # Button normal
        button(x, y2, buttonWidth, buttonHeight, green, bright_green,"normal")
        textDisplay("Normal", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )
        # Button hard
        button(x, y3, buttonWidth, buttonHeight, green, bright_green,"hard")
        textDisplay("Hard", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )
    elif playing:
        playing = False
        mainMenu = True
       
    pg.display.update()
    




             
                        
while playing: 
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

