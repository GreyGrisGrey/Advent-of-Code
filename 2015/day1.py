f = open("input.txt", "r")
parenthesis = f.readline()
floor = 0
step = 0
stepCheck = True
for i in parenthesis:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
    step += 1
    if floor == -1 and stepCheck:
        print(step)
        stepCheck = False
print(floor)