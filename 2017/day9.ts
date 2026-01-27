import * as fs from "fs"

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8")
    let inGarbage = false
    let openGroup = 0
    let total = 0
    for (let i = 0; i < data.length; i++) {
        if (data[i] === "<") {
            inGarbage = true
        } else if (data[i] === ">") {
            inGarbage = false
        } else if (data[i] === "!") {
            i++
        } else if (data[i] === "{" && !inGarbage) {
            openGroup++
        } else if (data[i] === "}" && !inGarbage) {
            total += openGroup
            openGroup--
        }
    }
    return total
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8")
    let inGarbage = false
    let total = 0
    for (let i = 0; i < data.length; i++) {
        if (data[i] === "<" && !inGarbage) {
            inGarbage = true
        } else if (data[i] === ">") {
            inGarbage = false
        } else if (data[i] === "!") {
            i++
        } else if (inGarbage) {
            total++
        }
    }
    return total
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())