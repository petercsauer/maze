import random

m = 5
n = 5
visited = []

def addOnehopNeighbor(x,y,m,n,f):
    
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    # if x-1>=0 and y-1>=0:
    #     f.append((x-1,y-1))
    # if x-1>=0 and y+1<n:
    #     f.append((x-1,y+1))
    # if x+1<m and y-1>=0:
    #     f.append((x+1,y-1))
    # if x+1<m and y+1<n:
    #     f.append((x+1,y+1))
    global maze
    if x+1<m:
        if maze[x+1][y]=='#':
            if (x+1,y) not in f:
                f.append((x+1,y))
    if x-1>=0:
        if maze[x-1][y]=='#':
            if (x-1,y) not in f:
                f.append((x-1,y))
    if y+1<n:
        if maze[x][y+1]=='#':
            if (x,y+1) not in f:
                f.append((x,y+1))
    if y-1>=0:
        if maze[x][y-1]=='#':
            if (x,y-1) not in f:
                f.append((x,y-1))

    return f

def addTwohopWalls(x,y,m,n,f,maze):
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    # if x-1>=0 and y-1>=0:
    #     if maze[x-1][y-1]=='#':
    #         if (x-1,y-1) not in f:
    #             f.append((x-1,y-1))
    # if x-1>=0 and y+1<n:
    #     if maze[x-1][y+1]=='#':
    #         if (x-1,y+1) not in f:
    #             f.append((x-1,y+1))
    # if x+1<m and y-1>=0:
    #     if maze[x+1][y-1]=='#':
    #         if (x+1,y-1) not in f:
    #             f.append((x+1,y-1))
    # if x+1<m and y+1<n:
    #     if maze[x+1][y+1]=='#':
    #         if (x+1,y+1) not in f:
    #             f.append((x+1,y+1))
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

def printMaze(m):

    for row in m:
        for col in row:
            print(col,end='')
        print()
    print()

def twoAwayHelper(cellC, cellF, m, n):
    if (cellF[0]-cellC[0])>0 and cellF[0]+1<m:
        return (cellF[0]+1,cellF[1])
    if (cellF[0]-cellC[0])<0 and cellF[0]-1>=0:
        return (cellF[0]-1,cellF[1])
    if (cellF[1]-cellC[1])>0 and cellF[1]+1<n:
        return (cellF[0],cellF[1]+1)
    if (cellF[1]-cellC[1])<0 and cellF[1]-1>=0:
        return (cellF[0],cellF[1]-1)
    return False

def createmaze(m,n):
    frontier = []


    #maze = [['#'] * m for i in range(n)]
    for x in range(0,m):
        maze.append([])
        for y in range(0,n):
            maze[x].append('#')
    printMaze(maze)
    rand_x = random.randint(0,m-1)
    rand_y = random.randint(0,n-1)
    maze[rand_x][rand_y] = ' '
    frontier = addOnehopNeighbor(rand_x,rand_y,m,n,frontier)
    visited.append((rand_x,rand_y))

    while len(frontier)>0:
        neighbors = []
        print(frontier)
        cellC = frontier[random.randint(0,len(frontier)-1)]
        visited.append(cellC)
        neighbors = addOnehopNeighbor(cellC[0],cellC[1],m,n,neighbors)

        while len(neighbors)>0:
            cellF=neighbors[random.randint(0,len(neighbors)-1)]
            if twoAwayHelper(cellC, cellF, m, n):
                if (twoAwayHelper(cellC, cellF, m, n)[0],twoAwayHelper(cellC, cellF, m, n)[1]) in visited:
                    neighbors.remove(cellF)
                else:  
                    break
        frontier.remove(cellC)
        visited.append(cellF)
        maze[cellF[0]][cellF[1]]=' '
        frontier = addOnehopNeighbor(cellF[0],cellF[1],m,n,frontier)
       


    printMaze(maze)



maze = []
createmaze(m,n)


    
        

    