def part1(fileName):
    total = 0
    for i in open(fileName, "r").readline().strip("\n").split(","):
        curr = 0
        for j in i:
            curr = ((curr + ord(j)) * 17) % 256
        total += curr
    return total

def part2(fileName):
    boxList = []
    total = 0
    for i in range(256):
        boxList.append({})
    for i in open(fileName, "r").readline().strip("\n").split(","):
        if "=" in i:
            split = i.split("=")
            curr = 0
            for j in split[0]: curr = ((curr + ord(j)) * 17) % 256
            boxList[curr][split[0]] = int(split[1])
        else:
            i = i.strip("-")
            curr = 0
            for j in i: curr = ((curr + ord(j)) * 17) % 256
            if i in boxList[curr]: del boxList[curr][i]
    for i in range(len(boxList)):
        count = 0
        for j in boxList[i]:
            count += 1
            total += boxList[i][j] * count * (i+1)
    return total

print(part1("in.txt"))
print(part2("in.txt"))