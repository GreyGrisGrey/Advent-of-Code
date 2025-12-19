def part1():
    num = 50
    count = 0
    for i in open("in.txt").read().split("\n"):
        num = (num - int(i[1::]) if i[0] == "L" else num + int(i[1::])) % 100
        if num == 0:
            count += 1
    return count

def part2():
    num = 50
    count = 0
    for i in open("in.txt").read().split("\n"):
        newNum = int(i[1::])
        for j in range(newNum):
            if i[0] == "L":
                num -= 1
            if i[0] == "R":
                num += 1
            if num == 0:
                count += 1
            if num == 100:
                count += 1
                num -= 100
            if num < 0:
                num += 100
    return count

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())