import * as fs from "fs";
function moveTail(currHead, currTail, map, num = -1): void {
    if (num == -1 || num == 9) {
        map.set(currTail[0].toString().concat(":", currTail[1].toString()), true)
    }
    let dist = Math.abs(currHead[0] - currTail[0]) + Math.abs(currHead[1] - currTail[1])
    if (dist >= 3 || Math.abs(currHead[0] - currTail[0]) > 1 || Math.abs(currHead[1] - currTail[1]) > 1) {
        currTail[0] += (currHead[0] - currTail[0]) > 0 ? 1 : 0
        currTail[0] -= (currHead[0] - currTail[0]) < 0 ? 1 : 0
        currTail[1] += (currHead[1] - currTail[1]) > 0 ? 1 : 0
        currTail[1] -= (currHead[1] - currTail[1]) < 0 ? 1 : 0
        return
    }
    return
}

function part1(): number {
    let currHead = [0, 0], currTail = [0, 0], map = new Map(), a = fs.readFileSync("in.txt", "utf8").split("\r\n")
    for (let i = 0; i < a.length; i++) {
        let steps = [a[i].split(" ")[0], parseInt(a[i].split(" ")[1])]
        while (steps[1] > 0) {
            steps[1] -= 1
            currHead[0] += (steps[0] == "R") ? 1 : 0
            currHead[0] -= (steps[0] == "L") ? 1 : 0
            currHead[1] += (steps[0] == "D") ? 1 : 0
            currHead[1] -= (steps[0] == "U") ? 1 : 0
            moveTail(currHead, currTail, map)
        }
    }
    map.set(currTail[0].toString().concat(":", currTail[1].toString()), true)
    return map.size
}

function part2(): number {
    let currHead = [0, 0], currTails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], map = new Map(), a = fs.readFileSync("in.txt", "utf8").split("\r\n")
    for (let i = 0; i < a.length; i++) {
        let steps = [a[i].split(" ")[0], parseInt(a[i].split(" ")[1])]
        while (steps[1] > 0) {
            steps[1] -= 1
            currHead[0] += (steps[0] == "R") ? 1 : 0
            currHead[0] -= (steps[0] == "L") ? 1 : 0
            currHead[1] += (steps[0] == "D") ? 1 : 0
            currHead[1] -= (steps[0] == "U") ? 1 : 0
            moveTail(currHead, currTails[0], map, 1)
            for (let j = 0; j < 8; j++) {
                moveTail(currTails[j], currTails[j + 1], map, j + 2)
            }
        }
    }
    map.set(currTails[8][0].toString().concat(":", currTails[8][1].toString()), true)
    return map.size
}

console.log(part1())
console.log(part2())