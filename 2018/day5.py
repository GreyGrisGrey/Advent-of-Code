def part1():
    molecule = open('in.txt').read()
    flag = True
    while flag:
        flag = False
        count = 0
        newMol = ""
        while count < len(molecule):
            if count + 1 < len(molecule) and molecule[count].capitalize() == molecule[count + 1].capitalize() and molecule[count] != molecule[count + 1]:
                flag = True
                count += 2
            else:
                newMol += molecule[count]
                count += 1
        if flag:
            molecule = newMol
    res = [len(molecule), len(molecule)]
    for i in range(26):
        part2Partial = eliminateLetter(chr(65 + i), molecule)
        if part2Partial < res[1]:
            res[1] = part2Partial
    return res

def eliminateLetter(letter, molecule):
    flag = True
    while flag:
        flag = False
        count = 0
        newMol = ""
        while count < len(molecule):
            if count + 1 < len(molecule) and molecule[count].capitalize() == molecule[count + 1].capitalize() and molecule[count] != molecule[count + 1]:
                flag = True
                count += 2
            elif molecule[count].capitalize() == letter:
                flag = True
                count += 1
            else:
                newMol += molecule[count]
                count += 1
        if flag:
            molecule = newMol
    return len(molecule)

if __name__ == "__main__":
    res = part1()
    print("Part 1:", res[0])
    print("Part 2:", res[1])