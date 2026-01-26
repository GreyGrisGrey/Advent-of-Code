import * as fs from "fs"

function part1(): string {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let itemMap: Map<string, number> = new Map()
    let rootMap: Map<string, boolean> = new Map()
    let dataList: Array<Array<any>> = new Array()
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" -> ")
        let item = line[0].split(" ")
        itemMap.set(item[0], dataList.length)
        rootMap.set(item[0], true)
        let newLine: Array<any> = [Number(item[1].substring(1, item[1].length - 1))]
        if (line.length == 2) {
            newLine = newLine.concat(line[1].split(", "))
        }
        dataList.push(newLine)
    }
    
    let iter1 = itemMap.values()
    let curr1 = iter1.next()
    while (!curr1.done) {
        for (let i = 0; i < dataList[curr1.value].length; i++) {
            rootMap.set(dataList[curr1.value][i], false)
        }
        curr1 = iter1.next()
    }
    
    let iter2 = itemMap.keys()
    let curr2 = iter2.next()
    while (!curr2.done) {
        if (rootMap.get(curr2.value)) {
            return curr2.value
        }
        curr2 = iter2.next()
    }
    return "error"
}

function recurse(dataList: Array<Array<any>>, itemMap: Map<string, number>, curr: string): Array<number> {
    let currItems = dataList[itemMap.get(curr)!]
    if (currItems.length == 1) {
        return [0, currItems[0]]
    }
    let first = -1
    let second = -1
    for (let i = 1; i < currItems.length; i++) {
        let res = recurse(dataList, itemMap, currItems[i])
        if (res[0] == 1) {
            return res
        } else if (first == -1) {
            first = res[1]
        } else if (second == -1) {
            second = res[1]
        } else if (first == second && first != res[1]) {
            let difference = first - res[1]
            return [1, dataList[itemMap.get(currItems[i])!][0] + difference]
        } else if (first != second) {
            if (first == res[1]) {
                let difference = first - second
                return [1, dataList[itemMap.get(currItems[2])!][0] + difference]
            } else {
                let difference = second - first
                return [1, dataList[itemMap.get(currItems[1])!][0] + difference]
            }
        }
    }
    return [0, currItems[0] + first * (currItems.length - 1)]
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let itemMap: Map<string, number> = new Map()
    let dataList: Array<Array<any>> = new Array()
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" -> ")
        let item = line[0].split(" ")
        itemMap.set(item[0], dataList.length)
        let newLine: Array<any> = [Number(item[1].substring(1, item[1].length - 1))]
        if (line.length == 2) {
            newLine = newLine.concat(line[1].split(", "))
        }
        dataList.push(newLine)
    }
    return recurse(dataList, itemMap, part1())[1]
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())