import * as fs from "fs"

function progressSand(sand, blocked, minimum, partTwo = false): boolean {
    let next = [sand[0] * 10000 + (sand[1] + 1), (sand[0] - 1) * 10000 + (sand[1] + 1), (sand[0] + 1) * 10000 + (sand[1] + 1)]
    if (!blocked.has(next[0])) {
        sand[1] += 1
    } else if (!blocked.has(next[1])) {
        sand[1] += 1
        sand[0] -= 1
    } else if (!blocked.has(next[2])) {
        sand[1] += 1
        sand[0] += 1
    } else {
        return false
    }
    if ((!partTwo && sand[1] == minimum) || (partTwo && sand[1] == minimum + 1)) {
        return false
    }
    return true
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), total = 0, blocked = new Map(), minY = 0
    for (let i = 0; i < data.length; i++) {
        let instruct = data[i].split(" -> "), curr = [0, 0]
        for (let j = 0; j < instruct.length; j++) {
            let step = instruct[j].split(",").map((val) => parseInt(val))
            if (curr[0] == 0) {
                curr[0] = step[0]
                curr[1] = step[1]
            }
            blocked.set(curr[0] * 10000 + curr[1], true)
            while (Math.abs(curr[0] - step[0]) > 0) {
                curr[0] += curr[0] > step[0] ? -1 : 1
                blocked.set(curr[0] * 10000 + curr[1], true)
            }
            while (Math.abs(curr[1] - step[1]) > 0) {
                curr[1] += curr[1] > step[1] ? -1 : 1
                blocked.set(curr[0] * 10000 + curr[1], true)
            }
            if (curr[1] > minY) {
                minY = curr[1]
            }
        }
    }
    while (true) {
        let sand = [500, 0], conflag = true
        while (conflag) {
            conflag = progressSand(sand, blocked, minY)
        }
        if (sand[1] != minY) {
            total += 1
            blocked.set(sand[0] * 10000 + sand[1], true)
        } else {
            return total
        }
    }
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), total = 0, blocked = new Map(), minY = 0
    for (let i = 0; i < data.length; i++) {
        let instruct = data[i].split(" -> "), curr = [0, 0]
        for (let j = 0; j < instruct.length; j++) {
            let step = instruct[j].split(",").map((val) => parseInt(val))
            if (curr[0] == 0) {
                curr[0] = step[0]
                curr[1] = step[1]
            }
            blocked.set(curr[0] * 10000 + curr[1], true)
            while (Math.abs(curr[0] - step[0]) > 0) {
                curr[0] += curr[0] > step[0] ? -1 : 1
                blocked.set(curr[0] * 10000 + curr[1], true)
            }
            while (Math.abs(curr[1] - step[1]) > 0) {
                curr[1] += curr[1] > step[1] ? -1 : 1
                blocked.set(curr[0] * 10000 + curr[1], true)
            }
            if (curr[1] > minY) {
                minY = curr[1]
            }
        }
    }
    for (let i = 0; i < (minY + 6) * 2; i++) {
        blocked.set((500 - (minY + 3) + i) * 10000 + (minY + 2), true)
    }
    while (true) {
        let sand = [500, 0], conflag = true
        while (conflag) {
            conflag = progressSand(sand, blocked, minY + 2)
        }
        total += 1
        if (sand[1] != 0) {
            blocked.set(sand[0] * 10000 + sand[1], true)
        } else if (sand[1] == 0) {
            return total
        }
    }
}


console.log(part1())
console.log(part2())