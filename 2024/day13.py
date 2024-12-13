import math
def part1():
    f = open("input.txt")
    end = 0
    A = 0
    B = 0
    pos = 0
    for i in f:
        if A == 0:
            words = i.split(" ")
            A = [int(words[2][2:-1:]), int(words[3][2:-1:])]
        elif B == 0:
            words = i.split(" ")
            B =  [int(words[2][2:-1:]), int(words[3][2:-1:])]
        elif pos == 0:
            words = i.split(", ")
            pos = [int(words[0][9::]), int(words[1][2::].strip())]
        else:
            end += newEquation(A, B, pos)
            A = 0
            B = 0
            pos = 0
    end += newEquation(A, B, pos)
    return end

def newEquation(A, B, end):
    Bstar = [B[0]*A[1], B[1]*A[0]]
    endStar = [end[0]*A[1], end[1]*A[0]]
    newEq = [Bstar[0]-Bstar[1], endStar[0]-endStar[1]]
    newB = newEq[1]/newEq[0]
    newA = (end[1] - newB*B[1])/A[1]
    if newA > -1 and newB > -1 and math.ceil(newB) == math.floor(newB) and math.ceil(newA) == math.floor(newA):
        return newA*3 + newB
    else:
        return 0
    
def part2():
    f = open("test.txt")
    end = 0
    A = 0
    B = 0
    pos = 0
    for i in f:
        if A == 0:
            words = i.split(" ")
            A = [int(words[2][2:-1:]), int(words[3][2:-1:])]
        elif B == 0:
            words = i.split(" ")
            B =  [int(words[2][2:-1:]), int(words[3][2:-1:])]
        elif pos == 0:
            words = i.split(", ")
            pos = [int(words[0][9::])+10000000000000, int(words[1][2::].strip())+10000000000000]
        else:
            end += newEquation(A, B, pos)
            A = 0
            B = 0
            pos = 0
    end += newEquation(A, B, pos)
    return end

print(part1())
print(part2())