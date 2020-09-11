import random

m = 15
n = 30
maze=[]

def addTwohopNeighbor(x,y,m,n,f):
    
    global maze
    if x+2<m:
        if maze[x+2][y]=='#':
            if (x+2,y) not in f:
                f.append((x+2,y))
    if x-2>=0:
        if maze[x-2][y]=='#':
            if (x-2,y) not in f:
                f.append((x-2,y))
    if y+2<n:
        if maze[x][y+2]=='#':
            if (x,y+2) not in f:
                f.append((x,y+2))
    if y-2>=0:
        if maze[x][y-2]=='#':
            if (x,y-2) not in f:
                f.append((x,y-2))

    return f

def addTwohopWalls(x,y,m,n,f,maze):
    if x+2<m:        
        if (x+2,y) not in f:
            f.append((x+2,y))
    if x-2>=0:
    
        if (x-2,y) not in f:
            f.append((x-2,y))
    if y+2<n:
        
        if (x,y+2) not in f:
            f.append((x,y+2))
    if y-2>=0:
        
        if (x,y-2) not in f:
            f.append((x,y-2))
     
    return f

def printMaze(m):

    for row in m:
        for col in row:
            print(col,end='')
        print()
    print()

def pickRandSE(m,n):
    x=random.randint(0,m-1)
    y=random.randint(0,n-1)
    x2=random.randint(0,m-1)
    y2=random.randint(0,n-1)
    while maze[x][y]=='#':
        x=random.randint(0,m-1)
        y=random.randint(0,n-1)
    while maze[x2][y2]=='#' or (x,y)==(x2,y2):
        x2=random.randint(0,m-1)
        y2=random.randint(0,n-1)
    return (x,y,x2,y2)

def createmaze(m,n):
    frontier = []

    for x in range(0,m):
        maze.append([])
        for y in range(0,n):
            maze[x].append('#')
    rand_x = random.randint(0,m-1)
    rand_y = random.randint(0,n-1)
    maze[rand_x][rand_y] = ' '
    frontier = addTwohopNeighbor(rand_x,rand_y,m,n,frontier)

    while len(frontier)>0:
        neighbors = []
        cellC = frontier[random.randint(0,len(frontier)-1)]
        neighbors = addTwohopWalls(cellC[0],cellC[1],m,n,neighbors, maze)

        while len(neighbors)>0:
            cellF=neighbors[random.randint(0,len(neighbors)-1)]
            if maze[cellF[0]][cellF[1]]==' ':
                break
            else:  
                neighbors.remove(cellF)
               
        cellA=[int(abs((cellC[0]+cellF[0])/2)),int(abs((cellC[1]+cellF[1])/2))]
     
        maze[cellA[0]][cellA[1]]=' '
        maze[cellC[0]][cellC[1]]=' '
        frontier.remove(cellC)
        frontier=addTwohopNeighbor(cellC[0],cellC[1],m,n,frontier)
    
    startAndEnd = pickRandSE(m,n)
    maze[startAndEnd[0]][startAndEnd[1]]='S'
    maze[startAndEnd[2]][startAndEnd[3]]='E'


    return maze



def writeMaze():
    f = open("maze.txt", "a")
    for m in maze:
        line = ''.join(m)
        f.write(line)
        f.write('\n')
    f.close


createmaze(m,n)
writeMaze()
# frontier = []

# frontier = addTwohopNeighbor(1,1,m,n,frontier)

# print(frontier)

    
        

    