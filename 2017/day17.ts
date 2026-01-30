import * as fs from "fs"

function part1(): number {
    let currIndex = 0
    let move = Number(fs.readFileSync("in.txt", "utf8"))
    let buffer: Array<number> = [0]
    for (let i = 1; i < 2018; i++) {
        currIndex = (currIndex + move) % buffer.length
        buffer.splice(currIndex + 1, 0, i)
        currIndex++
    }
    return buffer[(currIndex + 1) % buffer.length]
}

function part2a(): number {
    let move = Number(fs.readFileSync("in.txt", "utf8"))
    let currSize = 1
    let currIndex = 0
    let currNext = 0
    for (let i = 1; i < 50000001; i++) {
        currIndex = (currIndex + move) % currSize
        currSize++
        if (currIndex == 0) {
            currNext = i
        }
        currIndex++
    }
    return currNext
}

console.log("Part 1:", part1())
console.log("Part 2:", part2a())