class box:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.identity = count

    def value(self):
        return self.y*100 + self.x
    
    def getIdentity(self):
        return self.identity

    def next(self, direction):
        if direction == ">":
            return [self.x+2, self.y]
        elif direction == "<":
            return [self.x-1, self.y]
        elif direction == "^":
            return [[self.x, self.y-1], [self.x+1, self.y-1]]
        else:
            return [[self.x, self.y+1], [self.x+1, self.y+1]]
    
    def move(self, direction, grid):
        if direction == ">":
            grid[self.y][self.x] = None
            grid[self.y][self.x+2] = self
            self.x += 1
        elif direction == "<":
            grid[self.y][self.x+1] = None
            grid[self.y][self.x-1] = self
            self.x -= 1
        elif direction == "^":
            grid[self.y][self.x] = None
            grid[self.y-1][self.x] = self
            grid[self.y][self.x+1] = None
            grid[self.y-1][self.x+1] = self
            self.y -= 1
        else:
            grid[self.y][self.x] = None
            grid[self.y+1][self.x] = self
            grid[self.y][self.x+1] = None
            grid[self.y+1][self.x+1] = self
            self.y += 1

def part1():
    f = open("input.txt")
    end = 0
    grid = []
    gridy = True
    directions = ""
    yCount = 0
    for i in f:
        if gridy and i != "\n":
            xCount = 0
            newLine = i.strip()
            gridLine = []
            for j in newLine:
                if j == "@":
                    curr = [yCount, xCount]
                    gridLine.append(".")
                else:
                    gridLine.append(j)
                xCount += 1
            grid.append(gridLine)
            yCount += 1
        elif i == "\n":
            gridy = False
        else:
            directions = directions + i.strip()
    for i in directions:
        curr = doMove(i, grid, curr)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                end += i*100 + j
    return end

def doMove(move, grid, curr):
    currX = curr[1]
    currY = curr[0]
    if move == "<":
        currX -= 1
    elif move == ">":
        currX += 1
    elif move == "^":
        currY -= 1
    else:
        currY += 1
    while True:
        if grid[currY][currX] == ".":
            break
        elif grid[currY][currX] == "#":
            return [curr[0], curr[1]]
        else:
            if move == "<":
                currX -= 1
            elif move == ">":
                currX += 1
            elif move == "^":
                currY -= 1
            else:
                currY += 1
    grid[currY][currX] = "O"
    if move == "<":
        curr[1] -= 1
    elif move == ">":
        curr[1] += 1
    elif move == "^":
        curr[0] -= 1
    else:
        curr[0] += 1
    grid[curr[0]][curr[1]] = "."
    return [curr[0], curr[1]]

def part2():
    f = open("input.txt")
    end = 0
    grid = []
    gridy = True
    directions = ""
    yCount = 0
    boxes = []
    boxCount = 0
    for i in f:
        if gridy and i != "\n":
            xCount = 0
            newLine = i.strip()
            gridLine = []
            for j in newLine:
                if j == "@":
                    curr = [yCount, xCount*2]
                    gridLine.append(None)
                    gridLine.append(None)
                elif j == "O":
                    newBox = box(xCount*2, yCount, boxCount)
                    gridLine.append(newBox)
                    gridLine.append(newBox)
                    boxes.append(newBox)
                    boxCount += 1
                elif j == ".":
                    gridLine.append(None)
                    gridLine.append(None)
                else:
                    gridLine.append("#")
                    gridLine.append("#")
                xCount += 1
            grid.append(gridLine)
            yCount += 1
        elif i == "\n":
            gridy = False
        else:
            directions = directions + i.strip()
    for i in directions:
        curr = doMove2(i, grid, curr)
    for i in boxes:
        end += i.value()
    return end

def doMove2(direction, grid, curr):
    if direction == "<":
        curr[1] -= 1
    elif direction == ">":
        curr[1] += 1
    elif direction == "^":
        curr[0] -= 1
    else:
        curr[0] += 1
    nextLine = [[curr[1], curr[0]]]
    safety = True
    while True:
        end = True
        newLine = []
        for i in nextLine:
            if direction == "<":
                if grid[i[1]][i[0]] != None and grid[i[1]][i[0]] != "#":
                    newLine.append(grid[i[1]][i[0]].next(direction))
                    end = False
                elif grid[i[1]][i[0]] == "#":
                    return [curr[0], curr[1]+1]
            elif direction == ">":
                if grid[i[1]][i[0]] != None and grid[i[1]][i[0]] != "#":
                    newLine.append(grid[i[1]][i[0]].next(direction))
                    end = False
                elif grid[i[1]][i[0]] == "#":
                    return [curr[0], curr[1]-1]
            elif direction == "^":
                if grid[i[1]][i[0]] != None and grid[i[1]][i[0]] != "#":
                    newLine.append(grid[i[1]][i[0]].next(direction)[0])
                    newLine.append(grid[i[1]][i[0]].next(direction)[1])
                    end = False
                elif grid[i[1]][i[0]] == "#":
                    return [curr[0]+1, curr[1]]
            else:
                if grid[i[1]][i[0]] != None and grid[i[1]][i[0]] != "#":
                    newLine.append(grid[i[1]][i[0]].next(direction)[0])
                    newLine.append(grid[i[1]][i[0]].next(direction)[1])
                    end = False
                elif grid[i[1]][i[0]] == "#":
                    return [curr[0]-1, curr[1]]
        nextLine = newLine
        if end and safety:
            safety = False
        elif end:
            break
    movingList = []
    nextLine = [[curr[1], curr[0]]]
    safety = True
    while True:
        end = True
        newLine = []
        for i in nextLine:
            if direction == "<":
                if grid[i[1]][i[0]] != None:
                    newLine.append(grid[i[1]][i[0]].next(direction))
                    movingList.append(grid[i[1]][i[0]])
                    end = False
            elif direction == ">":
                if grid[i[1]][i[0]] != None:
                    newLine.append(grid[i[1]][i[0]].next(direction))
                    movingList.append(grid[i[1]][i[0]])
                    end = False
            elif direction == "^":
                if grid[i[1]][i[0]] != None:
                    newLine.append(grid[i[1]][i[0]].next(direction)[0])
                    newLine.append(grid[i[1]][i[0]].next(direction)[1])
                    movingList.append(grid[i[1]][i[0]])
                    end = False
            else:
                if grid[i[1]][i[0]] != None:
                    newLine.append(grid[i[1]][i[0]].next(direction)[0])
                    newLine.append(grid[i[1]][i[0]].next(direction)[1])
                    movingList.append(grid[i[1]][i[0]])
                    end = False
        nextLine = newLine
        doneList = []
        if safety and end:
            safety = False
        elif end:
            movingList.reverse()
            for i in movingList:
                if i.getIdentity() not in doneList:
                    i.move(direction, grid)
                    doneList.append(i.getIdentity())
            return [curr[0], curr[1]]
    



print(part1())
print(part2())