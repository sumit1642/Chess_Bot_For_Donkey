# ChessBotRaskolnikov/main.py
import pygame as py
import time
from functions import *


class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((width, height))
        self.clock = py.time.Clock()
        self.font = py.font.match_font("arial")

    def new(self):
        self.globalTime = time.time()
        self.whiteMove = True
        self.moveCount = 0
        self.pieces = py.sprite.Group()

        self.all_buttons = []
        b = Button(self, 800, 100, 70, 20, "print")
        self.board = [None] * 64

        # sfenToBoard(self,self.board,"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.board = fenToBoard(
            self,
            self.board,
            "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2",
        )

    def update(self):
        for p in self.pieces:
            p.update()
        if self.all_buttons[0].clicked():
            print("Starting....")
            for i in self.board:
                if i:
                    print(i.type, i.boardCounter, i.boardPos)
                else:
                    print("n")

    def draw(self):
        self.screen.fill(bgcolor)
        # draw chessboard
        x, y0 = offx, offy
        r = py.Rect(0, 0, 0, 0)
        for i in range(8):
            y = y0 + tileSize * i
            for j in range(8):
                l = x + tileSize * j
                t = y
                r.left = l
                r.top = t
                r.width = tileSize
                r.height = tileSize

                # draw

                py.draw.rect(self.screen, boardColors[(i + j) % 2], r)
                """if self.board[i*8+j]:
                    c = self.board[i*8+j].type
                else:
                    c = "n"
                self.draw_text(c,int(tileSize/2),white,l+tileSize/2,t)"""

                # self.draw_text(counterToPos(i*8 + j) + str(i*8 + j),int(tileSize/2),white,l+tileSize/2,t)
                # print(r.left)
                # py.draw.rect(self.screen,boardColors[0],py.Rect(100,100,500,500),10)
        # drawing piecce

        self.pieces.draw(self.screen)
        # turns
        if self.whiteMove:
            self.draw_text("White to move", 60, white, 800, 100)
        else:
            self.draw_text("black to move", 60, white, 800, 100)

        # draw button
        for i in self.all_buttons:
            i.show()

        py.display.flip()


def makeMove(self, startCounter, endCounter):
    s = startCounter
    e = endCounter

    print(f"Trying to move from {counterToPos(s)} to {counterToPos(e)}...")

    if not (0 <= s < len(self.board)) or not (0 <= e < len(self.board)):
        print("❌ Invalid move! Out of bounds.")
        return

    tempPiece = self.board[s]
    if tempPiece is None:
        print("❌ No piece at the starting position!")
        return

    print(f"✅ Moving {tempPiece} to {counterToPos(e)}")

    self.board[s] = None  # Remove piece from the start position

    if self.board[e]:
        print(f"💥 Capturing {self.board[e]} at {counterToPos(e)}")
        self.board[e].kill()

    self.board[e] = tempPiece  # Move the piece
    print(f"🎉 Move complete! {tempPiece} is now at {counterToPos(e)}")

    self.moveCount += 1
    self.whiteMove = not self.whiteMove
    print(
        f"➡️ Move #{self.moveCount} | {'White' if self.whiteMove else 'Black'} to move."
    )

    def run(self):
        m = [[63, 62], [56, 57], [48, 49]]
        while True:
            self.update()
            self.draw()
            self.events()
            # black
            if not self.whiteMove and len(m) > 0:
                self.makeMove(m[0][0], m[0][1])
                m.remove(m[0])
            self.dt = 1 / max(0.001, (time.time() - self.globalTime))
            py.display.set_caption(str(round(self.dt, 3)))
            self.globalTime = time.time()

    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                for piece in self.pieces:
                    piece.checkSelection()

    def draw_text(self, text, size, color, x, y):
        font = py.font.Font(self.font, size)
        text = str(text)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def quit(self):
        py.quit()
        exit()


g = Game()
g.new()
g.run()
