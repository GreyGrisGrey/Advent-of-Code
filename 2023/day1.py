def isInt(string):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    if string in nums:
        return True
    else:
        return False
    


def part1():
    total = 0
    for i in open("in.txt", "r"):
        first = None
        last = None
        for j in i:
            if isInt(j):
                if first == None:
                    first = j
                last = j
        total += int(first + last)
    return total

def part2():
    total = 0
    numDict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for i in open("in.txt", "r"):
        first = None
        last = None
        for j in range(len(i)):
            for k in range(5):
                if k + j >= len(i):
                    break
                if k == 0 and isInt(i[j]):
                    if first == None:
                        first = i[j]
                    last = i[j]
                elif k != 0 and isInt(i[j:j+k+1:]):
                    if first == None:
                        first = numDict[i[j:j+k+1:]]
                    last = numDict[i[j:j+k+1:]]
        total += int(first + last)
    return total

print(part1())
print(part2())