import pygame as pg
import sys
from settings import *

class Menu:
    """Une classe qui correspond a un mur"""
    def __init__(self, screen):
        """Initialise la classe Mur"""

        self.screen = screen

        self.currentWindow = "context"
        self.closed = False

        self.x = 416
        self.y = 320
        self.buttonWidth = 192
        self.buttonHeight = 80
        self.y2 = self.y + (self.buttonHeight+32)
        self.y3 = self.y + (self.buttonHeight+32)*2
        self.y4 = self.y + (self.buttonHeight+32)*3
        self.hover = False
        self.difficulty = "Easy"

        # Images
        self.image_money = pg.image.load("images/gold.png").convert_alpha()
        self.image_credits = pg.image.load("images/mainMenu/credits.png").convert_alpha()
        self.image_gameTitle = pg.image.load("images/mainMenu/game_title.png").convert_alpha()
        self.image_highScores = pg.image.load("images/mainMenu/high_scores.png").convert_alpha()
        self.image_mainMenu = pg.image.load("images/mainMenu/main_menu.png").convert_alpha()
        self.image_mainMenuBackground = pg.image.load("images/mainMenu/main_menu_background.png").convert_alpha()
        self.image_normalBackGround = pg.image.load("images/mainMenu/normal_background.png").convert_alpha()
        self.image_introBackGround = pg.image.load("images/mainMenu/intro_background.png").convert_alpha()
        self.image_difficultyBackground = pg.image.load("images/mainMenu/difficulty_background.png").convert_alpha()
        self.image_creditsBackground = pg.image.load("images/mainMenu/credits_background.png").convert_alpha()
        self.image_backSign = pg.image.load("images/mainMenu/back_sign.png").convert_alpha()
        self.image_difficultyBuilding = pg.image.load("images/mainMenu/difficulty_building.png").convert_alpha()
        self.image_debris = pg.image.load("images/mainMenu/debris.png").convert_alpha()

        # Sounds
        self.WOOD_HOVER = pg.mixer.Sound('sounds/wood_hover.ogg')
        self.WOOD_CLICK = pg.mixer.Sound('sounds/wood_hover.ogg')

    def textObjects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def textDisplay(self, msg, color, size, x, y, font = 'font/Glegoo-Regular.ttf'):
        smallText = pg.font.Font(font, size)
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
                    self.currentWindow = "Highscores"
                    self.difficulty = "Easy"
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "normal":
                    self.currentWindow = "Highscores"
                    self.difficulty = "Normal"
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "hard":
                    self.currentWindow = "Highscores"
                    self.difficulty = "Hard"
                    self.closed = True
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "mainMenu":
                    self.currentWindow = "mainMenu"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "skip":
                    self.currentWindow = "mainMenu"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
                elif action == "Highscores":
                    self.currentWindow = "Highscores"
                    self.WOOD_CLICK.play()
                    pg.time.delay(150)
        else:
            pg.draw.rect(self.screen, ic, (x, y, w, h))
            #self.hover = False
            return False

    def draw(self,highscores):
        """Appelee a chaque tour de boucle, cette fonction affiche le menu"""

        
        
        self.screen.fill(white)
        
        if self.currentWindow == "context":
            #skip button
            x = 731
            y = 469
            buttonWidth = 990-731
            buttonHeight = 547-469
            self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "skip")
            #background
            self.screen.blit(self.image_introBackGround, (0, 0))
            #rectangle
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
            
            

        elif self.currentWindow == "mainMenu":
            # self.button play
            self.button(self.x, self.y, self.buttonWidth, self.buttonHeight, green, bright_green, "Play")
            # self.button help
            self.button(self.x, self.y2, self.buttonWidth, self.buttonHeight, green, bright_green,"Help")
            # self.button quit
            self.button(self.x, self.y3, self.buttonWidth, self.buttonHeight, green, bright_green,"quit")
            # self.button Credits
            self.button(90, 581, 197, 126, green, bright_green,"Credits")
            # self.button Highscores
            self.button(736, 364, 193, 107, green, bright_green,"Highscores")
            self.screen.blit(self.image_mainMenuBackground, (0, 0))
            self.screen.blit(self.image_mainMenu, (0, 0))
            self.screen.blit(self.image_gameTitle, (0, 0))
            self.screen.blit(self.image_credits, (0, 0))
            self.screen.blit(self.image_highScores, (0, 0))

        elif self.currentWindow == "helpMenu":
            self.screen.blit(self.image_normalBackGround, (0, 0))
            self.textDisplay("How to play", black, 30, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/15))
            # Button retour
            self.button(50, SCREEN_HEIGHT/15, self.buttonWidth/2, self.buttonHeight/2, green, bright_green, "mainMenu")
            self.textDisplay("Main Menu", black, 10, (50+(self.buttonWidth/4)), ((SCREEN_HEIGHT/15)+(self.buttonHeight/4)) )
        elif self.currentWindow == "creditsScreen":
            x = 731
            y = 469
            buttonWidth = 990-731
            buttonHeight = 547-469
            self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "skip")
            self.screen.blit(self.image_creditsBackground, (0, 0))
            y = 35
            x = SCREEN_WIDTH//2
            textColor = white
            # Rectangle derriere les credits
            see_through = pg.Surface((SCREEN_WIDTH//6 * 2 - 15,SCREEN_HEIGHT//11 * 5)).convert_alpha()
            see_through.fill((80, 80, 80, 150))
            self.screen.blit(see_through, (350,70))
            offset = 64
            self.textDisplay("Credits", white, 45, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/24),'font/Glegoo-Bold.ttf')
            #1st Programmers
            self.textDisplay("Programmers", textColor, 20, x, ((self.buttonHeight/3)+offset),'font/Glegoo-Bold.ttf') 
            offset -= 20
            self.textDisplay("Telmo Marques", textColor, 20, x, ((self.buttonHeight/3)+offset+y*2) )
            self.textDisplay("Adrien Gervraud", textColor, 20, x, ((self.buttonHeight/3)+offset+(y*3)))
            self.textDisplay("Antoine Breso", textColor, 20, x, ((self.buttonHeight/3)+offset+(y*4)) )
            self.textDisplay("Colin Vaufrey", textColor, 20, x, ((self.buttonHeight/3)+offset+(y*5)) )
            #2nd Game Designer
            self.textDisplay("Game Designer", textColor, 20, x, ((self.buttonHeight/3)+offset+(y*7)),'font/Glegoo-Bold.ttf' )
            offset -= 20
            self.textDisplay("Maxime Morin", textColor, 20, x, ((self.buttonHeight/3)+offset+(y*9)) )
            #
            see_through = pg.Surface((SCREEN_WIDTH//6 * 3 - 15,SCREEN_HEIGHT//8 * 2 - 50)).convert_alpha()
            see_through.fill((80, 80, 80, 150))
            self.screen.blit(see_through, (50,520))
            self.textDisplay("Sources", white, 45, (SCREEN_WIDTH/4) + 50, 480,'font/Glegoo-Bold.ttf')
            #1st Programmers
            self.textDisplay("Music", textColor, 20, (SCREEN_WIDTH/10) - 10, 550,'font/Glegoo-Bold.ttf') 
            self.textDisplay("Aerocity - Stranger", textColor, 20, (SCREEN_WIDTH/3) - 40, 550 )
            self.textDisplay("Cloudkicker - Night", textColor, 20, (SCREEN_WIDTH/3) - 40, 585 )
            self.textDisplay("Sound effects", textColor, 20, (SCREEN_WIDTH/10) + 25, 615,'font/Glegoo-Bold.ttf') 
            self.textDisplay("Youtube channel \"All Sounds\"", textColor, 20, (SCREEN_WIDTH/3) + 15, 615 )
        elif self.currentWindow == "Highscores":
            x = 731
            y = 469
            buttonWidth = 990-731
            buttonHeight = 547-469
            self.button(731, 469, buttonWidth, buttonHeight, green, bright_green, "skip")
            # draw background
            self.screen.blit(self.image_creditsBackground, (0, 0))
            #button a gauche
            #self.button(25, 466, 259, 70, green, bright_green, "mainMenu")
            y = 60
            x = SCREEN_WIDTH//2
            textColor = white
            # Rectangle derriere les credits
            see_through = pg.Surface((SCREEN_WIDTH//7 * 4 - 100,SCREEN_HEIGHT//5 * 4)).convert_alpha()
            see_through.fill((80, 80, 80, 150))
            self.screen.blit(see_through, (170,70))
            self.textDisplay("Highscores", white, 45, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/24),'font/Glegoo-Bold.ttf')
            #1st Programmers
            baseY = (SCREEN_HEIGHT/24)
            offset = -55
            i = 1
            for highscore in highscores:
                i += 1
                self.textDisplay(highscore [2] + " : " + highscore[1] + " - " + highscore[0] , textColor, 20, x - 115,offset +  baseY+(y*i) )
            
            #2nd Game Designer
        elif self.currentWindow == "difficultyMenu":
            # self.button easy
            self.button(self.x, self.y, self.buttonWidth, self.buttonHeight, green, bright_green, "easy")
            # self.button normal
            self.button(self.x, self.y2, self.buttonWidth, self.buttonHeight, green, bright_green, "normal")
            # self.button hard
            self.button(self.x, self.y3, self.buttonWidth, self.buttonHeight, green, bright_green, "hard")
            # Button retour
            self.button(25, 466, 259, 70, green, bright_green, "mainMenu")
            self.screen.blit(self.image_difficultyBackground, (0, 0))
            self.screen.blit(self.image_backSign, (0, 0))
            self.screen.blit(self.image_difficultyBuilding, (0, 0))
            self.screen.blit(self.image_debris, (0, 0))
            self.screen.blit(self.image_gameTitle, (0, 0))
            
            

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
                goldImgX += 40
            elif money > 99:
                goldImgX += 70
            elif money > 999:
                goldImgX += 100
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