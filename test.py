import pygame 
pygame.init()
from village import *

screenWidth = 1024
screenHeight = 768

gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First game")
clock = pygame.time.Clock()
clock.tick(15)

theVillage = village(gameDisplay, screenWidth, screenHeight)
theVillage.draw()


