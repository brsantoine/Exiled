import pygame as pg
from settings import *

class Player:
    """Une classe qui correspond au joueur du jeu"""
    def __init__(self, x, y, w, h):
        """Initialise la classe Joueur"""
        self.rect = pg.Rect(x, y, w, h)

    def update(self, keys, collisionList):
        """Appelée à chaque tour de boucle, cette méthode permet de mettre les coordonnées à jour"""

        dx = 0
        dy = 0

        if keys[pg.K_LEFT]:
            dx -= 5
        if keys[pg.K_RIGHT]:
            dx += 5
        if keys[pg.K_UP]:
            dy -= 5
        if keys[pg.K_DOWN]:
            dy += 5

        self.rect.left += dx

        if self.rect.collidelist(collisionList) != -1:
            self.rect.left -= dx
            
        self.rect.top += dy

        if self.rect.collidelist(collisionList) != -1:
            self.rect.top -= dy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > 10000:
            self.rect.left = 10000
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > 10000:
            self.rect.top = 10000

    def draw(self, screen):
        """Appelée à chaque tour de boucle, cette fonction affiche le joueur"""

        pg.draw.rect(screen, (0, 255, 0), self.rect)