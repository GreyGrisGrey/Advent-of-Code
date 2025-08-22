from math import floor

def partBoth(fileName = "in.txt"):
    end = [0, 0]
    for i in open(fileName).read().split("\n"):
        res = floor(int(i)/3) - 2
        end[0] += res
        while res > 0:
            end[1] += res
            res = floor(res/3) - 2
    return end

if __name__ == "__main__":
    res = partBoth("in1.txt")
    print("Part 1:", res[0], "\nPart 2:", res[1])