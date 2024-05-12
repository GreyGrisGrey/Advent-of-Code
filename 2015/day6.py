def part1():
    f = open("input.txt")
    lightMap = {}
    for i in range(1000):
        for j in range(1000):
            lightMap[str(i) + "x" + str(j)] = False
    for i in f:
        line = i.split()
        if line[0] == "toggle":
            start = line[1].split(",")
            end = line[3].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    lightMap[str(count1) + "x" + str(count2)] = not lightMap[str(count1) + "x" + str(count2)]
                    count2 += 1
                count1 += 1
        elif line[1] == "on":
            start = line[2].split(",")
            end = line[4].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    lightMap[str(count1) + "x" + str(count2)] = True
                    count2 += 1
                count1 += 1
        else:
            start = line[2].split(",")
            end = line[4].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    lightMap[str(count1) + "x" + str(count2)] = False
                    count2 += 1
                count1 += 1
    lights = 0
    for i in lightMap:
        if lightMap[i]:
            lights += 1
    print(lights)

def part2():
    f = open("input.txt")
    lightMap = {}
    for i in range(1000):
        for j in range(1000):
            lightMap[str(i) + "x" + str(j)] = 0
    for i in f:
        line = i.split()
        if line[0] == "toggle":
            start = line[1].split(",")
            end = line[3].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    lightMap[str(count1) + "x" + str(count2)] += 2
                    count2 += 1
                count1 += 1
        elif line[1] == "on":
            start = line[2].split(",")
            end = line[4].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    lightMap[str(count1) + "x" + str(count2)] += 1
                    count2 += 1
                count1 += 1
        else:
            start = line[2].split(",")
            end = line[4].split(",")
            start[0] = int(start[0])
            start[1] = int(start[1])
            end[0] = int(end[0])
            end[1] = int(end[1])
            count1 = start[0]
            while count1 <= end[0]:
                count2 = start[1]
                while count2 <= end[1]:
                    if lightMap[str(count1) + "x" + str(count2)] > 0:
                        lightMap[str(count1) + "x" + str(count2)] -=1
                    count2 += 1
                count1 += 1
    lights = 0
    for i in lightMap:
        lights += lightMap[i]
    print(lights)

part1()
part2()