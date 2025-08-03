def check(num):
    prev = "a"
    flag = False
    prevNum = 0
    for i in str(num):
        if int(i) < prevNum:
            return False
        if i == prev:
            flag = True
        prev = i
        prevNum = int(i)
    return flag

def check2(num):
    for i in range(len(str(num)) - 1):
        if str(num)[i] == str(num)[i+1]:
            if i == 0 and str(num)[i+1] != str(num)[i+2]:
                return True
            elif i == len(str(num)) - 2 and str(num)[i - 1] != str(num)[i]:
                return True
            elif str(num)[i - 1] != str(num)[i] and str(num)[i+1] != str(num)[i+2]:
                return True
    return False

def partBoth():
    res = [0, 0]
    start, end = open("in.txt").read().split("-")
    for i in range(int(end) + 1):
        if i >= int(start) and check(i):
            if check2(i):
                res[1] += 1
            res[0] += 1
    print("Part 1:", res[0], "\nPart 2:", res[1])

partBoth()