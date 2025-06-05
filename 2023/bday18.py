def BFS(perimeterDict, open):
    closed = {}
    while len(open) > 0:
        curr = open[0].copy()
        key = str(curr[0]) + ":" + str(curr[1])
        if key in closed or key in perimeterDict:
            del open[0]
            closed[key] = True
            pass
        else:
            del open[0]
            closed[key] = True
            open.append([curr[0]+1, curr[1]])
            open.append([curr[0]-1, curr[1]])
            open.append([curr[0], curr[1]+1])
            open.append([curr[0], curr[1]-1])
            open.append([curr[0]+1, curr[1]-1])
            open.append([curr[0]-1, curr[1]-1])
            open.append([curr[0]+1, curr[1]+1])
            open.append([curr[0]-1, curr[1]+1])
    return len(closed)

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
            res[1] -= 1
            perimeterDict[str(curr[0]) + ":" + str(curr[1])] = res[2]
        if curr[0] < X[0]:
            X[0] = curr[0]
        elif curr[0] > X[1]:
            X[1] = curr[0]
        if curr[1] < Y[0]:
            Y[0] = curr[1]
        elif curr[1] > Y[1]:
            Y[1] = curr[1]
    return BFS(perimeterDict, [[1, 1]])

def part2():
    vertexDict = {}
    dirDict = {"R":(1, 0), "L":(-1, 0), "U":(0, -1), "D":(0, 1)}
    curr = [0, 0]
    mins = [0, 0]
    for i in open("in.txt"):
        res = i.strip().split(" ")
        res[1] = int(res[1])
        if ":".join(curr) in vertexDict:
            vertexDict[":".join(curr)] += res[0]
        else:
            vertexDict[":".join(curr)] = res[0]
        curr[0] += dirDict[res[0]][0]
        curr[1] += dirDict[res[0]][1]

print(part1())