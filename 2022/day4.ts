import * as fs from "fs";
function partBoth(): number[] {
    let pairs = fs.readFileSync("in.txt", "utf8").split("\r\n"), count1 = 0, count2 = 0
    for (let i = 0; i < pairs.length; i++) {
        let assigns = pairs[i].split(",").map((val) => val.split("-").map((val2) => parseInt(val2)))
        if ((assigns[0][0] <= assigns[1][0] && assigns[0][1] >= assigns[1][1]) || (assigns[0][0] >= assigns[1][0] && assigns[0][1] <= assigns[1][1])) {
            count1 += 1
        }
        count2 += assigns[0][0] > assigns[1][1] || assigns[0][1] < assigns[1][0] ? 0 : 1
    }
    return [count1, count2]
}

console.log(partBoth())