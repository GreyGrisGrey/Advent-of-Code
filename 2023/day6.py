def part1():
    times = []
    dists = []
    for i in open("in.txt", "r"):
        if len(times) == 0:
            i = i[6::].strip().split(" ")
            for j in i:
                if j != "":
                    times.append(int(j))
        else:
            i = i[10::].strip().split(" ")
            for j in i:
                if j != "":
                    dists.append(int(j))
    total = 1
    for i in range(len(times)):
        winFlag = False
        count = 0
        wins = 0
        while True:
            if winFlag and count * (times[i]-count) < dists[i]:
                break
            elif winFlag or count * (times[i]-count) >= dists[i]:
                wins += 1
                winFlag = True
            count += 1
        total *= wins
    return total

#Binary search seems most reasonable for part 2, but the numbers are so low I'm electing to use the previous brute force solution.

def part2():
    time = ""
    dist = ""
    for i in open("in.txt", "r"):
        if time == "":
            i = i[6::].strip().split(" ")
            for j in i:
                time += j
        else:
            i = i[10::].strip().split(" ")
            for j in i:
                dist += j
    total = 1
    times = [int(time)]
    dists = [int(dist)]
    for i in range(len(times)):
        winFlag = False
        count = 0
        wins = 0
        while True:
            if winFlag and count * (times[i]-count) < dists[i]:
                break
            elif winFlag or count * (times[i]-count) >= dists[i]:
                wins += 1
                winFlag = True
            count += 1
        total *= wins
    return total

print(part1())
print(part2())