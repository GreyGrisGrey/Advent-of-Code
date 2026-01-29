import * as fs from "fs"

function checkMatch(num1: number, num2: number): boolean {
    let string1 = num1.toString(2).padStart(35, "0").slice(19)
    let string2 = num2.toString(2).padStart(35, "0").slice(19)
    if (string1 === string2) {
        return true
    }
    return false
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let num1 = Number(data[0].split(" ")[4])
    let num2 = Number(data[1].split(" ")[4])
    let total = 0
    for (let i = 0; i < 40000000; i++) {
        num1 = (num1 * 16807) % 2147483647
        num2 = (num2 * 48271) % 2147483647
        if (checkMatch(num1, num2)) {
            total++
        }
    }
    return total
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let num1 = Number(data[0].split(" ")[4])
    let num2 = Number(data[1].split(" ")[4])
    let total = 0
    for (let i = 0; i < 5000000; i++) {
        num1 = (num1 * 16807) % 2147483647
        num2 = (num2 * 48271) % 2147483647
        while (num1 % 4 != 0) {
            num1 = (num1 * 16807) % 2147483647
        }
        while (num2 % 8 != 0) {
            num2 = (num2 * 48271) % 2147483647
        }
        if (checkMatch(num1, num2)) {
            total++
        }
    }
    return total
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())