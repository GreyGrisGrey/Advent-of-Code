"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function part1() {
    var a = fs.readFileSync("in.txt", "utf8").split("\r\n"), count1 = 0, count2 = 0;
    for (var i = 0; i < a.length; i++) {
        var assigns = a[i].split(",").map(function (val) { return val.split("-").map(function (val2) { return parseInt(val2); }); });
        if ((assigns[0][0] <= assigns[1][0] && assigns[0][1] >= assigns[1][1]) || (assigns[0][0] >= assigns[1][0] && assigns[0][1] <= assigns[1][1])) {
            count1 += 1;
        }
        count2 += assigns[0][0] > assigns[1][1] || assigns[0][1] < assigns[1][0] ? 0 : 1;
    }
    return [count1, count2];
}
console.log(part1());
