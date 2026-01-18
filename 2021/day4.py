def part1():
    boards = []
    lines = []
    instructs = []
    for i in open("in.txt").read().split("\n"):
        if len(instructs) == 0:
            instructs = list(map(lambda x: int(x), i.split(",")))
        elif len(lines) == 5:
            boards.append(lines)
            lines = []
        elif len(i) != 0:
            nums = i.split(" ")
            newLine = []
            for j in nums:
                if j != "":
                    newLine.append([int(j), False])
            lines.append(newLine)
    if len(lines) == 5:
        boards.append(lines)
    for i in instructs:
        for j in boards:
            for k in range(5):
                for l in range(5):
                    if j[k][l][0] == i:
                        j[k][l][1] = True
                        if checkWon(j):
                            return getVal(j, i)
    return -1

def getVal(board, mult):
    total = 0
    for i in range(5):
        for j in range(5):
            if not board[i][j][1]:
                total += board[i][j][0]
    return total * mult

def checkWon(board):
    for i in range(5):
        good = True
        for j in range(5):
            if not board[i][j][1]:
                good = False
        if good:
            return True
    for i in range(5):
        good = True
        for j in range(5):
            if not board[j][i][1]:
                good = False
        if good:
            return True
    if board[0][0][1] and board[1][1][1] and board[2][2][1] and board[3][3][1] and board[4][4][1]:
        return True
    if board[4][0][1] and board[3][1][1] and board[2][2][1] and board[1][3][1] and board[0][4][1]:
        return True
    return False
    

def part2():
    boards = []
    lines = []
    instructs = []
    dones = []
    lastWon = -1
    for i in open("in.txt").read().split("\n"):
        if len(instructs) == 0:
            instructs = list(map(lambda x: int(x), i.split(",")))
        elif len(lines) == 5:
            boards.append(lines)
            lines = []
        elif len(i) != 0:
            nums = i.split(" ")
            newLine = []
            for j in nums:
                if j != "":
                    newLine.append([int(j), False])
            lines.append(newLine)
    if len(lines) == 5:
        boards.append(lines)
    for i in instructs:
        for j in boards:
            for k in range(5):
                for l in range(5):
                    if j[k][l][0] == i:
                        j[k][l][1] = True
                        if checkWon(j) and j not in dones:
                            dones.append(j)
                            lastWon = getVal(j, i)
    return lastWon

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())