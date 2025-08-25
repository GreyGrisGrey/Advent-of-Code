from intCode import intMachine

def part1(fileName = "in.txt"):
    machine = intMachine(fileName = fileName)
    val = ""
    comDict = {"w":"west", "e":"east", "n":"north", "s":"south", "i":"inv"}
    res = [0, 0]
    out = ""
    while res[1] != ord("?"):
        res = machine.run()
        out += chr(res[1])
    print(out)
    while True:
        if val in comDict or val.split(" ")[0] == "take" or val.split(" ")[0] == "drop":
            print(val, "------")
            if val in comDict:
                val = comDict[val]
            for i in val:
                machine.addInput(ord(i))
            machine.addInput(10)
            res = [0, 0]
            out = ""
            prevs = [0, 0, 0]
            while prevs[2] != ord("?") or prevs[0] != ord("n") or prevs[1] != ord("d"):
                res = machine.run()
                if res[1] == None:
                    print(out)
                    return
                out += chr(res[1])
                prevs[0] = prevs[1]
                prevs[1] = prevs[2]
                prevs[2] = res[1]
            print(out)
        val = input()

if __name__ == "__main__":
    part1("in25.txt")