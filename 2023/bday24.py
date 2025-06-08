import numpy as np
def convertToLine(nums):
    toAxis = [-nums[0][0]/nums[1][0], -nums[0][1]/nums[1][1]]
    goal = nums[0][1] + (toAxis[0] * nums[1][1])
    return [1/((nums[0][0] + (toAxis[1] * nums[1][0])) / goal), 1], goal

def checkGood(minCoord, maxCoord, res, first, second):
    if res[0] < minCoord or res[0] > maxCoord or res[1] < minCoord or res[1] > maxCoord:
        return [0, first, second, res]
    elif (res[0] > first[0][0] and first[1][0] < 0) or (res[0] < first[0][0] and first[1][0] > 0):
        return [0, first, second, res]
    elif (res[0] > second[0][0] and second[1][0] < 0) or (res[0] < second[0][0] and second[1][0] > 0):
        return [0, first, second, res]
    elif (res[1] > first[0][1] and first[1][1] < 0) or (res[1] < first[0][1] and first[1][1] > 0):
        return [0, first, second, res]
    elif (res[1] > second[0][1] and second[1][1] < 0) or (res[1] < second[0][1] and second[1][1] > 0):
        return [0, first, second, res]
    return [1, first, second, res]

def getIntersect(first, second, minCoord, maxCoord):
    sys1, sys2 = convertToLine(first), convertToLine(second)
    if sys1[0][0] == sys2[0][0]:
        return [0]
    lines = np.array([sys1[0], sys2[0]])
    solves = np.array([sys1[1], sys2[1]])
    res = np.linalg.solve(lines, solves)
    return checkGood(minCoord, maxCoord, res, first, second)

def getHail(fileName):
    start = list(map(lambda x: x.split(" @ "), open(fileName).read().split("\n")))
    hail = []
    for i in start:
        hail.append(list(map(lambda x: list(map(lambda y: int(y), x.split(", "))), i)))
    return hail

def part1(fileName, minimum, maximum):
    total = 0
    hail = getHail(fileName)
    for i in range(len(hail)):
        for j in range(len(hail)):
            if i > j:
                res = getIntersect(hail[i], hail[j], minimum, maximum)
                total += res[0]
    return total

class Hail:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.distDict = {}

    def getPos(self):
        return self.pos
    
    def addDist(self, other, step):
        if step not in self.distDict:
            self.distDict[step] = {}
        dist = other.getPos()
        self.distDict[step][other] = [dist[0] - self.pos[0] - self.vel[0], dist[1] - self.pos[1] - self.vel[1], dist[2] - self.pos[2] - self.vel[2]]
    
    def forward(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]
    
    def getDistDict(self):
        return self.distDict

print(part1("in.txt", 200000000000000, 400000000000000))