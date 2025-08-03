def countOrbit(curr, orbits, mapping):
    if curr not in mapping:
        return 1
    count = 1
    for i in orbits[mapping[curr]]:
        count += countOrbit(i, orbits, mapping)
    return count
    

def part1():
    mapping = {}
    orbits = []
    curr = 0
    for i in open("in.txt").read().split("\n"):
        line = i.split(")")
        if line[0] not in mapping:
            mapping[line[0]] = curr
            orbits.append([])
            curr += 1
        orbits[mapping[line[0]]].append(line[1])
    total = 0
    for i in mapping:
        total += countOrbit(i, orbits, mapping) - 1
    print("Part 1:", total)
    
def part2():
    mapping = {}
    reversing = {}
    orbits = []
    curr = 0
    for i in open("in.txt").read().split("\n"):
        line = i.split(")")
        if line[0] not in mapping:
            mapping[line[0]] = curr
            orbits.append([])
            curr += 1
        orbits[mapping[line[0]]].append(line[1])
        reversing[line[1]] = line[0]
    end = "SAN"
    opens = ["YOU"]
    closed = []
    count = 0
    remaining = 1
    while True:
        if remaining == 0:
            remaining = len(opens)
            count += 1
        curr = opens[0]
        remaining -= 1
        if curr == end:
            print("Part 2:", count-2)
            return
        if curr in mapping:
            for i in orbits[mapping[curr]]:
                if i not in closed:
                    opens.append(i)
                    closed.append(i)
        if curr in reversing and reversing[curr] not in closed:
            opens.append(reversing[curr])
            closed.append(reversing[curr])
        del opens[0]

if __name__ == "__main__":
    part1()
    part2()