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
        self.population = 2
        self.airTank = 100
        self.populationTank = 20
        self.boots = False

        self.gameDisplay = gameDisplay
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # Interactive menu
        self.menu = True
        self.upgrades = False
        self.skills = False
        self.skills2 = False

        # Utilities
        self.inTheVillage = True
        self.timerAir = False
        self.timerPop = False
        self.timerGold = False
        self.lose = False
        self.win = False
        self.launchExpedition = False

    def minusAir(self):
        self.timerAir = False
        if self.air > 0:
            self.air -= int(self.population/5)
        else:
            self.lose = True

    def plusPopulation(self):
        self.timerPop = False
        if self.population < self.populationTank:
            self.population += 1
    
    def plusGold(self):
        self.gold += int(self.population/4)
        self.timerGold = False

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
            
            if action == "house":
                img = pygame.image.load("images/house_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "airTank":
                img = pygame.image.load("images/air_tank_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "purifier":
                img = pygame.image.load("images/air_purifier_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "upgrades":
                img = pygame.image.load("images/town_upgrades_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "skills":
                img = pygame.image.load("images/skills_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "expedition":
                img = pygame.image.load("images/expedition_sign.png")
                self.gameDisplay.blit(img, (0, 0))

            elif action == "boots":
                img = pygame.image.load("images/boots_sign.png")
                self.gameDisplay.blit(img, (0, 0))

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
                        self.populationTank += 20
                        pygame.time.delay(150)

                elif action == "airTank":
                    if self.gold >= PRICE_AIR_TANK:
                        self.gold -= PRICE_AIR_TANK
                        self.airTank += 50
                        pygame.time.delay(150)

                elif action == "purifier":
                    if self.gold >= PRICE_PURIFIER:
                        self.gold -= PRICE_PURIFIER
                        self.win = True
                elif action == "boots":
                    if self.gold >= PRICE_BOOTS:
                        self.gold -= PRICE_BOOTS
                        self.boots = True

                elif action == "menu":
                    self.menu = True
                    self.upgrades = self.upgrades2 = self.skills  = False
                    pygame.time.delay(150)

                elif action == "upgrades":
                    self.menu = self.upgrades2 = self.skills = False
                    self.upgrades = True

                    pygame.time.delay(150)

                elif action == "skills":
                    self.menu = self.upgrades = self.upgrades2 = False
                    self.skills = True
                    pygame.time.delay(150)

                elif action == "expedition":
                    self.launchExpedition = True
                    pygame.time.delay(150)
                
                

        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        #######   
                
    def draw(self):
        """Affiche le menu du village"""

        img = pygame.image.load("images/background_image.png")
        self.gameDisplay.blit(img, (0, 0))

        ####### RESSOURCES #######
        img = pygame.image.load("images/resources.png")
        self.gameDisplay.blit(img, (0, 0))
        ## Air
        self.textDisplay("Air " + str(self.air) + " / " + str(self.airTank), black, 30, 100, 20)

        ## Gold
        self.textDisplay("Gold " + str(self.gold), black, 30, 85, 55)

        ## Population
        img = pygame.image.load("images/population.png")
        self.gameDisplay.blit(img, (0, 0))
        self.textDisplay("Population " + str(self.population) + " / " + str(self.populationTank), black, 30, 870, 20) 
        
        ####### 

        ####### GENERAL ####### 
        img = pygame.image.load("images/town_name.png")
        self.gameDisplay.blit(img, (0, 0))
        #######

        ####### CONVERT GOLD TO AIR #######
        x = 96 
        y = 430
        buttonWidth = 192
        buttonHeight = 32
        y2 = y+(buttonHeight+16)
        y3 = y+(buttonHeight+16)*2

        #img = pygame.image.load("images/gold.png")
        #self.gameDisplay.blit(img, (85, 352))

        #img = pygame.image.load("images/airBottle.png")
        #self.gameDisplay.blit(img, (180, 352))

        self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "goldToAir1")
        self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "goldToAir10")
        self.button(x, y3, buttonWidth, buttonHeight, green, bright_green, "goldToAirMax")

        if self.gold < LOW_PRICE_AIR:
            self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            self.button(x, y3, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            
        if self.gold < MID_PRICE_AIR or self.air > self.airTank - 10:
            self.button(x, y2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
        
        if self.air >= self.airTank:
            self.button(x, y, buttonWidth, buttonHeight, red, red)
            self.button(x, y2, buttonWidth, buttonHeight, red, red)
            self.button(x, y3, buttonWidth, buttonHeight, red, red)

        img = pygame.image.load("images/air_converter.png")
        self.gameDisplay.blit(img, (0, 0))

        self.textDisplay("500 -> 1", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2))) 
        self.textDisplay("5000 -> 10", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2))) 
        self.textDisplay("MAX", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/2)))
        #######

        ####### SHOP UPGRADE #######
        x = 416
        y = 320
        buttonWidth = 224
        buttonHeight = 80
        y2 = y+(buttonHeight+32)
        y3 = y+(buttonHeight+32)*2

        if self.menu:
            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "upgrades")
            self.textDisplay("Town upgrades", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2)) ) 
            
            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "skills")
            self.textDisplay("Skills", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2)) )

            img = pygame.image.load("images/town_hall.png")
            self.gameDisplay.blit(img, (0, 0))

        elif self.upgrades:
            self.button(388, 222, 61, 66, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "house")
            if self.gold < PRICE_HOUSE:
                self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100) )
            self.textDisplay("House (-2000)", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y3, buttonWidth, buttonHeight, green, bright_green, "purifier")
            if self.gold < PRICE_PURIFIER:
                self.button(x, y3, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100) )
            self.textDisplay("Air purifier", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "airTank")
            if self.gold < PRICE_AIR_TANK:
                self.button(x, y2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100) )
            self.textDisplay("Air tank", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )

            img = pygame.image.load("images/town_upgrades.png")
            self.gameDisplay.blit(img, (0, 0))

        elif self.skills:
            self.button(388, 222, 61, 66, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "boots")
            self.textDisplay("Courir", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            #self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
            #self.textDisplay("Cape", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            img = pygame.image.load("images/skills.png")
            self.gameDisplay.blit(img, (0, 0))
            
            
        ####### 

        ####### EXPEDITION #######
        x = 731
        y = 469
        buttonWidth = 990-731
        buttonHeight = 547-469
        self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "expedition")
        img = pygame.image.load("images/expedition.png")
        self.gameDisplay.blit(img, (0, 0))
        #######

        pygame.display.update()
        
