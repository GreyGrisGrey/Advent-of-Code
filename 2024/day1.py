def partBoth():
    left, right = [], []
    numDict = {}
    total = [0, 0]
    for i in open("in.txt"):
        res = i.strip().split("   ")
        numDict[int(res[1])] = 1 if int(res[1]) not in numDict else numDict[int(res[1])] + 1
        left.append(int(res[0]))
        right.append(int(res[1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        total[0] += abs(left[i] - right[i])
        if left[i] in numDict:
            total[1] += left[i] * numDict[left[i]]
    return total

print(partBoth())