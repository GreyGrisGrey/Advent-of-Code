import * as fs from "fs"

function checkCond(regMap: Map<string, number>, line: Array<string>): boolean {
    let checkNum = Number(line[6])
    let currNum = regMap.get(line[4])!
    if (line[5] == ">=" && currNum >= checkNum) {
        return true
    } if (line[5] == "!=" && currNum != checkNum) {
        return true
    } if (line[5] == "<" && currNum < checkNum) {
        return true
    } if (line[5] == ">" && currNum > checkNum) {
        return true
    } if (line[5] == "==" && currNum === checkNum) {
        return true
    } if (line[5] == "<=" && currNum <= checkNum) {
        return true
    }
    return false
}

function part1(): number {
    let regMap: Map<string, number> = new Map()
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" ")
        if (!regMap.has(line[0])) {
            regMap.set(line[0], 0)
        }
        if (!regMap.has(line[4])) {
            regMap.set(line[4], 0)
        }
        if (checkCond(regMap, line)) {
            if (line[1] == "inc") {
                regMap.set(line[0], regMap.get(line[0])! + Number(line[2]))
            } else {
                regMap.set(line[0], regMap.get(line[0])! - Number(line[2]))
            }
        }
    }
    let iter = regMap.entries()
    let curr = iter.next()
    let maximum = 0
    while (!curr.done) {
        if (curr.value[1] > maximum) {
            maximum = curr.value[1]
        }
        curr = iter.next()
    }
    return maximum
}

function part2(): number {
    let regMap: Map<string, number> = new Map()
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let maximum = 0
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" ")
        if (!regMap.has(line[0])) {
            regMap.set(line[0], 0)
        }
        if (!regMap.has(line[4])) {
            regMap.set(line[4], 0)
        }
        if (checkCond(regMap, line)) {
            if (line[1] == "inc") {
                let newNum = regMap.get(line[0])! + Number(line[2])
                regMap.set(line[0], newNum)
                if (newNum > maximum) {
                    maximum = newNum
                }
            } else {
                let newNum = regMap.get(line[0])! - Number(line[2])
                regMap.set(line[0], newNum)
                if (newNum > maximum) {
                    maximum = newNum
                }
            }
        }
    }
    return maximum
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())