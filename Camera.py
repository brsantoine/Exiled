from settings import *

class Camera:
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def draw(self, win, player, displayList, enemyHitboxList, mapWidth, mapHeight):

        """Afficher les elements a l'ecran et bouger la camera en fonction de la position du joueur"""
        cameraX = player.rect.left + (player.rect.width // 2) - (SCREEN_WIDTH // 2)
        cameraY  = player.rect.top + (player.rect.height // 2) - (SCREEN_HEIGHT // 2)

        # On centre la camera tant que le joueurs n'atteind pas les bords
        if  cameraX >=  0 and cameraX < mapWidth - SCREEN_WIDTH:
            self.x = cameraX

        if  cameraY >= 0 and cameraY < mapHeight - SCREEN_HEIGHT:
            self.y = cameraY

        # Calcul de l'X du joueur en fonction s'il est en haut, bas ou entre les 2
        if cameraX >= 0  and cameraX < mapWidth - SCREEN_WIDTH:
            playerX = (SCREEN_WIDTH // 2) - (player.rect.width // 2)
        else:
            # Si le joueur est a droite"""
            if cameraX >= mapWidth - SCREEN_WIDTH:
                self.x = mapWidth - SCREEN_WIDTH
                playerX = player.rect.left - mapWidth + SCREEN_WIDTH
            # Si le joueur est a gauche"""
            else:
                self.x = 0
                playerX = player.rect.left


        # Calcul de l'Y du joueur en fonction s'il est a gauche, droite ou entre les 2
        if cameraY >= 0 and cameraY < mapHeight - SCREEN_HEIGHT:
            playerY = (SCREEN_HEIGHT // 2) - (player.rect.height // 2)
        else:
            # Si le joueur est en dessous
            if cameraY >= mapHeight - SCREEN_HEIGHT:
                self.y = mapHeight - SCREEN_HEIGHT
                playerY = player.rect.top - mapHeight + SCREEN_HEIGHT
            # Si le joueur est au dessus    
            else:
                self.y = 0
                playerY = player.rect.top

        for element in displayList:
            element.draw(win,element.rect.left - self.x,element.rect.top - self.y)
        for elem in enemyHitboxList:
            pg.draw.rect(win, (200, 200, 200), pg.Rect(elem.left - self.x,elem.top - self.y, elem.width, elem.height))
        player.draw(win, playerX, playerY)
