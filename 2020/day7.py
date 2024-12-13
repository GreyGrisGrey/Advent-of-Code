def partTotal():
    f = open("input.txt")
    itemDict = {}
    itemIndex = 0
    itemList = []
    itemCounts = []
    end = 0
    for i in f:
        words = i.split(" ")
        itemDict[words[0] + words[1]] = itemIndex
        itemIndex += 1
        count = 4
        numList = []
        bagList = []
        while count < len(words):
            if words[count] == "no":
                break
            if (count)%4 == 0:
                numList.append(int(words[count]))
                count += 1
            elif (count)%4 == 1:
                bagList.append(words[count] + words[count+1])
                count += 3
        itemList.append(bagList)
        itemCounts.append(numList)
    bagCount = 0
    for i in itemDict:
        tempList = [i]
        tempCount = [1]
        if i != "shinygold":
            while len(tempList) > 0:
                if tempList[len(tempList)-1] == "shinygold":
                    end += 1
                    tempList = []
                else:
                    temp = tempList[len(tempList)-1]
                    del tempList[len(tempList)-1]
                    for j in itemList[itemDict[temp]]:
                        tempList.append(j)
        else:
            while len(tempList) > 0:
                tempIndex = len(tempList)-1
                temp = tempList[tempIndex]
                tempVal = tempCount[tempIndex]
                del tempCount[tempIndex]
                del tempList[tempIndex]
                for j in itemCounts[itemDict[temp]]:
                    bagCount += j * tempVal
                    tempCount.append(j*tempVal)
                for j in itemList[itemDict[temp]]:
                    tempList.append(j)
    return "Part 1: " + str(end) + " Part 2: " + str(bagCount)

print(partTotal())