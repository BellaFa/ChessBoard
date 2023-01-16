import pygame, sys
from pygame.locals import *
import gamePieces

# set up the screen
pygame.init()
DISPLAYSURF = pygame.display.set_mode(  (800,800))
pygame.display.set_caption('Chess Game')

# initialize colors
GREEN = (85,107,47)
WHITE = (255,255,240)

# set up board squares
x=0
y =0 
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if(j %2 ==0):
                pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, 100, 100))
            else:
                pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, 100, 100))
        else:
            if(j %2 == 0):
                pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, 100, 100))
            else:
                pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, 100, 100))
        y+= 100
    x+= 100
    y=0
 
currSquare = [(0),(0),(0)]
preSquare = [(0),(0),(1)]



def highlight():

    # find the top left coordinate of the square the cursor is hovering over
    x = pygame.mouse.get_pos()[0] 
    y = pygame.mouse.get_pos()[1]
    if x < 100: x = 0
    else: x = x - (x % 100) 
    if y < 100: y = 0
    else: y = y - (y % 100) 
    
    # highlight square
    color =  DISPLAYSURF.get_at((x, y))[:3]
    if color == WHITE:
        pygame.draw.rect(DISPLAYSURF, (225,225,225) , (x, y, 100, 100))
        currSquare[2] = 1
    if color == GREEN:
        pygame.draw.rect(DISPLAYSURF, (60,78,33), (x, y, 100, 100))
        currSquare[2] = 0


    currSquare[0] = x
    currSquare[1] = y

    # revert square to normal when cursor leaves it
    if currSquare[0] != preSquare[0] or currSquare[1] != preSquare[1]:
        if preSquare[2] == 1:
            pygame.draw.rect(DISPLAYSURF, WHITE , (preSquare[0], preSquare[1], 100, 100))
        if preSquare[2] == 0:
            pygame.draw.rect(DISPLAYSURF, GREEN, (preSquare[0], preSquare[1], 100, 100))
        preSquare[0] = x
        preSquare[1] = y
        preSquare[2] = currSquare[2]
        






# game loop
while True:
    for event in pygame.event .get():

        # update highlighted squares from cursor location
        highlight()
       
        
        
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        pygame.display.update()