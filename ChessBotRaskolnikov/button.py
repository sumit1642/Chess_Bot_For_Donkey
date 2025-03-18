from settings import *
vec = py.math.Vector2
class Button():
    def __init__(self,game,x,y,w,h,text):
        self.game = game
        self.text = text
        self.rect = py.Rect(x,y,w,h)
        self.color = (20,20,20)
        self.game.all_buttons.append(self)
    def show(self):
        mos = vec(py.mouse.get_pos())
        if self.rect.x < mos.x  < self.rect.right and self.rect.y < mos.y < self.rect.bottom:
            self.color = (200,50,36)
        else:
            self.color = (20,20,20)
        py.draw.rect(self.game.screen,self.color,self.rect)
        self.game.draw_text(self.text,int(self.rect.width/(len(self.text)+1))*2,white,self.rect.centerx,self.rect.centery)
    def clicked(self):
        clicked = py.mouse.get_pressed()[0]

        #clicked = False
        
        if clicked:
            pos = vec(py.mouse.get_pos())
            if self.rect.left < pos.x < self.rect.right and  self.rect.top < pos.y < self.rect.bottom:
                return True 
        return False

def counterToCoord(count):
    y = 7-int(count/8) 
    x = count % 8
   
    return (x,y)
def coordToCounter(t):
    x = int((t[0]-offx)/tileSize)
    y = 7-int((t[1]-offy)/tileSize)

    return (x + y*8)

def posToCounter(pos):
    t = {"a":7,
         "b":6,
         "c":5,
         "d":4,
         "e":3,
         "f":2,
         "g":1,
         "h":0}
    x = t[pos[0]]
    y = int(pos[1])-1
    return x*8 + y

def counterToPos(count):
    x = int(count%8)
    y = int(count/8) + 1
    
    t = "abcdefgh"

    return t[x] + str(y)




