def part1():
    f = open("input.txt")
    dataMap = {"children:": 3, "cats:": 7, "samoyeds:": 2, "pomeranians:": 3, "akitas:": 0, "vizslas:": 0, "goldfish:": 5, "trees:": 3, "cars:": 2, "perfumes:": 1}
    for i in f:
        line = i.split()
        if dataMap[line[2]] == int(line[3][0:len(line[3])-1:]) and dataMap[line[4]] == int(line[5][0:len(line[5])-1:]) and dataMap[line[6]] == int(line[7][0:len(line[7]):]):
            print(i)

def part2():
    f = open("input.txt")
    dataMap = {"children:": 3, "cats:": 7, "samoyeds:": 2, "pomeranians:": 3, "akitas:": 0, "vizslas:": 0, "goldfish:": 5, "trees:": 3, "cars:": 2, "perfumes:": 1}
    for i in f:
        line = i.split()
        checker = True
        checks = [[line[2], int(line[3][0:len(line[3])-1:])], [line[4], int(line[5][0:len(line[5])-1:])], [line[6], int(line[7][0:len(line[7]):])]]
        for j in checks:
            if (j[0] == "cats:" or j[0] == "trees:"):
                if not (dataMap[j[0]] < j[1]):
                    checker = False
            elif(j[0] == "pomeranians:" or j[0] == "goldfish:"): 
                if not (dataMap[j[0]] > j[1]):
                    checker = False
            else:
                if not (dataMap[j[0]] == j[1]):
                    checker = False
        if checker == True:
            print(i)

part1()
part2()