import * as fs from "fs";

function part1(): number {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    var res = 0
    for (let i = 0; i < data.length; i++) {
        var nums = data[i].split("\t")
        var maximum = 0
        var minimum = 9999
        for (let j = 0; j < nums.length; j++) {
            if (Number(nums[j]) > maximum) {
                maximum = Number(nums[j])
            }
            if (Number(nums[j]) < minimum) {
                minimum = Number(nums[j])
            }
        }
        res += maximum - minimum
    }
    return res
}

function part2(): number {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    var res = 0
    for (let i = 0; i < data.length; i++) {
        var nums = data[i].split("\t")
        for (let j = 0; j < nums.length; j++) {
            for (let k = 0; k < nums.length; k++) {
                if ((k != j) && (Number(nums[k]) >= Number(nums[j])) && ((nums[k] % nums[j]) == 0)) {
                    res += nums[k] / nums[j]
                }
            }
        }
    }
    return res
}

console.log("Part 1:", part1())
console.log("Part 1:", part2())