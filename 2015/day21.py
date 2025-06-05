# Done by manually calculating the cost of damage versus armour
# The required quantity of both to win is printed by the code below
def partBoth():
    file = open('in.txt')
    play = 100
    boss = int(file.readline().strip("\n").split(" ")[2])
    bossDmg = int(file.readline().strip("\n").split(" ")[1])
    bossArm = int(file.readline().split(" ")[1])
    for i in range(12):
        dmg = i
        winBar = []
        for j in range(9):
            temp = [boss, play]
            while temp[0] > 0 and temp[1] > 0:
                temp[0] -= max((dmg - bossArm), 1)
                if temp[0] > 0:
                    temp[1] -= max((bossDmg - j), 1)
            winBar.append(True if temp[1] > 0 else False)
        print(winBar)

partBoth()