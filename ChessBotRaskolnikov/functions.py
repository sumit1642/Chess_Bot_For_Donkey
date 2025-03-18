from piece import *

def fenToBoard(game,board,strings):
    b = board
    string = strings.split()[0]
    table = {"p" : "black-pawn",
             "n" : "black-knight",
             "r" : "black-rook",
             "b" : "black-bishop",
             "q" : "black-queen",
             "k" : "black-king",
    
             "P" : "white-pawn",
             "N" : "white-knight",
             "R" : "white-rook",
             "B" : "white-bishop",
             "Q" : "white-queen",
             "K" : "white-king"
             }
    letters =  "pnrbqkPNRBKQ"
    counter = 0
    t = string[::-1].split("/")
    for j in t:
        for i in j[::-1]:
            if i in letters:
                
                p = Piece(game,counter,table[i])
                
                b[counter] = p
                counter += 1

            else:
                if i !="/":
                    counter += int(i)
    return b


