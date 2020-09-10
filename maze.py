import random

m = 5
n = 5


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

def addTwohopWalls(x,y,m,n,f,maze):
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    if x-1>=0 and y-1>=0:
        if maze[x-1][y-1]=='#':
            f.append((x-1,y-1))
    if x-1>=0 and y+1<n:
        if maze[x-1][y+1]=='#':
            f.append((x-1,y+1))
    if x+1<m and y-1>=0:
        if maze[x+1][y-1]=='#':
            f.append((x+1,y-1))
    if x+1<m and y+1<n:
        if maze[x+1][y+1]=='#':
            f.append((x+1,y-1))
    if x+2<m:
        if maze[x+2][y]=='#':
            f.append((x+2,y))
    if x-2>=0:
        if maze[x-2][y]=='#':
            f.append((x-2,y))
    if y+2<n:
        if maze[x][y+2]=='#':
            f.append((x,y+2))
    if y-2>=0:
        if maze[x][y-2]=='#':
            f.append((x,y-2))
     
    return f

def printMaze(m):

    for row in m:
        for col in row:
            print(col,end='')
        print()
    print()

def createmaze(m,n):
    frontier = []

    maze = [['#']*m]*n
    printMaze(maze)
    rand_x = random.randint(0,m-1)
    rand_y = random.randint(0,n-1)
    maze[rand_x][rand_y] = ' '
    frontier = addTwohopNeighbor(rand_x,rand_y,m,n,frontier)

    while len(frontier) > 0:
        neighbors = []
        cellC = frontier[random.randint(0,len(frontier)-1)]
        neighbors = addTwohopNeighbor(cellC[0],cellC[1],m,n,neighbors)
        free = False
        while not free:
            cellF=neighbors[random.randint(0,len(neighbors)-1)]
            if maze[cellF[0]][cellF[1]]==' ':
                free=True
        cellA=[int(abs((cellC[0]+cellF[0])/2)),int(abs((cellC[1]+cellF[1])/2))]
        maze[cellA[0]][cellA[1]]=' '
        frontier.remove(cellC)
        frontier=addTwohopWalls(cellA[0],cellA[1],m,n,frontier,maze)
        printMaze(maze)

    # print(maze)
    printMaze(maze)

createmaze(m,n)
# frontier = []

# frontier = addTwohopNeighbor(1,1,m,n,frontier)

# print(frontier)

    
        

    