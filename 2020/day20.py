from math import sqrt, floor

class Tile():
    def __init__(self, grid, length, ID):
        right = ""
        left = ""
        up = ""
        down = ""
        for i in range(length):
            left += "1" if grid[i][0] == "#" else "0"
            right += "1" if grid[i][length-1] == "#" else "0"
            up += "1" if grid[0][i] == "#" else "0"
            down += "1" if grid[length-1][i] == "#" else "0"
        self.ID = ID
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.grid = grid
        self.matches = [True, True, True, True]
    
    def getDir(self, direction):
        if direction == "U":
            return self.up
        elif direction == "D":
            return self.down
        elif direction == "L":
            return self.left
        else:
            return self.right
    
    def getNum(self):
        return self.ID
    
    def rotate90(self):
        temp = self.left[::-1]
        self.left = self.down
        self.down = self.right[::-1]
        self.right = self.up
        self.up = temp
        newGrid = []
        for i in range(len(self.grid)):
            newGridLine = []
            for j in range(len(self.grid[0])):
                newGridLine.append(self.grid[len(self.grid)-(j+1)][i])
            newGrid.append(newGridLine)
        self.grid = newGrid
    
    def reflectH(self):
        temp = self.up
        self.up = self.down
        self.down = temp
        self.right = self.right[::-1]
        self.left = self.left[::-1]
        newGrid = []
        for i in range(len(self.grid)):
            newGrid.append(self.grid[len(self.grid)-(1+i)])
        self.grid = newGrid
    
    def setMatched(self, index):
        self.matches[index] = False
    
    def getMatchCount(self):
        total = 0
        for i in self.matches:
            if i:
                total += 1
        return total
    
    def orient(self):
        if self.matches[0] and self.matches[3]:
            for i in range(3):
                self.rotate90()
        elif self.matches[3]:
            for i in range(2):
                self.rotate90()
        elif self.matches[1]:
            self.rotate90()
    
    def getGrid(self):
        return self.grid

def compareTiles(A, B, matchList):
    dirs = ["U", "D", "L", "R"]
    add = True
    for i in range(4):
        for j in range(4):
            for k in range(8):
                B.rotate90()
                if k % 4 == 0:
                    B.reflectH()
                if A.getDir(dirs[i]) == B.getDir(dirs[j]):
                    if add:
                        matchList.append(B)
                        add = False
                    A.setMatched(i)

def part1(fileName):
    tiles = []
    tileNumDict = {}
    tileMatchList = []
    total = 1
    num = None
    for i in open(fileName, "r"):
        if i[0] == "#" or i[0] == ".":
            newTile.append(i.strip("\n"))
        elif i[0] != "\n":
            num = int(i.strip(":\n").split(" ")[1])
            newTile = []
        else:
            tiles.append(Tile(newTile, len(newTile[0]), num))
    tiles.append(Tile(newTile, len(newTile[0]), num))
    count = 0
    for i in tiles:
        print(count)
        tileNumDict[i] = count
        newList = []
        tileMatchList.append(newList)
        count += 1
        for j in tiles:
            if i != j:
                compareTiles(i, j, newList)
    for i in tiles:
        if i.getMatchCount() == 2:
            total *= i.getNum()
    return total, tiles, tileNumDict, tileMatchList

def matchTile(left, right, tile):
    if left == None:
        curr = tile.getDir("U")
        direction = "U"
        check = right.getDir("D")
    else:
        check = left.getDir("R")
        direction = "L"
        curr = tile.getDir("L")
    count = 0
    while (curr != check) and count < 9:
        if count == 0 or count == 4:
            tile.reflectH()
        tile.rotate90()
        curr = tile.getDir(direction)
        count += 1
    if count == 9:
        return False
    else:
        return True

