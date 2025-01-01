from queue import Queue

def part1(maximum, file):
    count = 0
    nums = {}
    for i in open(file):
        if len(nums) < maximum or sumCheck(nums, int(i)):
            nums[count] = int(i)
            count = count + 1 if count < maximum else 0
        else:
            return int(i)


def part2(invalid, file):
    currSet = Queue()
    currTotal = 0
    for i in open(file):
        currSet.put(int(i))
        currTotal += int(i)
        while currTotal > invalid:
            currTotal -= currSet.get()
        if currTotal == invalid:
            break
    minimum = currSet.get()
    maximum = minimum
    while currSet.qsize() != 0:
        next = currSet.get()
        if next < minimum:
            minimum = next
        elif next > maximum:
            maximum = next
    print("Part 2 :", minimum + maximum)


def sumCheck(numDict, checkNum):
    for i in numDict:
        if ((checkNum - numDict[i]) in numDict.values()) and ((checkNum - numDict[i]) != numDict[i]):
            return True
    return False

invalid = part1(25, "input.txt")
print("Part 1 :", invalid)
part2(invalid, "input.txt")