from math import floor

class Node():
    def __init__(self, x, y, sym):
        self.x = x
        self.y = y
        self.count = 0
        self.seen = {}
        self.adj = {}
        self.even = None
    
    def setEven(self, bool):
        self.even = bool
    
    def increment(self, step, num=1, loop = False):
        if loop == False and num != 0:
            return False
        if num in self.seen:
            return False
        elif step == 1:
            self.count += 1
            self.seen[num] = True
        else:
            self.seen[num] = False
        return True
    
    def getCount(self):
        return self.count
    
    def setAdj(self, adj, passover):
        self.adj[adj] = passover
    
    def getAdj(self):
        return self.adj
    
    def getCoords(self):
        return self.x, self.y

def small(num, limit):
    x = num % 1000000
    y = int((num-x)/1000000)
    if abs(x) + abs(y) < limit:
        return False
    return True

def step(paths, step, loop=False, limit=0, size=1):
    newPaths = {}
    for i in paths:
        news = i.getAdj()
        for j in news:
            for k in paths[i]:
                if (limit == 0 or small(k, limit))and j.increment(step, k+news[j], loop):
                    if j not in newPaths:
                        newPaths[j] = {}
                    newPaths[j][k+news[j]] = True
    return newPaths

def expandDiamond(paths, steps):
    newPaths = {}
    for i in paths:
        newPaths[i] = {}
        for j in paths[i]:
            if j % 1000000 == 0:
                if j > 0:
                    newPaths[i][j+(1000000*steps)] = True
                else:
                    newPaths[i][j-1000000*steps] = True
            elif abs(j) < 500000:
                if j > 0:
                    newPaths[i][j+1*steps] = True
                else:
                    newPaths[i][j-1*steps] = True
            elif abs(j) < 1500000:
                if j < 0:
                    if j < -1000000:
                        for k in range(steps+1):
                            key = (-1000000 * k) + (-1 * (steps-k))
                            newPaths[i][j+key] = True
                    else:
                        for k in range(steps+1):
                            key = (-1000000 * k) + (1 * (steps-k))
                            newPaths[i][j+key] = True
                else:
                    if j > 1000000:
                        for k in range(steps+1):
                            key = (1000000 * k) + (1 * (steps-k))
                            newPaths[i][j+key] = True
                    else:
                        for k in range(steps+1):
                            key = (1000000 * k) + (-1 * (steps-k))
                            newPaths[i][j+key] = True
            else:
                if j > 0:
                    newPaths[i][j+1000000*steps] = True
                else:
                    newPaths[i][j-1000000*steps] = True
    return newPaths

def part1(spaces, fileName):
    spaceDict = {}
    y = 0
    for i in open(fileName):
        x = 0
        for j in i:
            if j != "\n" and j != "#":
                spaceDict[y * 1000 + x] = Node(x, y, j)
            if j == "S":
                start = (x, y)
            x += 1
        y += 1
    total = 0
    for i in spaceDict:
        coords = spaceDict[i].getCoords()
        options = [[coords[0], coords[1]+1], [coords[0]+1, coords[1]], [coords[0]-1, coords[1]], [coords[0], coords[1]-1]]
        for j in options:
            passover = 0
            if j[0] > (x-1):
                j[0] = 0
                passover = 1
            elif j[0] < 0:
                j[0] = x-1
                passover = -1
            elif j[1] > (x-1):
                j[1] = 0
                passover = 1000000
            elif j[1] < 0:
                j[1] = x-1
                passover = -1000000
            if (j[1]*1000 + j[0]) in spaceDict:
                spaceDict[i].setAdj(spaceDict[(j[1]*1000 + j[0])], passover)
    paths = {spaceDict[start[0]*1000 + start[1]]:{0:True}}
    for i in range(spaces):
        paths = step(paths, (spaces-i)%2)
    for i in spaceDict:
        total += spaceDict[i].getCount()
    return total

def countEvenOdd(start, even):
    seen = {}
    curr = [start]
    evens = 0
    odds = 0
    while len(curr) > 0:
        next = []
        for i in curr:
            new = i.getAdj()
            for j in new:
                if j not in seen:
                    seen[j] = True
                    next.append(j)
                    j.setEven(even)
                    if even:
                        evens += 1
                    else:
                        odds += 1
        even = not even
        curr = next
    return evens, odds

def scanGrid(start, steps, add, mult):
    seen = {start:True}
    curr = {start:True}
    total = 0
    if add:
        total += mult
    if steps == 0:
        return mult
    elif steps < 0:
        return 0
    add = not add
    for i in range(steps+1):
        next = {}
        for j in curr:
            new = j.getAdj()
            for k in new:
                if (k not in seen) and not new[k]:
                    seen[k] = True
                    next[k] = True
                    if add:
                        total += mult
        curr = next
        add = not add
    return total

def part2(steps, fileName):
    y = 0
    total = 0
    spaceDict = {}
    for i in open(fileName):
        x = 0
        for j in i:
            if j != "#" and j != "\n":
                spaceDict[y * 1000 + x] = Node(x, y, j)
            if j == "S":
                start = [x, y]
            x += 1
        y += 1
    x -= 1
    y -= 1
    for i in spaceDict:
        coords = spaceDict[i].getCoords()
        options = [[coords[0], coords[1]+1], [coords[0]+1, coords[1]], [coords[0]-1, coords[1]], [coords[0], coords[1]-1]]
        for j in options:
            passover = False
            if j[0] > (x):
                j[0] = 0
                passover = True
            elif j[0] < 0:
                j[0] = x
                passover = True
            elif j[1] > (x):
                j[1] = 0
                passover = True
            elif j[1] < 0:
                j[1] = x
                passover = True
            if (j[1]*1000 + j[0]) in spaceDict:
                spaceDict[i].setAdj(spaceDict[(j[1]*1000 + j[0])], passover)
    evens, odds = countEvenOdd(spaceDict[start[1] * 1000 + start[0]], False)
    corners = {spaceDict[0]:1, spaceDict[x]:1, spaceDict[(y)*1000]:1, spaceDict[(y)*1000 + (x)]:1}
    edges = {spaceDict[start[0]]:1, spaceDict[start[1]*1000]:1, spaceDict[start[0]+(y)*1000]:1, spaceDict[start[1]*1000 + x]:1}
    x += 1
    remaining = (steps - (x)) - int((x+1)/2)
    index = (True if steps % 2 == 0 else False)
    if index:
        total += evens
        total += 4 * odds
    else:
        total += odds
        total += 4 * evens
    universes = 8
    steps = 0
    while remaining > (x):
        remaining -= (x)
        if index:
            total += universes * evens
        else:
            total += universes * odds
        universes += 4
        index = not index
        steps += 1
        for i in corners:
            corners[i] += 1
    for i in corners:
        total += scanGrid(i, int(remaining + (x) - (x+1)/2), (steps)%2, corners[i])
        total += scanGrid(i, int(remaining - (x+1)/2), (steps+1)%2, corners[i]+1)
    for i in edges:
        total += scanGrid(i, int(remaining), not index, edges[i])
    return total

print(part1(64, "in.txt"))
print(part2(26501365, "in.txt"))