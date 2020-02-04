import pygame as pg
from Wall import *
from settings import *

class Map:
    """Une classe qui correspond à un building"""
    def __init__(self, hitboxFile, img):
        """Initialise la classe Building"""

        self.img = img

        self.wallList = []

        file = open("maps/" + hitboxFile + ".map")

        notDone = True

        x = 0
        y = 0

        while notDone:

            line = file.readline()

            if not line:
                notDone = False
            else:
                for lettre in line:
                    if lettre == 'X':
                        self.wallList.append(Wall(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    x += 1
                
            y += 1
            x = 0

        file.close()

    def draw(self, screen, x, y):
        """Appelée à chaque tour de boucle, cette fonction affiche le building"""

        screen.blit(self.img, (x, y))