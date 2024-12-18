def part1():
    blocked = {}
    count = 0
    for i in open("input.txt"):
        if count < 1024:
            blocked[i.strip()] = False
        count += 1
    openList = ["0,0"]
    count = 0
    while True:
        newOpen = []
        for i in openList:
            for j in (BFS(blocked, i)):
                newOpen.append(j)
            blocked[i] = False
        count += 1
        openList = newOpen
        if "70,70" in newOpen:
            return count
                
def part2():
    blocked = {}
    count = 0
    for i in open("input.txt"):
        blocked[i.strip()] = False
        count += 1
        openList = ["0,0"]
        count2 = 0
        blocked2 = {}
        for j in blocked:
            blocked2[j] = False
        while count2 < 5000:
            newOpen = []
            for j in openList:
                for k in (BFS(blocked2, j)):
                    newOpen.append(k)
                blocked2[j] = False
            count2 += 1
            openList = newOpen
            if "70,70" in newOpen:
                break
        if count2 == 5000:
            return i

#rather inefficient
def BFS(blocked, open):
    next = []
    coords = open.split(",")
    if open not in blocked and int(coords[0])>=0 and int(coords[1])>= 0 and int(coords[0])<71 and int(coords[1])<71:
        options = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        next = []
        coords = open.split(",")
        for i in options:
            next.append(str(int(coords[0])+i[0]) + "," + str(int(coords[1])+i[1]))
        blocked[open] = False
    return next

print(part1())
print(part2())