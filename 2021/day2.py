def part1():
    location = [0, 0]
    for i in open("in.txt").read().split("\n"):
        i = i.split(" ")
        if i[0] == "forward":
            location[0] += int(i[1])
        elif i[0] == "down":
            location[1] += int(i[1])
        else:
            location[1] -= int(i[1])
    return location[0] * location[1]

def part2():
    location = [0, 0]
    aim = 0
    for i in open("in.txt").read().split("\n"):
        i = i.split(" ")
        if i[0] == "forward":
            location[0] += int(i[1])
            location[1] += aim * int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        else:
            aim -= int(i[1])
    return location[0] * location[1]

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())