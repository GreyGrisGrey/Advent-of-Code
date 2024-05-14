def part1():
    f = open("input.txt")
    finalStringLen = 0
    finalMemLen = 0
    normals = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in f:
        if i[len(i)-1] == "\n":
            i = i[:len(i)-1:]
        count = 1
        stringLen = 2
        memLen = 0
        slash = False
        while count < len(i)-1:
            if slash:
                if i[count] == "\\" or i[count] == "\"":
                    stringLen += 1
                    count += 1
                else:
                    stringLen += 3
                    count += 3
                slash = False
            else:
                if i[count] in normals:
                    stringLen += 1
                    memLen += 1
                    count += 1
                elif i[count] == "\\":
                    stringLen += 1
                    memLen += 1
                    count += 1
                    slash = True
        finalStringLen += stringLen
        finalMemLen += memLen
    print(finalStringLen - finalMemLen)
    return finalStringLen

def part2():
    f = open("input.txt")
    finalStringLen = 0
    normals = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in f:
        if i[len(i)-1] == "\n":
            i = i[:len(i)-1:]
        count = 1
        stringLen = 6
        while count < len(i)-1:
            if i[count] in normals:
                stringLen += 1
            elif i[count] == "\\" or i[count] == "\"":
                stringLen += 2
            count += 1
        finalStringLen += stringLen
    print(finalStringLen - part1())

part1()
part2()