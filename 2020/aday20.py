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
    
    def reflectH(self):
        temp = self.up
        self.up = self.down
        self.down = temp
        self.right = self.right[::-1]
        self.left = self.left[::-1]
    
    def reflectV(self):
        temp = self.left
        self.left = self.right
        self.right = temp
        self.up = self.up[::-1]
        self.down = self.down[::-1]
    
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
        check = left.getDir("L")
        direction = "L"
        curr = tile.getDir("R")
    count = 0
    while curr != check and count < 8:
        if count == 0 or count == 4:
            tile.reflectH()
        tile.rotate90()
        curr = tile.getDir(direction)
        count += 1
    if count == 8:
        return False
    else:
        return True

def addLayer(outskirts, tileNumDict, tileMatchList, doneDict, smaller):
    newDict = {}
    newList = []
    for i in outskirts:
        for j in tileMatchList[tileNumDict[i]]:
            if j not in doneDict:
                newDict[j] = True
                newList.append(j)
                doneDict[j] = True
    if smaller:
        for i in range(len(outskirts)-1):
            matchTile(outskirts[i], outskirts[i+1], newList[i])
    else:
        reverse = False
        for i in range(len(outskirts)+1):
            if i == 0:
                res = matchTile(None, outskirts[i], newList[i])
                if not res:
                    reverse = True
                    break
            elif i == len(outskirts):
                matchTile(outskirts[i-1], None, newList[i])
            else:
                matchTile(outskirts[i-1], outskirts[i], newList[i])
        if reverse:
            for i in range(len(outskirts)+1):
                num = len(outskirts) - i
                if i == 0:
                    matchTile(outskirts[num - 1], None, newList[i])
                elif i == len(outskirts):
                    matchTile(None, outskirts[0], newList[i])
                else:
                    matchTile(outskirts[num -1 ], outskirts[num], newList[i])
    return newDict, newList

def orientate(prev, curr):
    if prev == None:
        for i in curr:
            curr.orient()

def produceMap(tile, tiles, tileDict, tileNumDict, tileMatchList):
    options = [[tile]]
    doneDict = {}
    for i in range(4):
        for j in options[i]:
            doneDict[j] = True
        if i <= 1:
            smaller = False
        else:
            smaller = True
        newOptions, newList = addLayer(options[i], tileNumDict, tileMatchList, doneDict, smaller)
        options.append(newList)
    for i in options:
        newLine = []
        for j in i:
            newLine.append(j.getNum())
        print(newLine)
    return 

def part2(tiles, tileNumDict, tileMatchList):
    tileDict = {}
    corner = None
    for i in tiles:
        tileDict[i] = True
        if corner == None and i.getMatchCount() == 2:
            corner = i
    count = 0
    arrangement = produceMap(corner, tiles, tileDict, tileNumDict, tileMatchList)
    return 0

res = part1("test.txt")
print(res[0], part2(res[1], res[2], res[3]))