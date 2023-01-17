initialBoard = [['bR','bN', 'bB', 'bQ', 'bK','bB','bN','bR'],
            ['bp', 'bp','bp', 'bp','bp','bp','bp','bp'],
            ['N', 'N', 'N', 'N','N','N','N','N'],
            ['N', 'N', 'N', 'N','N','N','N','N'],
            ['N', 'N', 'N', 'N','N','N','N','N'],
            ['N', 'N', 'N', 'N','N','N','N','N'],
            ['wp', 'wp', 'wp', 'wp','wp','wp','wp','wp'],
            ['wR','wN', 'wB', 'wQ', 'wK','wB','wN','wR']]

initialUsed = [[1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]

class Game: 
    def __init__(self, board,used):
        self.b = board
        self.u = used

    def updateP(cls,coords):
        cls.b[coords[3]][coords[2]] = cls.b[coords[1]][coords[0]]
        cls.b[coords[1]][coords[0]] = 'N'
        
    

def updateBoardPosition(SIZE,x,y,newX,newY):
    # left coordinate position of square pressed
    if x < SIZE: x = 0
    else: x = x - (x % SIZE) 
    if y < SIZE: y = 0
    else: y = y - (y % SIZE)

    # left coordinate position of square released on 
    if newX < SIZE: newX = 0
    else: newX = newX - (newX % SIZE) 
    if newY < SIZE: newY = 0
    else: newY = newY - (newY % SIZE)

    # Find array index location
    fX = int(x/SIZE)
    fY = int(y/SIZE)

    sX = int(newX/SIZE)
    sY = int(newY/SIZE)

    return fX,fY,sX,sY
    