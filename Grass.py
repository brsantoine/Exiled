import pygame as pg
import os
from random import randint

class Grass:
    def __init__(self, left, top, width, height):

        spriteList = []

        for sprite in os.listdir("images/grassSprites"):
            spriteList.append(sprite)

        randomSprite = randint(0, len(spriteList) - 1)
        
        self.img = pg.image.load("images/grassSprites/" + spriteList[randomSprite])

        self.rect = pg.Rect(left, top, width, height)

    def draw(self, screen, x, y):

        screen.blit(self.img, (x, y))