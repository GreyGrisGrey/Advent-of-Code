from math import sqrt

def changeCircuits(allCirc, new1, new2, new3):
    old1 = allCirc[new1]
    old2 = allCirc[new2]
    allCirc[new1] = new3
    allCirc[new2] = new3
    changed = 2
    for i in range(len(allCirc)):
        if (allCirc[i] == old1 or allCirc[i] == old2) and allCirc[i] != 0:
            allCirc[i] = new3
            changed += 1
    if changed >= len(allCirc):
        return True
    return False
    

def partBoth():
    circuits = []
    points = []
    for point in open("in.txt").read().split("\n"):
        points.append(point)
        circuits.append(0)
    distances = []
    for i in range(len(points)):
        lineDist = []
        for j in range(len(points)):
            if i == j:
                lineDist.append(999999999999)
            else:
                nums1, nums2 = list(map(lambda x: int(x), points[i].split(","))), list(map(lambda x: int(x), points[j].split(",")))
                lineDist.append(sqrt(abs(nums1[0] - nums2[0])**2 + abs(nums1[1] - nums2[1])**2 + abs(nums1[2] - nums2[2])**2))
        distances.append(lineDist)
    for i in range(1000):
        minDist = [999999999999, 0, 0]
        for j in range(len(distances)):
            for k in range(len(distances[j])):
                if distances[j][k] < minDist[0]:
                    minDist[0] = distances[j][k]
                    minDist[1] = j
                    minDist[2] = k
        distances[minDist[1]][minDist[2]] = 999999999999
        distances[minDist[2]][minDist[1]] = 999999999999
        res = changeCircuits(circuits, minDist[1], minDist[2], i + 1)
    numDict = {}
    for i in circuits:
        numDict[i] = 1 if i not in numDict else numDict[i] + 1
    top3 = [1, 1, 1]
    for i in numDict:
        if i != 0:
            if numDict[i] > top3[0]:
                top3[2] = top3[1]
                top3[1] = top3[0]
                top3[0] = numDict[i]
            elif numDict[i] > top3[1]:
                top3[2] = top3[1]
                top3[1] = numDict[i]
            elif numDict[i] > top3[2]:
                top3[2] = numDict[i]
    count = 1000
    while True:
        minDist = [999999999999, 0, 0]
        for j in range(len(distances)):
            for k in range(len(distances[j])):
                if circuits[j] == circuits[k] and circuits[j] != 0:
                    distances[j][k] = 999999999999
                    distances[k][j] = 999999999999
                if distances[j][k] < minDist[0]:
                    minDist[0] = distances[j][k]
                    minDist[1] = j
                    minDist[2] = k
        distances[minDist[1]][minDist[2]] = 999999999999
        distances[minDist[2]][minDist[1]] = 999999999999
        res = changeCircuits(circuits, minDist[1], minDist[2], count + 1)
        count += 1
        if res:
            return [top3[0] * top3[1] * top3[2], int(points[minDist[1]].split(",")[0]) * int(points[minDist[2]].split(",")[0])]

if __name__ == "__main__":
    res = partBoth()
    print("Part 1:", res[0])
    print("Part 2:", res[1])