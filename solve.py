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
    maze = []
    for x in mazeString:
        line = split(x.rstrip("\n"))
        maze.append(line)
    return maze

printMaze(importMaze(readMaze()))