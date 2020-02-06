import pygame as pg
from settings import *

class Enemy:
    def __init__(self,x,y,end,direction,delay,stand_still): # x,y = positions initiales ; end = position finale
        self.rect = pg.Rect(x,y,TAILLE_CASE,TAILLE_CASE)  
        self.direction = direction # 0 pour horizontal 1 pour vertical
        self.end = end # Pixel fin
        if self.direction == 0 :
            self.path = [x, x +end]
            self.facing = "Right"
        else:
            self.path = [y,y + end]
            self.facing = "Down"
        self.walkCount = 0
        self.vel = ENEMY_VELOCITY
        self.delay = delay # Nombre de boucles avant de tourner
        self.delayCounter = 0
        self.stand_still = stand_still # 0 pour faux , 1 pour gauche , 2 pour up, 3 pour droite, 4 pour down
        if self.stand_still > 0:
            if self.stand_still == 1:
                self.facing = "Left"
            elif self.stand_still == 2:
                self.facing = "Up"
            elif self.stand_still == 3:
                self.facing = "Right"
            else :
                self.facing = "Down" 

        self.imgStunned = pg.image.load("images/airBottle.png")
        self.stunned = False
        self.stunnedCounter = 0

        self.downSprites = [pg.image.load("images/guard/guardDownStill.png"), pg.image.load("images/guard/guardDownWalking1.png"), pg.image.load("images/guard/guardDownStill.png"), pg.image.load("images/guard/guardDownWalking2.png")]
        self.upSprites = [pg.image.load("images/guard/guardUpStill.png"), pg.image.load("images/guard/guardUpWalking1.png"), pg.image.load("images/guard/guardUpStill.png"), pg.image.load("images/guard/guardUpWalking2.png")]
        self.leftSprites = [pg.image.load("images/guard/guardLeftStill.png"), pg.image.load("images/guard/guardLeftWalking1.png"), pg.image.load("images/guard/guardLeftStill.png"), pg.image.load("images/guard/guardLeftWalking2.png")]
        self.rightSprites = [pg.image.load("images/guard/guardRightStill.png"), pg.image.load("images/guard/guardRightWalking1.png"), pg.image.load("images/guard/guardRightStill.png"), pg.image.load("images/guard/guardRightWalking2.png")]

        self.sprite = self.upSprites[0]

        self.walkingProgress = 0
        self.walking = False

    def update(self):
        if self.stand_still == 0 and self.stunned == False:
            if self.direction == 0:
                temp = self.rect.left
            else:
                temp = self.rect.top

            
            if self.vel > 0:
                if temp + self.vel < self.path[1] :
                    self.walking = True
                    temp += self.vel
                elif self.delay == self.delayCounter:
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    self.delayCounter = 0
                    if self.direction == 0 :
                        self.facing = "Left"
                    else:
                        self.facing = "Up"
                else :
                    self.walking = False
                    self.delayCounter += 1
            else:
                if temp - self.vel > self.path[0] :
                    self.walking = True
                    temp += self.vel
                elif self.delay == self.delayCounter :
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    self.delayCounter = 0
                    if self.direction == 0 :
                        self.facing = "Right"
                    else:
                        self.facing = "Down"
                else :
                    self.delayCounter += 1
                    self.walking = False

            if self.direction == 0:
                self.rect.left = temp
            else:
                self.rect.top = temp
        elif self.stunned == True:
            self.stunnedCounter += 1
            if self.stunnedCounter >= ENEMY_STUNNEDTIME:
                self.stunnedCounter = 0
                self.stunned = False

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
        else:
            if self.facing == "Down":
                self.sprite = self.downSprites[0]
            elif self.facing == "Up":
                self.sprite = self.upSprites[0]
            elif self.facing == "Right":
                self.sprite = self.rightSprites[0]
            elif self.facing == "Left":
                self.sprite = self.leftSprites[0]

    def getHitbox(self) :
        hitbox = []
        if self.stunned == False:
            if self.facing == "Left" :
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 3),self.rect.top , TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top + (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.facing == "Right" :
                hitbox.append(pg.Rect(self.rect.left + (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left ,self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top , TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left ,self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left + (TAILLE_CASE * 1),self.rect.top + (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.facing == "Up" :
                hitbox.append(pg.Rect(self.rect.left,self.rect.top - (TAILLE_CASE * 3), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top, TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left,self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.facing == "Down" :
                hitbox.append(pg.Rect(self.rect.left,self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top , TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top + (TAILLE_CASE * 2), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left,self.rect.top + (TAILLE_CASE * 3), TAILLE_CASE * 1,TAILLE_CASE * 1))
       
        return hitbox

    def gotStunned(self):
        self.stunned = True
        self.stunnedCounter = 0

    def draw(self,screen,x,y):
        if self.stunned == True:
            screen.blit(self.imgStunned, (x, y))
        else:
            screen.blit(self.sprite, (x, y))
    




