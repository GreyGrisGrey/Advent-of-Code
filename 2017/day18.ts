import * as fs from "fs"

function runCommand(registers: Map<string, number>, currIndex: number, data: Array<string>, delivered: Array<number>): Array<number> {
    let instruct = data[currIndex].split(" ")
    let second = 0
    let send = 0
    if (!registers.has(instruct[1])) {
        registers.set(instruct[1], 0)
    }
    if (instruct.length == 3) {
        if (instruct[2].charCodeAt(0) < 58 && instruct[2].charCodeAt(0) > 44) {
            second = Number(instruct[2])
        } else if (registers.has(instruct[2])) {
            second = registers.get(instruct[2])!
        }
    } else if (instruct.length == 2) {
        if (instruct[1].charCodeAt(0) < 58 && instruct[1].charCodeAt(0) > 44) {
            send = Number(instruct[1])
        } else if (registers.has(instruct[1])) {
            send = registers.get(instruct[1])!
        }
    }
    if (instruct[0] == "snd") {
        return [currIndex + 1, send, 1]
    } else if (instruct[0] == "set") {
        registers.set(instruct[1], second)
    } else if (instruct[0] == "add") {
        registers.set(instruct[1], registers.get(instruct[1])! + second)
    } else if (instruct[0] == "mul") {
        registers.set(instruct[1], registers.get(instruct[1])! * second)
    } else if (instruct[0] == "mod") {
        registers.set(instruct[1], (registers.get(instruct[1])! + (second * 1000)) % second)
    } else if (instruct[0] == "rcv") {
        if (delivered.length != 0) {
            registers.set(instruct[1], delivered[0])
            return [currIndex + 1, 0, 3]
        } else {
            return [currIndex, 0, 2]
        }
    } else if (instruct[0] == "jgz") {
        if (instruct[1].charCodeAt(0) < 58 && instruct[1].charCodeAt(0) > 44) {
            let jump = Number(instruct[1])
            if (jump > 0) {
                currIndex += second - 1
            }
        } else if (registers.get(instruct[1])! > 0) {
            currIndex += second - 1
        }
    }
    currIndex++
    return [currIndex, 0, 0]
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let registers: Map<string, number> = new Map()
    let currIndex = 0
    let lastSound = 0
    let lastCheck = false
    while (currIndex < data.length && currIndex >= 0) {
        let instruct = data[currIndex].split(" ")
        let second = 0
        if (instruct.length == 3) {
            if (instruct[2].charCodeAt(0) < 58 && instruct[2].charCodeAt(0) > 44) {
                second = Number(instruct[2])
            } else if (registers.has(instruct[2])) {
                second = registers.get(instruct[2])!
            }
        }
        if (!registers.has(instruct[1])) {
            registers.set(instruct[1], 0)
        }
        if (instruct[0] == "snd") {
            lastCheck = true
            lastSound = registers.get(instruct[1])!
        } else if (instruct[0] == "set") {
            registers.set(instruct[1], second)
        } else if (instruct[0] == "add") {
            registers.set(instruct[1], registers.get(instruct[1])! + second)
        } else if (instruct[0] == "mul") {
            registers.set(instruct[1], registers.get(instruct[1])! * second)
        } else if (instruct[0] == "mod") {
            registers.set(instruct[1], (registers.get(instruct[1])! + (second * 1000)) % second)
        } else if (instruct[0] == "rcv") {
            if (lastCheck) {
                return lastSound
            }
        } else if (instruct[0] == "jgz") {
            if (registers.get(instruct[1])! > 0) {
                currIndex += second - 1
            }
        }
        currIndex++
    }
    return 1
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let registers1: Map<string, number> = new Map()
    let currIndex1 = 0
    let currHeld1: Array<number> = new Array()
    registers1.set("p", 0)
    let registers2: Map<string, number> = new Map()
    let currIndex2 = 0
    let currHeld2: Array<number> = new Array()
    registers2.set("p", 1)
    let currSent = 0
    let done: Array<boolean> = [false, false]
    while (true) {
        if (currIndex1 < 0 || currIndex1 >= data.length) {
            done[0] = true
        }
        if (currIndex2 < 0 || currIndex2 >= data.length) {
            done[1] = true
        }
        let res1: Array<number> = [-1, 0, 2]
        if (!done[0]) {
            let packet1: Array<number> = new Array()
            if (currHeld1.length != 0) {
                packet1.push(currHeld1[0])
            }
            res1 = runCommand(registers1, currIndex1, data, packet1)
        }
        let res2: Array<number> = [-1, 0, 2]
        if (!done[1]) {
            let packet2: Array<number> = new Array()
            if (currHeld2.length != 0) {
                packet2.push(currHeld2[0])
            }
            res2 = runCommand(registers2, currIndex2, data, packet2)
        }
        if (res1[2] === 2 && res2[2] === 2) {
            return currSent
        }
        if (res1[2] === 1) {
            currHeld2.push(res1[1])
        }
        if (res2[2] === 1) {
            currHeld1.push(res2[1])
            currSent++
        }
        if (res1[2] === 3) {
            currHeld1 = currHeld1.slice(1)
        }
        if (res2[2] === 3) {
            currHeld2 = currHeld2.slice(1)
        }
        currIndex1 = res1[0]
        currIndex2 = res2[0]
    }
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())