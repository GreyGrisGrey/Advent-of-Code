def interpolate(line):
    lines = []
    for i in range(len(line)):
        line[i] = int(line[i])
    lines.append(line)
    while notZero(line):
        newLine = []
        for i in range(len(line)-1):
            newLine.append(line[i+1]-line[i])
        lines.append(newLine)
        line = newLine
    return lines

def notZero(line):
    for i in line:
        if i != 0:
            return True
    return False

def extrapolate(lines, flag):
    for i in range(len(lines)):
        if i == 0:
            newVal = 0
        elif flag:
            newVal = lines[len(lines)-(i+1)][len(lines[len(lines)-(i+1)])-1] + newVal
        else:
            newVal = lines[len(lines)-(i+1)][0] - newVal
    return newVal

def partBoth():
    total = [0, 0]
    for i in open("in.txt", "r"):
        res = interpolate(i.strip("\n").split(" "))
        total[0] += extrapolate(res, True)
        total[1] += extrapolate(res, False)
    return total

print(partBoth())