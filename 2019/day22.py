from math import floor

def forwardStep(data, index, deckSize):
    if data[index[1]] == "deal into new stack":
        index[0] = abs((deckSize - 1) - index[0])
    else:
        line = data[index[1]].split(" ")
        if line[0] == "deal":
            index[0] = (index[0] * int(line[3])) % deckSize
        else:
            index[0] = (index[0] - int(line[1])) % deckSize

def deckStep(data, index, deckPosition, deckSize):
    if data[index[1]] == "deal into new stack":
        deckPosition[0] = (deckPosition[0] - deckPosition[1]) % deckSize
        deckPosition[1] = (deckPosition[1] * -1) % deckSize
    else:
        line = data[index[1]].split(" ")
        if line[0] == "deal":
            deckPosition[1] *= euclidAlgorithm(deckSize, int(line[3]))
            deckPosition[1] = deckPosition[1] % deckSize
        else:
            deckPosition[0] = (deckPosition[0] + int(line[1]) * deckPosition[1]) % deckSize
                
def part1(fileName = "in.txt"):
    deckSize = 10007
    data = open(fileName).read().split("\n")
    index = [2019, 0]
    cache = {}
    cache["2019:0"] = True
    flag = True
    while index[1] < len(data):
        if not flag and str(index[0]) + ":" + str(index[1]) in cache:
            return
        if flag:
            flag = False
        forwardStep(data, index, deckSize)
        index[1] += 1
    return index[0]

def euclidAlgorithm(num1, num2):
    indices = [[1, 0], [0, 1]]
    nums = [num1, num2]
    prev = num1
    curr = num2
    count = 0
    flag = True
    while curr != 0:
        change = [indices[count][0] + floor(prev/curr) * indices[count + 1][0] * -1, indices[count][1] + floor(prev/curr) * indices[count + 1][1] * -1]
        indices.append(change)
        nextNum = prev % curr
        nums.append(nextNum)
        prev = curr
        curr = nextNum
        flag = not flag
        count += 1
    return indices[count][1]

def exponentialModulo(num, exponent, additionalNum):
    total = 1
    for i in range(len(str(exponent))):
        digit = int(str(exponent)[len(str(exponent)) - (1 + i)])
        total = (total * (num**digit)) % additionalNum
        num = (num**10) % additionalNum
    return int(total)

def part2(fileName = "in.txt"):
    deckSize = 119315717514047
    shuffleCount = 101741582076661
    data = open(fileName).read().split("\n")
    deckPosition = [0, 1]
    for i in range(len(data)):
        deckStep(data, [0, i], deckPosition, deckSize)
    deckPosition[0] = (deckPosition[0] * (1 - (exponentialModulo(deckPosition[1], shuffleCount, deckSize))) * pow((1 - deckPosition[1]) % deckSize, deckSize - 2, deckSize)) % deckSize
    deckPosition[1] = exponentialModulo(deckPosition[1], shuffleCount, deckSize)
    return (deckPosition[0] + (deckPosition[1] * 2020)) % deckSize

if __name__ == "__main__":
    print("Part 1:", part1("in22.txt"))
    print("Part 2:", part2("in22.txt"))