import pygame
from settings import *

pygame.init()

class village(object):
    """Classe qui correspond au village et ressources ainsi qu a son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en debut de partie"""
        # Ressources
        self.gold = 12000
        self.air = 100
        self.population = 0
        self.airTank = 100
        self.populationTank = 10
        self.lose = False

        self.gameDisplay = gameDisplay
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # Interactive menu
        self.menu = True
        self.upgrades = False
        self.skills = False
        self.skills2 = False

        # Utilities
        self.village = True
        self.timerAir = False
        self.timerPop = False

    def minusAir(self):
        self.timerAir = False
        if self.air > 0:
            self.air -= 1
        else:
            self.lose = True

    def plusPopulation(self):
        if self.population < self.populationTank:
            self.population += 1
            self.timerPop = False

    ###### FUNCTIONS ######
    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textDisplay(self, msg, color, size, x, y):
        smallText = pygame.font.Font('freesansbold.ttf', size)
        textSurf, textRect = self.textObjects(msg, smallText, color)
        textRect.center = (x, y)
        self.gameDisplay.blit(textSurf, textRect)

    def button(self, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                    quit()
                elif action == "nothing":
                    pygame.time.delay(1)

                elif action == "goldToAir1":
                    if self.air < self.airTank and self.gold >= LOW_PRICE_AIR:
                        self.air += 1
                        self.gold -= LOW_PRICE_AIR
                        pygame.time.delay(150)

                elif action == "goldToAir10":
                    if self.air <= self.airTank-10 and self.gold >= MID_PRICE_AIR:
                        self.air += 10
                        self.gold -= MID_PRICE_AIR
                        pygame.time.delay(150)

                elif action == "goldToAirMax":
                    while self.air < self.airTank and self.gold >= LOW_PRICE_AIR:
                        self.gold -= LOW_PRICE_AIR
                        self.air += 1

                elif action == "house":
                    if self.gold >= PRICE_HOUSE:
                        self.gold -= PRICE_HOUSE
                        self.populationTank += 50

                elif action == "menu":
                    self.menu = True
                    self.upgrades = self.upgrades2 = self.skills  = False

                elif action == "upgrades":
                    self.menu = self.upgrades2 = self.skills = False
                    self.upgrades = True

                elif action == "upgrades2":
                    self.menu = self.upgrades = self.skills = False
                    self.upgrades2 = True

                elif action == "skills":
                    self.menu = self.upgrades = self.upgrades2 = False
                    self.skills = True

                elif action == "expedition":
                    self.village = False

        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        #######   
                
    def draw(self):
        """Affiche le menu du village"""

        self.gameDisplay.fill(white)
        
        ## Titre en haut
        self.textDisplay("Village", black, 30, (self.screenWidth/2), (self.screenHeight/15))

        ####### RESSOURCES #######
        ## Air
        self.textDisplay("Air " + str(self.air), black, 30, 60, 20)

        ## Gold
        self.textDisplay("Gold " + str(self.gold), black, 30, 200, 20)

        ## Population
        self.textDisplay("Population " + str(self.population), black, 30, 900, 20) 
        ####### 

        ####### CONVERT GOLD TO AIR #######
        x = 80 
        y = 432
        buttonWidth = 192
        buttonHeight = 32
        y2 = y+(buttonHeight+16)
        y3 = y+(buttonHeight+16)*2

        img = pygame.image.load("images/gold.png")
        self.gameDisplay.blit(img, (85, 352))

        img = pygame.image.load("images/airBottle.png")
        self.gameDisplay.blit(img, (180, 352))

        self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "goldToAir1")
        self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "goldToAir10")
        self.button(x, y3, buttonWidth, buttonHeight, green, bright_green, "goldToAirMax")

        if self.gold < LOW_PRICE_AIR:
            self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            self.button(x, y3, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            
        if self.gold < MID_PRICE_AIR or self.air > 90:
            self.button(x, y2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
        
        if self.air >= 100:
            self.button(x, y, buttonWidth, buttonHeight, red, red)
            self.button(x, y2, buttonWidth, buttonHeight, red, red)
            self.button(x, y3, buttonWidth, buttonHeight, red, red)

        self.textDisplay("500 -> 1", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2))) 
        self.textDisplay("5000 -> 10", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2))) 
        self.textDisplay("MAX", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/2))) 
        #######

        ####### SHOP UPGRADE #######
        x = 400
        y = 320
        buttonWidth = 224
        buttonHeight = 80
        y2 = y+(buttonHeight+32)
        y3 = y+(buttonHeight+32)*2

        if self.menu:
            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "upgrades")
            self.textDisplay("Town upgrades", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2)) ) 
            
            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "skills")
            self.textDisplay("Skills", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2)) )

        elif self.upgrades:
            self.button(x-48, y-64, 32, 32, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "house")
            self.textDisplay("House (-2000)", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            if self.gold < PRICE_HOUSE:
                self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100) )


            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Air purifier", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            self.button(x, y3, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Air tank", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )

            self.button(x+144, y3+buttonHeight+16, 32, 32, (200, 200, 200), (100, 100, 100), "upgrades2")

        elif self.upgrades2:
            self.button(x-32, y-32, 32, 32, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Nothing", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Nothing", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            self.button(x+16, y3+32, 32, 32, (200, 200, 200), (100, 100, 100), "upgrades")

        elif self.skills:
            self.button(x-48, y-64, 32, 32, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Courir", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Cape", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            
            
        ####### 
        ####### EXPEDITION #######
        self.button(700, 600, buttonWidth, buttonHeight, green, bright_green, "expedition")

        #######

        pygame.display.update()
        
