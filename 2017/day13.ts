import * as fs from "fs"

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\n")
    let layers: Array<number> = new Array()
    let depths: Array<number> = new Array()
    let scans: Array<number> = new Array()
    let directions: Array<boolean> = new Array()
    let maximum = 0
    let currLayer = 0
    let currWall = 0
    let res = 0
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(": ").map((num: string) => Number(num))
        layers.push(line[0])
        depths.push(line[1])
        scans.push(0)
        directions.push(true)
        maximum = line[0]
    }
    while (currLayer <= maximum) {
        if (currLayer == layers[currWall]) {
            if (scans[currWall] == 0) {
                res += depths[currWall] * layers[currWall]
            }
            currWall++
        }
        for (let i = 0; i < layers.length; i++) {
            if (directions[i]) {
                scans[i]++
            } else {
                scans[i]--
            }
            if (scans[i] == depths[i] - 1) {
                directions[i] = false
            } else if (scans[i] == 0) {
                directions[i] = true
            }
        }
        currLayer++
    }
    return res
}


function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\n")
    let layers: Array<number> = new Array()
    let depths: Array<number> = new Array()
    let scans: Array<number> = new Array()
    let directions: Array<boolean> = new Array()
    let packets: Array<Array<number>> = new Array()
    let maximum = 0
    let currTime = 0
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(": ").map((num: string) => Number(num))
        layers.push(line[0])
        depths.push(line[1])
        scans.push(0)
        directions.push(true)
        maximum = line[0]
    }
    while (true) {
        let newPacket: Array<number> = [currTime, 0, 0]
        let removed: Array<number> = new Array()
        packets.push(newPacket)
        for (let i = 0; i < packets.length; i++) {
            if (packets[i][1] > maximum) {
                return packets[i][0]
            }
            if (packets[i][1] == layers[packets[i][2]]) {
                if (scans[packets[i][2]] == 0) {
                    removed.push(i)
                }
                packets[i][2]++
            }
            packets[i][1]++
        }
        for (let i = 0; i < layers.length; i++) {
            if (directions[i]) {
                scans[i]++
            } else {
                scans[i]--
            }
            if (scans[i] == depths[i] - 1) {
                directions[i] = false
            } else if (scans[i] == 0) {
                directions[i] = true
            }
        }
        removed.reverse()
        for (let i = 0; i < removed.length; i++) {
            packets.splice(removed[i], 1)
        }
        currTime++
    }
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())