import pygame as pg
from settings import *

class Enemy:
    def __init__(self,x,y,end,direction,delay,stand_still): # x,y = positions initiales ; end = position finale
        self.rect = pg.Rect(x,y,TAILLE_CASE,TAILLE_CASE)  
        self.direction = direction # 0 pour horizontal 1 pour vertical
        self.end = end # Pixel fin
        if self.direction == 0 :
            self.path = [x, x +end]
            self.side = "Right"
        else:
            self.path = [y,y + end]
            self.side = "Down"
        self.walkCount = 0
        self.vel = ENEMY_VELOCITY
        self.delay = delay # Nombre de boucles avant de tourner
        self.delayCounter = 0
        self.stand_still = stand_still # 0 pour faux , 1 pour gauche , 2 pour up, 3 pour droite, 4 pour down
        if self.stand_still > 0:
            if self.stand_still == 1:
                self.side = "Left"
            elif self.stand_still == 2:
                self.side = "Up"
            elif self.stand_still == 3:
                self.side = "Right"
            else :
                self.side = "Down" 

        self.img = pg.image.load("images/guard.png")
        self.imgStunned = pg.image.load("images/airBottle.png")
        self.stunned = False
        self.stunnedCounter = 0

    def update(self):
        if self.stand_still == 0 and self.stunned == False:
            if self.direction == 0:
                temp = self.rect.left
            else:
                temp = self.rect.top

            
            if self.vel > 0:
                if temp + self.vel < self.path[1] :
                    temp += self.vel
                elif self.delay == self.delayCounter:
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    self.delayCounter = 0
                    if self.direction == 0 :
                        self.side = "Left"
                    else:
                        self.side = "Up"
                else :
                    self.delayCounter += 1
            else:
                if temp - self.vel > self.path[0] :
                    temp += self.vel
                elif self.delay == self.delayCounter :
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    self.delayCounter = 0
                    if self.direction == 0 :
                        self.side = "Right"
                    else:
                        self.side = "Down"
                else :
                    self.delayCounter += 1

            if self.direction == 0:
                self.rect.left = temp
            else:
                self.rect.top = temp
        elif self.stunned == True:
            self.stunnedCounter += 1
            if self.stunnedCounter >= ENEMY_STUNNEDTIME:
                self.stunnedCounter = 0
                self.stunned = False

    def getHitbox(self) :
        hitbox = []
        if self.stunned == False:
            if self.side == "Left" :
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 3),self.rect.top , TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top + (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.side == "Right" :
                hitbox.append(pg.Rect(self.rect.left + (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left ,self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top , TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left ,self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left + (TAILLE_CASE * 1),self.rect.top + (TAILLE_CASE * 2), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.side == "Up" :
                hitbox.append(pg.Rect(self.rect.left,self.rect.top - (TAILLE_CASE * 3), TAILLE_CASE * 1,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top - (TAILLE_CASE * 2), TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 2),self.rect.top - (TAILLE_CASE * 1), TAILLE_CASE * 5,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left - (TAILLE_CASE * 1),self.rect.top, TAILLE_CASE * 3,TAILLE_CASE * 1))
                hitbox.append(pg.Rect(self.rect.left,self.rect.top + (TAILLE_CASE * 1), TAILLE_CASE * 1,TAILLE_CASE * 1))
            elif self.side == "Down" :
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
            screen.blit(self.img, (x, y))
    




