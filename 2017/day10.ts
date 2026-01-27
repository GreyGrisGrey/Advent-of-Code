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

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split(",").map((item: string) => Number(item))
    let skip = 0
    let curr = 0
    let numList: Array<number> = new Array()
    for (let i = 0; i < 256; i++) {
        numList.push(i)
    }
    
    for (let i = 0; i < data.length; i++) {
        reverseSection(numList, curr, data[i] - 1)
        curr = (curr + skip + data[i]) % numList.length
        skip++
    }
    return numList[0] * numList[1]
}

function part2(): string {
    let data = fs.readFileSync("in.txt", "utf8").split("").map((input:string) => Number(input.charCodeAt(0))).concat([17,31,73,47,23])
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

console.log("Part 1:", part1())
console.log("Part 2:", part2())