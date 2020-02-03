from settings import *

class Camera(object):
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def __init__(self,mapBg):
        self.mapWidth = mapBg.get_rect().width
        self.mapHeight = mapBg.get_rect().height
        self.mapBg = mapBg
        self.x = 400
        self.y = 400
        print(self.mapWidth,self.mapHeight)

    def draw(self, win, player, list ):
        cameraX = player.rect.left - (player.rect.width // 2) - (SCREEN_WIDTH // 2)
        cameraY  = player.rect.top - (player.rect.height // 2) - (SCREEN_HEIGHT // 2)

        
        if  cameraX >=  0 and cameraX < self.mapWidth - SCREEN_WIDTH:
            self.x = cameraX

        if  cameraY >= 0 and cameraY < self.mapHeight - SCREEN_HEIGHT:
            self.y = cameraY


        
        print(player.rect.top,player.rect.left)

        if cameraX >= 0 and cameraX < self.mapWidth - SCREEN_WIDTH:
            playerX = (SCREEN_WIDTH // 2) - (player.rect.width // 2)
        else:
            if cameraX >= self.mapWidth - SCREEN_WIDTH:
                playerX = player.rect.left - self.mapWidth + SCREEN_WIDTH - player.rect.width
            else:   
                playerX =  player.rect.left - player.rect.width
                if playerX < 0 :
                    playerX = 0

        if cameraY >= 0 and cameraY < self.mapHeight - SCREEN_HEIGHT:
            playerY = (SCREEN_HEIGHT // 2) - (player.rect.height // 2)
        else:
            if cameraY >= self.mapHeight - SCREEN_HEIGHT:
                playerY = player.rect.top - self.mapHeight + SCREEN_HEIGHT - player.rect.height
            else:
                playerY = player.rect.top - player.rect.height
                if playerY < 0 :
                    playerY = 0


        win.blit(self.mapBg,(-self.x,-self.y))  
        player.draw(win,playerX,playerY)