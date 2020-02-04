from settings import *

class Camera(object):
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def __init__(self,mapBg):
        self.mapWidth = mapBg.get_rect().width
        self.mapHeight = mapBg.get_rect().height
        self.mapBg = mapBg
        self.x = 0
        self.y = 0
        print(self.mapWidth,self.mapHeight)

    def draw(self, win, player, list ):
        """Afficher les elements a l'ecran et bouger la camera en fonction de la position du joueur"""
        cameraX = player.rect.left - (player.rect.width // 2) - (SCREEN_WIDTH // 2)
        cameraY  = player.rect.top - (player.rect.height // 2) - (SCREEN_HEIGHT // 2)

        """On centre la camera tant que le joueurs n'atteind pas les bords"""
        if  cameraX >=  0 and cameraX < self.mapWidth - SCREEN_WIDTH:
            self.x = cameraX

        if  cameraY >= 0 and cameraY < self.mapHeight - SCREEN_HEIGHT:
            self.y = cameraY


        
        print(player.rect.left,player.rect.top)
        """calcul de l'X du joueur en fonction s'il est en haut,bas ou entre les 2"""
        if cameraX >= 0 and cameraX < self.mapWidth - SCREEN_WIDTH:
            playerX = (SCREEN_WIDTH // 2) - (player.rect.width // 2)
        else:
            #Si le joueur est a droite"""
            if cameraX >= self.mapWidth - SCREEN_WIDTH:
                playerX = player.rect.left - self.mapWidth + SCREEN_WIDTH - player.rect.width
                if playerX > SCREEN_WIDTH - (TAILLE_CASE*2):
                    playerX = SCREEN_WIDTH - (TAILLE_CASE*2)
            #Si le joueur est a gauche"""
            else:   
                #Le joueur est bloque par le mur de taille TAILLE_CASE
                playerX =  player.rect.left - player.rect.width
                if playerX < TAILLE_CASE :
                    playerX = TAILLE_CASE

        """calcul de l'Y du joueur en fonction s'il est a gauche,droite ou entre les 2"""
        if cameraY >= 0 and cameraY < self.mapHeight - SCREEN_HEIGHT:
            playerY = (SCREEN_HEIGHT // 2) - (player.rect.height // 2)
        else:
            #Si le joueur est en dessous"""
            if cameraY >= self.mapHeight - SCREEN_HEIGHT:
                playerY = player.rect.top - self.mapHeight + SCREEN_HEIGHT - player.rect.height
                #Le joueur est bloque par le mur de taille TAILLE_CASE
                if playerY > SCREEN_HEIGHT - (TAILLE_CASE*2):
                    playerY = SCREEN_HEIGHT - (TAILLE_CASE*2)
            #Si le joueur est au dessus"""    
            else:
                playerY = player.rect.top - player.rect.height
                #Le joueur est bloque par le mur de taille TAILLE_CASE
                if playerY < TAILLE_CASE :
                    playerY = TAILLE_CASE


        win.blit(self.mapBg,(-self.x,-self.y))  
        player.draw(win,playerX,playerY)