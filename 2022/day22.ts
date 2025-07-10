import * as fs from "fs"

function parseInstructions(line: string): Array<any> {
    let instructs = new Array<any>, curr = "", dirs = ["R", "L"]
    for (let i = 0; i < line.length; i++) {
        if (dirs.includes(line[i])) {
            instructs.push(parseInt(curr))
            instructs.push(line[i])
            curr = ""
        } else {
            curr = curr.concat(line[i])
        }
    }
    instructs.push(parseInt(curr))
    return instructs
}

function moveStep(heading: number, curr: number, mapping: Map<number, string>, maxX: number, maxY: number): number {
    while (true) {
        curr += heading
        if (curr % 500 > 400) {
            curr += maxY
        } else if (curr % 500 >= maxY) {
            curr -= maxY
        } else if (curr < 0) {
            curr += maxX * 1000
        } else if (curr > ((maxX + 1) * 1000) - 1) {
            curr -= ((maxX + 1) * 1000)
        }
        if (mapping.get(curr) == ".") {
            return curr
        } else if (mapping.get(curr) == "#") {
            return moveStep(-heading, curr, mapping, maxX, maxY)
        }
    }
}

function runInstruct(heading: number, curr: number, currInstruct: any, mapping: Map<number, string>, maxX: number, maxY: number): Array<number> {
    if ((currInstruct == "R" && heading == 1000) || (currInstruct == "L" && heading == -1000)) {
        heading = 1
    } else if ((currInstruct == "R" && heading == 1) || (currInstruct == "L" && heading == -1)) {
        heading = -1000
    } else if ((currInstruct == "R" && heading == -1000) || (currInstruct == "L" && heading == 1000)) {
        heading = -1
    } else if (currInstruct == "R" || currInstruct == "L") {
        heading = 1000
    } else {
        while (currInstruct > 0) {
            let prev = curr, res = moveStep(heading, curr, mapping, maxX, maxY)
            if (res == prev) {
                currInstruct = 0
            } else {
                curr = res
            }
            currInstruct -= 1
        }
    }
    return [curr, heading]
}

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), nums = (data.map(line => line.length).slice(0, data.length - 2)), maximum = 0
    for (let i = 0; i < nums.length; i++) {
        maximum = nums[i] > maximum ? nums[i] : maximum
    }
    let x = maximum, y = nums.length, spaces = new Map<number, string>, start = [1000, 1000]
    for (let i = 0; i < x; i++) {
        for (let j = 0; j < y; j++) {
            if (i > data[j].length) {
                spaces.set(i * 1000 + j, " ")
            } else {
                spaces.set(i * 1000 + j, data[j][i])
                if (start[1] > j && data[j][i] != " ") {
                    start = [i, j]
                }
            }
        }
    }
    let curr = start[0] * 1000 + start[1], instructs = parseInstructions(data[data.length - 1]), heading = 1000, dirMapping = new Map([[1000, 0], [1, 1], [-1000, 2], [-1, 3]])
    for (let i = 0; i < instructs.length; i++) {
        let res = runInstruct(heading, curr, instructs[i], spaces, x, y)
        curr = res[0], heading = res[1]
    }
    curr += 1001
    return ((curr % 500) * 1000) + ((curr - (curr % 500)) / 250) + dirMapping.get(heading)
}


// part 2 is not in any way general
class Face {
    spaces: Map<number, boolean>
    tilt: number

    constructor(grid: Array<string>, start: Array<number>, size: number, direction: number) {
        this.spaces = new Map<number, boolean>
        this.tilt = direction
        for (let i = 0; i < size; i++) {
            for (let j = 0; j < size; j++) {
                if (grid[start[0] + i][start[1] + j] == ".") {
                    this.spaces.set((i) * 1000 + j, true)
                } else {
                    this.spaces.set((i) * 1000 + j, false)
                }
            }
        }
    }
}

class Cube {
    adj = [[1, 2, 3, 4], [5, 2, 0, 4], [1, 5, 3, 0], [5, 4, 0, 2], [5, 1, 0, 3], [1, 4, 3, 2]]
    dirMap = new Map([[">>", 0], [">^", 0], ["><", 1], ["^^", 0], ["^>", 0], ["^v", 1], ["vv", 0], ["v<", 0], ["v^", 1], ["<v", 0], ["<<", 0], ["<>", 1]])
    faces: Array<Face>
    faceMap: Map<number, Face>
    pairings: Map<string, string>
    maximum = 49

