def countOrbit(curr, orbits, mapping):
    if curr not in mapping:
        return 1
    count = 1
    for i in orbits[mapping[curr]]:
        count += countOrbit(i, orbits, mapping)
    return count
    

def part1(fileName = "in.txt"):
    mapping = {}
    orbits = []
    curr = 0
    for i in open(fileName).read().split("\n"):
        line = i.split(")")
        if line[0] not in mapping:
            mapping[line[0]] = curr
            orbits.append([])
            curr += 1
        orbits[mapping[line[0]]].append(line[1])
    total = 0
    for i in mapping:
        total += countOrbit(i, orbits, mapping) - 1
    return total
    
def part2(fileName = "in.txt"):
    mapping = {}
    reversing = {}
    orbits = []
    curr = 0
    for i in open(fileName).read().split("\n"):
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
            return count - 2
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
    print("Part 1:", part1("in6.txt"))
    print("Part 2:", part2("in6.txt"))