def addLayer(outskirts, tileNumDict, tileMatchList, doneDict, smaller):
    newDict = {}
    newList = []
    if len(outskirts) == 1 or (len(outskirts) == 2 and smaller):
        for i in outskirts:
            for j in tileMatchList[tileNumDict[i]]:
                if j not in doneDict:
                    doneDict[j] = True
                    newList.append(j)
                    newDict[j] = True
    elif smaller:
        for i in range(len(outskirts)-1):
            lefts = tileMatchList[tileNumDict[outskirts[i]]]
            rights = tileMatchList[tileNumDict[outskirts[i+1]]]
            for j in lefts:
                if j in rights and j not in doneDict:
                    newList.append(j)
                    newDict[j] = True
                    doneDict[j] = True
    else:
        for i in range(len(outskirts)-1):
            lefts = tileMatchList[tileNumDict[outskirts[i]]]
            rights = tileMatchList[tileNumDict[outskirts[i+1]]]
            for j in lefts:
                if j not in doneDict and j not in rights:
                    newList.append(j)
                    newDict[j] = True
                    doneDict[j] = True
                elif j not in doneDict:
                    middle = j
            if middle not in doneDict:
                newList.append(middle)
                newDict[middle] = True
                doneDict[middle] = True
            for j in rights:
                if j not in doneDict:
                    newList.append(j)
                    newDict[j] = True
                    doneDict[j] = True
    if smaller:
        res = matchTile(outskirts[0], outskirts[1], newList[0])
        if not res:
            newList.reverse()
        for i in range(len(newList)):
            matchTile(outskirts[i], outskirts[i+1], newList[i])
    else:
        res = matchTile(None, outskirts[0], newList[0])
        if not res:
            newList.reverse()
        for i in range(len(newList)):
            if i == 0:
                matchTile(None, outskirts[0], newList[0])
            elif i == len(newList)-1:
                matchTile(outskirts[i-1], None, newList[i])
            else:
                matchTile(outskirts[i-1], outskirts[i], newList[i])
    return newDict, newList

def orientate(prev, curr):
    if prev == None:
        for i in curr:
            curr.orient()

def produceMap(tile, tiles, tileDict, tileNumDict, tileMatchList):
    options = [[tile]]
    doneDict = {}
    for i in range(22):
        for j in options[i]:
            doneDict[j] = True
        if i <= 10:
            smaller = False
        else:
            smaller = True
        newOptions, newList = addLayer(options[i], tileNumDict, tileMatchList, doneDict, smaller)
        options.append(newList)
    for i in options:
        newLine = []
        for j in i:
            newLine.append(j.getNum())
    tileGrid = []
    for i in range(int(sqrt(len(tiles)))):
        tileGrid.append([])
    for i in range(len(options)):
        for j in range(len(options[i])):
            tileGrid[min(i-j, int(sqrt(len(tiles)))-(1+j))].append(options[i][j])
    return tileGrid

def rotateGrid(grid):
    newGrid = []
    for i in range(len(grid)):
        newGridLine = ""
        for j in range(len(grid[0])):
            newGridLine += grid[len(grid)-(j+1)][i]
        newGrid.append(newGridLine)
    grid = newGrid
    return grid

def reflectGrid(grid):
    for i in range(floor(len(grid)/2)):
        temp = ""
        for j in grid[i]:
            temp += j
        grid[i] = grid[len(grid)-(1+i)]
        grid[len(grid)-(1+i)] = temp
    return

def checkSpace(grid, fullDict, x, y, full):
    if (y != 0) and (y != len(grid)-1) and (x+19 < len(grid[0])):
        dragon = True
        for i in full:
            if grid[y+i[1]][x+i[0]] != "#":
                dragon = False
        if dragon:
            for i in full:
                fullDict[str(x+i[0]) + ":" + str(y+i[1])] = True
    return

def checkDragons(grid):
    total = 0
    fullDict = {}
    count = 0
    full = [[0, 0], [1, 1], [4, 1], [5, 0], [6, 0], [7, 1], [10, 1], [11, 0], [12, 0], [13, 1], [16, 1], [17, 0], [18, 0], [19, 0], [18, -1]]
    while count < 8:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                checkSpace(grid, fullDict, j, i, full)
        if len(fullDict) != 0:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[j][i] == "#":
                        total += 1
            return total - len(fullDict)
        if count == 0 or count == 4:
            reflectGrid(grid)
        grid = rotateGrid(grid)
        count += 1
    return total

def part2(tiles, tileNumDict, tileMatchList):
    tileDict = {}
    corner = None
    for i in tiles:
        tileDict[i] = True
        if corner == None and i.getMatchCount() == 2:
            corner = i
    count = 0
    corner.orient()
    arrangement = produceMap(corner, tiles, tileDict, tileNumDict, tileMatchList)
    bigGrid = []
    for i in arrangement:
        tileLevel = []
        count = 0
        for j in i:
            newGrid = j.getGrid()
            for k in range(len(newGrid)):
                for l in range(len(newGrid[0])):
                    if l != 0 and l != 9 and k != 0 and k != 9:
                        if len(tileLevel) == count+(k-1):
                            tileLevel.append("")
                        tileLevel[count+(k-1)] += newGrid[k][l]
        count += 8
        for j in tileLevel:
            bigGrid.append(j)
    return checkDragons(bigGrid)

res = part1("in.txt")
print(res[0], part2(res[1], res[2], res[3]))