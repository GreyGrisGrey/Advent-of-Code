def check(ultra, path, i):
    if ultra and (abs(path[3]-i) != 2 and ((path[3] != i and path[2] > 2) or (path[3] == i and path[2] != 9))) or path[3] == -7:
        return True
    elif not ultra and (abs(path[3]-i) != 2 and (path[3] != i or path[2] != 2)):
        return True
    return False

def updatePath(ultra, path, grid):
    poss = []
    for i in range(4):
        if check(ultra, path, i):
            if i == 0: res = (path[0], path[1]-1)
            elif i == 2: res = (path[0], path[1]+1)
            elif i == 1: res = (path[0]+1, path[1])
            else: res = (path[0]-1, path[1])
            if res in grid:
                if path[3] == i:
                    poss.append((res[0], res[1], path[2]+1, i, path[4]+grid[res]))
                else:
                    poss.append((res[0], res[1], 0, i, path[4]+grid[res]))
    return poss

def part1(fileName):
    nodeDict = {}
    y = 0
    for i in open(fileName, "r"):
        x = 0
        for j in i.strip("\n"):
            nodeDict[(x, y)] = int(j)
            x += 1
        y += 1
    paths = [[0, 0, 0, -7, 0]]
    pathCache = {}
    for i in range(1500):
        newPaths = {}
        for j in paths:
            jPath = (j[0], j[1], j[2], j[3])
            if j[0] == y-1 and j[1] == x-1:
                return j[4]
            elif jPath in pathCache:
                pass
            elif j[4] == i:
                pathCache[jPath] = True
                res = updatePath(False, j, nodeDict)
                for k in res:
                    if k not in newPaths:
                        newPaths[k] = True
            else:
                if j not in newPaths:
                    newPaths[j] = True
        paths = newPaths
    return 0

def part2(fileName):
    nodeDict = {}
    y = 0
    for i in open(fileName, "r"):
        x = 0
        for j in i.strip("\n"):
            nodeDict[(x, y)] = int(j)
            x += 1
        y += 1
    paths = [[0, 0, 0, -7, 0]]
    pathCache = {}
    for i in range(1000):
        newPaths = {}
        for j in paths:
            jPath = (j[0], j[1], j[2], j[3])
            if j[0] == y-1 and j[1] == x-1:
                return j[4]
            elif jPath in pathCache:
                pass
            elif j[4] == i:
                pathCache[jPath] = True
                res = updatePath(True, j, nodeDict)
                for k in res:
                    if k not in newPaths:
                        newPaths[k] = True
            else:
                if j not in newPaths:
                    newPaths[j] = True
        paths = newPaths
    return 0

print(part1("in.txt"))
print(part2("in.txt"))