from intCode import intMachine

def part1():
    tiles = {}
    machine = intMachine(13)
    nums = [0, 0, 0]
    index = -1
    while True:
        if index == 0:
            tiles[nums[0] * 1000 + nums[1]] = nums[2]
        if index == -1:
            index = 0
        res = machine.run(getOuts = True)
        if res[0] == 0:
            nums[index] = res[1]
        else:
            break
        index = (index + 1) % 3
    total = 0
    for i in tiles:
        if tiles[i] == 2:
            total += 1
    print("Part 1:", total)

def printScreen(tiles):
    for i in range(42):
        print("")
        for j in range(30):
            if i * 1000 + j in tiles and tiles[i * 1000 + j] != 0:
                print(tiles[i * 1000 + j], end="")
            else:
                print(" ", end="")
    print("")

def part2():
    tiles = {}
    machine = intMachine(13)
    machine.setIndex(0, 2)
    currBall = None
    prevBall = None
    currPaddle = None
    ballDir = "D"
    nums = [0, 0, 0]
    index = -1
    score = 0
    while True:
        if index == 0:
            tiles[nums[0] * 1000 + nums[1]] = nums[2]
            if nums[0] == -1 and nums[1] == 0:
                score = nums[2]
            if nums[2] == 3:
                currPaddle = nums[0]
            if nums[2] == 4:
                currBall = nums[0]
                if prevBall != None and currBall < prevBall:
                    ballDir = "U"
                elif prevBall != None:
                    ballDir = "D"
            if currPaddle != None and currBall != None:
                if currBall == currPaddle:
                    machine.addInput(0)
                elif ballDir == "U" and currBall < currPaddle:
                    machine.addInput(-1)
                    currPaddle = None
                elif ballDir == "D" and currBall > currPaddle:
                    machine.addInput(1)
                    currPaddle = None
                else:
                    machine.addInput(0)
                prevBall = currBall
                currBall = None
        if index == -1:
            index = 0
        res = machine.run(getOuts = True)
        if res[0] == 0:
            nums[index] = res[1]
        else:
            break
        index = (index + 1) % 3
    print("Part 2:", score)

if __name__ == "__main__":
    part1()
    part2()