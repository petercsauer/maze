import sys, pygame

pygame.init()

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
importMaze(readMaze())


def findPath(m,n,x,y,goal_x,goal_y):
    if (x,y) in visited:
        return False
    visited.append((x,y))
    #base case
    if x < 0 or x > m-1 or y < 0 or y > n-1:
        return False
    
    if x == goal_x and y == goal_y:
        return True
    
    if maze[x][y] == '#':
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

m = len(maze)
n = len(maze[0])

findPath(m,n,start[0],start[1],end[0],end[1])
maze[start[0]][start[1]]='S'




n_block_width = m
n_block_height = n
blockSize = 20
width, height = n_block_width*blockSize, n_block_height*blockSize
screen = pygame.display.set_mode((width,height))
screen.fill((0,0,0))

def drawGrid():
        
        for i in range(n_block_width):
            for j in range(n_block_height):
                rect = pygame.Rect(i*blockSize,j*blockSize,blockSize,blockSize)
                

                if maze[i][j] == 'S':
                    #draw origin
                    pygame.draw.rect(screen,(119, 141, 169),rect,0)

                elif maze[i][j] == 'E':
                    #draw target end point
                    pygame.draw.rect(screen,(119, 141, 169),rect,0)

                elif maze[i][j] == '#':
                    pygame.draw.rect(screen,(65, 90, 119),rect,0)
                    
                elif maze[i][j] == '+':
                    pygame.draw.rect(screen,(224, 225, 221),rect,0)

                elif maze[i][j] == ' ':
                    pygame.draw.rect(screen,(13, 27, 42),rect,0)

                
                pygame.draw.rect(screen,(27, 38, 59),rect,1)

while True:
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
