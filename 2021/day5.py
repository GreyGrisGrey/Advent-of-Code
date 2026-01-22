def incrementMapping(mapping, index):
    mapping[index] = 1 if index not in mapping else mapping[index] + 1

def part1():
    lines = open('in.txt').read().split("\n")
    mapping = {}
    total = 0
    for i in lines:
        indices = i.split(" -> ")
        first = list(map(lambda x: int(x), indices[0].split(",")))
        second = list(map(lambda x: int(x), indices[1].split(",")))
        if first[0] == second[0] or first[1] == second[1]:
            incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] < second[0]:
                first[0] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] > second[0]:
                first[0] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[1] < second[1]:
                first[1] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[1] > second[1]:
                first[1] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
    for i in mapping:
        if mapping[i] >= 2:
            total += 1
    return total

def part2():
    lines = open('in.txt').read().split("\n")
    mapping = {}
    total = 0
    for i in lines:
        indices = i.split(" -> ")
        first = list(map(lambda x: int(x), indices[0].split(",")))
        second = list(map(lambda x: int(x), indices[1].split(",")))
        incrementMapping(mapping, first[0] * 1000000 + first[1])
        if first[0] == second[0] or first[1] == second[1]:
            while first[0] < second[0]:
                first[0] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] > second[0]:
                first[0] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[1] < second[1]:
                first[1] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[1] > second[1]:
                first[1] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
        else:
            while first[0] < second[0] and first[1] < second[1]:
                first[0] += 1
                first[1] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] > second[0] and first[1] < second[1]:
                first[0] -= 1
                first[1] += 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] < second[0] and first[1] > second[1]:
                first[0] += 1
                first[1] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
            while first[0] > second[0] and first[1] > second[1]:
                first[0] -= 1
                first[1] -= 1
                incrementMapping(mapping, first[0] * 1000000 + first[1])
    for i in mapping:
        if mapping[i] >= 2:
            total += 1
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())

# 21554 low