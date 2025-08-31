def partBoth():
    grid = {}
    res = [0, 0]
    overlapped = {}
    for i in open("in.txt").read().split("\n"):
        currLine = i.split(" ")
        start = list(map(lambda x: int(x), currLine[2].strip(":").split(",")))
        size = list(map(lambda x: int(x), currLine[3].split("x")))
        for j in range(size[0]):
            for k in range(size[1]):
                key = str(start[0] + j) + ":" + str(start[1] + k)
                if key in grid:
                    overlapped[grid[key]] = True
                    overlapped[int(currLine[0][1::])] = True
                grid[key] = int(currLine[0][1::]) if key not in grid else "None"
    for i in grid:
        if grid[i] == "None":
            res[0] += 1
        elif grid[i] not in overlapped:
            res[1] = grid[i]
    return res

if __name__ == "__main__":
    res = partBoth()
    print("Part 1:", res[0])
    print("Part 2:", res[1])