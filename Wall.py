import pygame as pg

class Wall:
    """Une classe qui correspond a un mur"""
    def __init__(self, left, top, width, height):
        """Initialise la classe Mur"""

        self.rect = pg.Rect(left, top, width, height)
        self.img = pg.image.load("images/wall.png")

    def draw(self, screen, x, y):
        """Appelee a chaque tour de boucle, cette fonction affiche le mur"""

        screen.blit(self.img, (x, y))