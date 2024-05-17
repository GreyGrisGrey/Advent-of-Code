f = open("input.txt")
racers = []
for i in f:
    line = i.split()
    racers.append([line[0], int(line[3]), int(line[6]), int(line[13]), 0, True, 0, 0])
for i in range(2503):
    print(i)
    for j in racers:
        if j[5]:
            j[6] += j[1]
            j[4] += 1
            if j[4] == j[2]:
                j[5] = not j[5]
                j[4] = 0
        else:
            j[4] += 1
            if j[4] == j[3]:
                j[5] = not j[5]
                j[4] = 0
    currWin = 0
    currWinners = []
    for j in racers:
        if j[6] > currWin:
            currWinners = [j]
            currWin = j[6]
        elif j[6] == currWin:
            currWinners.append(j)
    for j in currWinners:
        j[7] += 1
for i in racers:
    print(i)