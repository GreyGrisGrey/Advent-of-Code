import * as fs from "fs"

function reverseSection(numList: Array<number>, start: number, length:number): void {
    let currFront = start
    let currBack = start + length
    for (let i = 0; i < Math.floor((length + 1)/2); i++) {
        let temp = numList[(currFront + i) % numList.length]
        numList[(currFront + i) % numList.length] = numList[(currBack - i + 256) % numList.length]
        numList[(currBack - i + 256) % numList.length] = temp
    }
    return
}

function knot(input: string) : string {
    let data = input.split("").map((input:string) => Number(input.charCodeAt(0))).concat([17,31,73,47,23])
    let skip = 0
    let curr = 0
    let numList: Array<number> = new Array()
    let hexString = ""
    for (let i = 0; i < 256; i++) {
        numList.push(i)
    }
    
    for (let i = 0; i < 64; i++) {
        for (let i = 0; i < data.length; i++) {
            reverseSection(numList, curr, data[i] - 1)
            curr = (curr + skip + data[i]) % numList.length
            skip++
        }
    }
    
    for (let i = 0; i < 16; i++) {
        let currNum = 0
        for (let j = 0; j < 16; j++) {
            currNum = currNum ^ numList[i * 16 + j]
        }
        let newString = currNum.toString(16)
        if (newString.length == 1) {
            hexString += "0"
        }
        hexString += newString
    }
    return hexString
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8")
    let total = 0
    for (let i = 0; i < 128; i++) {
        let res = knot(data + "-" + i.toString())
        for (let j = 0; j < res.length; j++) {
            let digit = Number("0x" + res[j]).toString(2)
            for (let k = 0; k < digit.length; k++) {
                if (digit[k] == "1") {
                    total += 1
                }
            }
        }
    }
    return total
}

function BFS(currNum: number, startSpace: number, mapping: Map<number, number>): void {
    let options: Array<number> = [startSpace]
    let moves: Array<number> = [1, -1, 1000, -1000]
    let currIndex = 0
    while (currIndex < options.length) {
        let currSpace = options[currIndex]
        for (let i = 0; i < moves.length; i++) {
            if (mapping.has(currSpace + moves[i]) && mapping.get(currSpace + moves[i]) == 0) {
                mapping.set(currSpace + moves[i], currNum)
                options.push(currSpace + moves[i])
            }
        }
        currIndex++
    }
    return
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8")
    let mapping: Map<number, number> = new Map()
    let regions = 0
    for (let i = 0; i < 128; i++) {
        let res = knot(data + "-" + i.toString())
        for (let j = 0; j < res.length; j++) {
            let digit = Number("0x" + res[j]).toString(2).padStart(4, "0")
            for (let k = 0; k < digit.length; k++) {
                if (digit[k] == "1") {
                    mapping.set(i * 1000 + k + j * 4, 0)
                } else {
                    mapping.set(i * 1000 + k + j * 4, -1)
                }
            }
        }
    }
    for (let i = 0; i < 128; i++) {
        for (let j = 0; j < 128; j++) {
            if (mapping.get(i * 1000 + j) == 0) {
                regions++
                BFS(regions, i * 1000 + j, mapping)
            }
        }
    }
    return regions
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())