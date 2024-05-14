# The video explaining the problem was very interesting, but I was already in too deep with the brute force solution to stop

f = open("input.txt")
text = f.readline()
out = text
for i in range(50):
    print(i)
    text = out
    count = 0
    currNum = None
    out = ""
    for j in range(len(text)):
        if currNum == None:
            count = 1
            currNum = text[j]
        elif text[j] != currNum:
            out = out + str(count) + currNum
            count = 1
            currNum = text[j]
        else:
            count += 1
    out = out + str(count) + currNum
    if i == 39:
        print("Part 1 ", len(out))
print("Part2 ", len(out))