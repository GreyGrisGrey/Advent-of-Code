"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function part1() {
    var count = 0, a = fs.readFileSync("in.txt", "utf8").split("\r\n"), X = 1;
    var cycle = 0, cycleCount = 1;
    for (var i = 0; i < a.length; i++) {
        if (cycle >= 18) {
            count += 20 * X * cycleCount;
            cycle -= 40;
            cycleCount += 2;
        }
        if (a[i] != "noop") {
            X += parseInt(a[i].split(" ")[1]);
            cycle += 2;
        }
        else {
            cycle += 1;
        }
    }
    return count;
}
function part2() {
    var count = 0, a = fs.readFileSync("in.txt", "utf8").split("\r\n"), X = 1, cycle = -1, currInst = -1, currString = "";
    while (currInst < a.length - 1) {
        if (count == 0) {
            currInst += 1;
            count = a[currInst] == "noop" ? 1 : 2;
        }
        while (count > 0) {
            count -= 1;
            cycle += 1;
            currString = currString.concat((Math.abs(X - cycle) < 2) ? "#" : ".");
            if (cycle == 39) {
                console.log(currString);
                currString = "";
                cycle = -1;
            }
            if (count == 0 && a[currInst] != "noop") {
                X += parseInt(a[currInst].split(" ")[1]);
            }
        }
    }
}
console.log(part1());
part2();
