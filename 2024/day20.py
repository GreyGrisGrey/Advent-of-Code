class Node:
    def __init__(self, x, y, value = None):
        self.x = x
        self.y = y
        self.value = value
    
    def getCoords(self):
        return [self.x, self.y]
    
    def changeValue(self, value):
        if self.value == None or value < self.value:
            self.value = value
    
    def getValue(self):
        return self.value

def partBoth():
    count = 0
    gridDict = {}
    for i in open("input.txt"):
        for j in range(len(i)):
            if i[j] == ".":
                gridDict[str(j) + "," + str(count)] = Node(j, count)
            elif i[j] == "S":
                start = Node(j, count, 0)
                gridDict[str(j) + "," + str(count)] = start
            elif i[j] == "E":
                end = Node(j, count)
                gridDict[str(j) + "," + str(count)] = end
        count += 1
    dijkstra([start], gridDict, count-1)
    print(cheatCheck1(gridDict, 100))
    print(cheatCheck2(gridDict, 100))

def cheatCheck1(graph, condition):
    count = 0
    actions = [[0, 2], [2, 0], [0, -2], [-2, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for i in graph:
        currCoords = graph[i].getCoords()
        for j in actions:
            nextPos = str(currCoords[0] + j[0]) + "," + str(currCoords[1] + j[1])
            if nextPos in graph:
                save = graph[nextPos].getValue() - graph[i].getValue() - 2
                if save >= condition:
                    count += 1
    return count

def cheatCheck2(graph, condition):
    count = 0
    for i in graph:
        for j in graph:
            startCoord = graph[i].getCoords()
            endCoord = graph[j].getCoords()
            distance = abs(startCoord[0]-endCoord[0]) + abs(startCoord[1]-endCoord[1])
            if distance <= 20:
                value = graph[j].getValue() - graph[i].getValue() - distance
                if value >= condition:
                    count += 1
    return count

    
def dijkstra(open, graph, graphMax):
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
            newCoords = [currCoords[0] + i[0], currCoords[1] + i[1]]
            if newCoords[1] >= 0 and newCoords[0] >= 0 and newCoords[0] <= graphMax and newCoords[1] <= graphMax:
                possible = str(currCoords[0] + i[0]) + "," + str(currCoords[1] + i[1])
                if possible in graph:
                    graph[possible].changeValue(minimum+1)
                    if graph[possible] not in closed:
                        nextNodes.append(graph[possible])
        closed.append(nextNode)
        del open[nextIndex]
        for i in nextNodes:
            open.append(i)

partBoth()