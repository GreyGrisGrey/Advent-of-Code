class Node:
    def __init__(self, sym):
        self.sym = sym
        self.x = None
        self.y = None
        self.adj = [None, None, None, None]
    
    def addCoords(self, x, y):
        self.x = x
        self.y = y
    
    def addAdj(self, N, W, S, E):
        self.adj = [N, W, S, E]
    
    def changeSym(self, sym):
        self.sym = sym
    
    def pushDir(self, dirInt):
        if self.sym == "O" and self.adj[dirInt] != None and self.adj[dirInt].getSym() == ".":
            self.sym = "."
            self.adj[dirInt].changeSym("O")
            return True
        return False
    
    def getSym(self):
        return self.sym
    
    def getCoords(self):
        return self.x, self.y

def tiltGrid(gridDict, direction, size):
    for i in range(size):
        for j in gridDict:
            gridDict[j].pushDir(direction)

def tiltGrid2(gridDict, direction, size):
    for i in range(size):
        for j in range(size):
            if direction == 2: name = str(j) + ":" + str(size - (i+1))
            elif direction == 3: name = str(size - (j+1)) + ":" + str(i)
            else: name = str(j) + ":" + str(i)
            count = 1
            while name in gridDict and gridDict[name].pushDir(direction):
                if direction == 0: name = str(j) + ":" + str(i-count)
                elif direction == 1: name = str(j-count) + ":" + str(i)
                elif direction == 2: name = str(j) + ":" + str(size + count - (i+1))
                else: name = str(size + count -(j+1)) + ":" + str(i)
                count += 1

def countWeight(gridDict):
    total = 0
    for i in gridDict:
        total += 0 if gridDict[i].getSym() != "O" else gridDict[i].getCoords()[1]
    return total

def printDict(gridDict, size):
    for i in range(size):
        printLine = ""
        for j in range(size):
            printLine += gridDict[str(j) + ":" + str(i)].getSym()
        print(printLine)

def position(gridDict, size):
    pos = ""
    for i in range(size):
        for j in range(size):
            pos += gridDict[str(j) + ":" + str(i)].getSym()
    return pos

def determineLoop(pos, posDict, currNum):
    curr = pos
    step = 0
    flag = True
    while curr != pos or flag:
        flag = False
        curr = posDict[curr + ":" + str((currNum+step)%4)]
        step += 1
    return step

def partBoth(fileName, tilts):
    gridDict = {}
    y = 0
    for i in open(fileName, "r"):
        x = 0
        for j in i:
            if j != "\n":
                gridDict[str(x) + ":" + str(y)] = Node(j)
            x += 1
        maxX = x
        y += 1
    maxY = y
    for i in range(maxY):
        for j in range(maxX):
            north = None if (str(j) + ":" + str(i-1) not in gridDict) else gridDict[str(j) + ":" + str(i-1)]
            south = None if (str(j) + ":" + str(i+1) not in gridDict) else gridDict[str(j) + ":" + str(i+1)]
            east = None if (str(j+1) + ":" + str(i) not in gridDict) else gridDict[str(j+1) + ":" + str(i)]
            west = None if (str(j-1) + ":" + str(i) not in gridDict) else gridDict[str(j-1) + ":" + str(i)]
            gridDict[str(j) + ":" + str(i)].addAdj(north, west, south, east)
            gridDict[str(j) + ":" + str(i)].addCoords(maxX - j, maxY - i)
    posDict = {}
    prevPos = position(gridDict, maxY)
    for i in range(tilts):
        if prevPos + ":" + str(i%4) in posDict:
            loopSize = determineLoop(prevPos, posDict, i)
            steps = (tilts - i) % loopSize
            for j in range(steps):
                tiltGrid2(gridDict, (i+j)%4, maxY)
            break
        else:
            tiltGrid2(gridDict, i%4, maxY)
            newPos = position(gridDict, maxY)
            posDict[prevPos + ":" + str(i%4)] = newPos
            prevPos = newPos
    return countWeight(gridDict)
    
    
print(partBoth("in.txt", 1))
print(partBoth("in.txt", 4000000000))