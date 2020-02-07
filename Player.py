import pygame as pg
from AirBall import *
from settings import *

class Player:
    """Une classe qui correspond au joueur du jeu"""
    def __init__(self, playerSpawn, w, h):
        """Initialise la classe Joueur"""
        self.rect = pg.Rect(playerSpawn[0], playerSpawn[1], w, h)
        self.text = ""
        self.facing = "Down"
        self.AirBallCooldown = AIRBALL_COOLDOWN
        self.AirBallCooldownCounter = 0
        self.boots = 1
        self.hasAirSkill = False
        
        self.downSprites = [pg.image.load("images/player/playerDownStill.png"), pg.image.load("images/player/playerDownWalking1.png"), pg.image.load("images/player/playerDownStill.png"), pg.image.load("images/player/playerDownWalking2.png")]
        self.upSprites = [pg.image.load("images/player/playerUpStill.png"), pg.image.load("images/player/playerUpWalking1.png"), pg.image.load("images/player/playerUpStill.png"), pg.image.load("images/player/playerUpWalking2.png")]
        self.leftSprites = [pg.image.load("images/player/playerLeftStill.png"), pg.image.load("images/player/playerLeftWalking1.png"), pg.image.load("images/player/playerLeftStill.png"), pg.image.load("images/player/playerLeftWalking2.png")]
        self.rightSprites = [pg.image.load("images/player/playerRightStill.png"), pg.image.load("images/player/playerRightWalking1.png"), pg.image.load("images/player/playerRightStill.png"), pg.image.load("images/player/playerRightWalking2.png")]

        self.sprite = self.upSprites[0]

        self.grassSound = pg.mixer.Sound("sounds/walkingOnGrass.ogg")
        self.gustSound = pg.mixer.Sound("sounds/gust.ogg")

        self.walkingProgress = 0
        self.walking = False

    def update(self, keys, wallList, mapWidth, mapHeight):

        """Appelee a chaque tour de boucle, cette methode permet de mettre les coordonnees a jour"""

        dx = 0
        dy = 0

        if keys[pg.K_LEFT]:
            dx -= int(VELOCITY * self.boots)
        if keys[pg.K_RIGHT]:
            dx += int(VELOCITY * self.boots)
        if keys[pg.K_UP]:
            dy -= int(VELOCITY * self.boots)
        if keys[pg.K_DOWN]:
            dy += int(VELOCITY * self.boots)
        if keys[pg.K_LSHIFT]:
            dx = int(dx * self.boots)
            dx //= 2
            dy = int(dy * self.boots)
            dy //= 2

        if dy < 0:
            self.facing = "Up"
        elif dy > 0:
            self.facing = "Down"
        elif dx < 0:
            self.facing = "Left"
        elif dx > 0:
            self.facing = "Right"

        if dx != 0 or dy != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            self.walkingProgress += 1
            if self.walkingProgress >= 40:
                self.walkingProgress = 0
        else:
            self.walkingProgress = 0

        if self.walking:
            if self.facing == "Down":
                self.sprite = self.downSprites[(self.walkingProgress // 10)]
            elif self.facing == "Up":
                self.sprite = self.upSprites[(self.walkingProgress // 10)]
            elif self.facing == "Right":
                self.sprite = self.rightSprites[(self.walkingProgress // 10)]
            elif self.facing == "Left":
                self.sprite = self.leftSprites[(self.walkingProgress // 10)]
            if self.walkingProgress == 5:
                self.grassSound.play()
        else:
            if self.facing == "Down":
                self.sprite = self.downSprites[0]
            elif self.facing == "Up":
                self.sprite = self.upSprites[0]
            elif self.facing == "Right":
                self.sprite = self.rightSprites[0]
            elif self.facing == "Left":
                self.sprite = self.leftSprites[0]

        tempDx = dx
        tempDy = dy

        while self.rect.collidelist(wallList) == -1 and tempDx != 0:
            if tempDx > 0:
                self.rect.left += 1
                tempDx -= 1
            else:
                self.rect.left -= 1
                tempDx += 1
            
        if self.rect.collidelist(wallList) != -1:
            if dx > 0:
                self.rect.left -= 1
            else:
                self.rect.left += 1

        while self.rect.collidelist(wallList) == -1 and tempDy != 0:
            if tempDy > 0:
                self.rect.top += 1
                tempDy -= 1
            else:
                self.rect.top -= 1
                tempDy += 1
            
        if self.rect.collidelist(wallList) != -1:
            if dy > 0:
                self.rect.top -= 1
            else:
                self.rect.top += 1

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > mapWidth - self.rect.width:
            self.rect.left = mapWidth - self.rect.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > mapHeight - self.rect.height:
            self.rect.top = mapHeight - self.rect.height

        if self.AirBallCooldownCounter < self.AirBallCooldown:
            self.AirBallCooldownCounter += 1
        
    def AirBall(self,keys):
        if keys[pg.K_SPACE] and self.AirBallCooldownCounter >= self.AirBallCooldown and self.hasAirSkill == True:
            self.gustSound.play()
            self.AirBallCooldownCounter = 0
            return AirBall(self.rect.left ,self.rect.top ,self.facing)
        else:
            return False
    def gotBoots(self):
        self.boots = BOOTS_SPEED
    def gotAirSkill(self):
        self.hasAirSkill = True
    def draw(self, screen, x, y):
        """Appelee a chaque tour de boucle, cette fonction affiche le joueur"""

        screen.blit(self.sprite, (x, y))
