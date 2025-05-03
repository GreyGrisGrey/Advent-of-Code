def checkAdj(grid, indexY, indexX, num, gears):
    for i in range(len(num)):
        for j in range(3):
            for k in range(3):
                if checkExist(grid, indexY+j-1, indexX+k-(i+2)) and checkSymb(grid, indexY+j-1, indexX+k-(i+2)):
                    if (grid[indexY+j-1][indexX+k-(i+2)] == "*"):
                        gearIndex = str(indexY+j-1) + ":" + str(indexX+k-(i+2))
                        if gearIndex in gears:
                            gears[gearIndex] += ":" + num
                        else:
                            gears[gearIndex] = num
                    return int(num)
    return 0


def checkExist(grid, indexY, indexX):
    return False if ((indexX < 0) or (indexY < 0) or (indexY >= len(grid)) or (indexX >= len(grid[indexY]))) else True


def checkSymb(grid, indexY, indexX):
    return True if ((not grid[indexY][indexX].isalnum()) and (grid[indexY][indexX] != ".") and grid[indexY][indexX] != "\n") else False


def partBoth():
    grid = []
    res = [0, 0]
    gearDict = {}
    for i in open("in.txt", "r"):
        grid.append(i)
    for i in range(len(grid)):
        num = ""
        for j in range(len(grid[i])):
            if grid[i][j].isalnum():
                num += grid[i][j]
            elif len(num) != 0:
                res[0] += checkAdj(grid, i, j, num, gearDict)
                num = ""
    for i in gearDict:
        nums = gearDict[i].split(":")
        if len(nums) == 2:
            res[1] += int(nums[0]) * int(nums[1])
    return res

print(partBoth())
