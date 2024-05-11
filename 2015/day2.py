f = open("input.txt", "r")
totalPaper = 0
totalRibbon = 0
for i in f:
    lengths = i.split("x")
    for j in range(3):
        lengths[j] = int(lengths[j])
    totalPaper += 2*((lengths[0]*lengths[1]) + (lengths[0]*lengths[2]) + (lengths[1]*lengths[2]))
    totalPaper += min(lengths[0]*lengths[1], lengths[0]*lengths[2], lengths[1]*lengths[2])
    totalRibbon += lengths[0]*lengths[1]*lengths[2]
    totalRibbon += 2*min(lengths[0]+lengths[1], lengths[0]+lengths[2], lengths[1]+lengths[2])
print(totalPaper, totalRibbon)