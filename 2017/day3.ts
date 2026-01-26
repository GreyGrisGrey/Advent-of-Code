import * as fs from "fs";

function part1(): number {
    let goal = Number(fs.readFileSync("in.txt"))
    let curr = 1
    let distance = 0
    while (curr * curr <= goal) {
        curr += 2
        distance += 1
    }
    curr -= 2
    let minimum = 9999
    for (let i = 0; i < 4; i++){
        let res = Math.abs(goal - (curr * curr + distance + distance * 2 * i))
        if (res < minimum) {
            minimum = res
        }
    }
    return distance + minimum
}

function part2(): number {
    let goal = Number(fs.readFileSync("in.txt"))
    let numMap: Map<number, number> = new Map()
    let curr: Array<number> = [0, 0]
    let prev = 0
    let direction = "R"
    let maximum = 1
    while (prev <= goal) {
        let addTotal = 0
        if (prev == 0) {
            addTotal = 1
        }
        for (let i = -1; i < 2; i++) {
            for (let j = -1; j < 2; j++) {
                if ((i != j || i != 0) && numMap.get((i + curr[0]) * 10000 + j + curr[1]) != undefined) {
                    addTotal += numMap.get((i + curr[0]) * 10000 + j + curr[1])!
                }
            }
        }
        prev = addTotal
        numMap.set(curr[0] * 10000 + curr[1], addTotal)
        if (direction == "R") {
            curr[0] += 1
            if (curr[0] == maximum) {
                direction = "U"
            }
        } else if (direction == "U") {
            curr[1] += 1
            if (curr[1] == maximum) {
                direction = "L"
            }
        } else if (direction == "L") {
            curr[0] -= 1
            if (curr[0] == -maximum) {
                direction = "D"
            }
        } else if (direction == "D") {
            curr[1] -= 1
            if (curr[1] == -maximum) {
                direction = "R"
                maximum += 1
            }
        }
    }
    return prev
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())