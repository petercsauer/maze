
maze = []
visited=[]

def printMaze(m):
    for row in m:
        for col in row:
            print(col,end='')
        print()
    print()

def readMaze():
    f = open('maze.txt', 'r')
    mazeStrings=f.readlines()
    return mazeStrings

def split(word): 
    return [char for char in word]  

def importMaze(mazeString):
    for x in mazeString:
        line = split(x.rstrip("\n"))
        maze.append(line)
    return maze
printMaze(importMaze(readMaze()))
print(maze)


def findPath(m,n,x,y,goal_x,goal_y):
    if (x,y) in visited:
        return False
    visited.append((x,y))
    #base case
    if x < 0 or x > m-1 or y < 0 or y > n-1:
        print("edge")
        return False
    
    if x == goal_x and y == goal_y:
        return True
    print(x,y)
    if maze[x][y] == '#':
        print("wall")
        return False


    #mark x,y as part of solution path
    maze[x][y] = '+'

    #recursive case
    if findPath(m,n,x,y-1,goal_x,goal_y) == True:
        return True
    
    if findPath(m,n,x+1,y,goal_x,goal_y) == True:
        return True

    if findPath(m,n,x,y+1,goal_x,goal_y) == True:
        return True

    if findPath(m,n,x-1,y,goal_x,goal_y) == True:
        return True

    #unmark x,y
    maze[x][y] = ' '

    return False

def getStart():
    for m in range(len(maze)):
        for n in range(len(maze[m])):
            if maze[m][n] == 'S':
                return (m,n)

def getEnd():
    for m in range(len(maze)):
        for n in range(len(maze[m])):
            if maze[m][n] == 'E':
                return (m,n)

start = getStart()
end = getEnd()

findPath(15,30,start[0],start[1],end[0],end[1])
maze[start[0]][start[1]]='S'
printMaze(maze)