import time
class Node:
    def __init__(self, x, y, inLoop, symbol):
        self.inLoop = inLoop
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.trapped = None
        self.Checked = False
        self.Symbol = symbol
    
    def setUp(self, nextt):
        self.up = nextt
    
    def setDown(self, nextt):
        self.down = nextt
    
    def setRight(self, nextt):
        self.right = nextt
    
    def setLeft(self, nextt):
        self.left = nextt

    def setFalse(self):
        self.trapped = False
    
    def setTrue(self):
        self.trapped = True
        self.Symbol = "O"
    
    def getLoop(self):
        return inLoop


def isntOOB(x, y, pipeMap):
    if(x < 0) or (y < 0) or (y == len(pipeMap)) or (x == len(pipeMap[y])):
        return False
    else:
        return True


def BFS(start, pipeMap):
    open = [start]
    closed = []
    isTrapped = True
    start.Checked = True
    if not start.inLoop:
        while open:
            curr = open.pop(0)
            closed.append(curr)
            if (curr.left != None) and (not curr.left.inLoop) and (not curr.left.Checked) and (not curr.left in closed):
                open.append(curr.left)
                curr.left.Checked = True
            if (curr.right != None) and (not curr.right.inLoop) and (not curr.right.Checked) and (not curr.right in closed):
                open.append(curr.right)
                curr.right.Checked = True
            if (curr.up != None) and (not curr.up.inLoop) and (not curr.up.Checked) and (not curr.up in closed):
                open.append(curr.up)
                curr.up.Checked = True
            if (curr.down != None) and (not curr.down.inLoop) and (not curr.down.Checked) and (not curr.down in closed):
                open.append(curr.down)
                curr.down.Checked = True
            if (curr.left == None):
                isTrapped = False
            if (curr.right == None):
                isTrapped = False
            if (curr.up == None):
                isTrapped = False
            if (curr.down == None):
                isTrapped = False
        for i in closed:
            i.trapped = isTrapped
            if isTrapped:
                i.Symbol = "O"
    else:
        start.Symbol = "X"


def embiggen(pipeMap):
    biggerSize = len(pipeMap) * 2 - 1
    biggerWidth = len(pipeMap[0]) * 2 - 1
    count1 = 0
    count2 = 0
    newMap = []
    while count1 < biggerSize:
        newLine = []
        count2 = 0
        while count2 < biggerWidth:
            if(count2 % 2 == 0) and (count1 % 2 == 0):
                newLine.append(pipeMap[int(count1/2)][int(count2/2)].Symbol)
            elif(count1 % 2 == 0) and count1 != biggerWidth:
                if inbetween(pipeMap[int(count1/2)][int((count2-1)/2)].Symbol, pipeMap[int((count1/2))][int(((count2-1)/2)+1)].Symbol, True):
                    newLine.append("-")
                else:
                    newLine.append(".")
            elif(count2 % 2 == 0) and count2 != biggerSize:
                if inbetween(pipeMap[int((count1-1)/2)][int(count2/2)].Symbol, pipeMap[int(((count1-1)/2)+1)][int((count2/2))].Symbol, False):
                    newLine.append("|")
                else:
                    newLine.append(".")
            else:
                newLine.append(".")
            count2 += 1
        newMap.append(newLine)
        count1 += 1
    return newMap


def inbetween(sym1, sym2, horizontal):
    if horizontal:
        horizontal1 = ["F", "-", "L", "S"]
        horizontal2 = ["J", "-", "7", "S"]
        if (sym1 in horizontal1) and (sym2 in horizontal2):
            return True
        else:
            return False
    else:
        vertical1 = ["F", "|", "7", "S"]
        vertical2 = ["J", "|", "L", "S"]
        if (sym1 in vertical1) and (sym2 in vertical2):
            return True
        else:
            return False


