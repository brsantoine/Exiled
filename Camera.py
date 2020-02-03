from settings import *

class Camera(object):
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def __init__(self,mapBg):
        self.mapWidth = mapBg.get_rect().width
        self.mapHeight = mapBg.get_rect().height
        self.mapBg = mapBg
        self.x = 100
        self.y = 100

    def draw(self, win, player, list ):
        cameraX = player.rect.left + (player.rect.width // 2) - (SCREEN_WIDTH // 2)
        cameraY  = player.rect.top + (player.rect.height // 2) - (SCREEN_HEIGHT // 2) 
        if  cameraX > TAILLE_CASE and cameraX < self.mapWidth - TAILLE_CASE:
            self.x = cameraX

        if  cameraY > TAILLE_CASE and cameraY < self.mapHeight - TAILLE_CASE:
            self.y = cameraY   

        print(self.x,self.y)
        print(self.x - (player.rect.width // 2) + (SCREEN_WIDTH // 2),self.y - (player.rect.height // 2) + (SCREEN_HEIGHT // 2))
        print(player.rect)
        win.blit(self.mapBg,(-self.x,-self.y))  
        player.draw(win,(player.rect.width // 2) + (SCREEN_WIDTH // 2),(player.rect.height // 2) + (SCREEN_HEIGHT // 2))