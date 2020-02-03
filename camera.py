class camera(object):
    """Classe pour bouger la camera en fonction de la position du joueur dans la map"""
    def __init__(self,x,y,mapWidth,mapHeight):
        self.x = x
        self.y = y
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight

    def draw(self, win, playerX, playerY ):
        cameraX = playerX - (self.mapWidth // 2)
        cameraY = playerY - (self.mapHeight // 2) 
        if  cameraX > TAILLE_CASE and cameraX < self.mapWidth - TAILLE_CASE:
           self.x = cameraX 
           
        if  cameraY > TAILLE_CASE and cameraY < self.mapHeight - TAILLE_CASE:
           self.x = cameraY        