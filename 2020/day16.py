def part1():
    total = 0
    skip = False
    ticket = None
    tickets = []
    valDict = {}
    dictDone = False
    for i in open("in.txt", "r"):
        if i == "\n":
            dictDone = True
            skip = True
        elif skip:
            skip = False
        elif ticket == None:
            ticket = i.strip("\n").split(",")
        elif dictDone:
            tickets.append(i.strip("\n").split(","))
        else:
            nums = i.strip("\n").split(" ")
            rangeAMin, rangeAMax = nums[len(nums)-1].split("-")
            rangeBMin, rangeBMax = nums[len(nums)-3].split("-")
            count = 0
            while count < 1000:
                if count not in valDict:
                    valDict[count] = False
                elif (count < int(rangeAMax) and count > int(rangeAMin)) or (count < int(rangeBMax) and count > int(rangeBMin)):
                    valDict[count] = True
                count += 1
    for i in tickets:
        for j in i:
            if not valDict[int(j)]:
                total += int(j)
    return total

print(part1())