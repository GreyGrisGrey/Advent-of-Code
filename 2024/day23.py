def part1():
    binaryRelation = {}
    Ts = {}
    totals = {}
    for i in open("input.txt"):
        comps = i.split("-")
        comps[1] = comps[1].strip()
        binaryRelation[comps[0] + "-" + comps[1]] = True
        binaryRelation[comps[1] + "-" + comps[0]] = True
        if comps[0][0] == "t":
            Ts[comps[0]] = True
        elif comps[1][0] == "t":
            Ts[comps[1]] = True
        totals[comps[0]] = True
        totals[comps[1]] = True
    count = 0
    for i in binaryRelation:
        pair = i.split("-")
        for j in totals:
            if j != pair[0] and j != pair[1] and j + "-" + pair[0] in binaryRelation and j + "-" + pair[1] in binaryRelation and (j in Ts or pair[0] in Ts or pair[1] in Ts):
                count += 1
    print(int(count/6))

def part2():
    binaryRelation = {}
    Ts = {}
    totals = {}
    for i in open("input.txt"):
        comps = i.split("-")
        comps[1] = comps[1].strip()
        binaryRelation[comps[0] + "-" + comps[1]] = True
        binaryRelation[comps[1] + "-" + comps[0]] = True
        if comps[0][0] == "t":
            Ts[comps[0]] = True
        elif comps[1][0] == "t":
            Ts[comps[1]] = True
        totals[comps[0]] = True
        totals[comps[1]] = True
    maxCollection = set()
    for i in binaryRelation:
        collection = set(i.split("-"))
        for j in totals:
            addable = True
            for k in collection:
                if k + "-" + j not in binaryRelation:
                    addable = False
                    break
            if addable:
                collection.add(j)
        if len(collection) > len(maxCollection):
            maxCollection = collection
    colSorted = ",".join(sorted(list(maxCollection)))
    print(colSorted)

part1()
part2()