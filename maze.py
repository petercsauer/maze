import random

m = 10
n = 10


def addTwohopNeighbor(x,y,m,n,f):
    
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    if x-1>=0 and y-1>=0:
        f.append((x-1,y-1))
    if x-1>=0 and y+1<n:
        f.append((x-1,y+1))
    if x+1<m and y-1>=0:
        f.append((x+1,y-1))
    if x+1<m and y+1<n:
        f.append((x+1,y-1))
    if x+2<m:
        f.append((x+2,y))
    if x-2>=0:
        f.append((x-2,y))
    if y+2<n:
        f.append((x,y+2))
    if y-2>=0:
        f.append((x,y-2))

    return f

def addTwohopWalls(x,y,m,n,f):
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    if x-1>=0 and y-1>=0:
        if x-1==0 or y-1==0:
            f.append((x-1,y-1))
    if x-1>=0 and y+1<n:
        if x-1==0 or y+1==n-1:
            f.append((x-1,y+1))
    if x+1<m and y-1>=0:
        if x+1==m-1 or y-1==0:
            f.append((x+1,y-1))
    if x+1<m and y+1<n:
        if x+1==m-1 or y+1==n-1:
            f.append((x+1,y-1))
    if x+2==m-1:
        f.append((x+2,y))
    if x-2==0:
        f.append((x-2,y))
    if y+2==n-1:
        f.append((x,y+2))
    if y-2==0:
        f.append((x,y-2))
     
    return f

def printMaze(m):

    for row in m:
        for col in row:
            print(col,end='')
        print()

def createmaze(m,n):
    frontier = []

    maze = [['#']*m]*n
    print(maze)

    rand_x = random.randint(0,m-1)
    rand_y = random.randint(0,n-1)
    maze[rand_x][rand_y] = ' '
    frontier = addTwohopNeighbor(rand_x,rand_y,m,n,frontier)

    while len(frontier) > 0:
        neighbors = []
        cellC = frontier[random.randint(0,len(frontier)-1)]
        neighbors = addTwohopNeighbor(cellC[0],cellC[1],m,n,neighbors)
        cellF=neighbors[random.randint(0,len(frontier)-1)]
        cellA=[int(abs((cellC[0]-cellF[0])/2)),int(abs((cellC[1]-cellF[1])/2))]
        maze[cellA[0]][cellA[1]]=' '
        frontier.remove(cellC)
        frontier=addTwohopWalls(cellA[0],cellA[1],m,n,frontier)

    print(maze)
    printMaze(maze)

createmaze(m,n)




    
        

    