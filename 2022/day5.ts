import * as fs from "fs";
function shuffle(A, B, count, first): void {
    let start = (A.length - count)
    for (let i = 0; i < count; i++) {
        if (first) {
            B.push(A[start + (count - i) - 1])
        } else {
            B.push(A[start + i])
        }
    }
    A.splice(start, count)
    return
}


function part1(): string {
    let a = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let index = 0
    let stacks = Array()
    while (a[index][1] != "1") {
        let index2 = 1
        while (index2 < a[index].length) {
            if (stacks.length <= Math.floor((index2 - 1) / 4)) {
                stacks.push(Array())
            }
            if (a[index][index2] != " ") {
                stacks[Math.floor((index2 - 1) / 4)].push(a[index][index2])
            }
            index2 += 4
        }
        index += 1
    }
    index += 2
    for (let i in stacks) {
        stacks[i].reverse()
    }
    while (index < a.length) {
        let command = a[index].split(" ")
        shuffle(stacks[parseInt(command[3]) - 1], stacks[parseInt(command[5]) - 1], parseInt(command[1]), true)
        index += 1
    }
    let out = ""
    for (let i in stacks) {
        out = out.concat(stacks[i][stacks[i].length - 1])
    }
    return out
}


function part2(): string {
    let a = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let index = 0
    let stacks = Array()
    while (a[index][1] != "1") {
        let index2 = 1
        while (index2 < a[index].length) {
            if (stacks.length <= Math.floor((index2 - 1) / 4)) {
                stacks.push(Array())
            }
            if (a[index][index2] != " ") {
                stacks[Math.floor((index2 - 1) / 4)].push(a[index][index2])
            }
            index2 += 4
        }
        index += 1
    }
    index += 2
    for (let i in stacks) {
        stacks[i].reverse()
    }
    while (index < a.length) {
        let command = a[index].split(" ")
        shuffle(stacks[parseInt(command[3]) - 1], stacks[parseInt(command[5]) - 1], parseInt(command[1]), false)
        index += 1
    }
    let out = ""
    for (let i in stacks) {
        out = out.concat(stacks[i][stacks[i].length - 1])
    }
    return out
}

console.log(part1())
console.log(part2())