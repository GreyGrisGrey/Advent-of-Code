def checkGood(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return False
    return True

def part1(fileName = "in.txt"):
    cache = {}
    tiles = []
    data = open(fileName).read().split("\n")
    for i in data:
        newLine = []
        for j in i:
            newLine.append(j)
        tiles.append(newLine)
    while True:
        newString = ""
        for i in tiles:
            for j in i:
                newString += j
        if newString in cache:
            break
        cache[newString] = True
        newGrid = []
        adj = [[0, 1], [-1, 0], [1, 0], [0, -1]]
        for i in range(5):
            newLine = []
            for j in range(5):
                count = 0
                for k in adj:
                    if checkGood(i + k[0], j + k[1]) and tiles[i + k[0]][j + k[1]] == "#":
                        count += 1
                if count > 2 or (count != 1 and tiles[i][j] == "#"):
                    newLine.append(".")
                elif (count == 2 or count == 1):
                    newLine.append("#")
                else:
                    newLine.append(".")
            newGrid.append(newLine)
        tiles = newGrid
    bio = 0
    for i in range(5):
        for j in range(5):
            if tiles[i][j] == "#":
                bio += 2**(i*5 + j)
    return bio

def checkAdj(x, y, z, spaces):
    adjs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    nums = 0
    for i in adjs:
        curr = [x + i[0], y + i[1], z]
        if curr[0] == -3:
            curr = [-1, 0, z + 1]
        elif curr[0] == 3:
            curr = [1, 0, z + 1]
        elif curr[1] == -3:
            curr = [0, -1, z + 1]
        elif curr[1] == 3:
            curr = [0, 1, z + 1]
        elif curr[0] == 0 and curr[1] == 0:
            nums += checkLine(x, y, z - 1, spaces)
        if str(curr[0]) + ":" + str(curr[1]) + ":" + str(curr[2]) in spaces:
            nums += 1
    return nums

def checkLine(x, y, z, spaces):
    nums = 0
    for i in range(-2, 3):
        if y == 1:
            if str(i) + ":2:" + str(z) in spaces:
                nums += 1
        elif y == -1:
            if str(i) + ":-2:" + str(z) in spaces:
                nums += 1
        elif x == -1:
            if "-2:" + str(i) + ":" + str(z) in spaces:
                nums += 1
        elif x == 1:
            if "2:" + str(i) + ":" +  str(z) in spaces:
                nums += 1
    return nums

def part2(fileName = "in.txt"):
    data = open(fileName).read().split("\n")
    x = y = -2
    spaces = {}
    for i in data:
        for j in i:
            if j == "#":
                spaces[str(x) + ":" + str(y) + ":0"] = True
            x += 1
        y += 1
        x = -2
    minmax = [-1, 1]
    count = 0
    while count < 200:
        newSpaces = {}
        flags = [False, False]
        for i in range(minmax[0], minmax[1] + 1):
            for j in range(-2, 3):
                for k in range(-2, 3):
                    if j != 0 or k != 0:
                        adjacents = checkAdj(j, k, i, spaces)
                        if (str(j) + ":" + str(k) + ":" + str(i)) in spaces and adjacents == 1:
                            newSpaces[str(j) + ":" + str(k) + ":" + str(i)] = True
                            if i == minmax[0]:
                                flags[0] = True
                            elif i == minmax[1]:
                                flags[1] = True
                        elif (str(j) + ":" + str(k) + ":" + str(i)) not in spaces and (adjacents == 1 or adjacents == 2):
                            newSpaces[str(j) + ":" + str(k) + ":" + str(i)] = True
                            if i == minmax[0]:
                                flags[0] = True
                            elif i == minmax[1]:
                                flags[1] = True
        count += 1
        spaces = newSpaces
        if flags[0]:
            minmax[0] -= 1
        if flags[1]:
            minmax[1] += 1
    return len(spaces)

if __name__ == "__main__":
    print("Part 1:", part1("in24.txt"))
    print("Part 2:", part2("in24.txt"))