def part1():
    f = open("AoC10Test.txt", "r")
    pipeMap = []
    for i in f:
        pipeLine = []
        for j in i:
            if j != "\n":
                pipeLine.append(j)
        pipeMap.append(pipeLine)
    count1 = 0
    startX = 0
    startY = 0
    fin = True
    while (count1 < len(pipeMap)) and fin:
        count2 = 0
        while count2 < len(pipeMap[count1]):
            if pipeMap[count1][count2] == "S":
                startY = count1
                startX = count2
                count2 = len(pipeMap[count1])
                fin = False
            count2 += 1
        count1 += 1
    pos1 = [-1, -1]
    symb1 = ""
    pos2 = [-1, -1]
    symb2 = ""
    prev1 = [startX, startY]
    prev2 = [startX, startY]
    if isntOOB(startX+1, startY, pipeMap):
        if pipeMap[startY][startX+1] == "-" or pipeMap[startY][startX+1] == "7" or pipeMap[startY][startX+1] == "J":
            if pos1[0] == -1:
                pos1[0] = startX+1
                pos1[1] = startY
                symb1 = pipeMap[startY][startX+1]
            elif pos2[0] == -1:
                pos2[0] = startX+1
                pos2[1] = startY
                symb2 = pipeMap[startY][startX+1]
    if isntOOB(startX-1, startY, pipeMap):
        if pipeMap[startY][startX-1] == "-" or pipeMap[startY][startX-1] == "L" or pipeMap[startY][startX-1] == "F":
            if pos1[0] == -1:
                pos1[0] = startX-1
                pos1[1] = startY
                symb1 = pipeMap[startY][startX-1]
            elif pos2[0] == -1:
                pos2[0] = startX-1
                pos2[1] = startY
                symb2 = pipeMap[startY][startX-1]
    if isntOOB(startX, startY+1, pipeMap):
        if pipeMap[startY+1][startX] == "|" or pipeMap[startY+1][startX] == "L" or pipeMap[startY+1][startX] == "J":
            if pos1[0] == -1:
                pos1[0] = startX
                pos1[1] = startY+1
                symb1 = pipeMap[startY+1][startX]
            elif pos2[0] == -1:
                pos2[0] = startX
                pos2[1] = startY+1
                symb2 = pipeMap[startY+1][startX]
    if isntOOB(startX, startY-1, pipeMap):
        if pipeMap[startY-1][startX] == "|" or pipeMap[startY-1][startX] == "7" or pipeMap[startY-1][startX] == "F":
            if pos1[0] == -1:
                pos1[0] = startX
                pos1[1] = startY-1
                symb1 = pipeMap[startY-1][startX]
            elif pos2[0] == -1:
                pos2[0] = startX-1
                pos2[1] = startY-1
                symb2 = pipeMap[startY-1][startX]
    steps = 1
    inLoop = [[pos1[0], pos1[1]], [pos2[0], pos2[1]], [startX, startY]]
    while (pos1 != pos2) and (pos1 != prev2) and (pos2 != prev1):
        if symb1 == "|":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                pos1[1] = pos1[1] + 1
            else:
                prev1[1] = pos1[1]
                pos1[1] = pos1[1] -1
        elif symb1 == "-":
            if pos1[0] - prev1[0] == 1:
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] -1
        elif symb1 == "J":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] - 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] -1
        elif symb1 == "F":
            if pos1[1] - prev1[1] == -1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] + 1
        elif symb1 == "7":
            if pos1[1] - prev1[1] == -1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] - 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] + 1
        elif symb1 == "L":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] - 1
        symb1 = pipeMap[pos1[1]][pos1[0]]
        if symb2 == "|":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                pos2[1] = pos2[1] + 1
            else:
                prev2[1] = pos2[1]
                pos2[1] = pos2[1] -1
        elif symb2 == "-":
            if pos2[0] - prev2[0] == 1:
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] -1
        elif symb2 == "J":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] - 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] -1
        elif symb2 == "F":
            if pos2[1] - prev2[1] == -1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] + 1
        elif symb2 == "7":
            if pos2[1] - prev2[1] == -1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] - 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] + 1
        elif symb2 == "L":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] - 1
        symb2 = pipeMap[pos2[1]][pos2[0]]
        steps += 1
        inLoop.append([pos1[0], pos1[1]])
        inLoop.append([pos2[0], pos2[1]])
    print(pos1, pos2, symb1, symb2, steps)
    return inLoop


