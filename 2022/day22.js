"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function parseInstructions(line) {
    var instructs = new Array, curr = "", dirs = ["R", "L"];
    for (var i = 0; i < line.length; i++) {
        if (dirs.includes(line[i])) {
            instructs.push(parseInt(curr));
            instructs.push(line[i]);
            curr = "";
        }
        else {
            curr = curr.concat(line[i]);
        }
    }
    instructs.push(parseInt(curr));
    return instructs;
}
function moveStep(heading, curr, mapping, maxX, maxY) {
    while (true) {
        curr += heading;
        if (curr % 500 > 400) {
            curr += maxY;
        }
        else if (curr % 500 >= maxY) {
            curr -= maxY;
        }
        else if (curr < 0) {
            curr += maxX * 1000;
        }
        else if (curr > ((maxX + 1) * 1000) - 1) {
            curr -= ((maxX + 1) * 1000);
        }
        if (mapping.get(curr) == ".") {
            return curr;
        }
        else if (mapping.get(curr) == "#") {
            return moveStep(-heading, curr, mapping, maxX, maxY);
        }
    }
}
function runInstruct(heading, curr, currInstruct, mapping, maxX, maxY) {
    if ((currInstruct == "R" && heading == 1000) || (currInstruct == "L" && heading == -1000)) {
        heading = 1;
    }
    else if ((currInstruct == "R" && heading == 1) || (currInstruct == "L" && heading == -1)) {
        heading = -1000;
    }
    else if ((currInstruct == "R" && heading == -1000) || (currInstruct == "L" && heading == 1000)) {
        heading = -1;
    }
    else if (currInstruct == "R" || currInstruct == "L") {
        heading = 1000;
    }
    else {
        while (currInstruct > 0) {
            var prev = curr, res = moveStep(heading, curr, mapping, maxX, maxY);
            if (res == prev) {
                currInstruct = 0;
            }
            else {
                curr = res;
            }
            currInstruct -= 1;
        }
    }
    return [curr, heading];
}
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), nums = (data.map(function (line) { return line.length; }).slice(0, data.length - 2)), maximum = 0;
    for (var i = 0; i < nums.length; i++) {
        maximum = nums[i] > maximum ? nums[i] : maximum;
    }
    var x = maximum, y = nums.length, spaces = new Map, start = [1000, 1000];
    for (var i = 0; i < x; i++) {
        for (var j = 0; j < y; j++) {
            if (i > data[j].length) {
                spaces.set(i * 1000 + j, " ");
            }
            else {
                spaces.set(i * 1000 + j, data[j][i]);
                if (start[1] > j && data[j][i] != " ") {
                    start = [i, j];
                }
            }
        }
    }
    var curr = start[0] * 1000 + start[1], instructs = parseInstructions(data[data.length - 1]), heading = 1000, dirMapping = new Map([[1000, 0], [1, 1], [-1000, 2], [-1, 3]]);
    for (var i = 0; i < instructs.length; i++) {
        var res = runInstruct(heading, curr, instructs[i], spaces, x, y);
        curr = res[0], heading = res[1];
    }
    curr += 1001;
    return ((curr % 500) * 1000) + ((curr - (curr % 500)) / 250) + dirMapping.get(heading);
}
console.log(part1());
