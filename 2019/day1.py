from math import floor

def partBoth():
    end = [0, 0]
    for i in open("in.txt").read().split("\n"):
        res = floor(int(i)/3) - 2
        end[0] += res
        while res > 0:
            end[1] += res
            res = floor(res/3) - 2
    print("Part 1:", end[0], "\nPart 2:", end[1])

partBoth()