    constructor() {
        this.faces = new Array<Face>
        this.faceMap = new Map<number, Face>
        this.pairings = new Map<string, string>
        for (let i = 0; i < 6; i++) {
            let curr = i.toString()
            for (let j = 0; j < 4; j++) {
                if (j == 0) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), ">")
                } else if (j == 1) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "v")
                } else if (j == 2) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "<")
                } else {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "^")
                }
            }
        }
    }

    addFace(face: Face, position: number) {
        this.faceMap.set(position, face)
        if (this.faceMap.size == 6) {
            for (let i = 0; i < 6; i++) {
                this.faces.push(this.faceMap.get(i))
            }
        }
    }

    swapFace(curr: Array<any>) {
        let newFace = 0, dir2 = "", change = 0, fine = -1, wallNum = -1
        if (curr[0] > 49) {
            newFace = this.adj[curr[2]][0]
            fine = 1
        } else if (curr[0] < 0) {
            newFace = this.adj[curr[2]][2]
            fine = 1
        } else if (curr[1] < 0) {
            newFace = this.adj[curr[2]][3]
            fine = 0
        } else if (curr[1] > 49) {
            newFace = this.adj[curr[2]][1]
            fine = 0
        }
        for (let i = 0; i < 4; i++) {
            if (this.adj[newFace][i] == curr[2]) {
                if (i == 0) {
                    dir2 = "<"
                    change = this.dirMap.get(curr[3].concat(dir2))
                } else if (i == 1) {
                    dir2 = "^"
                    change = this.dirMap.get(curr[3].concat(dir2))
                } else if (i == 2) {
                    dir2 = ">"
                    change = this.dirMap.get(curr[3].concat(dir2))
                } else if (i == 3) {
                    dir2 = "v"
                    change = this.dirMap.get(curr[3].concat(dir2))
                }
            }
        }
        let news = [0, 0]
        if (dir2 == ">") {
            news[0] = 0
            if (change == 1) {
                news[1] = 49 - curr[fine]
            } else {
                news[1] = curr[fine]
            }
        } else if (dir2 == "<") {
            news[0] = 49
            if (change == 1) {
                news[1] = 49 - curr[fine]
            } else {
                news[1] = curr[fine]
            }
        } else if (dir2 == "^") {
            news[1] = 49
            if (change == 1) {
                news[0] = 49 - curr[fine]
            } else {
                news[0] = curr[fine]
            }
        } else {
            news[1] = 0
            if (change == 1) {
                news[0] = 49 - curr[fine]
            } else {
                news[0] = curr[fine]
            }
        }
        curr[0] = news[0]
        curr[1] = news[1]
        curr[2] = newFace
        curr[3] = dir2
    }
}

function runInstruct2(curr: Array<any>, currInstruct: any, cube: Cube) {
    if ((curr[3] == ">" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "<")) {
        curr[3] = "^"
    } else if ((curr[3] == "^" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "v")) {
        curr[3] = "<"
    } else if ((curr[3] == "v" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "^")) {
        curr[3] = ">"
    } else if (currInstruct == "L" || currInstruct == "R") {
        curr[3] = "v"
    } else {
        while (currInstruct > 0) {
            currInstruct -= moveStep2(curr, cube)
        }
    }
}

function moveStep2(curr: Array<any>, cube: Cube): number {
    if (curr[3] == ">") {
        curr[0] += 1
    } else if (curr[3] == "<") {
        curr[0] -= 1
    } else if (curr[3] == "v") {
        curr[1] += 1
    } else if (curr[3] == "^") {
        curr[1] -= 1
    }
    if (curr[0] > 49 || curr[0] < 0 || curr[1] < 0 || curr[1] > 49) {
        cube.swapFace(curr)
    }
    if (!cube.faces[curr[2]].spaces.get(curr[0] + curr[1] * 1000)) {
        runInstruct2(curr, "L", cube)
        runInstruct2(curr, "L", cube)
        moveStep2(curr, cube)
        runInstruct2(curr, "L", cube)
        runInstruct2(curr, "L", cube)
        return 1000000000
    }
    return 1
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), size = 50, indices = new Array<Array<number>>
    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
            if (i * size < data.length - 1 && j * size < data[i * size].length - 1 && data[i * size][j * size] != " ") {
                indices.push([i * size, j * size])
            }
        }
    }
    let headings = [0, 1, 0, 1, 0, 1], pos = [0, 1, 2, 3, 5, 4], cube = new Cube()
    for (let i = 0; i < 6; i++) {
        let newFace = new Face(data, indices[i], size, headings[i])
        cube.addFace(newFace, pos[i])
    }
    let instructs = parseInstructions(data[data.length - 1]), start = [0, 0, 0, ">"]
    for (let i = 0; i < instructs.length; i++) {
        runInstruct2(start, instructs[i], cube)
    }
    if (start[2] == 4) {
        start[2] = 5
    } else if (start[2] == 5) {
        start[2] = 4
    }
    start[0] += indices[start[2]][1] + 1
    start[1] += indices[start[2]][0] + 1
    let newNum = start[0] * 4 + start[1] * 1000
    if (start[3] == "^") {
        newNum += 3
    } else if (start[3] == "<") {
        newNum += 2
    } else if (start[3] == "v") {
        newNum += 1
    }
    return newNum
}

console.log(part1())
console.log(part2())