from intCode import intMachine

def partBoth():
    machines = {}
    flying = {}
    end = [0, 0]
    curr = None
    prev = None
    steps = 0
    for i in range(50):
        machines[i] = intMachine(23)
        machines[i].addInput(i)
    while True:
        flag = True
        steps += 1
        for i in range(50):
            res = machines[i].step()
            if res[0] == 0 and res[1] != None:
                flag = False
                if i in flying:
                    flying[i].append(res[1])
                    if len(flying[i]) == 3:
                        if flying[i][0] == 255 and end[0] == 0:
                            end[0] = flying[i][2]
                        if flying[i][0] == 255:
                            curr = [flying[i][1], flying[i][2]]
                        else:
                            machines[flying[i][0]].addInputs([flying[i][1], flying[i][2]])
                        del flying[i]
                else:
                    if (res[1] <= 49 and res[1] >= 0) or res[1] == 255:
                        flying[i] = [res[1]]
            elif res[0] != 0:
                print(res)
                return
        for i in range(50):
            if machines[i].retrieveInLen() != 0 or len(flying) != 0:
                flag = False
        if flag and curr != None:
            machines[0].addInputs(curr)
            if prev == curr[1]:
                end[1] = curr[1]
                return end
            prev = curr[1]
            curr = None

if __name__ == "__main__":
    res = partBoth()
    print("Part 1:", res[0])
    print("Part 2:", res[1])