"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function partBoth() {
    var map1 = new Map([
        ["A X", 4], ["A Y", 8], ["A Z", 3],
        ["B X", 1], ["B Y", 5], ["B Z", 9],
        ["C X", 7], ["C Y", 2], ["C Z", 6]
    ]);
    var map2 = new Map([
        ["A X", 3], ["A Y", 4], ["A Z", 8],
        ["B X", 1], ["B Y", 5], ["B Z", 9],
        ["C X", 2], ["C Y", 6], ["C Z", 7]
    ]);
    var count1 = 0, count2 = 0;
    var a = fs.readFileSync("in.txt", "utf8").split("\r\n");
    for (var i in a) {
        count1 += map1.get(a[i]);
        count2 += map2.get(a[i]);
    }
    return [count1, count2];
}
console.log(partBoth());
