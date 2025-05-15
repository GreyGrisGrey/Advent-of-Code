def solve(line):
    operands = []
    operators = []
    count = 0
    total = 0
    newOperand = ""
    while count < len(line):
        if line[count] in "1234567890":
            newOperand += line[count]
        elif newOperand != "" and line[count] == " ":
            operands.append(newOperand)
            newOperand = ""
        elif line[count] in "*+":
            operators.append(line[count])
        elif line[count] == "(":
            res = solve(line[count+1::])
            count += res[0]
            operands.append(res[1])
        elif line[count] == ")":
            count += 1
            operands.append(newOperand)
            break
        count += 1
    if count == len(line):
        operands.append(newOperand)
    total = int(operands[0])
    for i in range(len(operators)):
        if operators[i] == "*":
            total *= int(operands[i+1])
        else:
            total += int(operands[i+1])
    return count, total

def solve2(line):
    operands = []
    operators = []
    count = 0
    total = 0
    newOperand = ""
    while count < len(line):
        if line[count] in "1234567890":
            newOperand += line[count]
        elif newOperand != "" and line[count] == " ":
            operands.append(newOperand)
            newOperand = ""
        elif line[count] in "*+":
            operators.append(line[count])
        elif line[count] == "(":
            res = solve2(line[count+1::])
            count += res[0]
            operands.append(res[1])
        elif line[count] == ")":
            count += 1
            if newOperand != "":
                operands.append(newOperand)
            break
        count += 1
    if count == len(line) and newOperand != "":
        operands.append(newOperand)
    newOperands = []
    indexDict = {}
    for i in range(len(operands)):
        indexDict[i] = True
    newOp = int(operands[0])
    for i in range(len(operators)):
        if operators[i] == "+":
            newOp += int(operands[i+1])
        else:
            if newOp != 0:
                newOperands.append(newOp)
            newOp = int(operands[i+1])
    if newOp != 0:
        newOperands.append(newOp)
    total = newOperands[0]
    for i in range(len(newOperands)-1):
        total *= newOperands[i+1]
    return count, total

def partBoth():
    totalA = 0
    totalB = 0
    for i in open("in.txt", "r"):
        totalA += solve(i.strip("\n"))[1]
        totalB += solve2(i.strip("\n"))[1]
    return totalA, totalB

print(partBoth())