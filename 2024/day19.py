def partBoth():
    options = None
    goals = []
    end = 0
    total = 0
    for i in open("input.txt"):
        if options == None:
            options = i.split(", ")
            options[len(options)-1] = options[len(options)-1].strip()
        elif i != "\n":
            goals.append(i.strip())
    for i in goals:
        res = count(i, options, "", {})
        if res != 0:
            total += 1
            end += res
    print("Part 1:", total, " Part 2:", end)

def count(goal, options, curr, memoDict):
    if curr in memoDict: return memoDict[curr]
    elif curr == goal: return 1
    elif len(curr) >= len(goal): return 0
    for i in range(len(curr)):
        if curr[i] != goal[i]:
            memoDict[curr] = 0
            return 0
    total = 0
    for i in options:
        total += count(goal, options, curr + i, memoDict)
    memoDict[curr] = total
    return total

partBoth()