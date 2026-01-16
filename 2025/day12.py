def part1():
    good = 0
    trees = False
    sizes = [5, 7, 6, 7, 7, 7]
    for i in open("in.txt").read().split("\n"):
        if len(i.split(" ")) != 1:
            trees = True
        if trees:
            i = i.split(" ")
            first = i[0].strip(":").split("x")
            size = int(first[0]) * int(first[1])
            nums = list(map(lambda x: int(x), i[1::]))
            spaceReq = 0
            for j, k in enumerate(nums):
                spaceReq += k * sizes[j]
            if spaceReq < size:
                good += 1
    return good

if __name__ == "__main__":
    print("Part 1:", part1())