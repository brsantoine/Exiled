import pygame as pg
from settings import *

class Player:
    """Une classe qui correspond au joueur du jeu"""
    def __init__(self, playerSpawn, w, h):
        """Initialise la classe Joueur"""
        self.rect = pg.Rect(playerSpawn[0], playerSpawn[1], w, h)
        self.text = ""
        self.img = pg.image.load("images/player.png")

    def update(self, keys, wallList):

        """Appelee a chaque tour de boucle, cette methode permet de mettre les coordonnees a jour"""

        dx = 0
        dy = 0

        if keys[pg.K_LEFT]:
            dx -= VELOCITY
        if keys[pg.K_RIGHT]:
            dx += VELOCITY
        if keys[pg.K_UP]:
            dy -= VELOCITY
        if keys[pg.K_DOWN]:
            dy += VELOCITY
        if keys[pg.K_LSHIFT]:
            dx //= 2
            dy //= 2

        tempDx = dx
        tempDy = dy

        while self.rect.collidelist(wallList) == -1 and tempDx != 0:
            if tempDx > 0:
                self.rect.left += 1
                tempDx -= 1
            else:
                self.rect.left -= 1
                tempDx += 1
            
        if self.rect.collidelist(wallList) != -1:
            if dx > 0:
                self.rect.left -= 1
            else:
                self.rect.left += 1

        while self.rect.collidelist(wallList) == -1 and tempDy != 0:
            if tempDy > 0:
                self.rect.top += 1
                tempDy -= 1
            else:
                self.rect.top -= 1
                tempDy += 1
            
        if self.rect.collidelist(wallList) != -1:
            if dy > 0:
                self.rect.top -= 1
            else:
                self.rect.top += 1

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > MAP_WIDTH - self.rect.width:
            self.rect.left = MAP_WIDTH - self.rect.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > MAP_HEIGHT - self.rect.height:
            self.rect.top = MAP_HEIGHT - self.rect.height

        font = pg.font.Font('freesansbold.ttf', 32)
        self.text = font.render("X : " + str(self.rect.left) + " ; Y : " + str(self.rect.top), True, (255, 255, 255), (0, 0, 0))
        
      
    def draw(self, screen, x, y):
        """Appelee a chaque tour de boucle, cette fonction affiche le joueur"""

        textRect = self.text.get_rect()

        screen.blit(self.text, textRect)

        screen.blit(self.img, (x, y))