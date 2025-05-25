class Node:
    def __init__(self, sym):
        self.sym = sym
    
    def parseLaser(self, laser):
        if self.sym == "/":
            if laser[2] == 0: laser[2] = 1
            elif laser[2] == 3: laser[2] = 2
            elif laser[2] == 2: laser[2] = 3
            else: laser[2] = 0
        elif self.sym == "\\":
            if laser[2] == 0: laser[2] = 3
            elif laser[2] == 3: laser[2] = 0
            elif laser[2] == 2: laser[2] = 1
            else: laser[2] = 2
        elif self.sym == "|":
            return [[laser[0], laser[1], 0], [laser[0], laser[1], 2]]
        elif self.sym == "-":
            return [[laser[0], laser[1], 1], [laser[0], laser[1], 3]]
        return [laser]

def checkIn(laser, maxX, maxY):
    if laser[0] < 0 or laser[1] < 0 or laser[0] > maxX or laser[1] > maxY:
        return False
    return True

def printGrid(grid, nodeDict):
    for i in range(len(grid)):
        printLn = ""
        for j in range(len(grid[0])):
            if grid[i][j] in nodeDict:
                printLn += "X"
            else:
                printLn += "."
        print(printLn)


def part1():
    grid = []
    for i in open("in.txt", "r"):
        gridLine = []
        for j in i:
            if j != "\n":
                gridLine.append(Node(j))
        grid.append(gridLine)
    nodeDict = {}
    keyDict = {}
    lasers = [[-1, 0, 1]]
    while len(lasers) > 0:
        newLasers = []
        for i in lasers:
            key = str(i[0]) + ":" + str(i[1]) + ":" + str(i[2])
            if key not in keyDict:
                keyDict[key] = True
                if i[0] != -1:
                    nodeDict[grid[i[1]][i[0]]] = True
                if i[2] % 2 == 0:
                    i[1] += (-1) if i[2] == 0 else 1
                else:
                    i[0] += (-1) if i[2] == 3 else 1
                if checkIn(i, len(grid[0])-1, len(grid)-1):
                    for j in grid[i[1]][i[0]].parseLaser(i):
                        newLasers.append(j)
        lasers = newLasers
    return len(nodeDict)

def part2():
    grid = []
    for i in open("in.txt", "r"):
        gridLine = []
        for j in i:
            if j != "\n":
                gridLine.append(Node(j))
        grid.append(gridLine)
    maxEnergy = 0
    for k in range(len(grid)*4):
        nodeDict = {}
        keyDict = {}
        if k % 4 == 0: lasers = [[-1, k, 1]]
        elif k % 4 == 1: lasers = [[len(grid[0]), k, 3]]
        elif k % 4 == 2: lasers = [[k, -1, 2]]
        else: lasers = [[k, len(grid), 0]]
        while len(lasers) > 0:
            newLasers = []
            for i in lasers:
                key = str(i[0]) + ":" + str(i[1]) + ":" + str(i[2])
                if key not in keyDict:
                    keyDict[key] = True
                    if i[0] != -1 and i[0] != len(grid[0]) and i[1] != -1 and i[1] != len(grid):
                        nodeDict[grid[i[1]][i[0]]] = True
                    if i[2] % 2 == 0:
                        i[1] += (-1) if i[2] == 0 else 1
                    else:
                        i[0] += (-1) if i[2] == 3 else 1
                    if checkIn(i, len(grid[0])-1, len(grid)-1):
                        for j in grid[i[1]][i[0]].parseLaser(i):
                            newLasers.append(j)
            lasers = newLasers
        if len(nodeDict) > maxEnergy:
            maxEnergy = len(nodeDict)
    return maxEnergy

print(part1())
print(part2())