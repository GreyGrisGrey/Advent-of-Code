def part1():
    mappings = []
    seeds = None
    newMapping = []
    for i in open("in.txt", "r"):
        if seeds == None:
            seeds = i[7::].strip("\n").split(" ")
        elif i[0] == "s" or i[0] == "f" or i[0] == "h" or i[0] == "t" or i[0] == "l" or i[0] == "w":
            newMapping = []
        elif i[0] != "\n":
            i = i.split(" ")
            newMapping.append([int(i[0]), int(i[1]), int(i[2])])
        elif i[0] == "\n" and len(newMapping) != 0:
            mappings.append(newMapping)
    mappings.append(newMapping)
    newSeeds = []
    for i in seeds:
        newSeed = int(i)
        for j in mappings:
            for k in j:
                if newSeed >= k[1] and newSeed <= k[1] + k[2]:
                    newSeed = k[0] + (newSeed - k[1])
                    break
        newSeeds.append(newSeed)
    return min(newSeeds)

print(part1())