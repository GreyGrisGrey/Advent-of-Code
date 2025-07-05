import * as fs from "fs"

class Monkey {
    operation: string
    val: number
    left: string
    right: string
    done: boolean

    constructor(first: string, second: string, third: string) {
        if (first == "VAL") {
            this.val = parseInt(second)
            this.done = true
        } else {
            this.left = first
            this.operation = second
            this.right = third
            this.done = false
        }
    }

    checkDone(): boolean {
        return this.done
    }

    getVal(): number {
        return this.val
    }

    setVal(newNum: number): void {
        this.val = newNum
        this.done = true
    }

    getOp(): string {
        return this.operation
    }

    getPrevs(): Array<string> {
        return [this.left, this.right]
    }
}

function generate(file: string, humn = -1): Map<string, Monkey> {
    let data = fs.readFileSync(file, "utf8").split("\r\n"), nameMap = new Map<string, Monkey>
    for (let i = 0; i < data.length; i++) {
        let curr = data[i].split(" "), key = curr[0].slice(0, 4), newMonk: Monkey
        if (curr.length == 2) {
            if (humn != -1 && key == "humn") {
                newMonk = new Monkey("VAL", humn.toString(), "a")
            } else {
                newMonk = new Monkey("VAL", curr[1], "a")
            }
            nameMap.set(key, newMonk)
        } else {
            newMonk = new Monkey(curr[1], curr[2], curr[3])
            nameMap.set(key, newMonk)
        }
    }
    return nameMap
}

function recurse(curr: string, nameMap: Map<string, Monkey>): number {
    let currMonk = nameMap.get(curr)
    if (currMonk.checkDone()) {
        return currMonk.getVal()
    }
    let prevs = currMonk.getPrevs(), val = [recurse(prevs[0], nameMap), recurse(prevs[1], nameMap)], newVal: number
    if (currMonk.getOp() == "*") {
        newVal = val[0] * val[1]
    } else if (currMonk.getOp() == "+") {
        newVal = val[0] + val[1]
    } else if (currMonk.getOp() == "/") {
        newVal = val[0] / val[1]
    } else if (currMonk.getOp() == "-") {
        newVal = val[0] - val[1]
    }
    currMonk.setVal(newVal)
    return newVal
}

function partBoth(): Array<number> {
    let results = new Array<number>
    for (let i = 0; i < 2; i++) {
        let newMap = generate("in.txt", i), prevs = newMap.get("root").getPrevs(), val = [recurse(prevs[0], newMap), recurse(prevs[1], newMap)]
        results.push(val[0])
        results.push(val[1])
    }
    return [recurse("root", generate("in.txt")), (results[0] - results[1]) / (results[0] - results[2])]
}


console.log(partBoth())