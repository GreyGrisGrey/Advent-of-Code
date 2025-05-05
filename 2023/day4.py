def part1():
    total = 0
    for i in open("in.txt"):
        newCard = i.split(":")[1].split("|")
        left = newCard[0].strip().split(" ")
        right = newCard[1].strip().split(" ")
        newList = []
        for j in left:
            if j != "":
                newList.append(j)
        count = 0
        for j in right:
            if j in newList:
                count = 1 if count == 0 else count * 2
        total += count
    return total

def part2():
    total = 0
    cardDict = {}
    for i in range(199):
        cardDict[i+1] = 1
    curr = 1
    for i in open("in.txt"):
        newCard = i.split(":")[1].split("|")
        left = newCard[0].strip().split(" ")
        right = newCard[1].strip().split(" ")
        newList = []
        for j in left:
            if j != "":
                newList.append(j)
        count = 0
        for j in right:
            if j in newList:
                cardDict[curr + 1 + count] += cardDict[curr]
                count += 1
        curr += 1
    for i in cardDict:
        total += cardDict[i]
    return total

print(part1())
print(part2())