import pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

class village(object):
    """Classe qui correspond au village et ressources ainsi qu'à son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en début de partie"""
        self.gold = 0
        self.air = 1000
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
                #elif action == "goldToAir":
                    ##
        else:
            pygame.draw.rect(self.gameDisplay,ic, (x, y, w, h))

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
            y = 510
            buttonWidth = 300
            buttonHeight = 200

            self.button("Gold -> Air", black, x, y, buttonWidth, buttonHeight, green, bright_green, "goldToAir")
            ####### 

            pygame.display.update()
