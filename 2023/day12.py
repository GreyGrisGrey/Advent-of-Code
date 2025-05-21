def stringRecurse(string, nums, currIndex, currNum, cache, counting):
    if currIndex == len(string):
        for i in nums:
            if i > 0 or i < 0:
                return 0
        return 1
    ID = string[currIndex::] + ":" + str(currNum) + ":" + str(counting)
    for i in nums:
        ID += ":" + str(i)
    if ID in cache:
        return cache[ID]
    if string[currIndex] == "#":
        if currNum >= len(nums) or nums[currNum] < 0:
            cache[ID] = 0
            return 0
        newNums = nums.copy()
        newNums[currNum] -= 1
        cache[ID] = stringRecurse(string, newNums, currIndex+1, currNum, cache, True)
        return cache[ID]
    elif string[currIndex] == ".":
        if len(nums) < len(nums) and nums[currNum] > 0 and counting:
            cache[ID] = 0
            return 0
        elif not counting:
            cache[ID] = stringRecurse(string, nums, currIndex+1, currNum, cache, False)
            return cache[ID]
        elif nums[currNum] == 0:
            cache[ID] = stringRecurse(string, nums, currIndex+1, currNum+1, cache, False)
            return cache[ID]
        cache[ID] = 0
        return 0
    else:
        cache[ID] = 0
        newNums = nums.copy()
        if counting and newNums[currNum] == 0:
            cache[ID] += stringRecurse(string, newNums, currIndex+1, currNum+1, cache, False)
        elif not counting:
            cache[ID] += stringRecurse(string, newNums, currIndex+1, currNum, cache, False)
        if currNum < len(nums) and newNums[currNum] > 0:
            newNums[currNum] -= 1
            cache[ID] += stringRecurse(string, newNums, currIndex+1, currNum, cache, True)
        return cache[ID]

def enumerate(string, nums, cache):
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return stringRecurse(string, nums, 0, 0, cache, False)

def partBoth():
    res = [0, 0]
    cache = {}
    for i in open("in.txt", "r"):
        string, nums = i.strip("\n").split(" ")
        nums = nums.split(",")
        res[0] += enumerate(string, nums, cache)
        newString = string
        for j in range(4):
            newString += "?" + string
        res[1] += enumerate(newString, nums * 5, cache)
    return res

print(partBoth())