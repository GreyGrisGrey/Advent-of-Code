import * as fs from "fs"

class Valve {
    pressure: number
    name: string
    adjacent: Array<string>
    adjacentMap: Map<string, number>

    constructor(inputs, pressure, name) {
        this.adjacent = inputs
        this.pressure = pressure
        this.name = name
    }

    addPressure(time): number {
        return (time - 1) * this.pressure
    }

    getAdj(): Array<string> {
        return this.adjacent
    }

    getAdjMap(): Map<string, number> {
        return this.adjacentMap
    }

    setAdj(newMap): void {
        this.adjacentMap = newMap
        return
    }
}

function BFS(start, valves, opens): void {
    let currOpen = [[start, 0]], dones = new Map<string, number>, checked = new Array()
    while (dones.size < opens.length) {
        let nextOpen = valves.get(currOpen[0][0]).getAdj()
        if (opens.includes(currOpen[0][0]) && !checked.includes(currOpen[0][0])) {
            dones.set(currOpen[0][0], currOpen[0][1])
        }
        checked.push(currOpen[0][0])
        for (let i = 0; i < nextOpen.length; i++) {
            if (!checked.includes(nextOpen[i])) {
                currOpen.push([nextOpen[i], currOpen[0][1] + 1])
            }
        }
        currOpen = currOpen.slice(1, currOpen.length)
    }
    valves.get(start).setAdj(dones)
    return
}

function recurse1(currValve, currNum, valves, opens, time, closed): number {
    if (time <= 0) {
        return currNum
    } else if (closed.includes(currValve)) {
        return currNum
    }
    if (opens.includes(currValve)) {
        currNum += valves.get(currValve).addPressure(time)
        closed.push(currValve)
        time -= 1
    }
    let mapping = valves.get(currValve).getAdjMap(), best = currNum
    for (let i = 0; i < opens.length; i++) {
        let newClosed = closed.slice()
        let newStep = recurse1(opens[i], currNum, valves, opens, time - mapping.get(opens[i]), newClosed)
        if (newStep > best) {
            best = newStep
        }
    }
    return best
}

// this will take a while but it will do it
function recurse2(currValves, currNum, valves, opens, time, currTime, closed): number {
    if (currTime == time - 1) {
        return currNum
    }
    if ((closed.includes(currValves[0][0]) || closed.includes(currValves[1][0])) && (currValves[0][0] != "AA") && (currValves[1][0] != "AA")) {
        return currNum
    }
    let best = 0
    if (currTime == currValves[0][1]) {
        if (!closed.includes(currValves[0][0])) {
            currNum += valves.get(currValves[0][0]).addPressure(time - currTime + 1)
            closed.push(currValves[0][0])
        }
        let mapping = valves.get(currValves[0][0]).getAdjMap()
        for (let i = 0; i < opens.length; i++) {
            if (opens[i] != currValves[0][0]) {
                let newClosed = closed.slice()
                let newStep = recurse2([[opens[i], currTime + mapping.get(opens[i]) + 1], currValves[1]], currNum, valves, opens, time, currTime, newClosed)
                if (newStep > best) {
                    best = newStep
                }
            }
        }
    } else if (currTime == currValves[1][1]) {
        if (!closed.includes(currValves[1][0])) {
            currNum += valves.get(currValves[1][0]).addPressure(time - currTime + 1)
            closed.push(currValves[1][0])
        }
        let mapping = valves.get(currValves[1][0]).getAdjMap()
        for (let i = 0; i < opens.length; i++) {
            if (opens[i] != currValves[1][0]) {
                let newClosed = closed.slice()
                let newStep = recurse2([currValves[0], [opens[i], currTime + mapping.get(opens[i]) + 1]], currNum, valves, opens, time, currTime, newClosed)
                if (newStep > best) {
                    best = newStep
                }
            }
        }
    } else {
        best = recurse2(currValves, currNum, valves, opens, time, currTime + 1, closed)
    }
    return best
}

function partBoth(first): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), valves = new Map<string, Valve>, opens = new Map<string, Valve>, opensArr = new Array()
    for (let i = 0; i < data.length; i++) {
        let line = data[i].split(" "), important = [line[1], parseInt(line[4].slice(0, line[4].length - 1).split("=")[1])]
        let adj = new Array()
        for (let j = 9; j < line.length; j++) {
            if (j != line.length - 1) {
                adj.push(line[j].slice(0, line[j].length - 1))
            } else {
                adj.push(line[j])
            }
        }
        let newValve = new Valve(adj, important[1], important[0])
        valves.set(important[0], newValve)
        if (important[1] != 0) {
            opens.set(important[0], newValve)
            opensArr.push(important[0])
        }
    }
    for (let i = 0; i < opensArr.length; i++) {
        BFS(opensArr[i], valves, opensArr)
    }
    BFS("AA", valves, opensArr)
    if (first) {
        return recurse1("AA", 0, valves, opensArr, 30, new Array())
    }
    return recurse2([["AA", 0], ["AA", 0]], 0, valves, opensArr, 26, 0, new Array())
}

console.log(partBoth(true), partBoth(false))