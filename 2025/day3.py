def part1():
    count = 0
    for i in open("in.txt").read().split("\n"):
        nums = [0] * 2
        for j in range(len(i)):
            if j != len(i) - 1 and int(i[j]) > nums[0]:
                nums[0] = int(i[j])
                nums[1] = 0
            elif int(i[j]) > nums[1]:
                nums[1] = int(i[j])
        count += nums[0] * 10 + nums[1]
    return count

def part2():
    count = 0
    for i in open("in.txt").read().split("\n"):
        nums = [0] * 12
        for j in range(len(i)):
            clear = False
            for k in range(len(nums)):
                if clear:
                    nums[k] = 0
                elif j + (len(nums) - 1 - k) < len(i) and int(i[j]) > nums[k]:
                    nums[k] = int(i[j])
                    clear = True
        for j in range(len(nums)):
            count += nums[j] * 10 ** (len(nums) - 1 - j)
    return count

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())