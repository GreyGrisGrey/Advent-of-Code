def part1():
    end = 0
    f = open("input.txt", "r")
    grid = []
    count = 0
    for i in f:
        count2 = 0
        gridString = i.strip()
        gridLine = []
        for j in gridString:
            if j == "^":
                start = [count, count2, "up"]
            count2 += 1
            gridLine.append(j)
        grid.append(gridLine)
        count +=1
    directions = ["up", "right", "down", "left"]
    minimum = 0
    maximum = len(grid)-1
    while True:
        if start[2] == "up":
            grid[start[0]][start[1]] = "*"
            next = [start[0]-1, start[1], "up"]
            if next[0] < minimum:
                break
            if grid[next[0]][next[1]] == "#":
                next[2] = "right"
                next[1] += 1
                next[0] += 1
        elif start[2] == "down":
            grid[start[0]][start[1]] = "*"
            next = [start[0]+1, start[1], "down"]
            if next[0] > maximum:
                break
            if grid[next[0]][next[1]] == "#":
                next[2] = "left"
                next[1] -= 1
                next[0] -= 1
        elif start[2] == "left":
            grid[start[0]][start[1]] = "*"
            next = [start[0], start[1]-1, "left"]
            if next[1]<minimum:
                break
            if grid[next[0]][next[1]] == "#":
                next[2] = "up"
                next[1] += 1
                next[0] -= 1
        else:
            grid[start[0]][start[1]] = "*"
            next = [start[0], start[1]+1, "right"]
            if next[1] > maximum:
                break
            if grid[next[0]][next[1]] == "#":
                next[2] = "down"
                next[1] -= 1
                next[0] += 1
        start = next
    for i in grid:
        for j in i:
            if j == "*":
                end += 1
    return end

def part2():
    end = 0
    f = open("input.txt", "r")
    grid = []
    count = 0
    for i in f:
        count2 = 0
        gridString = i.strip()
        gridLine = []
        for j in gridString:
            if j == "^":
                start = [count, count2, "up"]
            count2 += 1
            gridLine.append(j)
        grid.append(gridLine)
        count +=1
    directions = ["up", "right", "down", "left"]
    minimum = 0
    maximum = len(grid)-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            count = 0
            temp = grid[i][j]
            tempStart = start
            grid[i][j] = "#"
            while count < ((maximum+1) *(maximum+1)):
                if start[2] == "up":
                    next = [start[0]-1, start[1], "up"]
                    if next[0] < minimum:
                        break
                    if grid[next[0]][next[1]] == "#":
                        next[2] = "right"
                        next[0] += 1
                elif start[2] == "down":
                    next = [start[0]+1, start[1], "down"]
                    if next[0] > maximum:
                        break
                    if grid[next[0]][next[1]] == "#":
                        next[2] = "left"
                        next[0] -= 1
                elif start[2] == "left":
                    next = [start[0], start[1]-1, "left"]
                    if next[1]<minimum:
                        break
                    if grid[next[0]][next[1]] == "#":
                        next[2] = "up"
                        next[1] += 1
                else:
                    next = [start[0], start[1]+1, "right"]
                    if next[1] > maximum:
                        break
                    if grid[next[0]][next[1]] == "#":
                        next[2] = "down"
                        next[1] -= 1
                start = next
                count += 1
            grid[i][j] = temp
            start = tempStart
            if count >= ((maximum+1) *(maximum+1)) and (i != start[0] or j != start[1]):
                end += 1
    return end

print(part1())
print(part2())