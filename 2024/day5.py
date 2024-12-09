def part1():
    f = open("input.txt", "r")
    orders = {}
    orderings = []
    count = 0
    lists = []
    listings = False
    end = 0
    for i in f:
        if i == "\n":
            listings = True
        elif listings:
            orderings.append(i.split(","))
            orderings[len(orderings)-1][len(i.split(","))-1] = orderings[len(orderings)-1][len(i.split(","))-1].strip()
        else:
            new = i.split("|")
            if new[0] not in orders:
                orders[new[0]] = count
                count += 1
                lists.append([new[1].strip()])
            else:
                lists[orders[new[0]]].append(new[1].strip())
    for i in orderings:
        for j in i:
            if j in orders:
                safe = False
                for k in i:
                    if k == j:
                        safe = True
                        break
                    elif k in lists[orders[j]]:
                        break
                if not safe:
                    break
        if safe:
            end += int(i[int((len(i)-1)/2)])
    return end

def part2(start):
    f = open("input.txt", "r")
    orders = {}
    orderings = []
    count = 0
    lists = []
    listings = False
    end = 0
    for i in f:
        if i == "\n":
            listings = True
        elif listings:
            orderings.append(i.split(","))
            orderings[len(orderings)-1][len(i.split(","))-1] = orderings[len(orderings)-1][len(i.split(","))-1].strip()
        else:
            new = i.split("|")
            if new[0] not in orders:
                orders[new[0]] = count
                count += 1
                lists.append([new[1].strip()])
            else:
                lists[orders[new[0]]].append(new[1].strip())
    for i in orderings:
        for j in range(len(i)):
            if i[len(i)-(j+1)] in orders:
                for k in range(len(i)):
                    if k == j:
                        break
                    elif i[len(i)-(k+1)] in lists[orders[i[len(i)-(j+1)]]]:
                        swap = i[len(i)-(j+1)]
                        i[len(i)-(j+1)] = i[len(i)-(k+1)]
                        i[len(i)-(k+1)] = swap
        end += int(i[int((len(i)-1)/2)])
    print("Part 2", "Part 1")
    print(end - start, start)

part2(part1())