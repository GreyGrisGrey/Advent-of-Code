def findDanger(ingredients, allergens, allergen, grid, dangers):
    index = 0
    for i in grid[allergens[allergen]]:
        if i:
            break
        index += 1
    count = 0
    for i in ingredients:
        if index == count:
            danger = i
            break
        count += 1
    dangers[allergen] = danger
    for i in allergens:
        grid[allergens[i]][count] = False
    return

def partBoth():
    allergens = {}
    ingredients = {}
    ingredCount = 0
    alleCount = 0
    total = 0
    lines = []
    grid = []
    safes = []
    dangers = {}
    for i in open("in.txt", "r"):
        i = i.strip(")\n")
        ingred, alle = i.split(" (contains ")
        lines.append([alle.split(", "), ingred.split(" ")])
        for j in alle.split(", "):
            if j not in allergens:
                allergens[j] = alleCount
                alleCount += 1
        for j in ingred.split(" "):
            if j not in ingredients:
                ingredients[j] = ingredCount
                ingredCount += 1
    for i in allergens:
        curr = []
        for j in ingredients:
            curr.append(True)
        grid.append(curr)
    for i in lines:
        for j in i[0]:
            for k in ingredients:
                if k not in i[1]:
                    grid[allergens[j]][ingredients[k]] = False
    for i in ingredients:
        safe = True
        for j in allergens:
            if grid[allergens[j]][ingredients[i]]:
                safe = False
                break
        if safe:
            safes.append(i)
    for i in lines:
        for j in safes:
            if j in i[1]:
                total += 1
    for i in range(len(allergens)):
        for j in allergens:
            count = 0
            for k in grid[allergens[j]]:
                if k:
                    count += 1
            if count == 1:
                findDanger(ingredients, allergens, j, grid, dangers)
        if len(dangers) == len(allergens):
            break
    allergenList = []
    for i in allergens:
        allergenList.append(i)
    allergenList.sort()
    ingredString = ""
    for i in allergenList:
        ingredString += dangers[i] + ","
    return total, ingredString.strip(",")

print(partBoth())