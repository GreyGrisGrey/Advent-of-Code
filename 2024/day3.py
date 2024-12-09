def part1():
    f = open("input.txt", "r")
    strings = []
    matcher = "mul(.,.)"
    matchIndex = 0
    mult1 = ""
    mult2 = ""
    total = 0
    nums = "0123456789"
    for i in f:
        strings.append(i.strip())
        for j in i:
            if matcher[matchIndex] == j:
                matchIndex += 1
            elif (matchIndex == 6 or matchIndex == 4) and j in nums:
                if matchIndex == 4:
                    mult1 = mult1 + j
                else:
                    mult2 = mult2 + j
            elif matchIndex == 4 and j == ",":
                matchIndex += 2
            elif matchIndex == 6 and j == ")":
                matchIndex = 0
                total += int(mult1) * int(mult2)
                mult1 = ""
                mult2 = ""
            else:
                matchIndex = 0
                mult1 = ""
                mult2 = ""
    print(total)

def part2():
    f = open("input.txt", "r")
    strings = []
    matcher = "mul(.,.)"
    matchIndex = 0
    mult1 = ""
    mult2 = ""
    total = 0
    nums = "0123456789"
    doer = "do()"
    donter = "don't()"
    doIndex = 0
    dontIndex = 0
    apply = True
    for i in f:
        strings.append(i.strip())
        for j in i:
            if matcher[matchIndex] == j:
                matchIndex += 1
            elif (matchIndex == 6 or matchIndex == 4) and j in nums:
                if matchIndex == 4:
                    mult1 = mult1 + j
                else:
                    mult2 = mult2 + j
            elif matchIndex == 4 and j == ",":
                matchIndex += 2
            elif matchIndex == 6 and j == ")":
                matchIndex = 0
                if apply:
                    total += int(mult1) * int(mult2)
                mult1 = ""
                mult2 = ""
            else:
                matchIndex = 0
                mult1 = ""
                mult2 = ""
            if apply:
                if donter[dontIndex] == j:
                    dontIndex += 1
                    if j == ")":
                        dontIndex = 0
                        apply = False
                else:
                    dontIndex = 0
            else:
                if doer[doIndex] == j:
                    doIndex += 1
                    if j == ")":
                        doIndex = 0
                        apply = True
                else:
                    doIndex = 0
    print(total)

part1()
part2()