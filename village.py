import pygame as pg
pg.init()

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

        self.village = True

    ###### Define in settings ######
    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textDisplay(self, msg, color, size, x, y):
        smallText = pg.font.Font('freesansbold.ttf', size)
        textSurf, textRect = self.textObjects(msg, smallText, color)
        textRect.center = (x, y)
        self.gameDisplay.blit(textSurf, textRect)

    def button(self, x, y, w, h, ic, ac, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(self.gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pg.quit()
                    quit()
                elif action == "nothing":
                    pg.time.delay(1)

                elif action == "goldToAir1":
                    if self.air < 100 and self.gold >= LOW_PRICE:
                        self.air += 1
                        self.gold -= LOW_PRICE
                        pg.time.delay(150)

                elif action == "goldToAir10":
                    if self.air <= 90 and self.gold >= MID_PRICE:
                        self.air += 10
                        self.gold -= MID_PRICE
                        pg.time.delay(150)

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
            pg.draw.rect(self.gameDisplay, ic, (x, y, w, h))

    #######   
            
    def draw(self):
        """Affiche le menu du village"""

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
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

        ####### SHOP UPGRADE #######
        x = 50
        y = 450
        buttonWidth = 250
        buttonHeight = 90
        y2 = y+(buttonHeight+10)
        y3 = y+(buttonHeight+10)*2

        if self.menu:
            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "townUpgrades")
            self.textDisplay("Town upgrades", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2)) ) 
            
            self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green, "skills")
            self.textDisplay("Skills", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2)) )

        elif self.upgrades:
            self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Maison", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Purificateur", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            self.button(x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Stockage d'air", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )

        elif self.skills:
            self.button(x, y, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Courir", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green)
            self.textDisplay("Cape", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )
        ####### 

        ####### CONVERT GOLD TO AIR #######
        x = 362 
        y = 450
        buttonWidth = 300
        buttonHeight = 90

        self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "goldToAir1")
        self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, green, bright_green, "goldToAir10")
        self.button(x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, green, bright_green, "goldToAirMax")

        if self.gold < LOW_PRICE:
            self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            self.button(x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            
        if self.gold < MID_PRICE or self.air > 90:
            self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
        
        if self.air >= 100:
            self.button(x, y, buttonWidth, buttonHeight, red, red)
            self.button(x, y+(buttonHeight+10)*1, buttonWidth, buttonHeight, red, red)
            self.button(x, y+(buttonHeight+10)*2, buttonWidth, buttonHeight, red, red)

        self.textDisplay("Gold -> Air 1", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2))) 
        self.textDisplay("Gold -> Air 10", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight+10)*1+(buttonHeight/2))) 
        self.textDisplay("Gold -> Air MAX", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight+10)*2+(buttonHeight/2))) 
        #######

        pg.display.update()
        
