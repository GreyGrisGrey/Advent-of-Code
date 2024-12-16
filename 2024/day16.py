class Node:
    def __init__(self, x, y, direction=None, value=None):
        self.x = x
        self.y = y
        self.value = value
        self.leastDirection = direction
        self.checked = False
        self.turns = 0
        self.forward = 0
        self.prev = None
    
    def getCoords(self):
        return [self.y, self.x]
    
    def getValue(self):
        return [self.value, self.leastDirection]
    
    def getTurns(self):
        return self.turns
    
    def getFor(self):
        return self.forward
    
    def check(self):
        self.checked = True
    
    def uncheck(self):
        self.checked = False
    
    def changeValue(self, new, direction, turn, node):
        if self.value == None or new < self.value:
            self.value = new
            self.leastDirection = direction
            if turn:
                self.forward = 1 + node.getFor()
                self.turns = 1 + node.getTurns()
            else:
                self.turns = node.getTurns()
                self.forward = 1 + node.getFor()

def partBoth():
    f = open("input.txt")
    y = 0
    graphMap = {}
    for i in f:
        x = 0
        for j in i:
            if j == "S":
                graphMap[str(x) + "," + str(y)] = Node(x, y, "LR", 0)
                start = graphMap[str(x) + "," + str(y)]
            elif j == "E":
                graphMap[str(x) + "," + str(y)] = Node(x, y)
                end = graphMap[str(x) + "," + str(y)]
            elif j == ".":
                graphMap[str(x) + "," + str(y)] = Node(x, y)
            x += 1
        y += 1
    dijkstra([start], graphMap)
    print("Part 1: " + str(end.getValue()[0]))
    reverse(end, graphMap, start, end.getTurns(), end.getFor(), end.getTurns())
    start.check()
    count = 0
    for i in graphMap:
        if graphMap[i].checked:
            count += 1
    print("Part 2: " + str(count))
    
def dijkstra(open, graph):
    closed = []
    actions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while len(open) > 0:
        minimum = None
        index = 0
        for i in open:
            if (minimum == None or i.getValue() < minimum):
                minimum = i.getValue()
                nextNode = i
                nextIndex = index
            index += 1
        nextNodes = []
        currCoords = nextNode.getCoords()
        for i in actions:
            possible = str(currCoords[1] + i[1]) + "," + str(currCoords[0] + i[0])
            if possible in graph:
                if (nextNode.getValue()[1] == "UD") and (currCoords[1] + i[1] != currCoords[1]):
                    graph[possible].changeValue(nextNode.getValue()[0] + 1001, "LR", True, nextNode)
                elif (nextNode.getValue()[1] == "UD"):
                    graph[possible].changeValue(nextNode.getValue()[0] + 1, "UD", False, nextNode)
                elif (nextNode.getValue()[1] == "LR") and (currCoords[0] + i[0] != currCoords[0]):
                    graph[possible].changeValue(nextNode.getValue()[0] + 1001, "UD", True, nextNode)
                else:
                    graph[possible].changeValue(nextNode.getValue()[0] + 1, "LR", False, nextNode)
                if graph[possible] not in closed:
                    nextNodes.append(graph[possible])
        closed.append(nextNode)
        del open[nextIndex]
        for i in nextNodes:
            open.append(i)

def reverse(curr, graph, start, turnsLeft, forwardLeft, maxTurns):
    if curr == start:
        return 1
    if forwardLeft == 0:
        return 0
    elif turnsLeft < 0:
        return 0
    curr.check()
    actions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    currCoords = curr.getCoords()
    val = curr.getValue()[0]
    forward = curr.getFor()
    turn = curr.getTurns()
    count = 0
    for i in actions:
        possible = str(currCoords[1] + i[1]) + "," + str(currCoords[0] + i[0])
        if possible in graph:
            possible = graph[possible]
            if val - 1 == possible.getValue()[0]:
                count += reverse(possible, graph, start, turnsLeft, forwardLeft-1, turnsLeft)
            elif val - 1001 == possible.getValue()[0]:
                count += reverse(possible, graph, start, turnsLeft-1, forwardLeft-1, turnsLeft)
            elif val + 999 == possible.getValue()[0] and possible.getTurns() <= maxTurns and possible.getFor() == forwardLeft-1:
                count += reverse(possible, graph, start, turnsLeft+1, forwardLeft-1, turnsLeft)
    if count == 0:
        curr.uncheck()
        return 0
    return count

partBoth()