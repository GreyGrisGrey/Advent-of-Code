def part1():
    blocks = []
    newBlock = []
    locks = []
    keys = []
    for i in open("input.txt"):
        if i == "\n":
            blocks.append(newBlock)
            newBlock = []
        else:
            newBlock.append(i.strip())
    blocks.append(newBlock)
    for i in blocks:
        if i[0] == "#####":
            locks.append(i)
        else:
            keys.append(i)
    keyVals = []
    for i in keys:
        blockVals = [0, 0, 0, 0, 0]
        for j in range(7):
            for k in range(5):
                if i[j][k] == "#":
                    blockVals[k] += 1
        keyVals.append(blockVals)
    lockVals = []
    count = 0
    for i in locks:
        blockVals = [0, 0, 0, 0, 0]
        for j in range(7):
            for k in range(5):
                if i[j][k] == "#":
                    blockVals[k] += 1
        lockVals.append(blockVals)
    for i in lockVals:
        for j in keyVals:
            adder = True
            for k in range(5):
                if i[k] + j[k] >= 8:
                    adder = False
                    break
            if adder:
                count += 1
    print(count)

part1()