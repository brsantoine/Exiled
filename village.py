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
    """Classe qui correspond au village et ressources ainsi qu'à son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en début de partie"""
        self.gold = 5000
        self.air = 0
        self.population = 1

        self.gameDisplay = gameDisplay
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    ###### Define in settings ######
    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def button(self, msg, fontColor, x, y, w, h, ic, ac, action=None):
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
                    if self.air < 100 and self.gold >= 500:
                        self.air += 1
                        self.gold -= 500
                        pygame.time.delay(100)
                elif action == "goldToAir10":
                    if self.air <= 90 and self.gold >= 5000:
                        self.air += 10
                        self.gold -= 5000
                        pygame.time.delay(100)
                elif action == "goldToAirMax":
                    while self.air < 100 and self.gold >= 500:
                        self.gold -= 500
                        self.air += 1                    


        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.Font('freesansbold.ttf', 15)
        textSurf, textRect = self.textObjects(msg, smallText, fontColor)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(textSurf, textRect)
    #######   
            
    def draw(self):
        """Affiche le menu du village"""

        self.village = True

        while self.village:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 30)
            TextSurf, TextRect = self.textObjects('Village', largeText, black)
            TextRect.center = ((self.screenWidth/2), (self.screenHeight/15))
            self.gameDisplay.blit(TextSurf, TextRect)

            ####### RESSOURCES #######
            ## Air
            smallText = pygame.font.Font('freesansbold.ttf', 30)
            textSurf, textRect = self.textObjects("Air " + str(self.air), smallText, black)
            textRect.center = (60, 20)
            self.gameDisplay.blit(textSurf, textRect) 

            ## Gold
            smallText = pygame.font.Font('freesansbold.ttf', 30)
            textSurf, textRect = self.textObjects("Gold " + str(self.gold), smallText, black)
            textRect.center = (200, 20)
            self.gameDisplay.blit(textSurf, textRect) 

            ## Population
            smallText = pygame.font.Font('freesansbold.ttf', 30)
            textSurf, textRect = self.textObjects("Population " + str(self.population), smallText, black)
            textRect.center = (900, 20)
            self.gameDisplay.blit(textSurf, textRect) 
            ####### 

            ####### SHOP UPGRADE #######
            x = 50
            y = 450
            buttonWidth = 250
            buttonHeight = 90

            self.button("Skill 1", black, x, y, buttonWidth, buttonHeight, green, bright_green)
            self.button("Skill 2", black, x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green)
            self.button("Skill 3", black, x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, green, bright_green)
            ####### 

            ####### CONVERT GOLD TO AIR #######
            x = 362 
            y = 450
            buttonWidth = 300
            buttonHeight = 90

            self.button("Gold -> Air 1", black, x, y, buttonWidth, buttonHeight, green, bright_green, "goldToAir1")
            self.button("Gold -> Air 10",  black, x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green, "goldToAir10")
            self.button("Gold -> Air MAX", black, x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, green, bright_green, "goldToAirMax")
                
            if self.gold < LOW_PRICE:
                self.button("Gold -> Air 1", black, x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
                self.button("Gold -> Air MAX", black, x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
                
            if self.gold < MID_PRICE or self.air > 90:
                self.button("Gold -> Air 10",  black, x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            
            if self.air >= 100:
                self.button("Gold -> Air 1", black, x, y, buttonWidth, buttonHeight, red, red)
                self.button("Gold -> Air 10",  black, x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, red, red)
                self.button("Gold -> Air MAX", black, x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, red, red)
            #######

            pygame.display.update()
            
