class Brick:
    def __init__(self, coA, coB):
        self.coordsA = coA
        self.coordsB = coB
        self.basis = [coA[0], coB[0], coA[1], coB[1]]
        self.floor = coA[2]
    
    def pushdownCheck(self, posDict):
        if self.floor == 1:
            return False
        for i in range(self.basis[1] - self.basis[0] + 1):
            for j in range(self.basis[3] - self.basis[2] + 1):
                if posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.floor - 1)] != None:
                    return False
        return True
    
    def pushDown(self, posDict):
        for i in range(self.basis[1] - self.basis[0] + 1):
            for j in range(self.basis[3] - self.basis[2] + 1):
                posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.coordsB[2])] = None
                posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.floor - 1)] = self
        self.coordsA[2] -= 1
        self.coordsB[2] -= 1
        self.floor -= 1
    
    def fillDict(self, posDict):
        for i in range(self.coordsB[0] - self.coordsA[0] + 1):
            for j in range(self.coordsB[1] - self.coordsA[1] + 1):
                for k in range(self.coordsB[2] - self.coordsA[2] + 1):
                    posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(k+self.floor)] = self
    
    def getBelow(self, posDict):
        belowDict = {}
        for i in range(self.coordsB[0] - self.coordsA[0] + 1):
            for j in range(self.coordsB[1] - self.coordsA[1] + 1):
                if posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.floor - 1)] != None:
                    belowDict[posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.floor - 1)]] = True
        return belowDict
    
    def getAbove(self, posDict):
        belowDict = {}
        for i in range(self.coordsB[0] - self.coordsA[0] + 1):
            for j in range(self.coordsB[1] - self.coordsA[1] + 1):
                if posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.coordsB[2] + 1)] != None:
                    belowDict[posDict[str(i+self.basis[0]) + ":" + str(j+self.basis[2]) + ":" + str(self.coordsB[2] + 1)]] = True
        return belowDict

def part1():
    posDict = {}
    brickDict = {}
    for i in open("in.txt"):
        res = i.strip("\n").split("~")
        brickDict[len(brickDict)] = Brick(list(map(int, res[0].split(","))), list(map(int, res[1].split(","))))
    for i in range(10):
        for j in range(10):
            for k in range(400):
                posDict[str(i) + ":" + str(j) + ":" + str(k)] = None
    for i in brickDict:
        brickDict[i].fillDict(posDict)
    fallen = True
    while fallen:
        fallen = False
        for i in brickDict:
            if brickDict[i].pushdownCheck(posDict):
                fallen = True
                brickDict[i].pushDown(posDict)
    belows = []
    for i in brickDict:
        belows.append(brickDict[i].getBelow(posDict))
    belowDict = {}
    for i in belows:
        if len(i) == 1:
            for j in i:
                belowDict[j] = True
    return len(brickDict) - len(belowDict)

def part2():
    posDict = {}
    brickDict = {}
    for i in open("in.txt"):
        res = i.strip("\n").split("~")
        brickDict[len(brickDict)] = Brick(list(map(int, res[0].split(","))), list(map(int, res[1].split(","))))
    for i in range(10):
        for j in range(10):
            for k in range(400):
                posDict[str(i) + ":" + str(j) + ":" + str(k)] = None
    for i in brickDict:
        brickDict[i].fillDict(posDict)
    fallen = True
    while fallen:
        fallen = False
        for i in brickDict:
            if brickDict[i].pushdownCheck(posDict):
                fallen = True
                brickDict[i].pushDown(posDict)
    belows = {}
    aboves = {}
    for i in brickDict:
        belows[brickDict[i]] = brickDict[i].getBelow(posDict)
        aboves[brickDict[i]] = brickDict[i].getAbove(posDict)
    fallCountDict = {}
    for i in brickDict:
        fallingDict = {brickDict[i]:True}
        count = 0
        while count < 200:
            newFalling = {}
            for l in fallingDict:
                for j in aboves[l]:
                    if j not in fallingDict:
                        falling = True
                        for k in belows[j]:
                            if k not in fallingDict:
                                falling = False
                                break
                        if falling:
                            newFalling[j] = True
            count += 1
            for j in newFalling:
                fallingDict[j] = newFalling[j]
        fallCountDict[i] = len(fallingDict)
    maximum = 0
    total = 0 
    for i in fallCountDict:
        total += fallCountDict[i]
        if fallCountDict[i] > maximum:
            maximum = fallCountDict[i]
    return total - len(brickDict)

print(part1())
print(part2())