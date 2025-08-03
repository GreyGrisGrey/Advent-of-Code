def partBoth():
    spaces = {}
    flag = True
    best = [-1, -1]
    for i in open("in.txt").read().split("\n"):
        curr = [0, 0]
        count = 0
        for j in i.split(","):
            for k in range(int(j[1::])):
                count += 1
                curr[0] += 1 if j[0] == "R" else -1 if j[0] == "L" else 0
                curr[1] += 1 if j[0] == "D" else -1 if j[0] == "U" else 0
                if flag:
                    spaces[curr[0] * 100000 + curr[1]] = count
                elif (curr[0] * 100000 + curr[1]) in spaces:
                    if (abs(curr[0]) + abs(curr[1]) < best[0]) or best[0] == -1:
                        best[0] = abs(curr[0]) + abs(curr[1])
                    if count + spaces[curr[0] * 100000 + curr[1]] < best[1] or best[1] == -1:
                        best[1] = count + spaces[curr[0] * 100000 + curr[1]]
        flag = False
    print("Part 1:", best[0], "\nPart 2:", best[1])

partBoth()