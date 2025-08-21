from math import floor, gcd, sin, cos, ceil
#Simply does not work for part 2, TODO return later
def search(step, prev, start, mapping):
    startCoords = [floor(start/1000) + 0.5, (start % 1000) + 0.5]
    change = [cos(step), -sin(step)]
    changePrev = [cos(prev), -sin(prev)]
    currCoords = [startCoords[0] + change[0]*70, startCoords[1] + change[1]*70]
    prevCoords = [startCoords[0] + changePrev[0]*70, startCoords[1] + changePrev[1]*70]
    while abs(currCoords[0] - startCoords[0]) > 0.3 or abs(currCoords[1] - startCoords[1]) > 0.3:
        currCoords[0] -= change[0] * 0.2
        currCoords[1] -= change[1] * 0.2
        prevCoords[0] -= changePrev[0] * 0.2
        prevCoords[1] -= changePrev[1] * 0.2
        if prev != -100000 and floor(currCoords[0]) + 0.5 and floor(currCoords[1]) + 0.5:
            if floor(currCoords[0]) + 0.5 <= currCoords[0] and floor(currCoords[1]) + 0.5 <= currCoords[1]:
                if (floor(currCoords[0]) * 1000 + floor(currCoords[1])) in mapping:
                    del mapping[floor(currCoords[0]) * 1000 + floor(currCoords[1])]
                    return [1, floor(currCoords[0]) * 1000 + floor(currCoords[1])]
    return [0, 0]

def part1(fileName = "in.txt"):
    asteroids = {}
    x, y = 0, 0
    for i in open("in.txt").read().split("\n"):
        for j in i:
            if j == "#":
                asteroids[x * 1000 + y] = True
            x += 1
        x = 0
        y += 1
    best = [0, 0, {}]
    maximum = y
    for i in asteroids:
        newMapping = asteroids.copy()
        del newMapping[i]
        total = -1
        for j in asteroids:
            if j != i:
                xDel, yDel = floor(j/1000) - floor(i/1000), (j % 1000) - (i % 1000)
                xCurr, yCurr = floor(i/1000) + xDel, (i % 1000) + yDel
                common = gcd(xDel, yDel)
                xDel = floor(xDel/common)
                yDel = floor(yDel/common)
                while (xCurr >= 0 and yCurr >= 0 and yCurr < maximum and xCurr < maximum):
                    xCurr += xDel
                    yCurr += yDel
                    if (xCurr * 1000 + yCurr) in newMapping:
                        del newMapping[xCurr * 1000 + yCurr]
        total = len(newMapping)
        if total >= best[0]:
            best[0] = total
            best[1] = i
            best[2] = newMapping
    print("Part 1:", best[0], best[1])
    total = 0
    prev = -100000
    for i in range(720):
        res = search((3.14159)/2 - (i/100), prev, best[1], best[2])
        prev = (3.14159)/2 - (i/100)
        total += res[0]
        if res[0] != 0:
            print(floor(res[1]/1000), res[1] % 1000, total)
        if total == 200:
            print(res[0], floor(res[1]/1000), res[1] % 1000)
            return
        


if __name__ == "__main__":
    part1("in10.txt")