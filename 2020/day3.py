def part1():
    f = open("input.txt", "r")
    end = 0
    curr = 0
    grid = []
    coords = [0]
    for i in f:
        grid.append(i.strip())
        if len(coords) == 1:
            coords.append(len(grid[0]))
        if i[curr] == "#":
            end += 1
        curr = (curr + 3)%coords[1]
    return end

def part2():
    end = 0
    curr = 0
    grid = []
    coords = [0]
    adders = [1, 3, 5, 7, 2]
    count = 0
    ends = []
    for j in adders:
        f = open("input.txt", "r")
        curr = 0
        end = 0
        for i in f:
            grid.append(i.strip())
            if len(coords) == 1:
                coords.append(len(grid[0]))
            if j == 2 and count == 0:
                if i[curr] == "#":
                    end += 1
                curr = (curr + 1)%coords[1]
                count = (count + 1)%2
            elif j == 2:
                count = (count + 1)%2
            else:
                if i[curr] == "#":
                    end += 1
                curr = (curr + j)%coords[1]
        ends.append(end)
    total = 1
    print(ends)
    for i in ends:
        total *= i
    return total

print(part1())
print(part2())