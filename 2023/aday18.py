def checkIn(perimeter, x, y, size):
    if str(x) + ":" + str(y) in perimeter:
        return True
    else:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        currs = [[x, y], [x, y], [x, y], [x, y]]
        flags = [False, False, False, False]
        for i in range(size):
            for j in range(4):
                if not flags[j]:
                    currs[j][0] += dirs[j][0]
                    currs[j][1] += dirs[j][1]
                    if str(currs[j][0]) + ":" + str(currs[j][1]) in perimeter:
                        flags[j] = True
        for i in flags:
            if not i:
                return False
        return True

def part1():
    perimeterDict = {}
    dirDict = {"R":(1, 0), "L":(-1, 0), "U":(0, -1), "D":(0, 1)}
    curr = [0, 0]
    X = [0, 0]
    Y = [0, 0]
    for i in open("in.txt", "r"):
        res = i.strip().split(" ")
        res[1] = int(res[1])
        while res[1] > 0:
            curr[0] += dirDict[res[0]][0]
            curr[1] += dirDict[res[0]][1]
            perimeterDict[str(curr[0]) + ":" + str(curr[1])] = res[2]
            res[1] -= 1
        if curr[0] < X[0]:
            X[0] = curr[0]
        elif curr[0] > X[1]:
            X[1] = curr[0]
        if curr[1] < Y[0]:
            Y[0] = curr[1]
        elif curr[1] > Y[1]:
            Y[1] = curr[1]
    for i in range(abs(X[0]) + abs(X[1]) + 1):
        for j in range(abs(Y[0]) + abs(Y[1]) + 1):
            if checkIn(perimeterDict, X[0]+i, Y[0]+j, 500):
                perimeterDict[str(X[0]+i) + ":" + str(Y[0]+j)] = True
    return len(perimeterDict)

print(part1())