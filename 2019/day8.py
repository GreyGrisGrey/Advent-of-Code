from math import floor

def partBoth(fileName = "in.txt"):
    data = open(fileName).read()
    best = [999, 0]
    mapping = {}
    for i in range(floor(len(data)/150)):
        counts = [0, 0, 0]
        for j in range(150):
            counts[int(data[i * 150 + j])] += 1
            if j not in mapping and int(data[i * 150 + j]) != 2:
                mapping[j] = int(data[i * 150 + j])
        if counts[0] < best[0]:
            best[0] = counts[0]
            best[1] = counts[1] * counts[2]
    for i in range(6):
        for j in range(25):
            if mapping[j + (25 * i)] == 1:
                print(mapping[j + (25 * i)], end="")
            else:
                print(" ", end = "")
        print("")
    return best[1]

if __name__ == "__main__":
    print("Part 2:")
    res = partBoth("in8.txt")
    print("Part 1:", res)