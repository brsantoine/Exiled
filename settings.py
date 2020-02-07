import pygame as pg

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TAILLE_CASE = 64
TITLE = "Breathless Town"
FPS = 30
VELOCITY = 8
ENEMY_VELOCITY = 4
ENEMY_HIGHDELAY = 60
ENEMY_LOWDELAY = 10
ENEMY_STUNNEDTIME = 120
AIRBALL_VELOCITY = 15
AIRBALL_COOLDOWN = 80
AIRBALL_RANGE = 7 # En cases
MAP_START_X = 6 * TAILLE_CASE
MAP_START_Y = 33 * TAILLE_CASE
BOOTS_SPEED = 1.3

MIN_GOLD_PER_CASH = 60
MAX_GOLD_PER_CASH = 80

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

#Village
STARTING_GOLD = 50000.0

LOW_PRICE_AIR = 50
MID_PRICE_AIR = 400
HIGH_PRICE_AIR = 1500

PRICE_HOUSE = 200
HOUSE_INCREASE = 50
HOUSE_VALUE = 5
PRICE_AIR_TANK = 500
AIR_TANK_INCREASE = 250
AIR_TANK_VALUE = 20
PRICE_PURIFIER = 5000

PRICE_BOOTS = 1000
PRICE_AIR_SKILL = 2000
