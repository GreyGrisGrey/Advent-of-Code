def part1():
    f = open("input.txt")
    string = f.readline()
    visited = {}
    curr = [0, 0]
    for i in string:
        visString = str(curr[0]) + "x" + str(curr[1])
        visited[visString] = True
        if i == "^":
            curr[0] += 1
        elif i == "<":
            curr[1] -= 1
        elif i == ">":
            curr[1] += 1
        elif i == "v":
            curr[0] -= 1
    visString = str(curr[0]) + "x" + str(curr[1])
    visited[visString] = True
    print(len(visited))

def part2():
    f = open("input.txt")
    string = f.readline()
    visited = {}
    curr1 = [0, 0]
    curr2 = [0, 0]
    real = True
    for i in string:
        if real:
            visString = str(curr2[0]) + "x" + str(curr2[1])
            visited[visString] = True
            if i == "^":
                curr1[0] += 1
            elif i == "<":
                curr1[1] -= 1
            elif i == ">":
                curr1[1] += 1
            elif i == "v":
                curr1[0] -= 1
        else:
            visString = str(curr1[0]) + "x" + str(curr1[1])
            visited[visString] = True
            if i == "^":
                curr2[0] += 1
            elif i == "<":
                curr2[1] -= 1
            elif i == ">":
                curr2[1] += 1
            elif i == "v":
                curr2[0] -= 1
        real = not real
    visString = str(curr1[0]) + "x" + str(curr1[1])
    visited[visString] = True
    visString = str(curr2[0]) + "x" + str(curr2[1])
    visited[visString] = True
    print(len(visited))


part1()
part2()