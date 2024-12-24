from math import floor
from queue import Queue

def part1():
    total = 0
    for i in open("input.txt"):
        secretNum = int(i.strip())
        curr1 = secretNum%10
        for j in range(2000):
            nextNum = secretNum*64
            secretNum = (nextNum^secretNum)%16777216
            nextNum = floor(secretNum/32)
            secretNum = (nextNum^secretNum)%16777216
            nextNum = secretNum*2048
            secretNum = (nextNum^secretNum)%16777216
        total += secretNum
    print(total)
    return

def part2():
    total = 0
    sequenceDict = {}
    starts = []
    count = 0
    for i in open("input.txt"):
        secretNum = int(i.strip())
        startNum = secretNum
        starts.append(str(startNum))
        curr1 = secretNum%10
        seqIndex = 0
        changeList = []
        count += 1
        for j in range(2000):
            nextNum = secretNum*64
            secretNum = (nextNum^secretNum)%16777216
            nextNum = floor(secretNum/32)
            secretNum = (nextNum^secretNum)%16777216
            nextNum = secretNum*2048
            secretNum = (nextNum^secretNum)%16777216
            if len(changeList) == 4:
                changeList[0] = changeList[1]
                changeList[1] = changeList[2]
                changeList[2] = changeList[3]
                changeList[3] = secretNum%10 - curr1
                res = str(startNum) + ";" + ":".join(str(x) for x in changeList)
                if res not in sequenceDict:
                    sequenceDict[res] = secretNum%10
            else:
                changeList.append(secretNum%10 - curr1)
                if len(changeList)== 4:
                    res = str(startNum) + ";" + ":".join(str(x) for x in changeList)
                    sequenceDict[res] = secretNum%10
            curr1 = secretNum%10
    maximum = 0
    # takes a second
    for i in range(19):
        for j in range(19):
            for k in range(19):
                for l in range(19):
                    sequence = str(i-9) + ":" + str(j-9) + ":" + str(k-9) + ":" + str(l-9)
                    total = 0
                    for m in starts:
                        if (m + ";" + sequence) in sequenceDict:
                            total += sequenceDict[m + ";" + sequence]
                    if total >= maximum:
                        maximum = total
    return

part2()