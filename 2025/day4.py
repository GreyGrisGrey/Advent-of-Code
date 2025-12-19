def countAdj(mapping, curr):
    adjCount = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if curr + j + i * 1000 in mapping and mapping[curr + j + i * 1000] == "@":
                adjCount += 1
    return adjCount
                

def part1():
    data = open("in.txt").read().split("\n")
    mapping = {}
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            mapping[i * 1000 + j] = data[i][j]
    for i in mapping:
        if mapping[i] == "@" and countAdj(mapping, i) <= 4:
            total += 1
    return total

def part2():
    data = open("in.txt").read().split("\n")
    mapping = {}
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            mapping[i * 1000 + j] = data[i][j]
    removed = True
    while removed:
        removed = False
        newMapping = mapping.copy()
        for i in mapping:
            if mapping[i] == "@" and countAdj(mapping, i) <= 4:
                total += 1
                removed = True
                newMapping[i] = "."
        mapping = newMapping
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())