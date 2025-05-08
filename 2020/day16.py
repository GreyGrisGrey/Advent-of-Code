def partBoth():
    totalError = 0
    skip = False
    ticket = None
    tickets = []
    valDictP1 = {}
    valDictP2 = {}
    valDicts = []
    dictDone = False
    valDictCount = 0
    for i in open("in.txt", "r"):
        if i == "\n":
            dictDone = True
            skip = True
        elif skip:
            skip = False
        elif dictDone and ticket != None:
            tickets.append(i.strip("\n").split(","))
        elif not dictDone:
            nums = i.strip("\n").split(" ")
            rangeAMin, rangeAMax = nums[len(nums)-1].split("-")
            rangeBMin, rangeBMax = nums[len(nums)-3].split("-")
            count = 0
            if len(nums) == 5:
                name = nums[0] + nums[1]
            elif len(nums) == 4:
                name = nums[0]
            valDictP2[name] = valDictCount
            valDicts.append({})
            valDictCount += 1
            while count < 1000:
                if (count <= int(rangeAMax) and count >= int(rangeAMin)) or (count <= int(rangeBMax) and count >= int(rangeBMin)):
                    valDictP1[count] = True
                    valDicts[valDictP2[name]][count] = True
                count += 1
        else:
            ticket = i.strip("\n").split(",")
    goodTickets = []
    for i in tickets:
        good = True
        for j in i:
            if int(j) not in valDictP1:
                totalError += int(j)
                good = False
        if good:
            goodTickets.append(i)
    columnDicts = []
    sums = []
    for i in valDicts:
        newTotal = 0
        newDict = {}
        for j in range(len(tickets[1])):
            newDict[j] = True
            for k in goodTickets:
                if int(k[j]) not in i:
                    newDict[j] = False
                    break
            if newDict[j] == True:
                newTotal += 1
        sums.append(newTotal)
        columnDicts.append(newDict)
    doneCols = {}
    for i in range(20):
        for j in range(len(sums)):
            if sums[j] == i + 1:
                for k in columnDicts[j]:
                    if columnDicts[j][k] == True and k not in doneCols:
                        for l in valDictP2:
                            if valDictP2[l] == j:
                                doneCols[k] = l
                        break
                break
    totalTicket = 1
    for i in doneCols:
        if "departure" in doneCols[i]:
            totalTicket *= int(ticket[i])
    return totalError, totalTicket

print(partBoth())