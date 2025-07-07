import * as fs from "fs"

function moveStorm(storm: number, direction: string, maxX: number, maxY: number): number {
    let directionMapping = new Map([[">", 1], ["<", -1], ["v", 1000], ["^", -1000]])
    storm += directionMapping.get(direction)
    if (Math.round((storm % 1000000) / 1000) > maxY) {
        storm -= maxY * 1000
    } else if (Math.round((storm % 1000000) / 1000) <= 0) {
        storm += maxY * 1000
    } else if (storm % 500 == 0) {
        storm += maxX
    } else if (storm % 500 > maxX) {
        storm -= maxX
    }
    return storm
}

function moveAvail(curr: number, safe: Map<number, boolean>, options: Map<number, boolean>): void {
    let poss = [curr, curr + 1000, curr - 1000, curr + 1, curr - 1]
    for (let i = 0; i < 5; i++) {
        if (safe.has(poss[i]) && safe.get(poss[i])) {
            options.set(poss[i], true)
        }
    }
}

function cleanAvail(saved: number, avail: Map<number, boolean>): void {
    let ents = avail.entries(), steps = avail.size
    for (let i = 0; i < steps; i++) {
        let curr = ents.next().value[0]
        if (curr != saved) {
            avail.delete(curr)
        }
    }
}

function partBoth(): Array<number> {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), end: number, maxX = 0, maxY = 0, index = 1
    let mapping = new Map<number, boolean>, storms = new Map<number, string>, available = new Map<number, boolean>
    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data[i].length; j++) {
            if (data[i][j] != "#") {
                if (data[i][j] != ".") {
                    storms.set(i * 1000 + j + index * 1000000, data[i][j])
                    index += 1
                }
                mapping.set(i * 1000 + j, true)
            } else {
                if (i > maxY) {
                    maxY = i - 1
                }
                if (j > maxX) {
                    maxX = j - 1
                }
            }
            if (i == 0 && data[i][j] == ".") {
                available.set(i * 1000 + j, true)
            }
            if (i == data.length - 1 && data[i][j] == ".") {
                end = i * 1000 + j
            }
        }
    }
    let count = 0, steps = [0, 0, 0], flag1 = false, flag2 = false, clean = false
    while (true) {
        let ents = mapping.entries(), nextMap = new Map<number, boolean>
        for (let i = 0; i < mapping.size; i++) {
            let curr = ents.next().value
            nextMap.set(curr[0], true)
        }
        let stormEnts = storms.entries(), nextStorms = new Map<number, string>
        for (let i = 0; i < storms.size; i++) {
            let curr = stormEnts.next().value
            nextStorms.set(moveStorm(curr[0], curr[1], maxX, maxY), curr[1])
            nextMap.set(curr[0] % 1000000, false)
        }
        let availEnts = available.entries(), nextAvail = new Map<number, boolean>
        for (let i = 0; i < available.size; i++) {
            let curr = availEnts.next().value
            if (curr[0] == end && !flag1 && !flag2) {
                steps[0] = count - 1
                flag1 = true
                clean = true
            } else if (curr[0] == 1 && flag1 && !flag2) {
                steps[1] = count - 1 - steps[0]
                flag2 = true
                clean = true
            } else if (curr[0] == end && flag1 && flag2) {
                steps[2] = count - 1 - steps[0] - steps[1]
                return [steps[0], steps[0] + steps[1] + steps[2]]
            }
            moveAvail(curr[0], nextMap, nextAvail)
        }
        if (clean) {
            if (flag2) {
                cleanAvail(1, nextAvail)
            } else {
                cleanAvail(end, nextAvail)
            }
            clean = false
        }
        storms = nextStorms
        mapping = nextMap
        available = nextAvail
        count += 1
    }
}

console.log(partBoth())