import * as fs from "fs"

function genFaces(nums): Array<string> {
    let strings = new Array<string>
    strings.push((nums[0] - 0.5).toString().concat("X", nums[1].toString(), "Y", nums[2].toString(), "Z"))
    strings.push((nums[0] + 0.5).toString().concat("X", nums[1].toString(), "Y", nums[2].toString(), "Z"))
    strings.push((nums[0]).toString().concat("X", (nums[1] - 0.5).toString(), "Y", nums[2].toString(), "Z"))
    strings.push((nums[0]).toString().concat("X", (nums[1] + 0.5).toString(), "Y", nums[2].toString(), "Z"))
    strings.push((nums[0]).toString().concat("X", nums[1].toString(), "Y", (nums[2] - 0.5).toString(), "Z"))
    strings.push((nums[0]).toString().concat("X", nums[1].toString(), "Y", (nums[2] + 0.5).toString(), "Z"))
    return strings
}

function nextCubes(nums): Array<string> {
    let strings = new Array<string>
    strings.push((nums[0] - 1).toString().concat(",", (nums[1]).toString(), ",", (nums[2]).toString()))
    strings.push((nums[0] + 1).toString().concat(",", (nums[1]).toString(), ",", (nums[2]).toString()))
    strings.push((nums[0]).toString().concat(",", (nums[1] - 1).toString(), ",", (nums[2]).toString()))
    strings.push((nums[0]).toString().concat(",", (nums[1] + 1).toString(), ",", (nums[2]).toString()))
    strings.push((nums[0]).toString().concat(",", (nums[1]).toString(), ",", (nums[2] - 1).toString()))
    strings.push((nums[0]).toString().concat(",", (nums[1]).toString(), ",", (nums[2] + 1).toString()))
    return strings
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), faceMap = new Map(), total = 0
    for (let i = 0; i < data.length; i++) {
        let vals = data[i].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])]
        let strings = genFaces(nums)
        for (let j = 0; j < strings.length; j++) {
            if (faceMap.has(strings[j])) {
                total -= 1
            } else {
                faceMap.set(strings[j], true)
                total += 1
            }
        }
    }
    return total
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), faceMap = new Map(), total = 0, closed = new Map<string, boolean>
    for (let i = 0; i < data.length; i++) {
        let vals = data[i].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])]
        let strings = genFaces(nums)
        closed.set(data[i], true)
        for (let j = 0; j < strings.length; j++) {
            faceMap.set(strings[j], true)
        }
    }
    let searchers = ["30,30,30"]
    while (searchers.length != 0) {
        let vals = searchers[0].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])]
        if (!closed.has(searchers[0]) && nums[0] > -2 && nums[1] > -2 && nums[2] > -2 && nums[0] < 31 && nums[1] < 31 && nums[2] < 31) {
            let options = genFaces(nums), newSearch = nextCubes(nums)
            for (let j = 0; j < options.length; j++) {
                if (faceMap.has(options[j])) {
                    total += 1
                }
                if (!closed.has(newSearch[j])) {
                    searchers.push(newSearch[j])
                }
            }
        }
        closed.set(searchers[0], true)
        searchers = searchers.slice(1, searchers.length)
    }
    return total
}

console.log(part1())
console.log(part2())