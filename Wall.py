import pygame as pg

class Wall:
    """Une classe qui correspond à un mur"""
    def __init__(self, left, top, width, height):
        """Initialise la classe Mur"""

        self.rect = pg.Rect(left, top, width, height)

    def draw(self, screen, x, y):
        """Appelée à chaque tour de boucle, cette fonction affiche le mur"""

        BLACK = (0, 0, 0)

        pg.draw.rect(screen, BLACK, pg.Rect(x, y, self.rect.width, self.rect.height))