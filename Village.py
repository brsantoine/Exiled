import pygame
from settings import *

pygame.init()

class Village(object):
    """Classe qui correspond au village et ressources ainsi qu a son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en debut de partie"""
        # Ressources
        self.gold = 12000
        self.air = 100
        self.population = 2
        self.airTank = 100
        self.populationTank = 20

        # Skills
        self.boots = False
        self.airskill = False

        # Screen
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

        # Images
        self.image_background = pygame.image.load("images/background_image.png").convert_alpha()
        self.image_ressources = pygame.image.load("images/resources.png").convert_alpha()
        self.image_house_sign = pygame.image.load("images/house_sign.png").convert_alpha()
        self.image_air_tank_sign = pygame.image.load("images/air_tank_sign.png").convert_alpha()
        self.image_population = pygame.image.load("images/population.png").convert_alpha()
        self.image_town_name = pygame.image.load("images/town_name.png").convert_alpha()
        self.image_air_converter = pygame.image.load("images/air_converter.png").convert_alpha()
        self.image_town_upgrades = pygame.image.load("images/town_upgrades.png").convert_alpha()
        self.image_town_hall = pygame.image.load("images/town_hall.png").convert_alpha()
        self.image_skills = pygame.image.load("images/skills.png").convert_alpha()
        self.image_expedition = pygame.image.load("images/expedition.png").convert_alpha()
        self.image_air_purifier_sign = pygame.image.load("images/air_purifier_sign.png").convert_alpha()
        self.image_town_upgrades_sign = pygame.image.load("images/town_upgrades_sign.png").convert_alpha()
        self.image_skills_sign = pygame.image.load("images/skills_sign.png").convert_alpha()
        self.image_expedition_sign = pygame.image.load("images/expedition_sign.png").convert_alpha()
        self.image_boots_sign = pygame.image.load("images/boots_sign.png").convert_alpha()

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
        smallText = pygame.font.Font('font/Glegoo-Regular.ttf', size)
        textSurf, textRect = self.textObjects(msg, smallText, color)
        textRect.center = (x, y)
        self.gameDisplay.blit(textSurf, textRect)

    def button(self, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if action == "house":
                self.gameDisplay.blit(self.image_house_sign, (0, 0))

            elif action == "airTank":
                self.gameDisplay.blit(self.image_air_tank_sign, (0, 0))

            elif action == "purifier":
                self.gameDisplay.blit(self.image_air_purifier_sign, (0, 0))

            elif action == "upgrades":
                self.gameDisplay.blit(self.image_town_upgrades_sign, (0, 0))

            elif action == "skills":
                self.gameDisplay.blit(self.image_skills_sign, (0, 0))

            elif action == "expedition":
                self.gameDisplay.blit(self.image_expedition_sign, (0, 0))

            elif action == "boots":
                self.gameDisplay.blit(self.image_boots_sign, (0, 0))
            
            #elif action == "airskill":
                #self.gameDisplay.blit(self.image_air_skill, (0, 0))

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
                    if self.gold >= PRICE_BOOTS and self.boots == False:
                        self.gold -= PRICE_BOOTS
                        self.boots = True

                elif action == "airskill":
                    if self.gold >= PRICE_AIR_SKILL and self.airskill == False:
                        self.gold -= PRICE_AIR_SKILL
                        self.airskill = True

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
                
        #else:

        #######   
                
    def draw(self):
        """Affiche le menu du village"""

        self.gameDisplay.blit(self.image_background, (0, 0))

        ####### RESSOURCES #######
        self.gameDisplay.blit(self.image_ressources, (0, 0))
        ## Air
        if (self.air == self.airTank):
            self.textDisplay(str(self.air), black, 30, 160, 56)
            self.textDisplay("(full)", black, 30, 160, 86)
        else:
            self.textDisplay(str(self.air) + " / " + str(self.airTank), black, 30, 160, 70)

        
        ## Gold
        self.textDisplay(str(self.gold), black, 30, 160, 167)

        ## Population
        self.gameDisplay.blit(self.image_population, (0, 0))
        self.textDisplay(str(self.population) + " / " + str(self.populationTank), black, 30, 911, 64) 
        
        ####### 

        ####### GENERAL ####### 
        self.gameDisplay.blit(self.image_town_name, (0, 0))
        #######

        ####### CONVERT GOLD TO AIR #######
        x = 96 
        y = 430
        buttonWidth = 192
        buttonHeight = 32
        y2 = y+(buttonHeight+16)
        y3 = y+(buttonHeight+16)*2

        #img = pygame.image.load("images/gold.png").convert_alpha()
        #self.gameDisplay.blit(img, (85, 352))

        #img = pygame.image.load("images/airBottle.png").convert_alpha()
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

        self.gameDisplay.blit(self.image_air_converter, (0, 0))

        self.textDisplay("100 -> 1", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2))) 
        self.textDisplay("1000 -> 10", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2))) 
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

            self.gameDisplay.blit(self.image_town_hall, (0, 0))

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

            self.gameDisplay.blit(self.image_town_upgrades, (0, 0))

        elif self.skills:
            self.button(388, 222, 61, 66, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "boots")
            self.textDisplay("Boots", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "airskill")
            self.textDisplay("Air skill", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            self.gameDisplay.blit(self.image_skills, (0, 0))
            
            
        ####### 

        ####### EXPEDITION #######
        x = 731
        y = 469
        buttonWidth = 990-731
        buttonHeight = 547-469
        self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "expedition")
        self.gameDisplay.blit(self.image_expedition, (0, 0))
        #######

        pygame.display.update()
        
