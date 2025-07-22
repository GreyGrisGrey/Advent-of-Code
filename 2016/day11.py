def stringMap(mapping, floor):
    order = ""
    for i in mapping:
        order += (str(i * 10 + mapping[i]) + "-")
    order += (str(floor))
    return order

def numMap(mapping, floor, size):
    order = 0
    nums = []
    for i in range(size):
        nums.append(mapping[(i+2) * 10] * 10 + mapping[(i+2) * 10 + 1])
    nums.sort()
    nums.append(floor)
    for i in nums:
        order = order * 100 + i
    return order

def checkFine(option, size):
    for i in range(size):
        index = (i+2)*10+1
        if option[1][index - 1] != option[1][index]:
            for j in range(size):
                if option[1][index] == option[1][(j+2)*10]:
                    return False
    return True

def checkDone(option):
    for i in option:
        if option[i] != 3:
            return False
    return True

def part1():
    data = map(lambda x: x.split(" "), open("in.txt", "r").read().split("\n"));
    nums = {}
    idMap = {}
    curr = 0
    currID = 2
    for i in data:
        if len(i) == 7:
            name = i[5].split("-")
            if name[0] not in idMap:
                idMap[name[0]] = currID
                currID += 1
            if len(name) == 2:
                nums[idMap[name[0]]*10 + 1] = curr
            else:
                nums[idMap[name[0]]*10] = curr
        elif len(i) > 7:
            for j in range(int((len(i)-5)/3)):
                name = i[len(i)-2 if j == 0 else 5 + (j-1)*3].split("-")
                if name[0] not in idMap:
                    idMap[name[0]] = currID
                    currID += 1
                if len(name) == 2:
                    nums[idMap[name[0]]*10 + 1] = curr
                else:
                    nums[idMap[name[0]]*10] = curr
        curr += 1
    opens = [(0, nums, 0)]
    closed = {}
    step = 0
    size = int(len(nums)/2)
    while True:
        curr = opens[0]
        name = numMap(curr[1], curr[2], size)
        if name not in closed:
            closed[name] = True
            if checkFine(curr, size):
                step += 1
                if checkDone(curr[1]):
                    return curr[0]
                for i in curr[1]:
                    for j in curr[1]:
                        if curr[1][i] == curr[2] and curr[1][j] == curr[2] and j <= i:
                            if curr[2] < 3:
                                newDict = curr[1].copy()
                                newDict[i] = curr[2] + 1
                                newDict[j] = curr[2] + 1
                                if numMap(newDict, curr[2]+1, size) not in closed:
                                    opens.append((curr[0] + 1, newDict, curr[2] + 1))
                            if curr[2] > 0:
                                newDict = curr[1].copy()
                                newDict[i] = curr[2] - 1
                                newDict[j] = curr[2] - 1
                                if numMap(newDict, curr[2]-1, size) not in closed:
                                    opens.append((curr[0] + 1, newDict, curr[2] - 1))
        del opens[0]

def part2():
    data = map(lambda x: x.split(" "), open("in.txt", "r").read().split("\n"));
    nums = {}
    idMap = {}
    curr = 0
    currID = 2
    for i in data:
        if len(i) == 7:
            name = i[5].split("-")
            if name[0] not in idMap:
                idMap[name[0]] = currID
                currID += 1
            if len(name) == 2:
                nums[idMap[name[0]]*10 + 1] = curr
            else:
                nums[idMap[name[0]]*10] = curr
        elif len(i) > 7:
            for j in range(int((len(i)-5)/3)):
                name = i[len(i)-2 if j == 0 else 5 + (j-1)*3].split("-")
                if name[0] not in idMap:
                    idMap[name[0]] = currID
                    currID += 1
                if len(name) == 2:
                    nums[idMap[name[0]]*10 + 1] = curr
                else:
                    nums[idMap[name[0]]*10] = curr
        curr += 1
    nums[currID*10] = 0
    nums[currID*10 + 1] = 0
    currID += 1
    nums[currID*10] = 0
    nums[currID*10 + 1] = 0
    opens = [(0, nums, 0)]
    closed = {}
    step = 0
    size = int(len(nums)/2)
    while True:
        curr = opens[0]
        name = numMap(curr[1], curr[2], size)
        if name not in closed:
            closed[name] = True
            if checkFine(curr, size):
                step += 1
                if checkDone(curr[1]):
                    return curr[0]
                for i in curr[1]:
                    for j in curr[1]:
                        if curr[1][i] == curr[2] and curr[1][j] == curr[2] and j <= i:
                            if curr[2] < 3:
                                newDict = curr[1].copy()
                                newDict[i] = curr[2] + 1
                                newDict[j] = curr[2] + 1
                                if numMap(newDict, curr[2]+1, size) not in closed:
                                    opens.append((curr[0] + 1, newDict, curr[2] + 1))
                            if curr[2] > 0:
                                newDict = curr[1].copy()
                                newDict[i] = curr[2] - 1
                                newDict[j] = curr[2] - 1
                                if numMap(newDict, curr[2]-1, size) not in closed:
                                    opens.append((curr[0] + 1, newDict, curr[2] - 1))
        del opens[0]

print(part1())
print(part2())