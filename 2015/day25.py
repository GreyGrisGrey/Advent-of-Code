def part1():
    nums = open("in.txt").read().split(" ")
    goal = [int(nums[len(nums)-3].strip(",")), int(nums[len(nums)-1].strip("."))]
    curr = [1, 1]
    maxRow = 1
    currStep = 20151125
    while curr[0] != goal[0] or curr[1] != goal[1]:
        if curr[0] == 1:
            maxRow += 1
            curr = [maxRow, 1]
        else:
            curr[0] -= 1
            curr[1] += 1
        currStep = (currStep * 252533) % 33554393
    return currStep

print(part1())