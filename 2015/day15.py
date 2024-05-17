def part1():
    f = open("input.txt")
    ingredients = []
    for i in f:
        line = i.split()
        ingredients.append([int(line[2][:len(line[2])-1:]), int(line[4][:len(line[4])-1:]), int(line[6][:len(line[6])-1:]), int(line[8][:len(line[8])-1:]), int(line[10][:len(line[10]):])])
    maximum = 0
    maximumIngredients = [0, 0, 0, 0]
    for i in range(101):
        for j in range(101-i):
            for k in range(101-(i+j)):
                newVal1 = (ingredients[0][0] * i) + (ingredients[1][0] * j) + (ingredients[2][0] * k) + (ingredients[3][0] * (100 - (k + i + j)))
                newVal2 = (ingredients[0][1] * i) + (ingredients[1][1] * j) + (ingredients[2][1] * k) + (ingredients[3][1] * (100 - (k + i + j)))
                newVal3 = (ingredients[0][2] * i) + (ingredients[1][2] * j) + (ingredients[2][2] * k) + (ingredients[3][2] * (100 - (k + i + j)))
                newVal4 = (ingredients[0][3] * i) + (ingredients[1][3] * j) + (ingredients[2][3] * k) + (ingredients[3][3] * (100 - (k + i + j)))
                if maximum < (newVal1 * newVal2 * newVal3 * newVal4) and newVal1 > 0 and newVal2 > 0 and newVal3 > 0:
                    maximum = (newVal1 * newVal2 * newVal3 * newVal4)
                    maximumIngredients = [i, j, k, (100 - (k + i + j))]
    print(maximum, maximumIngredients)

def part2():
    f = open("input.txt")
    ingredients = []
    for i in f:
        line = i.split()
        ingredients.append([int(line[2][:len(line[2])-1:]), int(line[4][:len(line[4])-1:]), int(line[6][:len(line[6])-1:]), int(line[8][:len(line[8])-1:]), int(line[10][:len(line[10]):])])
    maximum = 0
    maximumIngredients = [0, 0, 0, 0]
    for i in range(101):
        for j in range(101-i):
            for k in range(101-(i+j)):
                newVal1 = (ingredients[0][0] * i) + (ingredients[1][0] * j) + (ingredients[2][0] * k) + (ingredients[3][0] * (100 - (k + i + j)))
                newVal2 = (ingredients[0][1] * i) + (ingredients[1][1] * j) + (ingredients[2][1] * k) + (ingredients[3][1] * (100 - (k + i + j)))
                newVal3 = (ingredients[0][2] * i) + (ingredients[1][2] * j) + (ingredients[2][2] * k) + (ingredients[3][2] * (100 - (k + i + j)))
                newVal4 = (ingredients[0][3] * i) + (ingredients[1][3] * j) + (ingredients[2][3] * k) + (ingredients[3][3] * (100 - (k + i + j)))
                calories = (ingredients[0][4] * i) + (ingredients[1][4] * j) + (ingredients[2][4] * k) + (ingredients[3][4] * (100 - (k + i + j)))
                if maximum < (newVal1 * newVal2 * newVal3 * newVal4) and newVal1 > 0 and newVal2 > 0 and newVal3 > 0 and calories == 500:
                    maximum = (newVal1 * newVal2 * newVal3 * newVal4)
                    maximumIngredients = [i, j, k, (100 - (k + i + j))]
    print(maximum, maximumIngredients)

part1()
part2()