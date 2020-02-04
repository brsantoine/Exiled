import pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

LOW_PRICE = 500
MID_PRICE = 5000

class village(object):
    """Classe qui correspond au village et ressources ainsi qu a son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en debut de partie"""
        self.gold = 12000
        self.air = 0
        self.population = 1

        self.gameDisplay = gameDisplay
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.menu = True
        self.upgrades = False
        self.skills = False

    ###### Define in settings ######
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
                    if self.air < 100 and self.gold >= LOW_PRICE:
                        self.air += 1
                        self.gold -= LOW_PRICE
                        pygame.time.delay(150)

                elif action == "goldToAir10":
                    if self.air <= 90 and self.gold >= MID_PRICE:
                        self.air += 10
                        self.gold -= MID_PRICE
                        pygame.time.delay(150)

                elif action == "goldToAirMax":
                    while self.air < 100 and self.gold >= LOW_PRICE:
                        self.gold -= LOW_PRICE
                        self.air += 1

                elif action == "townUpgrades":
                    self.menu = False
                    self.upgrades = True
                    self.skills = False

                elif action == "skills":
                    self.menu = False
                    self.upgrades = False
                    self.skills = True

        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

    #######   
            
    def draw(self):
        """Affiche le menu du village"""

        self.village = True
        pygame.time.set_timer(1, 30000)

        while self.village:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == 1:
                    self.air -= 1

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

            if self.gold < LOW_PRICE:
                self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
                self.button(x, y3, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
                
            if self.gold < MID_PRICE or self.air > 90:
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
                self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "townUpgrades")
                self.textDisplay("Town upgrades", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2)) ) 
                
                self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "skills")
                self.textDisplay("Skills", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2)) )

            elif self.upgrades:
                self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
                self.textDisplay("Maison", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

                self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
                self.textDisplay("Purificateur", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

                self.button(x, y3, buttonWidth, buttonHeight, green, bright_green)
                self.textDisplay("Stockage d'air", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )

            elif self.skills:
                self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
                self.textDisplay("Courir", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

                self.button(x, y2, buttonWidth, buttonHeight, green, bright_green)
                self.textDisplay("Cape", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )
            ####### 

            

            pygame.display.update()
            
