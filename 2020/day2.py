def part1():
    f = open("input.txt", "r")
    end = 0
    for i in f:
        line = i.split(" ")
        relevant = line[1][0:1:]
        minMax = line[0].split("-")
        password = line[2].strip()
        count = 0
        minMax[1] = int(minMax[1])
        for j in password:
            if j == relevant:
                count += 1
                if count == minMax[1]+1:
                    end -= 1
        if count >= int(minMax[0]):
            end += 1
    return end

def part2():
    f = open("input.txt", "r")
    end = 0
    for i in f:
        line = i.split(" ")
        relevant = line[1][0:1:]
        minMax = line[0].split("-")
        password = line[2].strip()
        count = 0
        if password[int(minMax[0])-1] == relevant:
            count += 1
        if int(minMax[1])-1 <= len(password) and password[int(minMax[1])-1] == relevant:
            count += 1
        if count == 1:
            end += 1
    return end

print(part1())
print(part2())