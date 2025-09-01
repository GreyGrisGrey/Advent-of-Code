def part1():
    opens = []
    closed = {}
    counts = {False:0}
    count = 0
    for i in open("in.txt").read().split("\n"):
        counts[count] = 0
        coords = list(map(lambda x: int(x), i.split(", ")))
        opens.append([coords[0], coords[1], count, 0])
        count += 1
    steps = 0
    remaining = len(opens)
    options = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while steps < 202:
        if remaining == 0:
            if steps == 200:
                snapshot = counts.copy()
            remaining = len(opens)
            steps += 1
        remaining -= 1
        curr = opens[0]
        key = str(curr[0]) + ":" + str(curr[1])
        if key in closed and curr[2] != closed[key][0] and curr[3] <= closed[key][1]:
            counts[closed[key][0]] -= 1
            closed[key] = [False, 0]
        elif key not in closed:
            counts[curr[2]] += 1
            closed[key] = [curr[2], curr[3]]
            for i in range(4):
                nexts = [curr[0] + options[i][0], curr[1] + options[i][1], curr[2], curr[3] + 1]
                nextKey = str(nexts[0]) + ":" + str(nexts[1])
                if nextKey not in closed:
                    opens.append(nexts)
        del opens[0]
    maximum = 0
    for i in snapshot:
        if snapshot[i] == counts[i] and counts[i] > maximum:
            maximum = counts[i]
    return maximum

def part2():
    opens = []
    counts = {False:0}
    spaces = {}
    closed = {}
    count = 0
    minimums = [500, 500]
    maximums = [100, 100]
    for i in open("in.txt").read().split("\n"):
        counts[count] = 0
        coords = list(map(lambda x: int(x), i.split(", ")))
        opens.append([coords[0], coords[1], count])
        count += 1
        if coords[0] < minimums[0]:
            minimums[0] = coords[0]
        elif coords[0] > maximums[0]:
            maximums[0] = coords[0]
        if coords[1] < minimums[1]:
            minimums[1] = coords[1]
        elif coords[1] > maximums[1]:
            maximums[1] = coords[1]
    minimums[0] -= 10
    minimums[1] -= 10
    maximums[0] += 10
    maximums[1] += 10
    steps = 0
    remaining = len(opens)
    options = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while len(opens) != 0:
        if remaining == 0:
            remaining = len(opens)
            steps += 1
        remaining -= 1
        curr = opens[0]
        key1 = str(curr[0]) + ":" + str(curr[1])
        key2 = str(curr[0]) + ":" + str(curr[1]) + ":" + str(curr[2])
        if key1 not in spaces:
            spaces[key1] = 0
        if True:
            closed[key2] = True
            spaces[key1] += steps
            for i in options:
                nexts = [curr[0] + i[0], curr[1] + i[1], curr[2]]
                nextKey = str(nexts[0]) + ":" + str(nexts[1]) + ":" + str(nexts[2])
                if nexts[0] > minimums[0] and nexts[1] > minimums[1] and nexts[0] < maximums[0] and nexts[1] < maximums[1] and nextKey not in closed:
                    closed[nextKey] = True
                    opens.append(nexts)
        del opens[0]
    count = 0
    for i in spaces:
        if spaces[i] < 10000:
            count += 1
    return count

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
