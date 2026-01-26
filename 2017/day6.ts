import * as fs from "fs";

function arrangementToString(arrangement: Array<number>): string {
    return arrangement.map((num: number) => num.toString()).join("-")
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\t").map((num: string) => Number(num))
    let arrangementMap: Map<string, boolean> = new Map()
    let steps = 0
    while (true) {
        let newArrange = arrangementToString(data)
        if (arrangementMap.has(newArrange)) {
            return steps
        }
        steps += 1
        arrangementMap.set(newArrange, true)
        let maxBank = [0, -1]
        for (let i = 0; i < data.length; i++) {
            if (data[i] > maxBank[0]) {
                maxBank = [data[i], i]
            }
        }
        data[maxBank[1]] = 0
        for (let i = 0; i < data.length; i++) {
            data[i] += Math.floor(maxBank[0] / data.length)
            if ((i - maxBank[1] + data.length) % data.length <= maxBank[0] % data.length && maxBank[1] != i) {
                data[i] += 1
            }
        }
    }
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\t").map((num: string) => Number(num))
    let arrangementMap: Map<string, boolean> = new Map()
    let steps = 0
    let goalArrange: string = ""
    while (true) {
        let newArrange = arrangementToString(data)
        if (arrangementMap.has(newArrange) && goalArrange === "") {
            goalArrange = newArrange
            steps = 0
        } else if (newArrange === goalArrange) {
            return steps
        }
        steps += 1
        arrangementMap.set(newArrange, true)
        let maxBank = [0, -1]
        for (let i = 0; i < data.length; i++) {
            if (data[i] > maxBank[0]) {
                maxBank = [data[i], i]
            }
        }
        data[maxBank[1]] = 0
        for (let i = 0; i < data.length; i++) {
            data[i] += Math.floor(maxBank[0] / data.length)
            if ((i - maxBank[1] + data.length) % data.length <= maxBank[0] % data.length && maxBank[1] != i) {
                data[i] += 1
            }
        }
    }
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())