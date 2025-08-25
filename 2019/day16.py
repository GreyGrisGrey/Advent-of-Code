def calcDigit(inputString, repeater, i):
        currIndex = 0
        remaining = i
        res = 0
        count = 0
        while count < len(inputString):
            if currIndex == 0:
                count += i
                remaining = i + 1
                currIndex = 1
                if count >= len(inputString):
                    break
            else:
                res += int(inputString[count]) * repeater[currIndex]
                remaining -= 1
                count += 1
                if remaining <= 0:
                    count += i + 1
                    remaining = i + 1
                    currIndex = (currIndex + 2) % 4
        return abs(res) % 10


def runPhase(inputString, repeater, outList):
    for i in range(len(inputString)):
        outList.append(str(calcDigit(inputString, repeater, i)))
    return "".join(outList)
            

def part1(fileName = "in.txt"):
    repeater = [0, 1, 0, -1]
    inputString = open(fileName).read()
    outList = []
    for i in range(100):
        inputString = runPhase(inputString, repeater, outList)
        outList = []
    return inputString[0:8:]

# works if offset > input length/2 and in no other context.
# also quite slow.
def part2(fileName = "in.txt"):
    inputString = open(fileName).read()
    offset = int(inputString[0:7:])
    inputString *= 10000
    for i in range(100):
        nextLevel = []
        if i == 0:
            total = 0
            for j in range(len(inputString) - offset):
                total += int(inputString[len(inputString) - 1 - j])
                nextLevel.append(str(abs(total) % 10))
        else:
            total = 0
            for j in range(len(inputString)):
                total += int(inputString[len(inputString) - 1 - j])
                nextLevel.append(str(abs(total) % 10))
        nextLevel.reverse()
        inputString = nextLevel
    return "".join(inputString[0:8:])


if __name__ == "__main__":
    print("Part 1:", part1("in16.txt"))
    print("Part 2:", part2("in16.txt"))