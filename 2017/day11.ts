import * as fs from "fs"

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split(",")
    let moves: Array<number> = [0, 0]
    for (let i = 0; i < data.length; i++) {
        if (data[i] == "s") {
            moves[1] -= 2
        } else if (data[i] == "n") {
            moves[1] += 2
        } else if (data[i] == "ne") {
            moves[0] += 1
            moves[1] += 1
        } else if (data[i] == "se") {
            moves[0] += 1
            moves[1] -= 1
        } else if (data[i] == "nw") {
            moves[0] -= 1
            moves[1] += 1
        } else if (data[i] == "sw") {
            moves[0] -= 1
            moves[1] -= 1
        }
    }
    let extra = Math.max(Math.floor((Math.abs(moves[1]) - Math.abs(moves[0])) / 2), 0)
    return Math.abs(moves[0]) + extra
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split(",")
    let moves: Array<number> = [0, 0]
    let maximum = 0
    for (let i = 0; i < data.length; i++) {
        if (data[i] == "s") {
            moves[1] -= 2
        } else if (data[i] == "n") {
            moves[1] += 2
        } else if (data[i] == "ne") {
            moves[0] += 1
            moves[1] += 1
        } else if (data[i] == "se") {
            moves[0] += 1
            moves[1] -= 1
        } else if (data[i] == "nw") {
            moves[0] -= 1
            moves[1] += 1
        } else if (data[i] == "sw") {
            moves[0] -= 1
            moves[1] -= 1
        }
        let extra = Math.max(Math.floor((Math.abs(moves[1]) - Math.abs(moves[0])) / 2), 0)
        if (Math.abs(moves[0]) + extra > maximum) {
            maximum = Math.abs(moves[0]) + extra
        }
    }
    return maximum
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())