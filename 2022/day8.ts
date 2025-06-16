import * as fs from "fs";
function scan(direction, start, map, end): void {
    let curr = -1
    if (direction == "D") {
        while (start[1] < end) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] > curr) {
                map.set(start[0].toString().concat(":", start[1].toString()), [true, map.get(start[0].toString().concat(":", start[1].toString()))[1]])
                curr = map.get(start[0].toString().concat(":", start[1].toString()))[1]
            }
            start[1] += 1
        }
    } else if (direction == "U") {
        while (start[1] >= end) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] > curr) {
                map.set(start[0].toString().concat(":", start[1].toString()), [true, map.get(start[0].toString().concat(":", start[1].toString()))[1]])
                curr = map.get(start[0].toString().concat(":", start[1].toString()))[1]
            }
            start[1] -= 1
        }
    } else if (direction == "R") {
        while (start[0] < end) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] > curr) {
                map.set(start[0].toString().concat(":", start[1].toString()), [true, map.get(start[0].toString().concat(":", start[1].toString()))[1]])
                curr = map.get(start[0].toString().concat(":", start[1].toString()))[1]
            }
            start[0] += 1
        }
    } else if (direction == "L") {
        while (start[0] >= end) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] > curr) {
                map.set(start[0].toString().concat(":", start[1].toString()), [true, map.get(start[0].toString().concat(":", start[1].toString()))[1]])
                curr = map.get(start[0].toString().concat(":", start[1].toString()))[1]
            }
            start[0] -= 1
        }
    }
    return
}

function scan2(direction, start, end, num, map): number {
    let curr = num, count = 0, scan = true
    if (direction == "D") {
        while ((start[1] < end) && scan) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] >= curr) {
                scan = false
            }
            count += 1
            start[1] += 1
        }
    } else if (direction == "U") {
        while (start[1] >= end && scan) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] >= curr) {
                scan = false
            }
            count += 1
            start[1] -= 1
        }
    } else if (direction == "R") {
        while (start[0] < end && scan) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] >= curr) {
                scan = false
            }
            count += 1
            start[0] += 1
        }
    } else if (direction == "L") {
        while (start[0] >= end && scan) {
            if (map.get(start[0].toString().concat(":", start[1].toString()))[1] >= curr) {
                scan = false
            }
            count += 1
            start[0] -= 1
        }
    }
    return count
}

function part1(): number {
    let a = fs.readFileSync("in.txt", "utf8").split("\r\n"), map = new Map(), count = 0
    for (let i = 0; i < a[0].length; i++) {
        for (let j = 0; j < a.length; j++) {
            map.set(i.toString().concat(":", j.toString()), [false, parseInt(a[j][i])])
        }
    }
    for (let i = 0; i < a[0].length; i++) {
        scan("D", [i, 0], map, a.length)
        scan("U", [i, a.length - 1], map, 0)
    }
    for (let i = 0; i < a.length; i++) {
        scan("R", [0, i], map, a[0].length)
        scan("L", [a[0].length - 1, i], map, 0)
    }
    let vals = map.values()
    for (let i = 0; i < map.size; i++) {
        let nextVal = vals.next().value[0]
        if (nextVal) {
            count += 1
        }
    }
    return count
}

function part2(): number {
    let a = fs.readFileSync("in.txt", "utf8").split("\r\n"), map = new Map(), best = 0
    for (let i = 0; i < a[0].length; i++) {
        for (let j = 0; j < a.length; j++) {
            map.set(i.toString().concat(":", j.toString()), [false, parseInt(a[j][i])])
        }
    }
    for (let i = 0; i < a[0].length; i++) {
        for (let j = 0; j < a.length; j++) {
            let num1 = scan2("D", [i, j + 1], a.length, map.get(i.toString().concat(":", j.toString()))[1], map)
            let num2 = scan2("U", [i, j - 1], 0, map.get(i.toString().concat(":", j.toString()))[1], map)
            let num3 = scan2("R", [i + 1, j], a[0].length, map.get(i.toString().concat(":", j.toString()))[1], map)
            let num4 = scan2("L", [i - 1, j], 0, map.get(i.toString().concat(":", j.toString()))[1], map)
            if (best <= (num1 * num2 * num3 * num4)) {
                best = (num1 * num2 * num3 * num4)
            }
        }
    }
    return best
}


console.log(part1())
console.log(part2())