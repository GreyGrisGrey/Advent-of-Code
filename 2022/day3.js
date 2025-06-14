"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function part1() {
    var count = 0;
    var bags = fs.readFileSync("in.txt", "utf8").split("\r\n");
    for (var i in bags) {
        var map = new Map();
        for (var j = 0; j < bags[i].length; j++) {
            if (j < Math.floor(bags[i].length / 2)) {
                map.set(bags[i][j], true);
            }
            else {
                if (map.has(bags[i][j])) {
                    count += bags[i][j].charCodeAt(0) - 64 < 27 ? bags[i][j].charCodeAt(0) - 38 : bags[i][j].charCodeAt(0) - 96;
                    break;
                }
            }
        }
    }
    return count;
}
function part2() {
    var count = 0;
    var bags = fs.readFileSync("in.txt", "utf8").split("\r\n");
    for (var i = 0; i < Math.floor(bags.length / 3); i++) {
        var map = new Map();
        for (var j = 0; j < 3; j++) {
            for (var k = 0; k < bags[i * 3 + j].length; k++) {
                if (j == 0) {
                    map.set(bags[i * 3 + j][k], 1);
                }
                else if (map.has(bags[i * 3 + j][k])) {
                    if (j == 2 && map.get(bags[i * 3 + j][k]) > 1) {
                        count += bags[i * 3 + j][k].charCodeAt(0) - 64 < 27 ? bags[i * 3 + j][k].charCodeAt(0) - 38 : bags[i * 3 + j][k].charCodeAt(0) - 96;
                        break;
                    }
                    else if (j == 1) {
                        map.set(bags[i * 3 + j][k], 2);
                    }
                }
            }
        }
    }
    return count;
}
console.log(part1());
console.log(part2());
