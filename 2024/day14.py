from time import sleep

def part1():
    f = open("input.txt")
    end = 0
    robots = []
    wide = 101
    tall = 103
    for i in f:
        words = i.split(" ")
        velTemp = words[1].split(",")
        vel = [int(velTemp[0][2::]), int(velTemp[1].strip())]
        posTemp = words[0].split(",")
        pos = [int(posTemp[0][2::]), int(posTemp[1])]
        robots.append([pos, vel])
    for i in range(100):
        for j in robots:
            j[0][0] += j[1][0]
            j[0][1] += j[1][1]
            if j[0][0] < 0:
                j[0][0] += wide
            if j[0][1] < 0:
                j[0][1] += tall
            if j[0][0] >= wide:
                j[0][0] -= wide
            if j[0][1] >= tall:
                j[0][1] -= tall
    quads = [0, 0, 0, 0]
    right = 0
    down = 0
    for i in robots:
        right = 0
        down = 0
        if i[0][0] < int((wide-1)/2):
            right = 1
        elif i[0][0] > int((wide-1)/2):
            right = 2
        if i[0][1] < int((tall-1)/2):
            down = 1
        elif i[0][1] > int((tall-1)/2):
            down = 2
        if right == 2:
            if down == 2:
                quads[3] += 1
            elif down == 1:
                quads[1] += 1
        elif right == 1:
            if down == 2:
                quads[2] += 1
            elif down == 1:
                quads[0] += 1
    return quads[0]*quads[1]*quads[2]*quads[3]

def part2():
    f = open("input.txt")
    end = 0
    robots = []
    wide = 101
    tall = 103
    for i in f:
        words = i.split(" ")
        velTemp = words[1].split(",")
        vel = [int(velTemp[0][2::]), int(velTemp[1].strip())]
        posTemp = words[0].split(",")
        pos = [int(posTemp[0][2::]), int(posTemp[1])]
        robots.append([pos, vel])
    for i in range(30000):
        indexMapping = {}
        for j in robots:
            j[0][0] += j[1][0]
            j[0][1] += j[1][1]
            if j[0][0] < 0:
                j[0][0] += wide
            if j[0][1] < 0:
                j[0][1] += tall
            if j[0][0] >= wide:
                j[0][0] -= wide
            if j[0][1] >= tall:
                j[0][1] -= tall
            if (str(j[0][0]) + "," + str(j[0][1])) in indexMapping:
                indexMapping[str(j[0][0]) + "," + str(j[0][1])] += 1
            else:
                indexMapping[str(j[0][0]) + "," + str(j[0][1])] = 1
        for j in range(wide):
            gridLine = ""
            for k in range(tall):
                if (str(j) + "," + str(k)) in indexMapping:
                    gridLine = gridLine + "#"
                else:
                    gridLine = gridLine + "."
            # it takes a long time
            # and you must stare at your terminal the entire time
            # but it works on my computer
            if "#########" in gridLine:
                print(gridLine, i)
        if i%10 == 0:
            print(i)
        
    

print(part1())
part2()