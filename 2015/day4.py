# Works for part 2, to make it work for part 1 just remove " == result[13]" from line 8
import hashlib
string = open("input.txt").readline()
count = 0
while True:
    next = string + str(count)
    result = str(hashlib.md5(next.encode()).digest())
    if result[4] == result[5] == result[8] == result[9] == result[12] == result[13] == "0":
        break
    count += 1
print(count)