def part2(inLoop):
    f = open("AoC10.txt", "r")
    pipeMap = []
    for i in f:
        pipeLine = []
        for j in i:
            if j != "\n":
                pipeLine.append(j)
        pipeMap.append(pipeLine)
    count1 = 0
    nodeList = []
    OldLine = []
    nodeLines = []
    while count1 < len(pipeMap):
        count2 = 0
        NodeLine = []
        leftNode = None
        while count2 < len(pipeMap[count1]):
            newNode = Node(count2, count1, [count2, count1] in inLoop, pipeMap[count1][count2])
            nodeList.append(newNode)
            NodeLine.append(newNode)
            if leftNode != None:
                leftNode.setRight(newNode)
                newNode.setLeft(leftNode)
            leftNode = newNode
            count2 += 1
        count3 = 0
        while count3 < len(OldLine):
            OldLine[count3].setDown(NodeLine[count3])
            NodeLine[count3].setUp(OldLine[count3])
            count3 += 1
        count1 += 1
        OldLine = NodeLine
        nodeLines.append(NodeLine)
    biggerMap = embiggen(nodeLines)
    inLoop = part2part2(biggerMap)
    count1 = 0
    nodeList = []
    OldLine = []
    nodeLines = []
    while count1 < len(biggerMap):
        count2 = 0
        NodeLine = []
        leftNode = None
        while count2 < len(biggerMap[count1]):
            newNode = Node(count2, count1, [count2, count1] in inLoop, biggerMap[count1][count2])
            nodeList.append(newNode)
            NodeLine.append(newNode)
            if leftNode != None:
                leftNode.setRight(newNode)
                newNode.setLeft(leftNode)
            leftNode = newNode
            count2 += 1
        count3 = 0
        while count3 < len(OldLine):
            OldLine[count3].setDown(NodeLine[count3])
            NodeLine[count3].setUp(OldLine[count3])
            count3 += 1
        count1 += 1
        OldLine = NodeLine
        nodeLines.append(NodeLine)
        print(count1, len(biggerMap))
    for i in nodeList:
        if i.trapped == None:
            print(i)
            BFS(i, biggerMap)
    nestSize = 0
    for i in nodeList:
        if i.trapped and (i.x % 2 == 0) and (i.y % 2 == 0):
            nestSize += 1
    count2 = 0
    count = 0
    while count2 < len(biggerMap):
        printLine = ""
        count = 0
        while count < len(biggerMap[0]):
            printLine = printLine + nodeList[count + (count2 * len(biggerMap[0]))].Symbol
            count += 1
        count2 += 1
        print(printLine)
    print(nestSize)

