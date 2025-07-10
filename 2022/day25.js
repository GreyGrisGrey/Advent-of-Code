"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function snafu(num) {
    var newNum = 0;
    for (var i = 0; i < num.length; i++) {
        if (num[i] == "-") {
            newNum += (-1) * Math.pow(5, num.length - (i + 1));
        }
        else if (num[i] == "=") {
            newNum += (-2) * Math.pow(5, num.length - (i + 1));
        }
        else {
            newNum += parseInt(num[i]) * Math.pow(5, num.length - (i + 1));
        }
    }
    return newNum;
}
function part1() {
    var num = fs.readFileSync("in.txt", "utf8").split("\r\n").map(function (x) { return snafu(x); }).reduce(function (base, curr) { return base + curr; });
    var snafuNum = "", digit = 1;
    while (num > 0) {
        var stepVal = (num % (Math.pow(5, digit))) / (Math.pow(5, Math.max(digit - 1, 0)));
        if (stepVal == 3) {
            snafuNum = "=".concat(snafuNum);
            stepVal = -2;
        }
        else if (stepVal == 4) {
            snafuNum = "-".concat(snafuNum);
            stepVal = -1;
        }
        else {
            snafuNum = stepVal.toString().concat(snafuNum);
        }
        num -= stepVal * (Math.pow(5, Math.max(digit - 1, 0)));
        digit += 1;
    }
    return snafuNum;
}
console.log(part1());
