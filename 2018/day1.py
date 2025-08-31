def part1():
    num = 0
    for i in open("in.txt").read().split("\n"):
        num += int(i)
    return num

def part2():
    num = 0
    visited = {}
    visited[0] = True
    while True:
        for i in open("in.txt").read().split("\n"):
            num += int(i)
            if num in visited:
                return num
            visited[num] = True

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())