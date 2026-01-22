import * as fs from "fs";

function part1(): number{
    var data = fs.readFileSync("in.txt", "utf8")
    var res = 0
    for (var i = 0; i < data.length; i++){
        var second = (i + 1) % data.length
        if (data[second] == data[i]){
            res += Number(data[second])
        }
    }
    return res
}

function part2(): number{
    var data = fs.readFileSync("in.txt", "utf8")
    var res = 0
    for (var i = 0; i < data.length; i++){
        var second = (i + (data.length/2)) % data.length
        if (data[second] == data[i]){
            res += Number(data[second])
        }
    }
    return res
}

console.log(part1())
console.log(part2())