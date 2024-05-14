f = open("input.txt")
line = f.readline()
searchString = "-1234567890"
addString = ""
summation = 0
for i in range(len(line)):
    if line[i] in searchString:
        addString = addString + line[i]
    elif len(addString) > 0:
        summation += int(addString)
        addString = ""
print(summation)