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
// part 2 is not in any way general
var Face = /** @class */ (function () {
    function Face(grid, start, size, direction) {
        this.spaces = new Map;
        this.tilt = direction;
        for (var i = 0; i < size; i++) {
            for (var j = 0; j < size; j++) {
                if (grid[start[0] + i][start[1] + j] == ".") {
                    this.spaces.set((i) * 1000 + j, true);
                }
                else {
                    this.spaces.set((i) * 1000 + j, false);
                }
            }
        }
    }
    return Face;
}());
var Cube = /** @class */ (function () {
    function Cube() {
        this.adj = [[1, 2, 3, 4], [5, 2, 0, 4], [1, 5, 3, 0], [5, 4, 0, 2], [5, 1, 0, 3], [1, 4, 3, 2]];
        this.dirMap = new Map([[">>", 0], [">^", 0], ["><", 1], ["^^", 0], ["^>", 0], ["^v", 1], ["vv", 0], ["v<", 0], ["v^", 1], ["<v", 0], ["<<", 0], ["<>", 1]]);
        this.maximum = 49;
        this.faces = new Array;
        this.faceMap = new Map;
        this.pairings = new Map;
        for (var i = 0; i < 6; i++) {
            var curr = i.toString();
            for (var j = 0; j < 4; j++) {
                if (j == 0) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), ">");
                }
                else if (j == 1) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "v");
                }
                else if (j == 2) {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "<");
                }
                else {
                    this.pairings.set(curr.concat(":", this.adj[i][j].toString()), "^");
                }
            }
        }
    }
    Cube.prototype.addFace = function (face, position) {
        this.faceMap.set(position, face);
        if (this.faceMap.size == 6) {
            for (var i = 0; i < 6; i++) {
                this.faces.push(this.faceMap.get(i));
            }
        }
    };
    Cube.prototype.swapFace = function (curr) {
        var newFace = 0, dir2 = "", change = 0, fine = -1, wallNum = -1;
        if (curr[0] > 49) {
            newFace = this.adj[curr[2]][0];
            fine = 1;
        }
        else if (curr[0] < 0) {
            newFace = this.adj[curr[2]][2];
            fine = 1;
        }
        else if (curr[1] < 0) {
            newFace = this.adj[curr[2]][3];
            fine = 0;
        }
        else if (curr[1] > 49) {
            newFace = this.adj[curr[2]][1];
            fine = 0;
        }
        for (var i = 0; i < 4; i++) {
            if (this.adj[newFace][i] == curr[2]) {
                if (i == 0) {
                    dir2 = "<";
                    change = this.dirMap.get(curr[3].concat(dir2));
                }
                else if (i == 1) {
                    dir2 = "^";
                    change = this.dirMap.get(curr[3].concat(dir2));
                }
                else if (i == 2) {
                    dir2 = ">";
                    change = this.dirMap.get(curr[3].concat(dir2));
                }
                else if (i == 3) {
                    dir2 = "v";
                    change = this.dirMap.get(curr[3].concat(dir2));
                }
            }
        }
        var news = [0, 0];
        if (dir2 == ">") {
            news[0] = 0;
            if (change == 1) {
                news[1] = 49 - curr[fine];
            }
            else {
                news[1] = curr[fine];
            }
        }
        else if (dir2 == "<") {
            news[0] = 49;
            if (change == 1) {
                news[1] = 49 - curr[fine];
            }
            else {
                news[1] = curr[fine];
            }
        }
        else if (dir2 == "^") {
            news[1] = 49;
            if (change == 1) {
                news[0] = 49 - curr[fine];
            }
            else {
                news[0] = curr[fine];
            }
        }
        else {
            news[1] = 0;
            if (change == 1) {
                news[0] = 49 - curr[fine];
            }
            else {
                news[0] = curr[fine];
            }
        }
        curr[0] = news[0];
        curr[1] = news[1];
        curr[2] = newFace;
        curr[3] = dir2;
    };
    return Cube;
}());
function runInstruct2(curr, currInstruct, cube) {
    if ((curr[3] == ">" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "<")) {
        curr[3] = "^";
    }
    else if ((curr[3] == "^" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "v")) {
        curr[3] = "<";
    }
    else if ((curr[3] == "v" && currInstruct == "L") || (currInstruct == "R" && curr[3] == "^")) {
        curr[3] = ">";
    }
    else if (currInstruct == "L" || currInstruct == "R") {
        curr[3] = "v";
    }
    else {
        while (currInstruct > 0) {
            currInstruct -= moveStep2(curr, cube);
        }
    }
}
function moveStep2(curr, cube) {
    if (curr[3] == ">") {
        curr[0] += 1;
    }
    else if (curr[3] == "<") {
        curr[0] -= 1;
    }
    else if (curr[3] == "v") {
        curr[1] += 1;
    }
    else if (curr[3] == "^") {
        curr[1] -= 1;
    }
    if (curr[0] > 49 || curr[0] < 0 || curr[1] < 0 || curr[1] > 49) {
        cube.swapFace(curr);
    }
    if (!cube.faces[curr[2]].spaces.get(curr[0] + curr[1] * 1000)) {
        runInstruct2(curr, "L", cube);
        runInstruct2(curr, "L", cube);
        moveStep2(curr, cube);
        runInstruct2(curr, "L", cube);
        runInstruct2(curr, "L", cube);
        return 1000000000;
    }
    return 1;
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), size = 50, indices = new Array;
    for (var i = 0; i < 6; i++) {
        for (var j = 0; j < 6; j++) {
            if (i * size < data.length - 1 && j * size < data[i * size].length - 1 && data[i * size][j * size] != " ") {
                indices.push([i * size, j * size]);
            }
        }
    }
    var headings = [0, 1, 0, 1, 0, 1], pos = [0, 1, 2, 3, 5, 4], cube = new Cube();
    for (var i = 0; i < 6; i++) {
        var newFace = new Face(data, indices[i], size, headings[i]);
        cube.addFace(newFace, pos[i]);
    }
    var instructs = parseInstructions(data[data.length - 1]), start = [0, 0, 0, ">"];
    for (var i = 0; i < instructs.length; i++) {
        runInstruct2(start, instructs[i], cube);
    }
    if (start[2] == 4) {
        start[2] = 5;
    }
    else if (start[2] == 5) {
        start[2] = 4;
    }
    start[0] += indices[start[2]][1] + 1;
    start[1] += indices[start[2]][0] + 1;
    var newNum = start[0] * 4 + start[1] * 1000;
    if (start[3] == "^") {
        newNum += 3;
    }
    else if (start[3] == "<") {
        newNum += 2;
    }
    else if (start[3] == "v") {
        newNum += 1;
    }
    return newNum;
}
console.log(part1());
console.log(part2());
