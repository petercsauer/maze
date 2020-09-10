import random

m = 10
n = 10
visited = []

def addTwohopNeighbor(x,y,m,n,f):
    
    #x+2, x-2, y+2, y-2, (y+1,x+1),(y-1,x-1),(y+1,x-1),(y-1,x+1)
    # if x-1>=0 and y-1>=0:
    #     f.append((x-1,y-1))
    # if x-1>=0 and y+1<n:
    #     f.append((x-1,y+1))
    # if x+1<m and y-1>=0:
    #     f.append((x+1,y-1))
    # if x+1<m and y+1<n:
    #     f.append((x+1,y+1))
    if x+2<m and oneAwayHelper(x+2,y,f):
        f.append((x+2,y))
    if x-2>=0 and oneAwayHelper(x-2,y,f):
        f.append((x-2,y))
    if y+2<n and oneAwayHelper(x,y+2,f):
        f.append((x,y+2))
    if y-2>=0 and oneAwayHelper(x,y-2,f):
        f.append((x,y-2))

    return f

def oneAwayHelper(x,y,f):
    if (x,y) not in visited:
        # (x-1,y) not in f and (x+1,y) not in f and (x,y-1) not in f and (x,y+1) not in f and (x,y)
        return True
    else:
        return False

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
            if (x+2,y) not in f and oneAwayHelper(x+2,y,f):
                f.append((x+2,y))
    if x-2>=0:
        if maze[x-2][y]=='#':
            if (x-2,y) not in f and oneAwayHelper(x-2,y,f):
                f.append((x-2,y))
    if y+2<n:
        if maze[x][y+2]=='#':
            if (x,y+2) not in f and oneAwayHelper(x,y+2,f):
                f.append((x,y+2))
    if y-2>=0:
        if maze[x][y-2]=='#':
            if (x,y-2) not in f and oneAwayHelper(x,y-2,f):
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

    maze = []
    #maze = [['#'] * m for i in range(n)]
    for x in range(0,m):
        maze.append([])
        for y in range(0,n):
            maze[x].append('#')
    printMaze(maze)
    rand_x = random.randint(0,m-1)
    rand_y = random.randint(0,n-1)
    maze[rand_x][rand_y] = 'S'
    visited.append((rand_x, rand_y))
    frontier = addTwohopNeighbor(rand_x,rand_y,m,n,frontier)

    iter = 0
    while len(frontier)>0:
        neighbors = []
        print(frontier)
        cellC = frontier[random.randint(0,len(frontier)-1)]
        visited.append(cellC)
        neighbors = addTwohopNeighbor(cellC[0],cellC[1],m,n,neighbors)
        print("neighbors:"+str(neighbors))

        while len(neighbors)>0:
            cellF=neighbors[random.randint(0,len(neighbors)-1)]
            if maze[cellF[0]][cellF[1]]==' ' or maze[cellF[0]][cellF[1]]=='S':
                break
            else:  
                neighbors.remove(cellF)
               
        cellA=[int(abs((cellC[0]+cellF[0])/2)),int(abs((cellC[1]+cellF[1])/2))]
        print("C:"+str(cellC))
        print("F:"+str(cellF))
        print("A:"+str(cellA))
        maze[cellA[0]][cellA[1]]=' '
        visited.append(cellF)
        visited.append(cellA)
        frontier.remove(cellC)
        frontier=addTwohopWalls(cellA[0],cellA[1],m,n,frontier,maze)
        printMaze(maze)
        iter+=1

    # neighbors = []
    # cellC = frontier[random.randint(0,len(frontier)-1)]
    # neighbors = addTwohopNeighbor(cellC[0],cellC[1],m,n,neighbors)
    # free = False
    # while not free:
    #     cellF=neighbors[random.randint(0,len(neighbors)-1)]
    #     if maze[cellF[0]][cellF[1]]==' ':
    #         free=True
    # cellA=[int(abs((cellC[0]+cellF[0])/2)),int(abs((cellC[1]+cellF[1])/2))]
    # maze[cellA[0]][cellA[1]]=' '
    # frontier.remove(cellC)
    # frontier=addTwohopWalls(cellA[0],cellA[1],m,n,frontier,maze)

    # print(maze)
    printMaze(maze)

createmaze(m,n)
# frontier = []

# frontier = addTwohopNeighbor(1,1,m,n,frontier)

# print(frontier)

    
        

    