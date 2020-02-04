import pygame as pg
from settings import *

class Player:
    """Une classe qui correspond au joueur du jeu"""
    def __init__(self, x, y, w, h):
        """Initialise la classe Joueur"""
        self.rect = pg.Rect(x, y, w, h)

    def update(self, keys, wallList,enemyHitboxList):
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

        self.rect.left += dx

        if self.rect.collidelist(wallList) != -1:
            self.rect.left -= dx
            
        self.rect.top += dy

        if self.rect.collidelist(wallList) != -1:
            self.rect.top -= dy

        if self.rect.left <= TAILLE_CASE:
            self.rect.left = TAILLE_CASE
        if self.rect.left > MAP_WIDTH - TAILLE_CASE - self.rect.width:
            self.rect.left = MAP_WIDTH - TAILLE_CASE - self.rect.width
        if self.rect.top <= TAILLE_CASE:
            self.rect.top = TAILLE_CASE
        if self.rect.top > MAP_HEIGHT - TAILLE_CASE - self.rect.height:
            self.rect.top = MAP_HEIGHT - TAILLE_CASE - self.rect.height

        safe = True       
        if self.rect.collidelist(enemyHitboxList) != -1:
            safe = False
        return safe

    def draw(self, screen,x,y):
        """Appelee a chaque tour de boucle, cette fonction affiche le joueur"""

        pg.draw.rect(screen, (255, 150, 255), pg.Rect(x, y , self.rect.width, self.rect.height))