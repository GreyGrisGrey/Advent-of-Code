def shoelace(vals):
    total = 0
    for i in range(len(vals)):
        total += vals[len(vals)-1][0] * vals[0][1] if i == 0 else vals[i-1][0] * vals[i][1]
        total -= vals[0][0] * vals[len(vals)-1][1] if i == 0 else vals[i][0] * vals[i-1][1]
    return total

def partBoth(fileName, part):
    perim = 0
    count = 0
    vertices = {}
    curr = [0, 0]
    dirMap = {0:"R", 1:"D", 2:"L", 3:"U"}
    vertices[count] = [curr[0], curr[1]]
    for i in open(fileName):
        res = i.strip().split(" ")
        direction = dirMap[int(res[2][7])] if part else res[0]
        num = int(res[2][2:7:], 16) if part else int(res[1])
        vertices[count][1] -= 1 if direction == "L" else 0
        vertices[count][0] -= 1 if direction == "D" else 0
        count += 1
        perim += num
        curr[0] += num if direction == "R" else -num if direction == "L" else 0
        curr[1] += num if direction == "D" else -num if direction == "U" else 0
        vertices[count] = [curr[0], curr[1]]
        vertices[count][1] -= 1 if direction == "L" else 0
        vertices[count][0] -= 1 if direction == "D" else 0
    return int(shoelace(vertices)/2) + perim

print(partBoth("in.txt", False))
print(partBoth("in.txt", True))