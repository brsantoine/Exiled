import pygame as pg

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TAILLE_CASE = 64
TITLE = "Temp"
FPS = 30
VELOCITY = 8
ENEMY_VELOCITY = 4
ENEMY_HIGHDELAY = 60
ENEMY_LOWDELAY = 10
MAP_START_X = 6 * TAILLE_CASE
MAP_START_Y = 33 * TAILLE_CASE

MAP_BACKGROUND = pg.image.load("train.jpg")
MAP_WIDTH = MAP_BACKGROUND.get_rect().width
MAP_HEIGHT = MAP_BACKGROUND.get_rect().height

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

LOW_PRICE_AIR = 500
MID_PRICE_AIR = 5000

PRICE_HOUSE = 2000
