from math import ceil

def part1():
    data = open("in.txt").read().split("\n")
    mapping = {}
    end = None
    begin = []
    for i in data:
        ins, outs = i.split(" => ")
        newOut = outs.split(" ")
        newIns = [int(newOut[0])]
        for j in ins.split(", "):
            newIns.append(j.split(" "))
        mapping[newOut[1]] = newIns
        if newOut[1] == "FUEL":
            end = newOut[1]
        elif newIns[1][1] == "ORE":
            begin.append(newOut[1])
    required = 0
    opens = [(end, 1)]
    excess = {}
    while len(opens) != 0:
        curr = opens[0]
        divide = 1
        if curr[0] in excess and excess[curr[0]] >= curr[1]:
            excess[curr[0]] -= curr[1]
        else:
            if curr[0] in excess and excess[curr[0]] < curr[1]:
                curr = (curr[0], curr[1] - excess[curr[0]])
                excess[curr[0]] = 0
            for j in mapping[curr[0]]:
                if type(j) == int:
                    divide = j
                elif j[1] == "ORE":
                    required += int(j[0]) * ceil(curr[1] / divide)
                else:
                    opens.append((j[1], int(j[0]) * ceil(curr[1] / divide)))
            if (curr[1] % divide) != 0:
                if curr[0] in excess:
                    excess[curr[0]] += divide - (curr[1] % divide)
                else:
                    excess[curr[0]] = divide - (curr[1] % divide)
        del opens[0]
    print("Part 1:", required)

def part2():
    data = open("in.txt").read().split("\n")
    mapping = {}
    end = None
    begin = []
    for i in data:
        ins, outs = i.split(" => ")
        newOut = outs.split(" ")
        newIns = [int(newOut[0])]
        for j in ins.split(", "):
            newIns.append(j.split(" "))
        mapping[newOut[1]] = newIns
        if newOut[1] == "FUEL":
            end = newOut[1]
        elif newIns[1][1] == "ORE":
            begin.append(newOut[1])
    excess = {}
    for i in mapping:
        excess[i] = 0
    avail = 1000000000000
    count = 0
    # Definitely feels like theres an exceptionally clever numerical solution here I'm missing.
    while True:
        if count % 10000 == 0:
            print(count)
        opens = [(end, 1)]
        while len(opens) != 0:
            curr = opens[0]
            divide = 1
            if curr[0] in excess and excess[curr[0]] >= curr[1]:
                excess[curr[0]] -= curr[1]
            else:
                if curr[0] in excess and excess[curr[0]] < curr[1]:
                    curr = (curr[0], curr[1] - excess[curr[0]])
                    excess[curr[0]] = 0
                for j in mapping[curr[0]]:
                    if type(j) == int:
                        divide = j
                    elif j[1] == "ORE":
                        avail -= int(j[0]) * ceil(curr[1] / divide)
                    else:
                        opens.append((j[1], int(j[0]) * ceil(curr[1] / divide)))
                if (curr[1] % divide) != 0:
                    if curr[0] in excess:
                        excess[curr[0]] += divide - (curr[1] % divide)
                    else:
                        excess[curr[0]] = divide - (curr[1] % divide)
            del opens[0]
        if avail <= 0:
            break
        count += 1
    print("Part 2:", count)
            
        
    

if __name__ == "__main__":
    part1()
    part2()