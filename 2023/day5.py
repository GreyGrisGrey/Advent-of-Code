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

def createInterval(base, flag):
    if flag:
        return [int(base[0]), int(base[0]) + int(base[1]) - 1]
    else:
        return [[int(base[1]), int(base[2]) + int(base[1]) - 1], [int(base[0]), int(base[2]) + int(base[0]) - 1]]

def getOverlap(mapping, seed):
    diff = mapping[0][0] - mapping[1][0]
    if seed[0] >= mapping[0][0] and seed[1] <= mapping[0][1]:
        return [[seed[0] - diff, seed[1] - diff], []]
    elif seed[0] >= mapping[0][0] and seed[0] <= mapping[0][1]:
        return [[seed[0] - diff, mapping[1][1]], [[mapping[0][1]+1, seed[1]]]]
    elif seed[1] >= mapping[0][1] and seed[0] <= mapping[0][0]:
        return [[mapping[1][0], mapping[1][1]],[[seed[0], mapping[0][0]-1], [mapping[0][1]+1, seed[1]]]]
    elif seed[1] <= mapping[0][1] and seed[1] >= mapping[0][0]:
        return [[mapping[1][0], seed[1]-diff], [[seed[0], mapping[0][0]-1]]]
    return [[], [seed]]

def part2():
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
    for i in range(int(len(seeds)/2)):
        newSeeds.append([seeds[i*2], seeds[i*2+1]])
    mapInterv = []
    seedInterv = []
    for i in newSeeds:
        seedInterv.append(createInterval(i, True))
    for i in mappings:
        newMappings = []
        for j in i:
            newMappings.append(createInterval(j, False))
        mapInterv.append(newMappings)
    currSeeds = seedInterv
    for i in mapInterv:
        nextSeeds = []
        for j in i:
            newSeeds = []
            for k in currSeeds:
                res = getOverlap(j, k)
                if len(res[0]) != 0:
                    nextSeeds.append(res[0])
                if len(res[1]) != 0:
                    for l in res[1]:
                        newSeeds.append(l)
            currSeeds = newSeeds
        for j in currSeeds:
            nextSeeds.append(j)
        currSeeds = nextSeeds
    minimum = 999999999999
    for i in currSeeds:
        if i[0] < minimum:
            minimum = i[0]
    return minimum

print(part1())
print(part2())