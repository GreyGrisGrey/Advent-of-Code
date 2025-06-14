"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function swap(list, replacement, index) {
    var temp = list[index];
    list[index] = replacement;
    return temp;
}
function partBoth() {
    var a = fs.readFileSync("in.txt", "utf8").split("\r\n"), curr = 0, maximums = [0, 0, 0];
    a.push("");
    for (var i = 0; i < a.length; i++) {
        if (a[i] === "") {
            for (var j = 0; j < 3; j++) {
                if (curr > maximums[j]) {
                    curr = swap(maximums, curr, j);
                }
            }
            curr = 0;
        }
        else {
            curr += parseInt(a[i]);
        }
    }
    return [Math.max(maximums[0], maximums[1], maximums[2]), maximums.reduce(function (sum, num) { return sum + num; }, 0)];
}
console.log(partBoth());
