def partBoth(file, end):
    numDict = {}
    curr = 0
    for i in open(file).readline().split(","):
        numDict[int(i)] = curr
        curr += 1
    for i in range(end-1):
        if i < curr:
            total = 0
        else:
            if total in numDict:
                temp = numDict[total]
                numDict[total] = i
                total = i - temp
            else:
                numDict[total] = i
                total = 0
    return total

print("Part 1:", partBoth("input.txt", 2020))
print("Part 2:", partBoth("input.txt", 30000000))