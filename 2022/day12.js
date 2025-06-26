"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var Space = /** @class */ (function () {
    function Space(x, y, height) {
        this.dist = -1;
        this.x = x;
        this.y = y;
        this.height = height;
    }
    Space.prototype.tryHeight = function (height, newDist) {
        if ((newDist < this.dist || this.dist == -1) && ((this.height - 1 <= height) || (this.height == 26 && this.height - 2 <= height))) {
            this.dist = newDist;
            return this.height;
        }
        return -1;
    };
    Space.prototype.getHeight = function () {
        return this.height;
    };
    return Space;
}());
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), spaces = new Array(), start = [0, 0];
    for (var i = 0; i < data.length; i++) {
        var line = new Array();
        var printString = "";
        for (var j = 0; j < data[0].length; j++) {
            if (data[i][j] == "S") {
                var curr = new Space(j, i, 0);
                curr.tryHeight(0, 0);
                line.push(curr);
                start = [i, j];
                printString = printString.concat("X", " ");
            }
            else if (data[i][j] == "E") {
                line.push(new Space(j, i, 26));
                printString = printString.concat("26", " ");
            }
            else {
                line.push(new Space(j, i, data[i].charCodeAt(j) - 97));
                printString = printString.concat((data[i].charCodeAt(j) - 97).toString(), " ");
            }
        }
        spaces.push(line);
    }
    var open = [start], maximum = 0, steps = 1;
    while (maximum < 26 && steps < 500 && open.length > 0) {
        var newOpen = new Array();
        for (var i = 0; i < open.length; i++) {
            for (var j = 0; j < 4; j++) {
                var newIndex = [open[i][0], open[i][1]];
                newIndex[0] += j == 0 ? 1 : 0;
                newIndex[1] += j == 1 ? 1 : 0;
                newIndex[0] += j == 2 ? -1 : 0;
                newIndex[1] += j == 3 ? -1 : 0;
                if (newIndex[0] >= 0 && newIndex[1] >= 0 && newIndex[0] < data.length && newIndex[1] < data[0].length) {
                    var res = spaces[newIndex[0]][newIndex[1]].tryHeight(spaces[open[i][0]][open[i][1]].getHeight(), steps);
                    if (res != -1) {
                        newOpen.push(newIndex);
                        if (res > maximum) {
                            maximum = res;
                        }
                    }
                }
            }
        }
        steps += 1;
        open = newOpen;
    }
    return steps - 1;
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), spaces = new Array(), options = [];
    for (var i = 0; i < data.length; i++) {
        var line = new Array();
        var printString = "";
        for (var j = 0; j < data[0].length; j++) {
            if (data[i][j] == "S" || data[i][j] == "a") {
                var curr = new Space(j, i, 0);
                curr.tryHeight(0, 0);
                line.push(curr);
                options.push([i, j]);
                printString = printString.concat("X", " ");
            }
            else if (data[i][j] == "E") {
                line.push(new Space(j, i, 26));
                printString = printString.concat("26", " ");
            }
            else {
                line.push(new Space(j, i, data[i].charCodeAt(j) - 97));
                printString = printString.concat((data[i].charCodeAt(j) - 97).toString(), " ");
            }
        }
        spaces.push(line);
    }
    var open = options, maximum = 0, steps = 1;
    while (maximum < 26 && steps < 500 && open.length > 0) {
        var newOpen = new Array();
        for (var i = 0; i < open.length; i++) {
            for (var j = 0; j < 4; j++) {
                var newIndex = [open[i][0], open[i][1]];
                newIndex[0] += j == 0 ? 1 : 0;
                newIndex[1] += j == 1 ? 1 : 0;
                newIndex[0] += j == 2 ? -1 : 0;
                newIndex[1] += j == 3 ? -1 : 0;
                if (newIndex[0] >= 0 && newIndex[1] >= 0 && newIndex[0] < data.length && newIndex[1] < data[0].length) {
                    var res = spaces[newIndex[0]][newIndex[1]].tryHeight(spaces[open[i][0]][open[i][1]].getHeight(), steps);
                    if (res != -1) {
                        newOpen.push(newIndex);
                        if (res > maximum) {
                            maximum = res;
                        }
                    }
                }
            }
        }
        steps += 1;
        open = newOpen;
    }
    return steps - 1;
}
console.log(part1());
console.log(part2());
