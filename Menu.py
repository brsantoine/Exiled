import pygame as pg
from settings import *

class Menu:
    """Une classe qui correspond a un mur"""
    def __init__(self, screen):
        """Initialise la classe Mur"""

        self.screen = screen

        self.currentWindow = "mainMenu"
        self.closed = False

        self.x = 400
        self.y = 220
        self.buttonWidth = 224
        self.buttonHeight = 80
        self.y2 = self.y + (self.buttonHeight+32)
        self.y3 = self.y + (self.buttonHeight+32)*2
        self.y4 = self.y + (self.buttonHeight+32)*3

    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textDisplay(self, msg, color, size, x, y):
        smallText = pg.font.Font('freesansbold.ttf', size)
        textSurf, textRect = self.textObjects(msg, smallText, color)
        textRect.center = (x, y)
        self.screen.blit(textSurf, textRect)

    def button(self, x, y, w, h, ic, ac, action = None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(self.screen, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "quit":
                    sys.exit()
                elif action == "exitExpedition":
                    # village.gold += expedition.gold()
                    return True
                    pg.time.delay(150)
                elif action == "loseExpedition":
                    # village.gold += expedition.gold()
                    return True
                    pg.time.delay(150)
                elif action == "Play":
                    self.currentWindow = "difficultyMenu"
                    pg.time.delay(150)
                elif action == "Help":
                    self.currentWindow = "helpMenu"
                    pg.time.delay(150)
                elif action == "Credits":
                    self.currentWindow = "creditsScreen"
                    pg.time.delay(150)
                elif action == "easy":
                    self.closed = True
                    pg.time.delay(150)
                elif action == "normal":
                    self.closed = True
                    pg.time.delay(150)
                elif action == "hard":
                    self.closed = True
                    pg.time.delay(150)
                elif action == "mainMenu":
                    self.currentWindow = "mainMenu"
                    pg.time.delay(150)
        else:
            pg.draw.rect(self.screen, ic, (x, y, w, h))
            return False

    def draw(self):
        """Appelee a chaque tour de boucle, cette fonction affiche le mur"""

        self.screen.fill(white)

        if self.currentWindow == "mainMenu":
            self.textDisplay("Menu", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # self.button play
            self.button(self.x, self.y, self.buttonWidth, self.buttonHeight, green, bright_green, "Play")
            self.textDisplay("Play", black, 20, (self.x + (self.buttonWidth/2)), (self.y+(self.buttonHeight/3)) )
            # self.button help
            self.button(self.x, self.y2, self.buttonWidth, self.buttonHeight, green, bright_green,"Help")
            self.textDisplay("Help", black, 20, (self.x + (self.buttonWidth/2)), (self.y2+(self.buttonHeight/3)) )
            # self.button Credits
            self.button(self.x, self.y3, self.buttonWidth, self.buttonHeight, green, bright_green,"Credits")
            self.textDisplay("Credits", black, 20, (self.x+(self.buttonWidth/2)), (self.y3+(self.buttonHeight/3)) )
            # self.button quit
            self.button(self.x, self.y4, self.buttonWidth, self.buttonHeight, green, bright_green,"quit")
            self.textDisplay("Quit", black, 20, (self.x+(self.buttonWidth/2)), (self.y4+(self.buttonHeight/3)) )
        elif self.currentWindow == "helpMenu":
            self.textDisplay("How to play", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # Button retour
            self.button(50, SCREEN_HEIGHT/15, self.buttonWidth/2, self.buttonHeight/2, green, bright_green, "mainMenu")
            self.textDisplay("Main Menu", black, 10, (50+(self.buttonWidth/4)), ((SCREEN_HEIGHT/15)+(self.buttonHeight/4)) )
        elif self.currentWindow == "creditsScreen":
            self.textDisplay("Credits", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # Button retour
            self.button(50, SCREEN_HEIGHT/15, self.buttonWidth/2, self.buttonHeight/2, green, bright_green, "mainMenu")
            self.textDisplay("Main Menu", black, 10, (50+(self.buttonWidth/4)), ((SCREEN_HEIGHT/15)+(self.buttonHeight/4)) )
        elif self.currentWindow == "difficultyMenu":
            self.textDisplay("Difficulty", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # self.button easy
            self.button(self.x, self.y, self.buttonWidth, self.buttonHeight, green, bright_green, "easy")
            self.textDisplay("Easy", black, 20, (self.x+(self.buttonWidth/2)), (self.y+(self.buttonHeight/3)) )
            # self.button normal
            self.button(self.x, self.y2, self.buttonWidth, self.buttonHeight, green, bright_green,"normal")
            self.textDisplay("Normal", black, 20, (self.x+(self.buttonWidth/2)), (self.y2+(self.buttonHeight/3)) )
            # self.button hard
            self.button(self.x, self.y3, self.buttonWidth, self.buttonHeight, green, bright_green,"hard")
            self.textDisplay("Hard", black, 20, (self.x+(self.buttonWidth/2)), (self.y3+(self.buttonHeight/3)) )

    def drawDeath(self):
        Clicked = False
        see_through = pg.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
        see_through.fill((140, 140, 140, 200))
        self.screen.blit(see_through, (32,32))
        # Attend que l'utilisateur clique sur le bouton continuer
        while not Clicked:
            Clicked = self.button((SCREEN_WIDTH//2) - 125,(SCREEN_HEIGHT//2) + 100,250,70,green,bright_green,"loseExpedition")
            self.textDisplay("Return to town",black,20,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//2) + 100 + 35)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()