from math import floor

def part1(fileName = "in.txt"):
    data = open(fileName).read().split("\n")
    spaces = {}
    tags = []
    tagMapping = {}
    reverseTag = {}
    for i in range(len(data[0])):
        for j in range(len(data)):
            spaces[i * 1000 + j] = data[j][i]
            if data[j][i] != " " and data[j][i] != "." and data[j][i] != "#":
                tags.append([i, j, data[j][i]])
    for i in tags:
        flag = False
        adj = [i[2]]
        space = None
        for j in range(4):
            curr = [i[0], i[1]]
            curr[1] += 1 if j == 2 else -1 if j == 3 else 0
            curr[0] += 1 if j == 0 else -1 if j == 1 else 0
            key = curr[0] * 1000 + curr[1]
            if key not in spaces:
                break
            elif spaces[key] != " " and spaces[key] != "." and spaces[key] != "#":
                adj.append(spaces[key])
            elif spaces[key] != " ":
                space = key
                flag = True
        if flag:
            adj.sort()
            if adj[0] + ":" + adj[1] + ":1" in tagMapping:
                tagMapping[adj[0] + ":" + adj[1] + ":2"] = space
                reverseTag[space] = adj[0] + ":" + adj[1] + ":2"
            else:
                tagMapping[adj[0] + ":" + adj[1] + ":1"] = space
                reverseTag[space] = adj[0] + ":" + adj[1] + ":1"
    opens = [tagMapping["A:A:1"]]
    end = tagMapping["Z:Z:1"]
    closed = {}
    steps = 0
    remaining = 1
    options = [1000, -1000, 1, -1]
    while len(opens) != 0:
        if remaining == 0:
            steps += 1
            remaining = len(opens)
        remaining -= 1
        curr = opens[0]
        if curr == end:
            return steps
        for i in options:
            if (curr + i) not in closed and spaces[curr + i] != "#":
                closed[curr + i] = True
                if spaces[curr + i] == ".":
                    opens.append(curr + i)
                else:
                    currTag = reverseTag[curr]
                    if currTag != "A:A:1":
                        if currTag.split(":")[2] == "2":
                            nextSpace = ":".join(currTag.split(":")[0:2:]) + ":1"
                        else:
                            nextSpace = ":".join(currTag.split(":")[0:2:]) + ":2"
                        closed[tagMapping[nextSpace]] = True
                        opens.append(tagMapping[nextSpace])
        del opens[0]

def part2(fileName = "in.txt"):
    data = open(fileName).read().split("\n")
    spaces = {}
    tags = []
    tagMapping = {}
    reverseTag = {}
    for i in range(len(data[0])):
        for j in range(len(data)):
            spaces[i * 1000 + j] = data[j][i]
            if data[j][i] != " " and data[j][i] != "." and data[j][i] != "#":
                tags.append([i, j, data[j][i]])
    for i in tags:
        flag = False
        adj = [i[2]]
        space = None
        for j in range(4):
            curr = [i[0], i[1]]
            curr[1] += 1 if j == 2 else -1 if j == 3 else 0
            curr[0] += 1 if j == 0 else -1 if j == 1 else 0
            key = curr[0] * 1000 + curr[1]
            if key not in spaces:
                break
            elif spaces[key] != " " and spaces[key] != "." and spaces[key] != "#":
                adj.append(spaces[key])
            elif spaces[key] != " ":
                space = key
                flag = True
        if flag:
            adj.sort()
            if adj[0] + ":" + adj[1] + ":1" in tagMapping:
                tagMapping[adj[0] + ":" + adj[1] + ":2"] = space
                reverseTag[space] = adj[0] + ":" + adj[1] + ":2"
            else:
                tagMapping[adj[0] + ":" + adj[1] + ":1"] = space
                reverseTag[space] = adj[0] + ":" + adj[1] + ":1"
    opens = [[tagMapping["A:A:1"], 0]]
    end = tagMapping["Z:Z:1"]
    closed = {}
    steps = 0
    remaining = 1
    options = [1000, -1000, 1, -1]
    minmaxX = [18, 105]
    minmaxY = [18, 105]
    while len(opens) != 0:
        if remaining == 0:
            steps += 1
            remaining = len(opens)
        remaining -= 1
        curr = opens[0][0]
        if curr == end and opens[0][1] == 0:
            return steps
        for i in options:
            if (curr + i + (opens[0][1] * 1000000)) not in closed and spaces[curr + i] != "#":
                closed[curr + i + (opens[0][1] * 1000000)] = True
                if spaces[curr + i] == ".":
                    opens.append([curr + i, opens[0][1]])
                else:
                    currTag = reverseTag[curr]
                    if currTag != "A:A:1" and currTag != "Z:Z:1":
                        if currTag.split(":")[2] == "2":
                            nextSpace = ":".join(currTag.split(":")[0:2:]) + ":1"
                        else:
                            nextSpace = ":".join(currTag.split(":")[0:2:]) + ":2"
                        x = floor(curr/1000)
                        y = curr % 1000
                        num = -1 + opens[0][1]
                        if y > minmaxY[0] and y < minmaxY[1] and x < minmaxX[1] and x > minmaxX[0]:
                            num = 1 + opens[0][1]
                        if num >= 0:
                            closed[tagMapping[nextSpace] + num * 1000000] = True
                            opens.append([tagMapping[nextSpace], num])
        del opens[0]

if __name__ == "__main__":
    print("Part 1:", part1("in20.txt"))
    print("Part 2:", part2("in20.txt"))