def part2part2(bigMap):
    pipeMap = bigMap
    count1 = 0
    startX = 0
    startY = 0
    fin = True
    while (count1 < len(pipeMap)) and fin:
        count2 = 0
        while count2 < len(pipeMap[count1]):
            if pipeMap[count1][count2] == "S":
                startY = count1
                startX = count2
                count2 = len(pipeMap[count1])
                fin = False
            count2 += 1
        count1 += 1
    pos1 = [-1, -1]
    symb1 = ""
    pos2 = [-1, -1]
    symb2 = ""
    prev1 = [startX, startY]
    prev2 = [startX, startY]
    if isntOOB(startX+1, startY, pipeMap):
        if pipeMap[startY][startX+1] == "-" or pipeMap[startY][startX+1] == "7" or pipeMap[startY][startX+1] == "J":
            if pos1[0] == -1:
                pos1[0] = startX+1
                pos1[1] = startY
                symb1 = pipeMap[startY][startX+1]
            elif pos2[0] == -1:
                pos2[0] = startX+1
                pos2[1] = startY
                symb2 = pipeMap[startY][startX+1]
    if isntOOB(startX-1, startY, pipeMap):
        if pipeMap[startY][startX-1] == "-" or pipeMap[startY][startX-1] == "L" or pipeMap[startY][startX-1] == "F":
            if pos1[0] == -1:
                pos1[0] = startX-1
                pos1[1] = startY
                symb1 = pipeMap[startY][startX-1]
            elif pos2[0] == -1:
                pos2[0] = startX-1
                pos2[1] = startY
                symb2 = pipeMap[startY][startX-1]
    if isntOOB(startX, startY+1, pipeMap):
        if pipeMap[startY+1][startX] == "|" or pipeMap[startY+1][startX] == "L" or pipeMap[startY+1][startX] == "J":
            if pos1[0] == -1:
                pos1[0] = startX
                pos1[1] = startY+1
                symb1 = pipeMap[startY+1][startX]
            elif pos2[0] == -1:
                pos2[0] = startX
                pos2[1] = startY+1
                symb2 = pipeMap[startY+1][startX]
    if isntOOB(startX, startY-1, pipeMap):
        if pipeMap[startY-1][startX] == "|" or pipeMap[startY-1][startX] == "7" or pipeMap[startY-1][startX] == "F":
            if pos1[0] == -1:
                pos1[0] = startX
                pos1[1] = startY-1
                symb1 = pipeMap[startY-1][startX]
            elif pos2[0] == -1:
                pos2[0] = startX-1
                pos2[1] = startY-1
                symb2 = pipeMap[startY-1][startX]
    steps = 1
    inLoop = [[pos1[0], pos1[1]], [pos2[0], pos2[1]], [startX, startY]]
    while (pos1 != pos2) and (pos1 != prev2) and (pos2 != prev1):
        if symb1 == "|":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                pos1[1] = pos1[1] + 1
            else:
                prev1[1] = pos1[1]
                pos1[1] = pos1[1] -1
        elif symb1 == "-":
            if pos1[0] - prev1[0] == 1:
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] -1
        elif symb1 == "J":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] - 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] -1
        elif symb1 == "F":
            if pos1[1] - prev1[1] == -1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] + 1
        elif symb1 == "7":
            if pos1[1] - prev1[1] == -1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] - 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] + 1
        elif symb1 == "L":
            if pos1[1] - prev1[1] == 1:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[0] = pos1[0] + 1
            else:
                prev1[1] = pos1[1]
                prev1[0] = pos1[0]
                pos1[1] = pos1[1] - 1
        symb1 = pipeMap[pos1[1]][pos1[0]]
        if symb2 == "|":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                pos2[1] = pos2[1] + 1
            else:
                prev2[1] = pos2[1]
                pos2[1] = pos2[1] -1
        elif symb2 == "-":
            if pos2[0] - prev2[0] == 1:
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] -1
        elif symb2 == "J":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] - 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] -1
        elif symb2 == "F":
            if pos2[1] - prev2[1] == -1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] + 1
        elif symb2 == "7":
            if pos2[1] - prev2[1] == -1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] - 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] + 1
        elif symb2 == "L":
            if pos2[1] - prev2[1] == 1:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[0] = pos2[0] + 1
            else:
                prev2[1] = pos2[1]
                prev2[0] = pos2[0]
                pos2[1] = pos2[1] - 1
        symb2 = pipeMap[pos2[1]][pos2[0]]
        steps += 1
        inLoop.append([pos1[0], pos1[1]])
        inLoop.append([pos2[0], pos2[1]])
    print(pos1, pos2, symb1, symb2, steps)
    return inLoop


loopedTuples = part1()
part2(loopedTuples)
