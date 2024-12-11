def part1():
    f = open("input.txt", "r")
    array = []
    for i in f:
        array.append(int(i.strip()))
    for i in array:
        for j in array:
            if i != j and i + j == 2020:
                return i * j

def part2():
    f = open("input.txt", "r")
    array = []
    for i in f:
        array.append(int(i.strip()))
    array.sort()
    for i in array:
        for j in array:
            if j == i:
                pass
            else:
                temp = i + j
                for k in array:
                    if temp + k > 2020:
                        break
                    if j != k and i != k and temp + k == 2020:
                        return i * k * j

print(part1())
print(part2())