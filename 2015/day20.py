from math import sqrt, ceil

def getPrimes(num):
    temp = num
    primes = {}
    for i in range(num+1):
        while i != 0 and temp % (i+1) == 0:
            primes[i+1] = 1 if i+1 not in primes else (primes[i+1] + 1)
            temp = int(temp/(i+1))
        if temp == 1:
            break
    if temp == num:
        primes[temp] = 1
    return primes

def getFactors(num):
    temp = num
    factors = {}
    for i in range(ceil(sqrt(num))):
        if temp % (i+1) == 0:
            factors[i+1] = True
            factors[int(temp/(i+1))] = True
    return factors
    

def part1():
    goal = int(int(open('in.txt', "r").read())/10)
    currIndex = 1
    while True:
        total = 0
        for i in getFactors(currIndex):
            total += i
        if total >= goal:
            return currIndex
        currIndex += 1

def part2():
    goal = int(int(open('in.txt', "r").read())/10)
    currIndex = 1
    factorsCount = {}
    while True:
        total = 0
        for i in getFactors(currIndex):
            if i not in factorsCount:
                factorsCount[i] = 0
            if factorsCount[i] < 50:
                total += i*1.1
                factorsCount[i] += 1
        if total >= goal:
            return currIndex
        currIndex += 1

print(part1())
print(part2())