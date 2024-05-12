def part1():
    f = open("input.txt")
    banlist = ["ab", "cd", "pq", "xy"]
    vowellist = ["a", "e", "i", "o", "u"]
    nice = 0
    for i in f:
        vowels = 0
        doubles = False
        banned = False
        if i[0] in vowellist: vowels += 1;
        for j in range(len(i)-1):
            if i[j+1] in vowellist: vowels += 1
            if i[j] == i[j+1]: doubles = True
            if (i[j] + i[j+1]) in banlist:
                banned = True
                break
        if (not banned) and doubles and vowels >= 3: nice += 1
    print("Part 1 : ", nice)

def part2():
    f = open("input.txt")
    nice = 0
    for i in f:
        split = False
        doubles = False
        doubleList = []
        for j in range(len(i)-1):
            if j < len(i)-2 and i[j] == i[j+2]: split = True
            doubleList.append(i[j] + i[j+1])
        for j in range(len(doubleList)):
            for k in range(len(doubleList)):
                if (k > j+1 or k < j-1) and doubleList[j] == doubleList[k]: doubles = True
        if doubles and split: nice += 1
    print("Part 2 : ", nice)

part1()
part2()