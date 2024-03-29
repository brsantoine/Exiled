import pygame as pg

class Money:
    """Une classe qui correspond a un Money"""
    def __init__(self, left, top, width, height):
        """Initialise la classe Money"""

        self.rect = pg.Rect(left, top, width, height)
        self.img = pg.image.load("images/money.png")

    def draw(self, screen, x, y):
        """Appelee a chaque tour de boucle, cette fonction affiche la piece"""

        GREEN = (0, 255, 0)

        screen.blit(self.img, (x, y))