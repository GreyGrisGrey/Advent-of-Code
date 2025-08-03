from intCode import intMain

def part1():
    res = intMain(12, 2)
    if len(res) != 0:
        print("Part 1:", res[0])

def part2():
    for i in range(100):
        for j in range(100):
            res = intMain(i, j)
            if len(res) != 0 and res[0] == 19690720:
                print("Part 2:", 100 * i + j)
                return

if __name__ == "__main__":
    part1()
    part2()