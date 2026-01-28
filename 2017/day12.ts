import * as fs from "fs"

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let connections: Array<Array<number>> = new Array()
    let openIndices: Array<number> = [0]
    let doneIndices: Map<number, boolean> = new Map()
    let currIndex = 0
    let curr = 0
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" <-> ")
        connections.push(line[1].split(", ").map((newNum: string) => Number(newNum)))
    }
    
    while (true) {
        for (let i = 0; i < connections[curr].length; i++) {
            if (!doneIndices.has(connections[curr][i])) {
                doneIndices.set(connections[curr][i], true)
                openIndices.push(connections[curr][i])
            }
        }
        currIndex++
        if (currIndex == openIndices.length) {
            return doneIndices.size
        }
        curr = openIndices[currIndex]
    }
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let connections: Array<Array<number>> = new Array()
    let doneIndices: Map<number, boolean> = new Map()
    let groupCount = 0
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" <-> ")
        connections.push(line[1].split(", ").map((newNum: string) => Number(newNum)))
    }
    
    for (let i = 0; i < data.length; i++) {
        if (!doneIndices.has(i)) {
            let currIndex = 0
            let curr = i
            let openIndices: Array<number> = [curr]
            while (true) {
                for (let i = 0; i < connections[curr].length; i++) {
                    if (!doneIndices.has(connections[curr][i])) {
                        doneIndices.set(connections[curr][i], true)
                        openIndices.push(connections[curr][i])
                    }
                }
                currIndex++
                if (currIndex == openIndices.length) {
                    break
                }
                curr = openIndices[currIndex]
            }
            groupCount += 1
        }
    }
    return groupCount
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())