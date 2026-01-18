def part1():
    prev = 9999999
    total = 0
    for i in open("in.txt").read().split("\n"):
        if int(i) > prev:
            total += 1
        prev = int(i)
    return total

def part2():
    prevs = [99999, 99999, 99999]
    curr = 0
    total = 0
    for i in open("in.txt").read().split("\n"):
        prev = sum(prevs)
        prevs[curr] = int(i)
        if sum(prevs) > prev:
            total += 1
        curr = (curr + 1) % 3
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())