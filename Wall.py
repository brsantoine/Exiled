import pygame as pg
import os
from random import randint

class Wall:
    """Une classe qui correspond a un mur"""
    def __init__(self, left, top, width, height):
        """Initialise la classe Mur"""

        spriteList = []

        for sprite in os.listdir("images/wallSprites"):
            spriteList.append(sprite)

        randomSprite = randint(0, len(spriteList) - 1)
        
        self.img = pg.image.load("images/wallSprites/" + spriteList[randomSprite])

        self.rect = pg.Rect(left, top, width, height)

    def draw(self, screen, x, y):
        """Appelee a chaque tour de boucle, cette fonction affiche le mur"""

        screen.blit(self.img, (x, y))