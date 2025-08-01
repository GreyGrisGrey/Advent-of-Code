"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function check(map) {
    var mapKeys = map.values();
    for (var i = 0; i < map.size; i++) {
        if (mapKeys.next().value > 1) {
            return true;
        }
    }
    return false;
}
function partBoth(num) {
    var input = fs.readFileSync("in.txt", "utf8"), map = new Map(), index = 0;
    while ((index < num) || check(map)) {
        map.set(input[index], (map.has(input[index]) ? map.get(input[index]) + 1 : 1));
        if (index > num - 1) {
            map.set(input[index - num], map.get(input[index - num]) - 1);
        }
        index += 1;
    }
    return index;
}
console.log(partBoth(4));
console.log(partBoth(14));
