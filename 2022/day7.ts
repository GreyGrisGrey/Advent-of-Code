import * as fs from "fs";
function mapChain(map, chain, num): void {
    for (let i = 0; i < chain.length; i++) {
        map.set(chain[i], map.get(chain[i]) + num)
    }
    return
}

function partBoth(): number[] {
    let map = new Map(), input = fs.readFileSync("in.txt", "utf8").split("\r\n"), curr = new Array()
    let currPath = ""
    for (let i = 0; i < input.length; i++) {
        let line = input[i].split(" ")
        if (line[1] == "cd" && line[0] == "$") {
            if (line[2] == "..") {
                curr.splice(curr.length - 1)
                currPath = curr[curr.length - 1]
            } else {
                currPath = currPath.concat("-".concat(line[2]))
                curr.push(currPath)
                map.set(currPath, 0)
            }
        } else if (line[0] != "$" && line[0] != "dir") {
            mapChain(map, curr, parseInt(line[0]))
        }
    }
    let count = 0, vals = map.values()
    let unused = (70000000 - map.get("-/"))
    let needed = 30000000 - unused
    let minimum = map.get("-/")
    for (let i = 0; i < map.size; i++) {
        let nextVal = vals.next().value
        if (nextVal <= 100000) {
            count += nextVal
        }
        if (nextVal < minimum && nextVal >= needed) {
            minimum = nextVal
        }
    }
    return [count, minimum]
}

console.log(partBoth())
// 933843 low?
// 1218315 high.
// multiple of same dir name. fucks sake