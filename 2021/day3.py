def part1():
    nums = []
    for i in open("in.txt").read().split("\n"):
        while len(nums) < len(i):
            nums.append(0)
        for j in range(len(i)):
            nums[j] += 1 if i[j] == "1" else -1
    epsilon = 0
    gamma = 0
    mult = 2**(len(nums) - 1)
    for i in nums:
        if i < 0:
            gamma += mult
        else:
            epsilon += mult
        mult = int(mult/2)
    return gamma * epsilon

def part2():
    dataO2 = []
    dataCO2 = []
    for i in open("in.txt").read().split("\n"):
        dataO2.append(i)
        dataCO2.append(i)
    curr = 0
    while curr < len(dataO2[0]):
        newNums = [0, 0]
        newDataO2 = []
        newDataCO2 = []
        for i in dataO2:
            newNums[0] += 1 if i[curr] == "1" else -1
        for i in dataCO2:
            newNums[1] += 1 if i[curr] == "1" else -1
        for i in dataO2:
            if (newNums[0] >= 0 and i[curr] == "1") or (newNums[0] < 0 and i[curr] == "0") or len(dataO2) == 1:
                newDataO2.append(i)
        for i in dataCO2:
            if (newNums[1] < 0 and i[curr] == "1") or (newNums[1] >= 0 and i[curr] == "0") or len(dataCO2) == 1:
                newDataCO2.append(i)
        curr += 1
        dataO2 = newDataO2
        dataCO2 = newDataCO2
    return int(dataO2[0], base=2) * int(dataCO2[0], base=2)

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())