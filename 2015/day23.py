def checkRes(vals, instructs):
    curr = 0
    while curr >= 0 and curr < len(instructs):
        if instructs[curr][1][0] in "ab":
            valIndex = 0 if instructs[curr][1][0] == "a" else 1
        match instructs[curr][0]:
            case "hlf":
                vals[valIndex] = int(vals[valIndex]/2)
            case "tpl":
                vals[valIndex] *= 3
            case "inc":
                vals[valIndex] += 1
            case "jmp":
                curr += int(instructs[curr][1]) - 1
            case "jie":
                if vals[valIndex] % 2 == 0:
                    curr += int(instructs[curr][2]) - 1
            case "jio":
                if vals[valIndex] == 1:
                    curr += int(instructs[curr][2]) - 1
        curr += 1
    return vals[1]

def partBoth():
    instructs = list(map(lambda x: x.split(" "), open("in.txt").read().split("\n")))
    return checkRes([0, 0], instructs), checkRes([1, 0], instructs)

print(partBoth())