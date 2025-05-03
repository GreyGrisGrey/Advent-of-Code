def part1(red, blue, green):
    total = 0
    colDict = {"red":red, "blue":blue, "green":green}
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    count = 1
    for i in open("in.txt", "r"):
        num = ""
        col = ""
        flag = False
        skip = True
        poss = True
        for j in range(len(i)):
            if skip and i[j] == ":":
                skip = False
            elif (not skip) and i[j] in nums:
                num += i[j]
            elif num != "" and i[j] == " ":
                num = int(num)
                flag = True
            elif flag and i[j] != ";" and i[j] != "\n" and i[j] != ",":
                col += i[j]
            elif flag:
                if num > colDict[col]:
                    poss = False
                num = ""
                col = ""
                flag = False
        if poss:
            total += count
        count += 1
    return total

def part2():
    total = 0
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in open("in.txt", "r"):
        colDict = {"green":0, "red":0, "blue":0}
        num = ""
        col = ""
        flag = False
        skip = True
        for j in range(len(i)):
            if skip and i[j] == ":":
                skip = False
            elif (not skip) and i[j] in nums:
                num += i[j]
            elif num != "" and i[j] == " ":
                num = int(num)
                flag = True
            elif flag and i[j] != ";" and i[j] != "\n" and i[j] != ",":
                col += i[j]
            elif flag:
                if num > colDict[col]:
                    colDict[col] = num
                num = ""
                col = ""
                flag = False
        total += colDict["red"] * colDict["green"] * colDict["blue"]
    return total

print(part1(12, 14, 13))
print(part2())