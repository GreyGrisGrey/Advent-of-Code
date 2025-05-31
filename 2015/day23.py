def part1():
    instructs = []
    for i in open("in.txt"):
        instructs.append(i.strip("\n").split(" "))
    curr = 0
    vals = [1, 0]
    steps = 0
    while curr >= 0 and curr < len(instructs):
        steps += 1
        if instructs[curr][1][0] in "ab":
            valIndex = 0 if instructs[curr][1][0] == "a" else 1
        match instructs[curr][0]:
            case "hlf":
                vals[valIndex] /= 2
                vals[valIndex] = int(vals[valIndex])
                curr += 1
            case "tpl":
                vals[valIndex] *= 3
                curr += 1
            case "inc":
                vals[valIndex] += 1
                curr += 1
            case "jmp":
                curr += int(instructs[curr][1])
            case "jie":
                if vals[valIndex] % 2 == 0:
                    curr += int(instructs[curr][2])
                else:
                    curr += 1
            case "jio":
                if vals[valIndex] == 1:
                    curr += int(instructs[curr][2])
                else:
                    curr += 1
        print(curr, vals)
    return vals

print(part1())