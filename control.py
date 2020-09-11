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
    for m in mazeString:
        line = split(m.rstrip("\n"))
        maze.append(line)
    return maze
    
importMaze(readMaze())

n_block_width = 15
n_block_height = 30
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
                    pygame.draw.rect(screen,(0,0,255),rect,0)

                elif maze[i][j] == 'E':
                    #draw target end point
                    pygame.draw.rect(screen,(255,165,0),rect,0)

                elif maze[i][j] == '#':
                    pygame.draw.rect(screen,(120,120,120),rect,0)
                    
                elif maze[i][j] == '+':
                    pygame.draw.rect(screen,(255,0,0),rect,0)

                elif maze[i][j] == ' ':
                    pygame.draw.rect(screen,(0,0,0),rect,0)

                
                pygame.draw.rect(screen,(200,200,200),rect,1)

while True:
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

