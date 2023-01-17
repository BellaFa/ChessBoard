import pygame, sys
from pygame.locals import *
import board

# global 
IMAGES ={}
SIZE = 50
SCREENSIZE = 400
GREEN = (85,107,47)
WHITE = (255,255,240)
currSquare = [(0),(0),(0)]
preSquare = [(0),(0),(1)]

# set up board squares
def drawBoard(DISPLAYSURF):
    x=0
    y =0 
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if(j %2 ==0):
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, SIZE, SIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, SIZE, SIZE))
            else:
                if(j %2 == 0):
                    pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, SIZE, SIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, SIZE, SIZE))
            y+= SIZE
        x+= SIZE
        y=0
 
def highlight(DISPLAYSURF, board):

    # find the top left coordinate of the square the cursor is hovering over
    x = pygame.mouse.get_pos()[0] 
    y = pygame.mouse.get_pos()[1]
    if x < SIZE: x = 0
    else: x = x - (x % SIZE) 
    if y < SIZE: y = 0
    else: y = y - (y % SIZE) 
    
    # highlight square
    color =  DISPLAYSURF.get_at((x, y))[:3]
    if color == WHITE:
        pygame.draw.rect(DISPLAYSURF, (225,225,225) , (x, y, SIZE, SIZE))
        currSquare[2] = 1
        drawPieces(board,DISPLAYSURF)

    if color == GREEN:
        pygame.draw.rect(DISPLAYSURF, (60,78,33), (x, y, SIZE, SIZE))
        currSquare[2] = 0
        drawPieces(board,DISPLAYSURF)

    currSquare[0] = x
    currSquare[1] = y

    # revert square to normal when cursor leaves it
    if currSquare[0] != preSquare[0] or currSquare[1] != preSquare[1]:
        if preSquare[2] == 1:
            pygame.draw.rect(DISPLAYSURF, WHITE , (preSquare[0], preSquare[1], SIZE, SIZE))
            drawPieces(board,DISPLAYSURF)
        if preSquare[2] == 0:
            pygame.draw.rect(DISPLAYSURF, GREEN, (preSquare[0], preSquare[1], SIZE, SIZE))
            drawPieces(board,DISPLAYSURF)
        preSquare[0] = x
        preSquare[1] = y
        preSquare[2] = currSquare[2]
        

def loadImages():
    pieces = ['bB','bK','bN','bp','bQ','bR','wB','wK','wN','wp','wQ','wR']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"),(SIZE,SIZE))

def drawPieces(b, display):
    posX =0
    posY =0
    for r in range (8):
        for c in range (8):
            piece = b[r][c]
            if(piece != 'N'): display.blit(IMAGES[piece],(posY,posX)) 
            posY+=SIZE
        posX+= SIZE
        posY =0
        





def main():

    # set up the screen
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption('Chess Game')

    # draw board, load images, initialize game object
    drawBoard(DISPLAYSURF)
    loadImages()
    game = board.Game(board.initialBoard,board.initialUsed)
   
    # draw pieces
    drawPieces(game.b,DISPLAYSURF)

    # game loop
    while True:
        for event in pygame.event .get():

            # update highlighted squares from cursor location
            highlight(DISPLAYSURF,game.b)

            # If mouse button is down find square that's been clicked
            if event.type == MOUSEBUTTONDOWN:
                 x = pygame.mouse.get_pos()[0] 
                 y = pygame.mouse.get_pos()[1]
            if event.type == MOUSEBUTTONUP: # find square the mouse is released on
                newX = pygame.mouse.get_pos()[0] 
                newY = pygame.mouse.get_pos()[1]
                coords = board.updateBoardPosition(SIZE,x,y,newX,newY) 
                # if valid
                game.updateP(coords) # update position array
                
                drawBoard(DISPLAYSURF)
                drawPieces(game.b,DISPLAYSURF)

                


            if(event.type == QUIT):
                pygame.quit()
                sys.exit()
            pygame.display.update()

if __name__ == "__main__":
    main()