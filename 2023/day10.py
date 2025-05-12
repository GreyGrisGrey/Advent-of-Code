class Node:
    def __init__(self, symb, coords):
        self.adj1 = None
        self.adj2 = None
        self.coords = coords
        self.symb = symb
    
    def setAdjBoth(self, adj1, adj2):
        self.adj1 = adj1
        self.adj2 = adj2
    
    def setAdjBefore(self, adj):
        self.adj1 = adj
    
    def setAdjNext(self, adj):
        self.adj2 = adj
    
    def getCoords(self):
        return self.coords

    def setNext(self, grid):
        prev = self.adj1.getCoords()
        if self.symb == "|":
            if prev[1] - 1 == self.coords[1]:
                new = Node(grid[self.coords[1]-1][self.coords[0]], [self.coords[0], self.coords[1]-1])
            else:
                new = Node(grid[self.coords[1]+1][self.coords[0]], [self.coords[0], self.coords[1]+1])
        elif self.symb == "-":
            if prev[0] - 1 == self.coords[0]:
                new = Node(grid[self.coords[1]][self.coords[0]-1], [self.coords[0]-1, self.coords[1]])
            else:
                new = Node(grid[self.coords[1]][self.coords[0]+1], [self.coords[0]+1, self.coords[1]])
        elif self.symb == "J":
            if prev[0] == self.coords[0]:
                new = Node(grid[self.coords[1]][self.coords[0]-1], [self.coords[0]-1, self.coords[1]])
            else:
                new = Node(grid[self.coords[1]-1][self.coords[0]], [self.coords[0], self.coords[1]-1])
        elif self.symb == "L":
            if prev[0] == self.coords[0]:
                new = Node(grid[self.coords[1]][self.coords[0]+1], [self.coords[0]+1, self.coords[1]])
            else:
                new = Node(grid[self.coords[1]-1][self.coords[0]], [self.coords[0], self.coords[1]-1])
        elif self.symb == "F":
            if prev[0] == self.coords[0]:
                new = Node(grid[self.coords[1]][self.coords[0]+1], [self.coords[0]+1, self.coords[1]])
            else:
                new = Node(grid[self.coords[1]+1][self.coords[0]], [self.coords[0], self.coords[1]+1])
        elif self.symb == "7":
            if prev[0] == self.coords[0]:
                new = Node(grid[self.coords[1]][self.coords[0]-1], [self.coords[0]-1, self.coords[1]])
            else:
                new = Node(grid[self.coords[1]+1][self.coords[0]], [self.coords[0], self.coords[1]+1])
        self.setAdjNext(new)
        new.setAdjBefore(self)
    
    def getNext(self):
        return self.adj2

def partBoth():
    grid = []
    y = 0
    x = 0
    nodeDict = {}
    start = None
    for i in open("in.txt", "r"):
        grid.append(i.strip("\n"))
        for j in i:
            nodeDict[str(y) + ":" + str(x)] = False
            if j == "S":
                start = [x, y]
            x += 1
        y += 1
        x = 0
    curr = None
    startNode = None
    step = 0
    nodeDict[str(start[1]) + ":" + str(start[0])] = True
    while (curr == None) or (curr[0].getCoords() != curr[1].getCoords()):
        if curr == None:
            startNode = Node("S", start)
            curr = [Node(grid[start[1]][start[0]-1], [start[0]-1, start[1]]), Node(grid[start[1]+1][start[0]], [start[0], start[1]+1])]
            startNode.setAdjBoth(curr[0], curr[1])
            nodeDict[str(start[1]+1) + ":" + str(start[0])] = True
            nodeDict[str(start[1]) + ":" + str(start[0]-1)] = True
            curr[0].setAdjBefore(startNode)
            curr[1].setAdjBefore(startNode)
        else:
            curr[0].setNext(grid)
            curr[1].setNext(grid)
            curr = [curr[0].getNext(), curr[1].getNext()]
            coords1 = curr[0].getCoords()
            coords2 = curr[1].getCoords()
            nodeDict[str(coords1[1]) + ":" + str(coords1[0])] = True
            nodeDict[str(coords2[1]) + ":" + str(coords2[0])] = True
        step += 1
    inSide = 0
    for i in range(len(grid)):
        currJump = 0
        downFlag = False
        upFlag = False
        for j in range(len(grid[i])):
            if nodeDict[str(i) + ":" + str(j)] and grid[i][j] == "|":
                currJump += 1
            elif nodeDict[str(i) + ":" + str(j)]:
                if (downFlag and (grid[i][j] == "L" or grid[i][j] == "J")) or (upFlag and (grid[i][j] == "F" or grid[i][j] == "7")):
                    currJump += 1
                    downFlag = False
                    upFlag = False
                elif grid[i][j] != "-" and (downFlag or upFlag):
                    downFlag = False
                    upFlag = False
                elif grid[i][j] == "F" or grid[i][j] == "7":
                    downFlag = True
                elif grid[i][j] == "L" or grid[i][j] == "J":
                    upFlag = True
            elif currJump % 2 == 1 and not nodeDict[str(i) + ":" + str(j)]:
                inSide += 1
    return step, inSide

print(partBoth())