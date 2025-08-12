from math import floor
def BFS(mapping, start, keys):
    newStart = [start[0], start[1], 0, []]
    opens = [newStart]
    closed = {}
    keyPaths = {}
    newMapping = {}
    steps = 0
    remaining = 1
    newMapping[start[0] * 1000 + start[1]] = []
    while len(opens) > 0:
        curr = opens[0]
        currKey = curr[0] * 1000 + curr[1]
        nexts = [currKey + 1000, currKey - 1000, currKey + 1, currKey - 1]
        if remaining == 0:
            remaining = len(opens)
            steps += 1
        remaining -= 1
        closed[currKey] = True
        for i in nexts:
            if i not in closed and i in mapping:
                if mapping[i] == "." or ord(mapping[i]) > 93:
                    opens.append([floor(i/1000), i % 1000, steps, curr[3]])
                    newMapping[i] = curr[3]
                    closed[i] = True
                elif ord(mapping[i]) < 93 and mapping[i] != "#":
                    newOrder = curr[3].copy()
                    newOrder.append(mapping[i])
                    opens.append([floor(i/1000), i % 1000, steps, newOrder])
                    newMapping[i] = newOrder
                    closed[i] = True
        del opens[0]
    for i in keys:
        currLetter = i[2]
        required = newMapping[i[0] * 1000 + i[1]]
        keyPaths[currLetter] = required
    return keyPaths

def pathFind(first, second, mapping):
    newStart = [first[0], first[1], 0]
    opens = [newStart]
    closed = {}
    steps = 0
    remaining = 1
    while len(opens) > 0:
        curr = opens[0]
        currKey = curr[0] * 1000 + curr[1]
        nexts = [currKey + 1000, currKey - 1000, currKey + 1, currKey - 1]
        if remaining == 0:
            remaining = len(opens)
            steps += 1
        if curr[0] == second[0] and curr[1] == second[1]:
            return steps
        remaining -= 1
        closed[currKey] = True
        for i in nexts:
            if i not in closed and i in mapping:
                if mapping[i] != "#" or ord(mapping[i]) > 93:
                    opens.append([floor(i/1000), i % 1000, steps])
        del opens[0]
    return steps

def checkNext(first, second, keyMapping, checked):
    if first == second or chr(ord(second) - 32) in checked:
        return False
    for i in keyMapping[second]:
        if i not in checked:
            return False
    return True

def part1():
    data = open("in.txt").read().split("\n")
    spaces = {}
    start = None
    doors = []
    keys = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            spaces[j * 1000 + i] = data[i][j]
            if data[i][j] != "#" and data[i][j] != ".":
                if data[i][j] == "@":
                    start = [j, i]
                    keys.append([j, i, data[i][j]])
                elif ord(data[i][j]) < 93:
                    doors.append([j, i, data[i][j]])
                else:
                    keys.append([j, i, data[i][j]])
    keyPaths = BFS(spaces, start, keys)
    paths = {}
    for i in keys:
        paths[i[2]] = {}
        for j in keys:
            paths[i[2]][j[2]] = pathFind(i, j, spaces)
    opens = [["@", 0, [" "]]]
    cache = {}
    cache["@: "] = 0
    steps = 0
    while True:
        delList = []
        for i in range(len(opens)):
            if steps == opens[i][1]:
                if len(opens[i][2]) == len(keys):
                    return opens[i][1]
                delList.append(i)
                for j in keys:
                    if checkNext(opens[i][0], j[2], keyPaths, opens[i][2]):
                        newListing = opens[i][2].copy()
                        newListing.append(chr(ord(j[2]) - 32))
                        newListing.sort()
                        key = j[2] + ":" + "".join(newListing)
                        if key not in cache or opens[i][1] + paths[opens[i][0]][j[2]] < cache[key]:
                            opens.append([j[2], opens[i][1] + paths[opens[i][0]][j[2]], newListing])
                            cache[key] = opens[i][1] + paths[opens[i][0]][j[2]]
        delList.reverse()
        steps += 1
        for i in delList:
            del opens[i]

