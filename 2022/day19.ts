import * as fs from "fs"

function canBuild(costMap, currResource, currBots, maximums): Array<boolean> {
    let res = new Array<boolean>
    for (let i = 0; i < costMap.size; i++) {
        let costs = costMap.get(i), check = true
        if (currBots[i] >= maximums[i]) {
            check = false
        }
        for (let j = 0; j < currResource.length; j++) {
            if (currResource[j] < costs[j]) {
                check = false
            }
        }
        res.push(check)
    }
    return res
}

function build(index, costMap, currResource, currBots): Array<Array<number>> {
    let costs = costMap.get(index), result = [currResource.slice(), currBots.slice()]
    for (let i = 0; i < currResource.length - 1; i++) {
        result[0][i] -= costs[i]
    }
    result[1][index] += 1
    return result
}

function recurse1(costMap, currResource, currBots, time, maxTime, best, maximums, cache): number {
    if (time == maxTime) {
        return currResource[3]
    }
    if ((maxTime - time) * (currBots[3] + 2) + currResource[3] < best) {
        return 0
    }
    let options = canBuild(costMap, currResource, currBots, maximums)
    for (let i = 0; i < 4; i++) {
        currResource[i] += currBots[i]
    }
    for (let i = 0; i < 4; i++) {
        if (options[3 - i]) {
            let newArrs = build(3 - i, costMap, currResource, currBots), res = recurse(costMap, newArrs[0], newArrs[1], time + 1, maxTime, best, maximums, cache)
            best = res > best ? res : best
        }
    }
    let res = recurse(costMap, currResource, currBots, time + 1, maxTime, best, maximums, cache)
    return (res > best) ? res : best
}

function recurse(costMap, currResource, currBots, time, maxTime, best, maximums, cache): number {
    if (time == maxTime) {
        return currResource[3]
    }
    if (currResource[3] + (currBots[3] * (maxTime - time)) + ((maxTime - time - 1) * (maxTime - time) / 2) < best) {
        return 1
    }
    let key = currBots.join().concat(",", currResource.join(), ",", time.toString())
    if (cache.has(key)) {
        return cache.get(key)
    }
    let options = canBuild(costMap, currResource, currBots, maximums)
    for (let i = 0; i < 4; i++) {
        currResource[i] += currBots[i]
    }
    for (let i = 0; i < 4; i++) {
        if (options[3 - i]) {
            let newArrs = build(3 - i, costMap, currResource, currBots), res = recurse(costMap, newArrs[0], newArrs[1], time + 1, maxTime, best, maximums, cache)
            best = res > best ? res : best
        }
    }
    let res = recurse(costMap, currResource, currBots, time + 1, maxTime, best, maximums, cache)
    best = res > best ? res : best
    cache.set(key, best)
    return best
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), end = 0
    for (let i = 0; i < data.length; i++) {
        let robotCost = new Map<number, Array<number>>, dataSplit = data[i].split(" ")
        robotCost.set(0, [parseInt(dataSplit[6]), 0, 0])
        robotCost.set(1, [parseInt(dataSplit[12]), 0, 0])
        robotCost.set(2, [parseInt(dataSplit[18]), parseInt(dataSplit[21]), 0])
        robotCost.set(3, [parseInt(dataSplit[27]), 0, parseInt(dataSplit[30])])
        let maximums = [Math.max(parseInt(dataSplit[12]), parseInt(dataSplit[18]), parseInt(dataSplit[27])), parseInt(dataSplit[21]), parseInt(dataSplit[30]), 90]
        end += recurse(robotCost, [0, 0, 0, 0], [1, 0, 0, 0], 0, 24, 0, maximums, new Map<string, number>) * (i + 1)
    }
    return end
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), end = 1
    for (let i = 0; i < 3; i++) {
        let robotCost = new Map<number, Array<number>>, dataSplit = data[i].split(" ")
        robotCost.set(0, [parseInt(dataSplit[6]), 0, 0])
        robotCost.set(1, [parseInt(dataSplit[12]), 0, 0])
        robotCost.set(2, [parseInt(dataSplit[18]), parseInt(dataSplit[21]), 0])
        robotCost.set(3, [parseInt(dataSplit[27]), 0, parseInt(dataSplit[30])])
        let maximums = [Math.max(parseInt(dataSplit[12]), parseInt(dataSplit[18]), parseInt(dataSplit[27])), parseInt(dataSplit[21]), parseInt(dataSplit[30]), 30]
        end *= recurse(robotCost, [0, 0, 0, 0], [1, 0, 0, 0], 0, 32, 0, maximums, new Map<string, number>)
    }
    return end
}

console.log(part1())
console.log(part2())