def determineHand(hand):
    cardDict = {}
    for i in hand:
        if i in cardDict:
            cardDict[i] += 1
        else:
            cardDict[i] = 1
    maximum = 0
    for i in cardDict:
        if (maximum == 2 and cardDict[i] == 3) or (cardDict[i] == 2 and maximum == 3):
            return 2
        elif maximum == 2 and cardDict[i] == 2:
            return 4
        elif maximum < cardDict[i]:
            maximum = cardDict[i]
    if maximum == 3:
        return 3
    elif maximum == 2:
        return 5
    elif maximum == 1:
        return 6
    return abs(maximum - 5)

def restructureHand(hand, flag):
    newHand = ""
    handDict = {"A":"A", "K":"B", "Q":"C", "J":"D", "T":"E"}
    for i in hand:
        if i in handDict:
            if flag and i == "J":
                newHand += chr(122)
            else:
                newHand += handDict[i]
        else:
            newHand += chr(abs(ord(i)-60)+75)
    return newHand

def part1():
    total = 0
    hands = [[], [], [], [], [], [], []]
    count = 0
    for i in open("in.txt", "r"):
        i = i.strip().split(" ")
        hands[determineHand(i[0])].append([restructureHand(i[0], False), i[1]])
        count += 1
    for i in range(len(hands)):
        hands[i] = sorted(hands[i])
        for j in hands[i]:
            total += count * int(j[1])
            count -= 1
    return total

def determineHandWild(hand):
    cardDict = {}
    for i in hand:
        if i in cardDict:
            cardDict[i] += 1
        else:
            cardDict[i] = 1
    wilds = cardDict["J"]
    maximum = 0
    pair = False
    twoPair = False
    for i in cardDict:
        if i != "J":
            if cardDict[i] == 4:
                maximum = 4
                break
            if cardDict[i] == 3:
                maximum = 3
                break
            elif cardDict[i] == 2:
                maximum = 2
                if not pair:
                    pair = True
                else:
                    twoPair = True
            elif cardDict[i] == 1 and maximum == 0:
                maximum = 1
    maximum += wilds
    if maximum == 5:
        return 0
    if maximum == 4:
        return 1
    if maximum == 3 and twoPair:
        return 2
    if maximum == 3:
        return 3
    if maximum == 2:
        return 5
    if maximum == 1:
        return 6

def part2():
    total = 0
    hands = [[], [], [], [], [], [], []]
    count = 0
    for i in open("in.txt", "r"):
        i = i.strip().split(" ")
        if "J" in i[0]:
            hands[determineHandWild(i[0])].append([restructureHand(i[0], True), i[0], i[1]])
        else:
            hands[determineHand(i[0])].append([restructureHand(i[0], True), i[0], i[1]])
        count += 1
    for i in range(len(hands)):
        hands[i] = sorted(hands[i])
        for j in hands[i]:
            total += count * int(j[2])
            count -= 1
    return total

print(part1())
print(part2())