def BFS2(mapping, start, keys):
    newStart = [start[0], start[1], 0, []]
    opens = [newStart]
    closed = {}
    keyPaths = {}
    newMapping = {}
    steps = 0
    remaining = 1
    newMapping[start[0] * 1000 + start[1]] = []
    while len(opens) > 0:
        curr = opens[0]
        currKey = curr[0] * 1000 + curr[1]
        nexts = [currKey + 1000, currKey - 1000, currKey + 1, currKey - 1]
        if remaining == 0:
            remaining = len(opens)
            steps += 1
        remaining -= 1
        closed[currKey] = True
        for i in nexts:
            if i not in closed and i in mapping:
                if mapping[i] == "." or ord(mapping[i]) > 93:
                    opens.append([floor(i/1000), i % 1000, steps, curr[3]])
                    newMapping[i] = curr[3]
                    closed[i] = True
                elif ord(mapping[i]) < 93 and mapping[i] != "#":
                    newOrder = curr[3].copy()
                    newOrder.append(chr(ord(mapping[i]) + 32))
                    opens.append([floor(i/1000), i % 1000, steps, newOrder])
                    newMapping[i] = newOrder
                    closed[i] = True
        del opens[0]
    for i in keys:
        currLetter = i[2]
        if i[0] * 1000 + i[1] in newMapping:
            required = newMapping[i[0] * 1000 + i[1]]
            keyPaths[currLetter] = required
    return keyPaths


def part2():
    data = open("in.txt").read().split("\n")
    spaces = {}
    start = None
    doors = []
    keys = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            spaces[j * 1000 + i] = data[i][j]
            if data[i][j] != "#" and data[i][j] != ".":
                if data[i][j] == "@":
                    start = [j, i]
                elif ord(data[i][j]) < 93:
                    doors.append([j, i, data[i][j]])
                else:
                    keys.append([j, i, data[i][j]])
    spaces[start[0] * 1000 + start[1]] = "#"
    spaces[start[0] * 1000 + start[1] + 1] = "#"
    spaces[start[0] * 1000 + start[1] - 1] = "#"
    spaces[start[0] * 1000 + start[1] + 1000] = "#"
    spaces[start[0] * 1000 + start[1] - 1000] = "#"
    spaces[start[0] * 1000 + start[1] + 1001] = "@"
    spaces[start[0] * 1000 + start[1] - 1001] = "@"
    spaces[start[0] * 1000 + start[1] + 999] = "@"
    spaces[start[0] * 1000 + start[1] - 999] = "@"
    topLeft = BFS2(spaces, [start[0] - 1, start[1] - 1], keys)
    topRight = BFS2(spaces, [start[0] + 1, start[1] - 1], keys)
    bottomLeft = BFS2(spaces, [start[0] - 1, start[1] + 1], keys)
    bottomRight = BFS2(spaces, [start[0] + 1, start[1] + 1], keys)
    groups = [topLeft, topRight, bottomLeft, bottomRight]
    groupMapping = {}
    paths = {}
    andKeys = [[start[0] - 1, start[1] - 1, "@"], [start[0] + 1, start[1] - 1, "@"], [start[0] - 1, start[1] + 1, "@"], [start[0] + 1, start[1] + 1, "@"]]
    for i in range(len(groups)):
        newSet = [andKeys[i]]
        for j in keys:
            if j[2] in groups[i]:
                groupMapping[j[2]] = i
                newSet.append(j)
        for j in newSet:
            if j[2] == "@":
                j[2] = "@" + str(i)
            paths[j[2]] = {}
            for k in newSet:
                paths[j[2]][k[2]] = pathFind(j, k, spaces)
    opens = [[["@0", "@1", "@2", "@3"], 0, ["@0", "@1", "@2", "@3"]]]
    steps = 0
    cache = {}
    cache["@0@1@2@3:@0@1@2@3"] = True
    stoppedCount = 0
    while len(opens) != 0:
        delList = []
        for i in range(len(opens)):
            curr = opens[i]
            if curr[1] == steps:
                delList.append(i)
                if len(curr[2]) == len(keys) + 4:
                    return curr[1]
                for j in keys:
                    if j[2] not in curr[2] and checkNext(curr[0][groupMapping[j[2]]], j[2], groups[groupMapping[j[2]]], curr[2]):
                        jIndex = groupMapping[j[2]]
                        newStarts = []
                        newEnds = curr[2].copy()
                        newEnds.append(j[2])
                        for k in range(4):
                            if k != jIndex:
                                newStarts.append(curr[0][k])
                            else:
                                newStarts.append(j[2])
                        newEnds.sort()
                        key = "".join(newStarts) + ":" + "".join(newEnds)
                        if key not in cache or cache[key] > curr[1] + paths[curr[0][jIndex]][j[2]]:
                            opens.append([newStarts, curr[1] + paths[curr[0][jIndex]][j[2]], newEnds])
                            cache[key] = curr[1] + paths[curr[0][jIndex]][j[2]]
                        else:
                            stoppedCount += 1              
        delList.reverse()
        steps += 1
        for i in delList:
            del opens[i]
                        
                
if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())