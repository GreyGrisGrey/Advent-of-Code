import numpy as np
def convertToLine(nums):
    toAxis = [-nums[0][0]/nums[1][0], -nums[0][1]/nums[1][1]]
    goal = nums[0][1] + (toAxis[0] * nums[1][1])
    return [1/((nums[0][0] + (toAxis[1] * nums[1][0])) / goal), 1], goal

def checkGood(minCoord, maxCoord, res, A, B):
    if (res[0] < minCoord or res[0] > maxCoord or res[1] < minCoord or res[1] > maxCoord):
        return 0
    elif (res[0] > A[0][0] and A[1][0] < 0) or (res[0] < A[0][0] and A[1][0] > 0):
        return 0
    elif (res[0] > B[0][0] and B[1][0] < 0) or (res[0] < B[0][0] and B[1][0] > 0):
        return 0
    elif (res[1] > A[0][1] and A[1][1] < 0) or (res[1] < A[0][1] and A[1][1] > 0):
        return 0
    elif (res[1] > B[0][1] and B[1][1] < 0) or (res[1] < B[0][1] and B[1][1] > 0):
        return 0
    return 1

def getIntersect(A, B, vel = None):
    if vel != None:
        sys1 = [-(A[1][0] + vel[0]), B[1][0] + vel[0]]
        sys2 = [-(A[1][1] + vel[1]), B[1][1] + vel[1]]
        goals = [A[0][0] - B[0][0], A[0][1] - B[0][1]]
        lines = np.array([sys1, sys2])
        solves = np.array([goals[0], goals[1]])
        try:
            res = np.linalg.solve(lines, solves)
            if res[0].is_integer() and res[1].is_integer():
                return res
            return "NON-INT"
        except np.linalg.LinAlgError:
            return "PARALLEL"
    else:
        if B[1][1] == 0:
            sys2 = [[1, 0], B[0][1]]
        elif B[1][0] == 0:
            sys2 = [[0, 1], B[0][1]]
        else:
            sys2 = convertToLine(B)
        if A[1][1] == 0:
            sys1 = [[1, 0], A[0][1]]
        elif A[1][0] == 0:
            sys1 = [[0, 1], A[0][1]]
        else:
            sys1 = convertToLine(A)
        if sys1[0][0] == sys2[0][0] and sys1[0][1] == sys2[0][1]:
            return 0
        lines = np.array([sys1[0], sys2[0]])
        solves = np.array([sys1[1], sys2[1]])
        res = np.linalg.solve(lines, solves)
        return checkGood(200000000000000, 400000000000000, res, A, B)

def getHail(fileName):
    start = list(map(lambda x: x.split(" @ "), open(fileName).read().split("\n")))
    hail = []
    for i in start:
        hail.append(list(map(lambda x: list(map(lambda y: int(y), x.split(", "))), i)))
    return hail

def part1(fileName):
    total = 0
    hail = getHail(fileName)
    for i in range(len(hail)):
        for j in range(len(hail)):
            if i > j:
                total += getIntersect(hail[i], hail[j])
    return total

def getDistance(line, point, vel):
    if line[1][0] == 0 and (line[1][1] + vel[1]) == 0:
        return 0
    index = 1 if line[1][0] + vel[0] == 0 else 0
    dist = (line[0][index] - point[index]) / -(line[1][index] + vel[index])
    return dist if dist.is_integer() else -1

def checkLine(line, point, vel):
    div = getDistance(line, point, vel)
    if div == -1 or int(line[0][2] + ((line[1][2] + vel[2]) * div)) != point[2]:
        return False
    return True

def getLine(line, point, vel):
    return [point[0], point[1], int(line[0][2] + ((line[1][2] + vel[2]) * getDistance(line, point, vel)))]

def checkOption(hail, num, vel):
    res = getIntersect(hail[0], hail[1], vel)
    if type(res) == str:
        return None
    for k in range(num*2 + 1):
        vel[2] += 1
        point = [hail[0][0][0] + (hail[0][1][0] + vel[0]) * res[0], hail[0][0][1] + (hail[0][1][1] + vel[1]) * res[0]]
        intersection = getLine(hail[0], point, vel)
        good = True
        for i in hail:
            if not checkLine(i, intersection, vel):
                good = False
                break
        if good:
            return intersection
    return None

def part2(fileName):
    hail = getHail(fileName)
    num = 300
    vel = [-num, -num, -num]
    for i in range(num*2 + 1):
        for j in range(num*2 + 1):
            res = checkOption(hail, num, vel)
            if res != None:
                return int(sum(res))
            vel[2] = -num
            vel[1] += 1
        vel[1] = -num
        vel[0] += 1

print(part1("in.txt"))
print(part2("in.txt"))