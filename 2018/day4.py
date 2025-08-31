def getEntries(fileName = "in.txt"):
    sortable = list(map(lambda x: [x[1:17], x], open(fileName).read().split("\n")))
    sortable.sort(key = lambda x: x[0])
    return list(map(lambda x: x[1], sortable))

def part1():
    entries = getEntries()
    minutes = {}
    guardMinutes = {}
    curr = None
    sleepTime = None
    worst = [0, 0]
    for i in entries:
        currLine = i.split(" ")
        if currLine[2] == "Guard":
            curr = int(currLine[3][1::])
            if curr not in minutes:
                minutes[curr] = 0
                guardMinutes[curr] = {}
        elif currLine[2] == "falls":
            sleepTime = currLine[1].strip("]")
        else:
            wakeTime = currLine[1].strip("]")
            times = [list(map(lambda x: int(x), sleepTime.split(":"))), list(map(lambda x: int(x), wakeTime.split(":")))]
            if times[1][0] != 23:
                minutes[curr] += times[1][1]
                if times[0][0] != 23:
                    minutes[curr] -= times[0][1]
                    for j in range(times[1][1] - times[0][1]):
                        currNum = j + times[0][1]
                        guardMinutes[curr][currNum] = 1 if currNum not in guardMinutes[curr] else guardMinutes[curr][currNum] + 1
                else:
                    for j in range(times[1][1]):
                        guardMinutes[curr][j] = 1 if j not in guardMinutes[curr] else guardMinutes[curr][j] + 1
    for i in minutes:
        if minutes[i] > worst[0]:
            worst = [minutes[i], i]
    maximum = [0, 0]
    for i in guardMinutes[worst[1]]:
        if guardMinutes[worst[1]][i] > maximum[0]:
            maximum = [guardMinutes[worst[1]][i], i]
    return maximum[1] * worst[1]

def part2():
    entries = getEntries()
    minutes = {}
    guardMinutes = {}
    curr = None
    sleepTime = None
    worst = [0, 0]
    for i in entries:
        currLine = i.split(" ")
        if currLine[2] == "Guard":
            curr = int(currLine[3][1::])
            if curr not in minutes:
                minutes[curr] = 0
                guardMinutes[curr] = {}
        elif currLine[2] == "falls":
            sleepTime = currLine[1].strip("]")
        else:
            wakeTime = currLine[1].strip("]")
            times = [list(map(lambda x: int(x), sleepTime.split(":"))), list(map(lambda x: int(x), wakeTime.split(":")))]
            if times[1][0] != 23:
                minutes[curr] += times[1][1]
                if times[0][0] != 23:
                    minutes[curr] -= times[0][1]
                    for j in range(times[1][1] - times[0][1]):
                        currNum = j + times[0][1]
                        guardMinutes[curr][currNum] = 1 if currNum not in guardMinutes[curr] else guardMinutes[curr][currNum] + 1
                else:
                    for j in range(times[1][1]):
                        guardMinutes[curr][j] = 1 if j not in guardMinutes[curr] else guardMinutes[curr][j] + 1
    maximum = [0, 0, 0]
    for i in guardMinutes:
        for j in guardMinutes[i]:
            if guardMinutes[i][j] > maximum[0]:
                maximum = [guardMinutes[i][j], i, j]
    return maximum[1] * maximum[2]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())