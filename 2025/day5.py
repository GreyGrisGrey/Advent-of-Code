def part1():
    ranges = []
    rangeCheck = True
    total = 0
    for i in open("in.txt").read().split("\n"):
        if i == "":
            rangeCheck = False
        elif rangeCheck:
            ranges.append(list(map(lambda x:int(x), i.split("-"))))
        else:
            for j in ranges:
                if int(i) >= j[0] and int(i) <= j[1]:
                    total += 1
                    break
    return total

def checkOverlap(first, second):
    if first[0] >= second[0] and first[0] <= second[1]:
        return True
    if first[1] <= second[1] and first[1] >= second[0]:
        return True
    if second[0] <= first[1] and second[0] >= first[0]:
        return True
    if second[0] >= first[0] and second[0] <= first[1]:
        return True
    return False

def part2():
    ranges = []
    total = 0
    maximum = 0
    for i in open("in.txt").read().split("\n"):
        if i == "":
            break
        else:
            ranges.append(list(map(lambda x:int(x), i.split("-"))))
            if ranges[len(ranges) - 1][1] > maximum:
                maximum = ranges[len(ranges) - 1][1]
    merged = True
    while merged:
        merged = False
        mergedRanges = []
        newRanges = []
        for i in range(len(ranges)):
            for j in range(len(ranges)):
                if i != j and i not in mergedRanges and j not in mergedRanges and checkOverlap(ranges[i], ranges[j]):
                    newRange = [ranges[i][0], ranges[i][1], ranges[j][0], ranges[j][1]]
                    newRanges.append([min(newRange), max(newRange)])
                    mergedRanges.append(i)
                    mergedRanges.append(j)
                    merged = True
            if i not in mergedRanges:
                newRanges.append(ranges[i])
        ranges = newRanges
    for i in ranges:
        total += i[1] - i[0] + 1
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())