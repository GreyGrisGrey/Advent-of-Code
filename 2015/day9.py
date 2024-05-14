#The only difference in the two parts is if we're looking for max or min
#It's a bit slow, but it is an NP-Complete problem so that's to be expected

def maxRecurse(townDict, pathList, distance, path):
    if len(path) == 8:
        return distance
    possibleSolutions = []
    for i in townDict:
        if townDict[i] == True:
            nextTown = townDict.copy()
            nextTown[i] = False
            if len(path) == 0:
                possibleSolutions.append(maxRecurse(nextTown, pathList, 0, [i]))
            else:
                newPath = path.copy()
                newPath.append(i)
                for j in pathList:
                    if (j.split()[0] == i and j.split()[2] == path[len(path)-1]) or (j.split()[2] == i and j.split()[0] == path[len(path)-1]):
                        nextDistance = distance + int(j.split()[4])
                possibleSolutions.append(maxRecurse(nextTown, pathList, nextDistance, newPath))
    return max(possibleSolutions)

def minRecurse(townDict, pathList, distance, path):
    if len(path) == 8:
        return distance
    possibleSolutions = []
    for i in townDict:
        if townDict[i] == True:
            nextTown = townDict.copy()
            nextTown[i] = False
            if len(path) == 0:
                possibleSolutions.append(minRecurse(nextTown, pathList, 0, [i]))
            else:
                newPath = path.copy()
                newPath.append(i)
                for j in pathList:
                    if (j.split()[0] == i and j.split()[2] == path[len(path)-1]) or (j.split()[2] == i and j.split()[0] == path[len(path)-1]):
                        nextDistance = distance + int(j.split()[4])
                possibleSolutions.append(minRecurse(nextTown, pathList, nextDistance, newPath))
    return min(possibleSolutions)


f = open("input.txt")
towns = {}
paths = []
for i in f:
    name = i.split()[0]
    paths.append(i)
    if name not in towns:
        towns[i.split()[0]] = True
towns["Arbre"] = True
print(minRecurse(towns, paths, 0, []))
print(maxRecurse(towns, paths, 0, []))