import pygame
import sys
from MusicPlayer import *
from settings import *

pygame.init()

class Village(object):
    """Classe qui correspond au village et ressources ainsi qu a son interface"""

    def __init__(self, gameDisplay, screenWidth, screenHeight):
        """Affectation des ressources en debut de partie"""
        # Ressources
        self.gold = 500.0
        self.population = 20
        self.populationTank = 20
        self.house = 0

        self.air = 80.0
        self.airMax = 100
        self.airTank = 0

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
        self.alreadyLost = False

        # Utilities
        self.inTheVillage = True
        self.timerAir = False
        self.timerPop = False
        self.timerGold = False
        self.lose = False
        self.win = False
        self.launchExpedition = False
        self.difficulty = ""
        self.musicPlayer = MusicPlayer()

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
        self.image_skills_air = pygame.image.load("images/skills_gauntlets_sold_out.png").convert_alpha()
        self.image_skills_boots = pygame.image.load("images/skills_boots_sold_out.png").convert_alpha()
        self.image_skills_out = pygame.image.load("images/skills_both_sold_out.png").convert_alpha()
        self.image_expedition = pygame.image.load("images/expedition.png").convert_alpha()
        self.image_air_purifier_sign = pygame.image.load("images/air_purifier_sign.png").convert_alpha()
        self.image_town_upgrades_sign = pygame.image.load("images/town_upgrades_sign.png").convert_alpha()
        self.image_skills_sign = pygame.image.load("images/skills_sign.png").convert_alpha()
        self.image_expedition_sign = pygame.image.load("images/expedition_sign.png").convert_alpha()
        self.image_boots_sign = pygame.image.load("images/boots_sign.png").convert_alpha()
        self.image_gauntlets_sign = pygame.image.load("images/gauntlets_sign.png").convert_alpha() 
        self.image_gold= pygame.image.load("images/gold.png").convert_alpha()
        self.image_submit_score = pygame.image.load("images/Signs/submit_score.png").convert_alpha() 

        # Sound
        self.WOOD_CLICK = pygame.mixer.Sound('sounds/wood_click.ogg')
        self.AIRBUY_CLICK = pygame.mixer.Sound('sounds/breath.ogg')
        self.LOSEGAME = pygame.mixer.Sound('sounds/loseGame.ogg')
                
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def minusAir(self):
        self.timerAir = False
        if self.air > 1.0:
            if self.difficulty == "Easy":
                self.air -= (self.population/20)*0.17
            else:
                self.air -= (self.population/20)*0.2
        else:
            self.lose = True

    def plusPopulation(self):
        self.timerPop = False
        if self.population < self.populationTank:
            self.population += 1
    
    def plusGold(self):
        self.timerGold = False
        if self.difficulty == "Easy":
            self.gold += (self.population/20)*9
        else:
            self.gold += (self.population/20)*7.5

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

            elif action == "airMax":
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
                if not self.boots:
                    self.gameDisplay.blit(self.image_boots_sign, (0, 0))

            elif action == "airskill":
                if not self.airskill:
                    self.gameDisplay.blit(self.image_gauntlets_sign, (0, 0))
            
            #elif action == "airskill":
                #self.gameDisplay.blit(self.image_air_skill, (0, 0))

            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                    quit()
                elif action == "nothing":
                    pygame.time.delay(1)
                
                elif action == "endGame":
                    return True;

                elif action == "goldToAir1":
                    if self.air < self.airMax and self.gold >= LOW_PRICE_AIR:
                        self.air += 1
                        self.gold -= LOW_PRICE_AIR
                        self.AIRBUY_CLICK.play()
                        pygame.time.delay(150)

                elif action == "goldToAir10":
                    if self.air <= self.airMax-10 and self.gold >= MID_PRICE_AIR:
                        self.air += 10
                        self.gold -= MID_PRICE_AIR
                        self.AIRBUY_CLICK.play()
                        pygame.time.delay(150)

                elif action == "goldToAir50":
                    while self.air < self.airMax-50 and self.gold >= HIGH_PRICE_AIR:
                        self.gold -= HIGH_PRICE_AIR
                        self.air += 50
                        self.AIRBUY_CLICK.play()
                        pygame.time.delay(150)

                elif action == "house":
                    if self.gold >= PRICE_HOUSE+(self.house*HOUSE_INCREASE):
                        self.gold -= PRICE_HOUSE+(self.house*HOUSE_INCREASE)
                        self.house += 1
                        self.populationTank += HOUSE_VALUE
                        self.WOOD_CLICK.play()
                        pygame.time.delay(150)

                elif action == "airMax":
                    if self.gold >= PRICE_AIR_TANK+(self.airTank*AIR_TANK_INCREASE):
                        self.gold -= PRICE_AIR_TANK+(self.airTank*AIR_TANK_INCREASE)
                        self.airTank += 1
                        self.airMax += AIR_TANK_VALUE
                        self.AIRBUY_CLICK.play()
                        pygame.time.delay(150)

                elif action == "purifier":
                    if self.gold >= PRICE_PURIFIER:
                        self.gold -= PRICE_PURIFIER
                        self.WOOD_CLICK.play()
                        self.win = True

                elif action == "boots":
                    if self.gold >= PRICE_BOOTS and self.boots == False:
                        self.gold -= PRICE_BOOTS
                        self.WOOD_CLICK.play()
                        self.boots = True

                elif action == "airskill":
                    if self.gold >= PRICE_AIR_SKILL and self.airskill == False:
                        self.gold -= PRICE_AIR_SKILL
                        self.WOOD_CLICK.play()
                        self.airskill = True

                elif action == "menu":
                    self.menu = True
                    self.upgrades = self.upgrades2 = self.skills  = False
                    self.WOOD_CLICK.play()
                    pygame.time.delay(150)

                elif action == "upgrades":
                    self.menu = self.upgrades2 = self.skills = False
                    self.upgrades = True
                    self.WOOD_CLICK.play()

                    pygame.time.delay(150)

                elif action == "skills":
                    self.menu = self.upgrades = self.upgrades2 = False
                    self.skills = True
                    self.WOOD_CLICK.play()
                    pygame.time.delay(150)

                elif action == "expedition":
                    self.launchExpedition = True
                    self.WOOD_CLICK.play()
                    pygame.time.delay(150)
                
        #else:
                
    def draw(self):
        """Affiche le menu du village"""

        self.gameDisplay.blit(self.image_background, (0, 0))

        ####### RESSOURCES #######
        self.gameDisplay.blit(self.image_ressources, (0, 0))
        ## Air
        self.textDisplay(str(int(self.air)), black, 30, 160, 55)
        self.textDisplay(" / " + str(int(self.airMax)), black, 30, 160, 86)
        
        ## Gold
        self.textDisplay(str(int(self.gold)), black, 30, 160, 167)

        ## Population
        self.gameDisplay.blit(self.image_population, (0, 0))
        self.textDisplay(str(int(self.population)) + " / " + str(int(self.populationTank)), black, 30, 911, 64) 

        popAirValue = 0.0
        popGoldValue = 0.0
        if self.difficulty == "Easy":
            popGoldValue = (self.population/20)*9
        else:
            popGoldValue = (self.population/20)*7.5

        if self.difficulty == "Easy":
            popAirValue = (self.population/20)*0.17
        else:
            popAirValue = (self.population/20)*0.2

        self.textDisplay(str(format(popAirValue, '.2f')) + " /s", black, 30, 910, 116)
        self.textDisplay(str(format(popGoldValue, '.2f')) + " /s", black, 30, 910, 162)  
        #self.air -= (self.population/20)*0.2
        #self.gold += (self.population/20)*7.5
        #format(math.pi, '.2f')

        
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
        self.button(x, y3, buttonWidth, buttonHeight, green, bright_green, "goldToAir50")

        if self.gold < LOW_PRICE_AIR:
            self.button(x, y, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            self.button(x, y3, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
            
        if self.gold < MID_PRICE_AIR or self.air > self.airMax - 10:
            self.button(x, y2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100))
        
        if self.air >= self.airMax:
            self.button(x, y, buttonWidth, buttonHeight, red, red)
            self.button(x, y2, buttonWidth, buttonHeight, red, red)
            self.button(x, y3, buttonWidth, buttonHeight, red, red)

        self.gameDisplay.blit(self.image_air_converter, (0, 0))

        self.textDisplay("50 -> 1", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/2))) 
        self.textDisplay("400 -> 10", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/2))) 
        self.textDisplay("1500 -> 50", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/2)))
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

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "airMax")
            if self.gold < PRICE_AIR_TANK:
                self.button(x, y2, buttonWidth, buttonHeight, (100, 100, 100), (100, 100, 100) )
            self.textDisplay("Air tank", black, 20, (x+(buttonWidth/2)), (y3+(buttonHeight/3)) )

            self.gameDisplay.blit(self.image_town_upgrades, (0, 0))
            self.textDisplay(str(PRICE_HOUSE+(self.house*HOUSE_INCREASE)), black, 17, 558, 384)
            self.textDisplay(str(PRICE_AIR_TANK+(self.airTank*AIR_TANK_INCREASE)), black, 17, 558, 496)

        elif self.skills:
            self.button(388, 222, 61, 66, (200, 200, 200), (100, 100, 100), "menu")

            self.button(x, y, buttonWidth, buttonHeight, green, bright_green, "boots")
            self.textDisplay("Boots", black, 20, (x+(buttonWidth/2)), (y+(buttonHeight/3)) )

            self.button(x, y2, buttonWidth, buttonHeight, green, bright_green, "airskill")
            self.textDisplay("Air skill", black, 20, (x+(buttonWidth/2)), (y2+(buttonHeight/3)) )

            if not self.boots and not self.airskill:
                self.gameDisplay.blit(self.image_skills, (0, 0))
            if not self.boots and self.airskill:
                self.gameDisplay.blit(self.image_skills_air, (0, 0))
            if self.boots and not self.airskill:
                self.gameDisplay.blit(self.image_skills_boots, (0, 0))
            if self.boots and self.airskill:
                self.gameDisplay.blit(self.image_skills_out, (0, 0))
            
            
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

    def drawDeath(self,time):
        if self.alreadyLost == False:
            self.alreadyLost = True
            Clicked = False
            see_through = pygame.Surface((SCREEN_WIDTH - TAILLE_CASE,SCREEN_HEIGHT - TAILLE_CASE)).convert_alpha()
            see_through.fill((140, 140, 140, 200))
            self.gameDisplay.blit(see_through, (32,32))
            # Attend que l'utilisateur clique sur le bouton continuer
            if self.win == True:
                textStr = "Congratulations, you saved your town!"
                self.musicPlayer.playWinMusic()
            else:
                textStr = "You lost!"
                self.musicPlayer.stop()
                self.LOSEGAME.play()
            goldStr = "Gold collected:"
            self.textDisplay(textStr,black,40,(SCREEN_WIDTH//2),(SCREEN_HEIGHT//8))
            # Gold
            goldImgX = (SCREEN_WIDTH//6 * 1) + 40
            if self.gold > 9:
                goldImgX += 40
            elif self.gold > 99:
                goldImgX += 70
            elif self.gold > 999:
                goldImgX += 100
            elif self.gold > 9999:
                goldImgX += 135
            self.textDisplay(goldStr,black,40,(SCREEN_WIDTH//4 * 1),(SCREEN_HEIGHT//4))
            self.textDisplay(str(int(self.gold)),black,40,(SCREEN_WIDTH//6 * 1) + 35,(SCREEN_HEIGHT//3))
            self.gameDisplay.blit(self.image_gold, (goldImgX, (SCREEN_HEIGHT//3) - 35))

            # Time
            minutes = str(time//60)
            seconds = str(time % 60)
            if int(seconds) <= 9:
                seconds = "0" + seconds
            self.textDisplay("Time spent:",black,40,(SCREEN_WIDTH//4 * 3),(SCREEN_HEIGHT//4))
            self.textDisplay(minutes + " : " + seconds,black,40,(SCREEN_WIDTH//4 * 3),(SCREEN_HEIGHT//3))
            self.gameDisplay.blit(self.image_submit_score, (0, 0))

            while not Clicked:
                            
                Clicked = self.button((SCREEN_WIDTH//2) - 190,(SCREEN_HEIGHT//2) + 100,380,100,green,bright_green,"endGame")
                
                
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.display.quit(); sys.exit()
            
