def part1():
    mults = [0, 0]
    for i in open("in.txt").read().split("\n"):
        counts = {}
        flags = [False, False]
        for j in i:
            counts[j] = 1 if j not in counts else counts[j] + 1
        for j in counts:
            if counts[j] == 2:
                flags[0] = True
            if counts[j] == 3:
                flags[1] = True
        if flags[0]:
            mults[0] += 1
        if flags[1]:
            mults[1] += 1
    return mults[0] * mults[1]

def part2():
    valids = open("in.txt").read().split("\n")
    for i in valids:
        for j in valids:
            if i != j:
                flag = False
                lastIndex = 0
                for k in range(len(i)):
                    if i[k] != j[k] and flag:
                        flag = False
                        break
                    elif i[k] != j[k]:
                        flag = True
                        lastIndex = k
                if flag:
                    return i[0:lastIndex:] + i[lastIndex+1::]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())