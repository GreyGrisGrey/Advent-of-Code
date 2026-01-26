import * as fs from "fs";

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n").map((num: string) => Number(num))
    let bounds = [0, data.length - 1]
    let curr = 0
    let steps = 0
    while (curr >= bounds[0] && curr <= bounds[1]) {
        let moveNum = data[curr]
        data[curr]++
        curr += moveNum
        steps++
    }
    return steps
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n").map((num: string) => Number(num))
    let bounds = [0, data.length - 1]
    let curr = 0
    let steps = 0
    while (curr >= bounds[0] && curr <= bounds[1]) {
        let moveNum = data[curr]
        if (data[curr] >= 3) {
            data[curr]--
        } else {
            data[curr]++
        }
        curr += moveNum
        steps++
    }
    return steps
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())