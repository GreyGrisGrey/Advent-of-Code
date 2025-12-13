from math import log, floor

def part1():
    returnVal = 0
    invalids = []
    maximum = 0
    for i in open("in.txt").read().split(","):
        invalids.append(list(map(lambda x: int(x), i.split("-"))))
        if int(i.split("-")[1]) > maximum:
            maximum = int(i.split("-")[1])
    for j in range(1, 500001):
        # floor(log(1000, 10)) is apparently 2, who knew.
        testNum = j + (j * 10**(floor(log(j, 10) + 0.000001) + 1))
        for k in invalids:
            if k[0] <= testNum and k[1] >= testNum:
                returnVal += testNum
    return returnVal

def part2():
    returnVal = 0
    invalids = []
    maximum = 0
    dones = []
    for i in open("in.txt").read().split(","):
        invalids.append(list(map(lambda x: int(x), i.split("-"))))
        if len(i.split("-")[1]) > maximum:
            maximum = len(i.split("-")[1])
    for j in range(1, 500001):
        testNum = int(str(j) + str(j))
        while len(str(testNum)) <= maximum:
            for k in invalids:
                if k[0] <= testNum and k[1] >= testNum and testNum not in dones:
                    print(k, testNum)
                    dones.append(testNum)
                    returnVal += testNum
            testNum = int(str(testNum) + str(j))
    return returnVal

if __name__ == "__main__":
    print(part1())
    print(part2())