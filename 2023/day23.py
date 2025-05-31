class Node:
    def __init__(self, icon, x, y):
        self.icon = icon
        self.x = x
        self.y = y
        if icon == "#":
            self.passable = [False, False, False, False]
        elif icon == "^":
            self.passable = [False, True, True, True]
        elif icon == "v":
            self.passable = [True, True, False, True]
        elif icon == "<":
            self.passable = [True, False, True, True]
        elif icon == ">":
            self.passable = [True, True, True, False]
        else:
            self.passable = [True, True, True, True]
    
    def checkEnter(self, dir):
        return self.passable[dir]
    
    def getIcon(self):
        return self.icon

def BFS(curr, end, checked, dirDict, nodeDict, steps):
    options = []
    while len(options) < 2:
        if curr == end:
            return steps
        options = []
        checked[curr] = True
        for i in dirDict:
            if curr + dirDict[i] in nodeDict and nodeDict[curr + dirDict[i]].checkEnter(i) and curr + dirDict[i] not in checked:
                options.append(curr + dirDict[i])
        if len(options) == 1:
            curr = options[0]
            steps += 1
    maximum = 0
    for i in options:
        res = BFS(i, end, checked.copy(), dirDict, nodeDict, steps+1)
        if res > maximum:
            maximum = res
    return maximum

def findVertices(nodes, dirDict, maxX, maxY, vertices):
    for i in range(maxX):
        for j in range(maxY):
            curr = nodes[i + j*1000]
            count = 0
            if curr.getIcon() != "#":
                for k in dirDict:
                    if (i + j*1000) + dirDict[k] in nodes and nodes[(i + j*1000) + dirDict[k]].getIcon() != "#":
                        count += 1
            if count != 2 and count != 0:
                vertices.append(i + j*1000)
    return

def findConnections(vertex, dirDict, vertices, nodes):
    adjs = []
    for i in dirDict:
        if vertex + dirDict[i] in nodes and nodes[vertex + dirDict[i]].getIcon() != "#":
            adjs.append(findConnection(vertex + dirDict[i], vertex, dirDict, vertices, nodes))
    return adjs

def findConnection(curr, prev, dirDict, vertices, nodes):
    steps = 1
    while curr not in vertices:
        for i in dirDict:
            temp = curr + dirDict[i]
            if temp in nodes and temp != prev and nodes[temp].getIcon() != "#":
                prev = curr
                curr = temp
                break
        steps += 1
    return [curr, steps]

# Slow, but only to the extent of 30 seconds
def recurse(currVertices, currCount, best, vertices, vertexAdj, index, end):
    if currVertices[index-1] == end:
        return currCount
    options = []
    for i in vertexAdj[currVertices[index-1]]:
        if i[0] not in currVertices:
            options.append(i)
    if len(options) == 0:
        return -1
    maximum = 0
    for i in options:
        copy = currVertices.copy()
        copy.append(i[0])
        res = recurse(copy, currCount + i[1], best, vertices, vertexAdj, index+1, end)
        if res > maximum:
            maximum = res
    return maximum

def partBoth(fileName):
    nodeDict = {}
    y = 0
    for i in open(fileName):
        x = 0
        for j in i:
            if j != "\n":
                nodeDict[x + (y*1000)] = Node(j, x, y)
            x += 1
        y += 1
    dirDict = {0:1000, 1:1, 2:-1000, 3:-1}
    vertices = []
    findVertices(nodeDict, dirDict, x-1, y, vertices)
    vertexAdj = {}
    for i in vertices:
        vertexAdj[i] = findConnections(i, dirDict, vertices, nodeDict)
    return BFS(1, (y-1)*1000 + (x-2), {}, dirDict, nodeDict, 0), recurse([1], 0, 0, vertices, vertexAdj, 1, (y-1)*1000 + (x-2))
    
print(partBoth("in.txt"))