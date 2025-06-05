def checkStep(val):
    manageEffects(val)
    if val[0] < 53 or val[1] <= 0:
        return None
    if val[3] <= 0:
        return [True, val[2], val]
    poss = [[val[0]-53, val[1], val[2]+53, val[3]-4, val[4], val[5].copy()]]
    if val[0] > 72:
        poss.append([val[0]-73, min(val[1]+2, 50), val[2]+73, val[3]-2, val[4], val[5].copy()])
    if val[0] > 112 and "S" not in val[5]:
        res = [val[0]-113, val[1], val[2]+113, val[3], val[4], val[5].copy()]
        res[5]["S"] = 6
        poss.append(res)
    if val[0] > 172 and "P" not in val[5]:
        res = [val[0]-173, val[1], val[2]+173, val[3], val[4], val[5].copy()]
        res[5]["P"] = 6
        poss.append(res)
    if val[0] > 228 and "R" not in val[5]:
        res = [val[0]-229, val[1], val[2]+229, val[3], val[4], val[5].copy()]
        res[5]["R"] = 5
        poss.append(res)
    for i in poss:
        bossTurn(i)
    return poss

def bossTurn(val):
    manageEffects(val)
    if val[3] <= 0:
        return
    val[1] -= max(val[4] - (7 if "S" in val[5] else 0), 1)

def manageEffects(val):
    dels = []
    for i in val[5]:
        if i == "P": val[3] -= 3
        elif i == "R": val[0] += 101
        val[5][i] -= 1
        if val[5][i] == 0: dels.append(i)
    for i in dels:
        del val[5][i]

def iteratePos(positions, step, minimum, hard):
    newPos = []
    for i in positions:
            if i[2] == step:
                if hard:
                    i[1] -= 1
                res = checkStep(i)
                if res != None and res[0] == True:
                    if res[1] < minimum:
                        minimum = res[1]
                elif res != None:
                    for j in res:
                        newPos.append(j)
            else:
                newPos.append(i)
    return newPos, minimum

def partBoth(fileName):
    file = open(fileName)
    positions1 = [[500, 50, 0, int(file.readline().strip("\n").split(" ")[2]), int(file.readline().split(" ")[1]), {}]]
    file = open(fileName)
    positions2 = [[500, 50, 0, int(file.readline().strip("\n").split(" ")[2]), int(file.readline().split(" ")[1]), {}]]
    step = 0
    minimums = [99999, 99999]
    while step < minimums[0] or step < minimums[1]:
        if step < minimums[0]: positions1, minimums[0] = iteratePos(positions1, step, minimums[0], False)
        if step < minimums[1]: positions2, minimums[1] = iteratePos(positions2, step, minimums[1], True)
        step += 1
    return minimums

print(partBoth("in.txt"))