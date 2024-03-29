from settings import *
from Enemy import *

class AirBall:
    def __init__(self,x,y,direction):
        self.rect = pg.Rect(x,y,TAILLE_CASE,TAILLE_CASE)  
        self.direction = direction # String avec Right,Left,Up,Down
        if self.direction == "Left":
            self.img = pg.image.load("images/airBall/airBallLeft.png")
            self.path = [x, x - (AIRBALL_RANGE * TAILLE_CASE)]
        if self.direction == "Right":
            self.path = [x, x + (AIRBALL_RANGE * TAILLE_CASE)]
            self.img = pg.image.load("images/airBall/airBallRight.png")
        if self.direction == "Up":
            self.path = [y, y - (AIRBALL_RANGE * TAILLE_CASE)]
            self.img = pg.image.load("images/airBall/airBallUp.png")
        if self.direction == "Down":
            self.path = [y, y + (AIRBALL_RANGE * TAILLE_CASE)]
            self.img = pg.image.load("images/airBall/airBallDown.png")
        self.vel = AIRBALL_VELOCITY
        
        

    def update(self, keys, wallList, enemyList, mapWidth, mapHeight):

        """Appelee a chaque tour de boucle, cette methode permet de mettre les coordonnees a jour"""


        dx = 0
        dy = 0

        if self.direction == "Left" and self.rect.left - self.vel > self.path[1]:
            dx -= self.vel
        elif self.direction == "Right" and self.rect.left + self.vel < self.path[1]:
            dx += self.vel
        elif self.direction == "Up" and self.rect.top - self.vel > self.path[1]:
            dy -= self.vel
        elif self.direction == "Down" and self.rect.top + self.vel < self.path[1]:
            dy += self.vel
        else:
            return False

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
            return False

        while self.rect.collidelist(wallList) == -1 and tempDy != 0:
            if tempDy > 0:
                self.rect.top += 1
                tempDy -= 1
            else:
                self.rect.top -= 1
                tempDy += 1
            
        if self.rect.collidelist(wallList) != -1:
            return False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > mapWidth - self.rect.width:
            self.rect.left = mapWidth - self.rect.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > mapHeight - self.rect.height:
            self.rect.top = mapHeight - self.rect.height

        if self.rect:
            for enemy in enemyList:
                if self.rect.colliderect(enemy.rect):
                    enemy.gotStunned()
                    return False
      
    def draw(self, win,x,y):
        """Appelee a chaque tour de boucle, cette fonction affiche le joueur"""


        win.blit(self.img, (x, y)) 
    
