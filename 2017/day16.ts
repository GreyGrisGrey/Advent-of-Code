import * as fs from "fs"

function part1(input: string = "none"): string {
    let data = fs.readFileSync("in.txt", "utf8").split(",")
    let pairs: Array<Array<number>> = new Array()
    let order: Array<number> = new Array()
    if (input == "none") {
        for (let i = 0; i < 16; i++) {
            pairs.push([i, i])
            order.push(-1)
        }
    } else {
        for (let i = 0; i < 16; i++) {
            pairs.push([input.charCodeAt(i) - 97, i])
            order.push(-1)
        }
    }
    for (let i = 0; i < data.length; i++) {
        if (data[i][0] === "p") {
            let num1 = -1
            let num2 = -1
            for (let j = 0; j < 16; j++) {
                if (pairs[j][0] === data[i].charCodeAt(1) - 97) {
                    num1 = j
                } if (pairs[j][0] === data[i].charCodeAt(3) - 97) {
                    num2 = j
                }
            }
            let temp = pairs[num1][1]
            pairs[num1][1] = pairs[num2][1]
            pairs[num2][1] = temp
        } else if (data[i][0] === "x") {
            let line = data[i].slice(1).split("/").map((num : string) => Number(num))
            let num1 = -1
            let num2 = -1
            for (let j = 0; j < 16; j++) {
                if (pairs[j][1] === line[0]) {
                    num1 = j
                } if (pairs[j][1] === line[1]) {
                    num2 = j
                }
            }
            let temp = pairs[num1][0]
            pairs[num1][0] = pairs[num2][0]
            pairs[num2][0] = temp
        } else {
            for (let j = 0; j < 16; j++) {
                pairs[j][1] = (pairs[j][1] + Number(data[i].slice(1))) % 16
            }
        }
    }
    let endString = ""
    for (let i = 0; i < 16; i++) {
        order[pairs[i][1]] = pairs[i][0]
    }
    for (let i = 0; i < 16; i++) {
        endString += String.fromCharCode(order[i] + 97)
    }
    return endString
}

function part2(): string {
    let curr = "abcdefghijklmnop"
    let repeats: Map<string, number> = new Map()
    let hasRepeat: Map<string, boolean> = new Map()
    let steps = 0
    let remaining = 1000000000
    while (remaining > 0) {
        if (repeats.has(curr) && !hasRepeat.has(curr)) {
            hasRepeat.set(curr, true)
            repeats.set(curr, steps - repeats.get(curr)!)
        }
        if (!repeats.has(curr)) {
            repeats.set(curr, steps)
        }
        if (repeats.has(curr) && hasRepeat.has(curr) && repeats.get(curr)! < remaining) {
            remaining -= repeats.get(curr)!
        } else {
            curr = part1(curr)
            remaining--
            steps++
        }
    }
    return curr
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())