def tree1(sizes, maxSize, curr, currSize):
    if currSize > maxSize:
        return 0
    if curr >= len(sizes):
        if currSize < maxSize:
            return 0
        return 1
    val = 0
    val += tree1(sizes, maxSize, curr+1, currSize)
    val += tree1(sizes, maxSize, curr+1, currSize+sizes[curr])
    return val

def tree2(sizes, maxSize, curr, currSize, currSet, minSet):
    if currSize > maxSize:
        return [0]
    elif currSet > minSet:
        return [0]
    if curr >= len(sizes):
        if currSize < maxSize:
            return [0]
        return [1, currSet]
    val = 0
    res = tree2(sizes, maxSize, curr+1, currSize, currSet, minSet)
    if len(res) == 2:
        if minSet >= res[1]:
            minSet = res[1]
            val = res[0]
    res = tree2(sizes, maxSize, curr+1, currSize+sizes[curr], currSet+1, minSet)
    if len(res) == 2:
        if minSet > res[1]:
            minSet = res[1]
            val = res[0]
        elif minSet == res[1]:
            val += res[0]
    return [val, minSet]

def part1():
    f = open("input.txt")
    containers = []
    for i in f:
        containers.append(int(i))
    print(tree1(containers, 150, 0, 0))

def part2():
    f = open("input.txt")
    containers = []
    for i in f:
        containers.append(int(i))
    print(tree2(containers, 150, 0, 0, 0, 999)[0])

part1()
part2()