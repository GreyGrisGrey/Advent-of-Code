def part1():
    curr = ["a", "b", "c", "d", "e", "f", "g", "h"]
    count = 0
    for i in open("in.txt", "r").read().split("\n"):
        i = i.strip().split(" ")
        count += 1
        if len(i) == 4:
            for j in range(int(i[2])):
                if i[1] == "right":
                    curr.insert(0, curr[7])
                    del curr[8]
                else:
                    curr.append(curr[0])
                    del curr[0]
        elif len(i) == 5:
            start = int(i[2])
            end = int(i[4])
            newList = []
            for j in range(len(curr)):
                if j < start or j > end:
                    newList.append(curr[j])
                else:
                    newList.append(curr[end - (j - start)])
            curr = newList
        elif len(i) == 7:
            for j in range(len(curr)):
                if curr[j] == i[6]:
                    index = j + 1 if j < 4 else j + 2
                    break
            for j in range(index):
                curr.insert(0, curr[len(curr) - 1])
                del curr[len(curr) - 1]
        elif i[0] == "move":
            start = int(i[2])
            end = int(i[5])
            if end < start:
                curr.insert(end, curr[start])
                del curr[start + 1]
            else:
                curr.insert(end + 1, curr[start])
                del curr[start]
        elif i[1] == "letter":
            for j in range(len(curr)):
                if curr[j] == i[2]:
                    index1 = j
                if curr[j] == i[5]:
                    index2 = j
            temp = curr[index1]
            curr[index1] = curr[index2]
            curr[index2] = temp
        else:
            temp = curr[int(i[2])]
            curr[int(i[2])] = curr[int(i[5])]
            curr[int(i[5])] = temp
    print("Part 1:", "".join(curr))


def part2():
    curr = ["f", "b", "g", "d", "c", "e", "a", "h"]
    data = open("in.txt", "r").read().split("\n")
    data.reverse()
    count = len(data)
    for i in data:
        i = i.strip().split(" ")
        count -= 1
        if len(i) == 4:
            for j in range(int(i[2])):
                if i[1] == "left":
                    curr.insert(0, curr[7])
                    del curr[8]
                else:
                    curr.append(curr[0])
                    del curr[0]
        elif len(i) == 5:
            start = int(i[2])
            end = int(i[4])
            newList = []
            for j in range(len(curr)):
                if j < start or j > end:
                    newList.append(curr[j])
                else:
                    newList.append(curr[end - (j - start)])
            curr = newList
        elif len(i) == 7:
            numMap = {1:1, 3:2, 5:3, 7:4, 2:6, 4:7, 6:8, 0:9}
            for j in range(len(curr)):
                if curr[j] == i[6]:
                    index = numMap[j]
                    break
            for j in range(index):
                curr.append(curr[0])
                del curr[0]
        elif i[0] == "move":
            start = int(i[2])
            end = int(i[5])
            if end < start:
                curr.insert(start + 1, curr[end])
                del curr[end]
            else:
                curr.insert(start, curr[end])
                del curr[end + 1]
        elif i[1] == "letter":
            for j in range(len(curr)):
                if curr[j] == i[2]:
                    index1 = j
                if curr[j] == i[5]:
                    index2 = j
            temp = curr[index1]
            curr[index1] = curr[index2]
            curr[index2] = temp
        else:
            temp = curr[int(i[2])]
            curr[int(i[2])] = curr[int(i[5])]
            curr[int(i[5])] = temp
    print("Part 2:", "".join(curr))
            
            
            

part1()
part2()