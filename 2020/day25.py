def part1():
    f = open("in.txt", "r")
    key1 = int(f.readline().strip("\n"))
    key2 = int(f.readline())
    subject = 7
    loop1 = 0
    curr1 = 1
    curr2 = 1
    while curr1 != key1:
        if curr1 != key1:
            curr1 *= subject
            curr1 = curr1 % 20201227
            loop1 += 1
    for i in range(loop1):
        curr2 *= key2
        curr2 = curr2 % 20201227
    return curr2

print(part1())