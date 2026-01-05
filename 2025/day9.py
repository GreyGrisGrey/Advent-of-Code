def part1():
    points = []
    maximum = 0
    listRects = []
    for i in open("in.txt", "r").read().split("\n"):
        points.append(list(map(lambda x: int(x), i.split(","))))
    for i in points:
        for j in points:
            size = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
            listRects.append(size)
            if size > maximum:
                maximum = size
    newRects = sorted(listRects)
    newRects.reverse()
    return maximum

def checkGood(point1, point2, point3):
    if point3[0] > point1[0] and point3[0] > point2[0]:
        return True
    if point3[0] < point1[0] and point3[0] < point2[0]:
        return True
    if point3[1] > point1[1] and point3[1] > point2[1]:
        return True
    if point3[1] < point1[1] and point3[1] < point2[1]:
        return True
    return False

def part2():
    points = []
    tiles = set()
    first = set()
    second = set()
    for i in open("in.txt", "r").read().split("\n"):
        points.append(list(map(lambda x: int(x), i.split(","))))
    points.append(points[0])
    curr = None
    for i in range(len(points) - 1):
        if curr == None:
            curr = points[i]
        next = points[i + 1]
        moveX = curr[0] - next[0]
        moveY = curr[1] - next[1]
        while moveX > 0:
            tiles.add((curr[0], curr[1]))
            first.add((curr[0], curr[1] + 1))
            second.add((curr[0], curr[1] - 1))
            moveX -= 1
            curr[0] -= 1
            tiles.add((curr[0], curr[1]))
            first.add((curr[0], curr[1] + 1))
            second.add((curr[0], curr[1] - 1))
        while moveX < 0:
            tiles.add((curr[0], curr[1]))
            first.add((curr[0], curr[1] - 1))
            second.add((curr[0], curr[1] + 1))
            moveX += 1
            curr[0] += 1
            tiles.add((curr[0], curr[1]))
            first.add((curr[0], curr[1] - 1))
            second.add((curr[0], curr[1] + 1))
        while moveY > 0:
            tiles.add((curr[0], curr[1]))
            first.add((curr[0] - 1, curr[1]))
            second.add((curr[0] + 1, curr[1]))
            moveY -= 1
            curr[1] -= 1
            tiles.add((curr[0], curr[1]))
            first.add((curr[0] - 1, curr[1]))
            second.add((curr[0] + 1, curr[1]))
        while moveY < 0:
            tiles.add((curr[0], curr[1]))
            first.add((curr[0] + 1, curr[1]))
            second.add((curr[0] - 1, curr[1]))
            moveY += 1
            curr[1] += 1
            tiles.add((curr[0], curr[1]))
            first.add((curr[0] + 1, curr[1]))
            second.add((curr[0] - 1, curr[1]))
    rayCurr = [5000, -1]
    flag = False
    while True:
        rayCurr[1] += 1
        if (rayCurr[0], rayCurr[1]) in first:
            flag = True
            break
        elif (rayCurr[0], rayCurr[1]) in second:
            flag = False
            break
    if flag:
        outline = first - (second | tiles)
    else:
        outline = second - (first | tiles)
    listRects = []
    for i in points:
        for j in points:
            size = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
            listRects.append([size, i, j])
    newRects = sorted(listRects)
    newRects.reverse()
    for i in newRects:
        good = True
        for j in outline:
            if not checkGood(i[1], i[2], j):
                good = False
                break
        if good:
            return i[0]
    return 0

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())