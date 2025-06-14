import * as fs from "fs";
function swap(list: number[], replacement: number, index: number): number {
    var temp = list[index]
    list[index] = replacement
    return temp
}

function partBoth(): number[] {
    var a = fs.readFileSync("in.txt", "utf8").split("\r\n"), curr = 0, maximums = [0, 0, 0]
    a.push("")
    for (var i = 0; i < a.length; i++) {
        if (a[i] === "") {
            for (var j = 0; j < 3; j++) {
                if (curr > maximums[j]) {
                    curr = swap(maximums, curr, j)
                }
            }
            curr = 0
        } else {
            curr += parseInt(a[i])
        }
    }
    return [Math.max(maximums[0], maximums[1], maximums[2]), maximums.reduce((sum, num) => sum + num, 0)]
}

console.log(partBoth())