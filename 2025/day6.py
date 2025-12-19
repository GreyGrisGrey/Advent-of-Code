def part1():
    rows = []
    total = 0
    for i in open("in.txt").read().split("\n"):
        currIndex = 0
        row = []
        for j in i.split(" "):
            if j != "":
                row.append(int(j) if j != "+" and j != "*" else j)
        rows.append(row)
    for i in range(len(rows[0])):
        if rows[len(rows) - 1][i] == "*":
            addNum = 1
            for j in range(len(rows) - 1):
                addNum *= rows[j][i]
        else:
            addNum = 0
            for j in range(len(rows) - 1):
                addNum += rows[j][i]
        total += addNum
    return total

def part2():
    operations = []
    total = 0
    data = open("in.txt").read().split("\n")
    newData = []
    for i in data[len(data) - 1]:
        if i != " ":
            operations.append(i)
    for i in range(len(data[0])):
        newLine = ""
        for j in range(len(data) - 1):
            if data[j][i] != " ":
                newLine += data[j][i]
        newData.append(newLine)
    currOp = 0
    currNum = 0
    while currOp < len(operations):
        if operations[currOp] == "*":
            addNum = 1
            while currNum < len(newData):
                if newData[currNum] != "":
                    addNum *= int(newData[currNum])
                    currNum += 1
                else:
                    currNum += 1
                    break
        elif operations[currOp] == "+":
            addNum = 0
            while currNum < len(newData):
                if newData[currNum] != "":
                    addNum += int(newData[currNum])
                    currNum += 1
                else:
                    currNum += 1
                    break
        currOp += 1
        total += addNum
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())