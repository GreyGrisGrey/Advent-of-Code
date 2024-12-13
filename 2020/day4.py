def part1():
    f = open("input.txt", "r")
    entries = {}
    required = ["hgt", "byr", "iyr", "eyr", "hcl", "ecl", "pid"]
    total = 0
    valid = 1
    for i in f:
        if i != "\n":
            tempEntries = i.split(" ")
            for j in tempEntries:
                tempEntry = j.split(":")
                entries[tempEntry[0]] = True
        else:
            for j in required:
                if j not in entries:
                    valid = 0
            total += valid
            entries = {}
            valid = 1
    for j in required:
        if j not in entries:
            valid = 0
    total += valid
    return total

def part2():
    f = open("input.txt", "r")
    entries = {}
    required = ["hgt", "byr", "iyr", "eyr", "hcl", "ecl", "pid"]
    total = 0
    eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    hclValid = "abcdef1234567890"
    for i in f:
        if i != "\n":
            tempEntries = i.split(" ")
            for j in tempEntries:
                tempEntry = j.split(":")
                entries[tempEntry[0]] = tempEntry[1].strip()
        else:
            total += checkValid(entries, eyes, required, hclValid)
            entries = {}
    total += checkValid(entries, eyes, required, hclValid)
    return total

def checkValid(entries, eyes, required, hclValid):
    valid = 1
    for j in required:
        if (j not in entries) or valid == 0:
            return 0
        else:
            print(j)
            match j:
                case "hcl":
                    try:
                        if len(entries[j]) == 7 and entries[j][0] == "#":
                            for k in range(6):
                                if entries[j][k+1] not in hclValid:
                                    return 0
                        else:
                            return 0
                    except:
                        return 0
                case "ecl":
                    if entries[j] not in eyes:
                            return 0
                case "hgt":
                    try:
                        if len(entries[j]) != 4 and len(entries[j]) != 5:
                            return 0
                        if len(entries[j]) == 4 and (entries[j][2:4:] == "cm" or 59 > int(entries[j][0:2:]) or 76 < int(entries[j][0:2:])):
                            return 0
                        elif len(entries[j]) == 5 and (entries[j][3:5:] == "in" or 150 > int(entries[j][0:3:]) or 193 < int(entries[j][0:3:])):
                            return 0
                    except:
                        return 0
                case "pid":
                    try:
                        if len(entries[j]) == 9:
                            test = int(entries[j])
                            print(test)
                        else:
                            return 0
                    except:
                        return 0
                case "iyr":
                    try:
                        if (2010 > int(entries[j])) or (int(entries[j]) > 2020):
                            return 0
                    except:
                        return 0
                case "byr":
                    try:
                        if (1920 > int(entries[j])) or (int(entries[j]) > 2002):
                            return 0
                    except:
                        return 0
                case "eyr":
                    try:
                        if (2020 > int(entries[j])) or (int(entries[j]) > 2030):
                            return 0
                    except:
                        return 0
    if valid == 1:
        print(entries)
    return valid

print(part1())
print(part2())