import * as fs from "fs"
function convertBlockLine(line, step): Array<Array<number>> {
    let newLine = new Array(), newStep = 0
    for (let i = 0; i < line.length; i++) {
        if (line[i] == "#") {
            newLine.push([newStep, step])
        }
        newStep += 1
    }
    return newLine
}

function genBlock(height, step, blocks): Array<Array<number>> {
    let newBlock = new Array()
    for (let i = 0; i < blocks[step].length; i++) {
        for (let j = 0; j < blocks[step][i].length; j++) {
            newBlock.push([blocks[step][i][j][0] + 2, blocks[step][i][j][1] + height + 3 + (blocks[step].length)])
        }
    }
    return newBlock
}

function pushBlock(block, mapping, direction): boolean {
    let good = true
    for (let i = 0; i < block.length; i++) {
        let newMove = [block[i][0], block[i][1]]
        newMove[0] += direction == "<" ? -1 : 0
        newMove[0] += direction == ">" ? 1 : 0
        newMove[1] -= direction == "v" ? 1 : 0
        if (mapping.has(newMove[0] * 10000 + newMove[1]) || newMove[1] < 0 || newMove[0] < 0 || newMove[0] > 6) {
            return false
        }
    }
    for (let i = 0; i < block.length; i++) {
        block[i][0] += direction == "<" ? -1 : 0
        block[i][0] += direction == ">" ? 1 : 0
        block[i][1] -= direction == "v" ? 1 : 0
    }
    return true
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8"), blocksFile = fs.readFileSync("blocks.txt", "utf8").split("\r\n")
    let blocks = new Array(), newBlock = new Array(), step = 0
    blocksFile.push("")
    for (let i = 0; i < blocksFile.length; i++) {
        if (blocksFile[i] == "") {
            blocks.push(newBlock)
            newBlock = new Array()
            step = 0
        } else {
            newBlock.push(convertBlockLine(blocksFile[i], step))
            step -= 1
        }
    }
    let height = -1, blockedMap = new Map(), block = new Array(), stopped = 0, index = 0
    while (stopped < 2022) {
        if (block.length == 0) {
            block = genBlock(height, step, blocks)
        }
        pushBlock(block, blockedMap, data[index])
        if (!pushBlock(block, blockedMap, "v")) {
            for (let j = 0; j < block.length; j++) {
                blockedMap.set(block[j][0] * 10000 + block[j][1], true)
                if (block[j][1] > height) {
                    height = block[j][1]
                }
            }
            step = step == blocks.length - 1 ? 0 : step + 1
            stopped += 1
            block = new Array()
        }
        index = index == data.length - 1 ? 0 : index + 1
    }
    return height + 1
}

function calcCycle(start, mapping): Array<number> {
    let index = 0, curr = [start[0], start[1]], cycle = [0, 0]
    while (index < 1000) {
        if (mapping.has(curr[0] * 10000 + curr[1])) {
            let newVal = mapping.get(curr[0] * 10000 + curr[1])
            cycle[0] += 1
            cycle[1] += newVal[1]
            curr[0] = (curr[0] + 1) % 5
            curr[1] = newVal[0]
        } else {
            break
        }
        if (curr[0] == start[0] && curr[1] == start[1]) {
            return cycle
        }
    }
    return [-1, -1]
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8"), blocksFile = fs.readFileSync("blocks.txt", "utf8").split("\r\n")
    let blocks = new Array(), newBlock = new Array(), step = 0
    let blockStepMap = new Map()
    blocksFile.push("")
    for (let i = 0; i < blocksFile.length; i++) {
        if (blocksFile[i] == "") {
            blocks.push(newBlock)
            newBlock = new Array()
            step = 0
        } else {
            newBlock.push(convertBlockLine(blocksFile[i], step))
            step -= 1
        }
    }
    let height = -1, blockedMap = new Map(), block = new Array(), stopped = 0, index = 0, flag = true
    let mapStep = 0, mapCurr = [0, 0]
    while (stopped < 1000000000000) {
        if (blockStepMap.has(index * 10000 + (step)) && flag) {
            let res = calcCycle(mapCurr, blockStepMap)
            if (res[0] != -1) {
                flag = false
                let num = Math.floor((1000000000000 - stopped) / res[0])
                stopped += num * res[0]
                height += num * res[1]
            }
        }
        if (flag) {
            if (block.length == 0) {
                block = genBlock(height, step, blocks)
                mapCurr = [step, index]
            }
            pushBlock(block, blockedMap, data[index])
            mapStep += 1
            if (!pushBlock(block, blockedMap, "v")) {
                let newHeight = height
                for (let j = 0; j < block.length; j++) {
                    blockedMap.set(block[j][0] * 10000 + block[j][1], true)
                    if (block[j][1] > newHeight) {
                        newHeight = block[j][1]
                    }
                }
                step = step == blocks.length - 1 ? 0 : step + 1
                stopped += 1
                block = new Array()
                if (stopped > 3000) {
                    blockStepMap.set(mapCurr[0] * 10000 + mapCurr[1], [index == data.length - 1 ? 0 : index + 1, (newHeight - height)])
                    mapStep += 1
                }
                height = newHeight
            }
            index = index == data.length - 1 ? 0 : index + 1
        } else {
            let newVal = blockStepMap.get(mapCurr[0] * 10000 + mapCurr[1])
            height += newVal[1]
            mapCurr[0] = (mapCurr[0] + 1) % 5
            mapCurr[1] = newVal[0]
            stopped += 1
        }
    }
    return height + 1
}

console.log(part1())
console.log(part2())
// 1514285718884
// 1514285714288 <---- CORRECT