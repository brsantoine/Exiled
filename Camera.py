from settings import *

class Camera(object):
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def __init__(self,mapBg):
        self.mapWidth = mapBg.get_rect().width
        self.mapHeight = mapBg.get_rect().height
        self.mapBg = mapBg
        self.x = 400
        self.y = 400

    def draw(self, win, player, list ):
        cameraX = player.rect.left - (player.rect.width // 2) - (SCREEN_WIDTH // 2)
        cameraY  = player.rect.top - (player.rect.height // 2) - (SCREEN_HEIGHT // 2)

        print(cameraX,cameraY)
        #if  cameraX >  (player.rect.height // 2) - (SCREEN_HEIGHT // 2) and cameraX < self.mapWidth - TAILLE_CASE:
        self.x = cameraX

        #if  cameraY > TAILLE_CASE and cameraY < self.mapHeight - TAILLE_CASE:
        self.y = cameraY   

      
        win.blit(self.mapBg,(-self.x,-self.y))  
        player.draw(win,((SCREEN_WIDTH // 2) - player.rect.width // 2),(SCREEN_HEIGHT // 2) - (player.rect.height // 2))