def recurse(rulesList, rulesDict, curr, indices):
    if curr == "A":
        options = 1
        for i in indices:
            options *= (indices[i][1] - indices[i][0]) + 1
        return options
    elif curr == "R":
        return 0
    options = 0
    for i in rulesList[rulesDict[curr]]:
        if i[1] == "<":
            res = i.split("<")
            num = int(res[1])
            split = {}
            for j in indices:
                split[j] = indices[j].copy()
            if indices[res[0]][0] < num:
                split[res[0]][1] = num - 1
                indices[res[0]][0] = num
                options += recurse(rulesList, rulesDict, rulesList[rulesDict[curr]][i], split)
        elif i[1] == ">":
            res = i.split(">")
            num = int(res[1])
            split = {}
            for j in indices:
                split[j] = indices[j].copy()
            if indices[res[0]][1] > num:
                split[res[0]][0] = num+1
                indices[res[0]][1] = num
                options += recurse(rulesList, rulesDict, rulesList[rulesDict[curr]][i], split)
        else:
            options += recurse(rulesList, rulesDict, rulesList[rulesDict[curr]][i], indices)
    return options

def partBoth():
    skip = True
    rules = {}
    rulesList = []
    total = 0
    for i in open("in.txt"):
        if i == "\n":
            skip = False
        elif skip:
            res = i.strip("}\n").split("{")
            rulesList.append({})
            rules[res[0]] = len(rulesList)-1
            for j in res[1].split(","):
                res2 = j.split(":")
                if len(res2) == 2:
                    rulesList[len(rulesList)-1][j.split(":")[0]] = j.split(":")[1]
                else:
                    rulesList[len(rulesList)-1]["else"] = res2[0]
        else:
            res = i.strip("{}\n").split(",")
            elfDict = {}
            for j in res:
                res2 = j.split("=")
                elfDict[res2[0]] = int(res2[1])
            curr = "in"
            while curr != "A" and curr != "R":
                for j in rulesList[rules[curr]]:
                    if j[1] == ">":
                        res3 = j.split(">")
                        if int(res3[1]) < elfDict[res3[0]]:
                            curr = rulesList[rules[curr]][j]
                            break
                    elif j[1] == "<":
                        res3 = j.split("<")
                        if int(res3[1]) > elfDict[res3[0]]:
                            curr = rulesList[rules[curr]][j]
                            break
                    else:
                        curr = rulesList[rules[curr]][j]
            if curr == "A":
                for j in elfDict:
                    total += elfDict[j]
    return total, recurse(rulesList, rules, "in", {"x":[1, 4000], "m":[1, 4000], "a":[1, 4000], "s":[1, 4000]})

print(partBoth())