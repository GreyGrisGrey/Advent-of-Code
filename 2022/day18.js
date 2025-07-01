"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function genFaces(nums) {
    var strings = new Array;
    strings.push((nums[0] - 0.5).toString().concat("X", nums[1].toString(), "Y", nums[2].toString(), "Z"));
    strings.push((nums[0] + 0.5).toString().concat("X", nums[1].toString(), "Y", nums[2].toString(), "Z"));
    strings.push((nums[0]).toString().concat("X", (nums[1] - 0.5).toString(), "Y", nums[2].toString(), "Z"));
    strings.push((nums[0]).toString().concat("X", (nums[1] + 0.5).toString(), "Y", nums[2].toString(), "Z"));
    strings.push((nums[0]).toString().concat("X", nums[1].toString(), "Y", (nums[2] - 0.5).toString(), "Z"));
    strings.push((nums[0]).toString().concat("X", nums[1].toString(), "Y", (nums[2] + 0.5).toString(), "Z"));
    return strings;
}
function nextCubes(nums) {
    var strings = new Array;
    strings.push((nums[0] - 1).toString().concat(",", (nums[1]).toString(), ",", (nums[2]).toString()));
    strings.push((nums[0] + 1).toString().concat(",", (nums[1]).toString(), ",", (nums[2]).toString()));
    strings.push((nums[0]).toString().concat(",", (nums[1] - 1).toString(), ",", (nums[2]).toString()));
    strings.push((nums[0]).toString().concat(",", (nums[1] + 1).toString(), ",", (nums[2]).toString()));
    strings.push((nums[0]).toString().concat(",", (nums[1]).toString(), ",", (nums[2] - 1).toString()));
    strings.push((nums[0]).toString().concat(",", (nums[1]).toString(), ",", (nums[2] + 1).toString()));
    return strings;
}
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), faceMap = new Map(), total = 0;
    for (var i = 0; i < data.length; i++) {
        var vals = data[i].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])];
        var strings = genFaces(nums);
        for (var j = 0; j < strings.length; j++) {
            if (faceMap.has(strings[j])) {
                total -= 1;
            }
            else {
                faceMap.set(strings[j], true);
                total += 1;
            }
        }
    }
    return total;
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), faceMap = new Map(), total = 0, closed = new Map;
    for (var i = 0; i < data.length; i++) {
        var vals = data[i].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])];
        var strings = genFaces(nums);
        closed.set(data[i], true);
        for (var j = 0; j < strings.length; j++) {
            faceMap.set(strings[j], true);
        }
    }
    var searchers = ["30,30,30"];
    while (searchers.length != 0) {
        var vals = searchers[0].split(","), nums = [parseInt(vals[0]), parseInt(vals[1]), parseInt(vals[2])];
        if (!closed.has(searchers[0]) && nums[0] > -2 && nums[1] > -2 && nums[2] > -2 && nums[0] < 31 && nums[1] < 31 && nums[2] < 31) {
            var options = genFaces(nums), newSearch = nextCubes(nums);
            for (var j = 0; j < options.length; j++) {
                if (faceMap.has(options[j])) {
                    total += 1;
                }
                if (!closed.has(newSearch[j])) {
                    searchers.push(newSearch[j]);
                }
            }
        }
        closed.set(searchers[0], true);
        searchers = searchers.slice(1, searchers.length);
    }
    return total;
}
console.log(part1());
console.log(part2());
