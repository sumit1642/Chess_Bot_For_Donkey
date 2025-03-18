from button import *

class Piece(py.sprite.Sprite):
    def __init__(self,game,counter,piece):
        self.game = game
        self.type = piece
        x,y = counterToCoord(counter)[0] * tileSize + offx,counterToCoord(counter)[1] * tileSize+offy
        py.sprite.Sprite.__init__(self,self.game.pieces)
        
        pathImage = "images/" + piece + ".png"
        self.image = py.image.load(pathImage)
        self.image = py.transform.scale(self.image,(tileSize,tileSize))
        self.rect = self.image.get_rect()
        self.boardCounter = counter
       
        self.pos = vec(x,y)
        self.boardPos = counterToPos(counter)
        #togooling
        self.selected  = False
        #self.rect.center = self.po
    def checkSelection(self):
        pos = vec(py.mouse.get_pos())
        if self.rect.left < pos.x < self.rect.right and  self.rect.top < pos.y < self.rect.bottom:
                self.selected = not self.selected
    def update(self):
        self.boardPos = counterToPos(self.boardCounter)
        c = coordToCounter(self.pos)
        
        if self.selected:
            pos = py.mouse.get_pos()
            self.pos.x = pos[0] - tileSize/2
            self.pos.y = pos[1] - tileSize/2

        else:
            if c != self.boardCounter:
                self.game.makeMove(self.boardCounter,c)
                self.boardCounter = c
            self.pos.y = offy + int((self.pos.y-offy + tileSize/2)/tileSize) * tileSize
            
            self.pos.x = offx + int((self.pos.x-offx + tileSize/2)/tileSize) * tileSize
        self.rect.left = self.pos.x
        self.rect.top = self.pos.y
        
        