def part1(file):
    coords = [0, 0]
    direction = [0, 1]
    for i in open(file):
        command = i[0]
        move = int(i[1::])
        match command:
            case "N":
                coords[1] -= move
            case "W":
                coords[0] -= move
            case "S":
                coords[1] += move
            case "E":
                coords[0] += move
            case "F":
                coords[direction[0]] += direction[1] * move
            case "R":
                if move == 180:
                    direction[1] *= -1
                else:
                    if move == 90 and direction[0] == 1:
                        direction[1] *= -1
                    elif move == 270 and direction[0] == 0:
                        direction[1] *= -1
                    direction[0] = (direction[0] + 1)%2
            case "L":
                if move == 180:
                    direction[1] *= -1
                else:
                    if move == 90 and direction[0] == 0:
                        direction[1] *= -1
                    elif move == 270 and direction[0] == 1:
                        direction[1] *= -1
                    direction[0] = (direction[0] + 1)%2
    return (abs(coords[0]) + abs(coords[1]))


def part2(file):
    shipCoords = [0, 0]
    wayCoords = [10, 1]
    for i in open(file):
        command = i[0]
        move = int(i[1::])
        match command:
            case "N":
                wayCoords[1] += move
            case "W":
                wayCoords[0] -= move
            case "S":
                wayCoords[1] -= move
            case "E":
                wayCoords[0] += move
            case "F":
                shipCoords[0] += wayCoords[0]*move
                shipCoords[1] += wayCoords[1]*move
            case "R":
                if move == 180:
                    wayCoords[1] *= -1
                    wayCoords[0] *= -1
                elif move == 90:
                    temp = wayCoords[0]
                    wayCoords[0] = wayCoords[1]
                    wayCoords[1] = -1 * temp
                else:
                    temp = wayCoords[0]
                    wayCoords[0] = -1 * wayCoords[1]
                    wayCoords[1] = temp
            case "L":
                if move == 180:
                    wayCoords[1] *= -1
                    wayCoords[0] *= -1
                elif move == 270:
                    temp = wayCoords[0]
                    wayCoords[0] = wayCoords[1]
                    wayCoords[1] = -1 * temp
                else:
                    temp = wayCoords[0]
                    wayCoords[0] = -1 * wayCoords[1]
                    wayCoords[1] = temp
    return (abs(shipCoords[0]) + abs(shipCoords[1]))

print("Part 1 :", part1("input.txt"))
print("Part 2 :", part2("input.txt"))