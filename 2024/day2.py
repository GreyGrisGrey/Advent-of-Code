def part1():
    f = open("input.txt", "r")
    safe = 0
    for i in f:
        line = i.split(" ")
        upper = None
        unsafe = False
        if len(line) < 2:
            safe += 1
        for j in range(len(line)-1):
            if upper == None and int(line[j]) > int(line[j+1]):
                upper = False
            elif upper == None and int(line[j]) < int(line[j+1]):
                upper = True
            if abs(int(line[j]) - int(line[j+1])) >= 1 and abs(int(line[j]) - int(line[j+1])) <= 3:
                if upper and int(line[j]) > int(line[j+1]):
                    unsafe = True
                    break
                if not upper and int(line[j]) < int(line[j+1]):
                    unsafe = True
                    break
            else:
                unsafe = True
                break
        if not unsafe:
            safe += 1
    print(safe)

def part2():
    f = open("input.txt", "r")
    safe = 0
    for i in f:
        newLine = i.split(" ")
        done = False
        for k in range(len(newLine)):
            line = []
            for m in range(len(newLine)):
                line.append(newLine[m])
            del line[k]
            if not done:
                upper = None
                unsafe = False
                unsafe2 = False
                if len(line) < 2:
                    safe += 1
                for j in range(len(line)-1):
                    if upper == None and int(line[j]) > int(line[j+1]):
                        upper = False
                    elif upper == None and int(line[j]) < int(line[j+1]):
                        upper = True
                    if abs(int(line[j]) - int(line[j+1])) >= 1 and abs(int(line[j]) - int(line[j+1])) <= 3:
                        if upper and int(line[j]) > int(line[j+1]):
                            unsafe = True
                            break
                        if not upper and int(line[j]) < int(line[j+1]):
                            unsafe = True
                            break
                    else:
                        unsafe = True
                        break
                if not unsafe:
                    safe += 1
                    done = True
    print(safe)

part1()
part2()