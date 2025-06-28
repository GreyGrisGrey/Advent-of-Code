"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function mapChain(map, chain, num) {
    for (var i = 0; i < chain.length; i++) {
        map.set(chain[i], map.get(chain[i]) + num);
    }
    return;
}
function partBoth() {
    var map = new Map(), input = fs.readFileSync("in.txt", "utf8").split("\r\n"), curr = new Array();
    var currPath = "";
    for (var i = 0; i < input.length; i++) {
        var line = input[i].split(" ");
        if (line[1] == "cd" && line[0] == "$") {
            if (line[2] == "..") {
                curr.splice(curr.length - 1);
                currPath = curr[curr.length - 1];
            }
            else {
                currPath = currPath.concat("-".concat(line[2]));
                curr.push(currPath);
                map.set(currPath, 0);
            }
        }
        else if (line[0] != "$" && line[0] != "dir") {
            mapChain(map, curr, parseInt(line[0]));
        }
    }
    var count = 0, vals = map.values();
    var unused = (70000000 - map.get("-/"));
    var needed = 30000000 - unused;
    var minimum = map.get("-/");
    for (var i = 0; i < map.size; i++) {
        var nextVal = vals.next().value;
        if (nextVal <= 100000) {
            count += nextVal;
        }
        if (nextVal < minimum && nextVal >= needed) {
            minimum = nextVal;
        }
    }
    return [count, minimum];
}
console.log(partBoth());