def part1(file):
    spaceMap = {}
    y = 0
    for i in open(file):
        x = 0
        for j in i:
            if j == "L":
                spaceMap[str(x) + ":" + str(y)] = False
            x += 1
        y += 1
    notSame = True
    adjMap = {}
    for i in spaceMap:
        adjMap[i] = adjacentSeats(True, spaceMap, i)
    while notSame:
        occupiedCount = 0
        notSame = False
        newDict = {}
        for i in spaceMap:
            count = 0
            for j in adjMap[i].split(";"):
                if spaceMap[j]:
                    count += 1
            if spaceMap[i] and count >= 4:
                newDict[i] = False
                notSame = True
            elif count == 0:
                newDict[i] = True
                if not spaceMap[i]:
                    notSame = True
            else:
                newDict[i] = spaceMap[i]
            if newDict[i]:
                occupiedCount += 1
        spaceMap = newDict
    return occupiedCount


def part2(file):
    spaceMap = {}
    y = 0
    for i in open(file):
        x = 0
        for j in i:
            if j == "L":
                spaceMap[str(x) + ":" + str(y)] = False
            x += 1
        y += 1
    notSame = True
    adjMap = {}
    for i in spaceMap:
        adjMap[i] = adjacentSeats(False, spaceMap, i)
    while notSame:
        occupiedCount = 0
        notSame = False
        newDict = {}
        for i in spaceMap:
            count = 0
            for j in adjMap[i].split(";"):
                if spaceMap[j]:
                    count += 1
            if spaceMap[i] and count >= 5:
                newDict[i] = False
                notSame = True
            elif count == 0:
                newDict[i] = True
                if not spaceMap[i]:
                    notSame = True
            else:
                newDict[i] = spaceMap[i]
            if newDict[i]:
                occupiedCount += 1
        spaceMap = newDict
    return occupiedCount


def adjacentSeats(part1, grid, space):
    options = [[0, 1], [1, 1], [-1, 1], [1, 0], [-1, 0], [0, -1], [1, -1], [-1, -1]]
    adjList = []
    coords = space.split(":")
    coords[0] = int(coords[0])
    coords[1] = int(coords[1])
    if not part1:
        for i in options:
            count = 0
            newCoords = [coords[0] + i[0], coords[1] + i[1]]
            while count < 100:
                if str(newCoords[0]) + ":" + str(newCoords[1]) in grid:
                    adjList.append(str(newCoords[0]) + ":" + str(newCoords[1]))
                    break
                else:
                    count += 1
                    newCoords[0] += i[0]
                    newCoords[1] += i[1]
    else:
        for i in options:
            newCoords = [coords[0] + i[0], coords[1] + i[1]]
            if str(newCoords[0]) + ":" + str(newCoords[1]) in grid:
                adjList.append(str(newCoords[0]) + ":" + str(newCoords[1]))
    return ";".join(adjList)

print("Part 1 :", part1("input.txt"))
print("Part 2 :", part2("input.txt"))