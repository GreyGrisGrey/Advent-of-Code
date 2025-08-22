from math import floor, gcd, atan2, pi

def partBoth(fileName = "in.txt"):
    asteroids = {}
    x, y = 0, 0
    for i in open(fileName).read().split("\n"):
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
    polars = []
    for i in best[2]:
        coords = [floor(i/1000) - floor(best[1]/1000), (i % 1000) - (best[1] % 1000)]
        newCoord = atan2(coords[1], coords[0])
        polars.append([newCoord, [floor(i/1000), i % 1000]])
    polars.sort(key= lambda x: x[0])
    polars.reverse()
    currIndex = len(polars) - 1
    while True:
        if polars[currIndex][0] >= -pi/2:
            currIndex = (currIndex - 199) % len(polars)
            return (best[0], polars[currIndex][1])
        currIndex -= 1


if __name__ == "__main__":
    res = partBoth("in10.txt")
    print("Part 1:", res[0])
    print("Part 2:", res[1][0] * 100 + res[1][1])