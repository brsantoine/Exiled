import pygame as pg
import sys
from settings import *

class Menu:
    """Une classe qui correspond a un mur"""
    def __init__(self, screen):
        """Initialise la classe Mur"""

        self.screen = screen

        self.currentWindow = "mainMenu"
        self.closed = False

        self.x = 416
        self.y = 320
        self.buttonWidth = 192
        self.buttonHeight = 80
        self.y2 = self.y + (self.buttonHeight+32)
        self.y3 = self.y + (self.buttonHeight+32)*2
        self.y4 = self.y + (self.buttonHeight+32)*3
        self.hover = False

        # Images
        self.image_money = pg.image.load("images/gold.png").convert_alpha()
        self.image_credits = pg.image.load("images/mainMenu/credits.png").convert_alpha()
        self.image_gameTitle = pg.image.load("images/mainMenu/game_title.png").convert_alpha()
        self.image_highScores = pg.image.load("images/mainMenu/high_scores.png").convert_alpha()
        self.image_mainMenu = pg.image.load("images/mainMenu/main_menu.png").convert_alpha()
        self.image_mainMenuBackground = pg.image.load("images/mainMenu/main_menu_background.png").convert_alpha()

        # Sounds
        self.WOOD_HOVER = pg.mixer.Sound('sounds/wood_hover.ogg')
        self.WOOD_CLICK = pg.mixer.Sound('sounds/wood_hover.ogg')

    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textDisplay(self, msg, color, size, x, y):
        smallText = pg.font.Font('font/Glegoo-Regular.ttf', size)
        textSurf, textRect = self.textObjects(msg, smallText, color)
        textRect.center = (x, y)
        self.screen.blit(textSurf, textRect)

    def button(self, x, y, w, h, ic, ac, action = None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(self.screen, ac, (x, y, w, h))
            #
            #if action == "quit" and self.hover == False:
            #    pg.time.delay(150)
            #elif action == "Play" and self.hover == False:
            #    pg.time.delay(150)
            #elif action == "Help" and self.hover == False:
            #    pg.time.delay(150)
            #elif action == "Credits" and self.hover == False:
            #   pg.time.delay(150)
            #elif action == "easy" and self.hover == False:
            #  pg.time.delay(150)
            #elif action == "normal" and self.hover == False:
            #    pg.time.delay(150)
            #elif action == "hard" and self.hover == False:
            #   pg.time.delay(150)
            #elif action == "mainMenu" and self.hover == False:
            #    pg.time.delay(150)
            #self.hover = True
            #
            if click[0] == 1 and action != None:
                if action == "quit":
                    pg.display.quit()
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
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "Help":
                    self.currentWindow = "helpMenu"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "Credits":
                    self.currentWindow = "creditsScreen"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "easy":
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "normal":
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "hard":
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "mainMenu":
                    self.currentWindow = "mainMenu"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
        else:
            pg.draw.rect(self.screen, ic, (x, y, w, h))
            #self.hover = False
            return False

    def draw(self):
        """Appelee a chaque tour de boucle, cette fonction affiche le menu"""

        
        
        self.screen.fill(white)
        
        if self.currentWindow == "context":
            self.screen.blit(self.image_mainMenuBackground, (0, 0))
            y = 25
            x = SCREEN_WIDTH//2
            textColor = white
            see_through = pg.Surface((SCREEN_WIDTH//5 * 4,SCREEN_HEIGHT//2 - 100)).convert_alpha()
            see_through.fill((80, 80, 80, 150))
            self.screen.blit(see_through, (100,52))
            #1st paragraph
            self.textDisplay("World War 3 was a devastating war involving 90% of the world's", textColor, 20, x, ((self.buttonHeight/3)+64) )
            self.textDisplay("countries. It had numerous consequences on the environment.", textColor, 20, x, ((self.buttonHeight/3)+64+y) )
            self.textDisplay("Air became unbreathable in more than half of the inhabited", textColor, 20, x, ((self.buttonHeight/3)+64+(y*2)))
            self.textDisplay("territories on Earth, including your town.", textColor, 20, x, ((self.buttonHeight/3)+64+(y*3)) )
            #2nd paragraph
            self.textDisplay("However, you still have hope. The winners of the war decided to monetize", textColor, 20, x, ((self.buttonHeight/3)+64+(y*5)) )
            self.textDisplay("air to assert their superiority. In order to surive, you decided", textColor, 20, x, ((self.buttonHeight/3)+64+(y*6)) )
            self.textDisplay("to raid the surrounding ruins to find money in order to purchase ", textColor, 20, x, ((self.buttonHeight/3)+64+(y*7)) )
            self.textDisplay("an air purifier which could offer you and your village independance.", textColor, 20, x, ((self.buttonHeight/3)+64+(y*8)) )
            x = 731
            y = 469
            buttonWidth = 990-731
            buttonHeight = 547-469

            self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "skip")
            

        elif self.currentWindow == "mainMenu":
            self.textDisplay("Menu", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # self.button play
            self.button(self.x, self.y, self.buttonWidth, self.buttonHeight, green, bright_green, "Play")
            self.textDisplay("Play", black, 20, (self.x + (self.buttonWidth/2)), (self.y+(self.buttonHeight/3)) )
            # self.button help
            self.button(self.x, self.y2, self.buttonWidth, self.buttonHeight, green, bright_green,"Help")
            self.textDisplay("Help", black, 20, (self.x + (self.buttonWidth/2)), (self.y2+(self.buttonHeight/3)) )
            # self.button quit
            self.button(self.x, self.y3, self.buttonWidth, self.buttonHeight, green, bright_green,"quit")
            self.textDisplay("Quit", black, 20, (self.x+(self.buttonWidth/2)), (self.y3+(self.buttonHeight/3)) )
            # self.button Credits
            self.button(90, 581, 197, 126, green, bright_green,"Credits")
            self.textDisplay("Credits", black, 20, (92+(197/2)), (560+(123/2)) )
            # self.button Highscores
            self.button(736, 364, 193, 107, green, bright_green,"Credits")
            self.screen.blit(self.image_mainMenuBackground, (0, 0))
            self.screen.blit(self.image_mainMenu, (0, 0))
            self.screen.blit(self.image_gameTitle, (0, 0))
            self.screen.blit(self.image_credits, (0, 0))
            self.screen.blit(self.image_highScores, (0, 0))

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
            # Button retour
            self.button(50, SCREEN_HEIGHT/15, self.buttonWidth/2, self.buttonHeight/2, green, bright_green, "mainMenu")
            self.textDisplay("Main Menu", black, 10, (50+(self.buttonWidth/4)), ((SCREEN_HEIGHT/15)+(self.buttonHeight/4)) )

    def drawDeath(self,win,time,money):
        Clicked = False
        see_through = pg.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
        see_through.fill((140, 140, 140, 200))
        self.screen.blit(see_through, (32,32))
        # Attend que l'utilisateur clique sur le bouton continuer
        while not Clicked:
            Clicked = self.button((SCREEN_WIDTH//2) - 125,(SCREEN_HEIGHT//2) + 100,250,70,green,bright_green,"loseExpedition")
            self.textDisplay("Return to town",black,20,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//2) + 100 + 35)
            if win == True:
                textStr = "You made it back safely!"
                goldStr = "Gold collected:"
            else:
                goldStr = "Gold lost:"
                textStr = "You got caught!"
            self.textDisplay(textStr,black,40,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//8))
            # Gold
            goldImgX = (SCREEN_WIDTH//6 * 1) + 40
            if money > 9:
                goldImgX += 15
            elif money > 99:
                goldImgX += 35
            elif money > 999:
                goldImgX += 60
            self.textDisplay(goldStr,black,40,(SCREEN_WIDTH//4 * 1),(SCREEN_HEIGHT//4))
            self.textDisplay(str(money),black,40,(SCREEN_WIDTH//6 * 1) + 35,(SCREEN_HEIGHT//3))
            self.screen.blit(self.image_money, (goldImgX, (SCREEN_HEIGHT//3) - 35))

            # Time
            minutes = str(time//60)
            seconds = str(time % 60)
            if int(seconds) <= 9:
                seconds = "0" + seconds
            self.textDisplay("Time spent:",black,40,(SCREEN_WIDTH//4 * 3),(SCREEN_HEIGHT//4))
            self.textDisplay(minutes + " : " + seconds,black,40,(SCREEN_WIDTH//4 * 3),(SCREEN_HEIGHT//3))


            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT: pg.display.quit(); sys.exit()