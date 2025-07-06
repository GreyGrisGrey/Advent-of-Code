"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function findDirection(map, space, step) {
    if (!map.has(space - 10000) && !map.has(space - 10001) && !map.has(space - 9999) && !map.has(space - 1)) {
        if (!map.has(space + 10000) && !map.has(space + 10001) && !map.has(space + 9999) && !map.has(space + 1)) {
            return 0;
        }
    }
    var options = [-10000, 10000, -1, 1], index = (step % 4);
    for (var i = 0; i < 4; i++) {
        if (!map.has(space - 10000) && !map.has(space - 10001) && !map.has(space - 9999) && index == 0) {
            return -10000;
        }
        else if (!map.has(space + 10000) && !map.has(space + 10001) && !map.has(space + 9999) && index == 1) {
            return 10000;
        }
        else if (!map.has(space - 1) && !map.has(space - 10001) && !map.has(space + 9999) && index == 2) {
            return -1;
        }
        else if (!map.has(space + 1) && !map.has(space + 10001) && !map.has(space - 9999) && index == 3) {
            return 1;
        }
        index = index == 3 ? 0 : index + 1;
    }
    return 0;
}
function checkGood(map, space) {
    if (map.get(space + 1) == map.get(space) || map.get(space - 1) == map.get(space)) {
        return false;
    }
    else if (map.get(space + 10000) == map.get(space) || map.get(space - 10000) == map.get(space)) {
        return false;
    }
    return true;
}
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), mapping = new Map;
    for (var i = 0; i < data.length; i++) {
        for (var j = 0; j < data[i].length; j++) {
            if (data[i][j] == "#") {
                mapping.set(i * 10000 + j, true);
            }
        }
    }
    for (var i = 0; i < 10; i++) {
        var planning = new Map, valid = new Map, newMap = new Map, keys_1 = mapping.keys();
        for (var j = 0; j < mapping.size; j++) {
            var curr = keys_1.next().value, res = findDirection(mapping, curr, i);
            planning.set(curr, res + curr);
            if (!valid.has(res + curr)) {
                valid.set(res + curr, true);
            }
            else {
                valid.set(res + curr, false);
            }
        }
        keys_1 = mapping.keys();
        for (var j = 0; j < mapping.size; j++) {
            var curr = keys_1.next().value;
            if (valid.get(planning.get(curr))) {
                newMap.set(planning.get(curr), true);
            }
            else {
                newMap.set(curr, true);
            }
        }
        mapping = newMap;
    }
    var keys = mapping.keys(), maximum = [0, 0], minimum = [999, 999];
    for (var i = 0; i < mapping.size; i++) {
        var curr = keys.next().value, second = curr % 10000;
        if (second > maximum[1] && second < 5000) {
            maximum[1] = second;
        }
        if (-(10000 - second) < minimum[1] && second > 5000) {
            minimum[1] = -(10000 - second);
        }
        if (Math.round(curr / 10000) > maximum[0]) {
            maximum[0] = Math.round(curr / 10000);
        }
        if (Math.round(curr / 10000) < minimum[0]) {
            minimum[0] = Math.round(curr / 10000);
        }
    }
    return (maximum[0] - minimum[0] + 1) * (maximum[1] - minimum[1] + 1) - mapping.size;
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), mapping = new Map;
    for (var i = 0; i < data.length; i++) {
        for (var j = 0; j < data[i].length; j++) {
            if (data[i][j] == "#") {
                mapping.set(i * 10000 + j, true);
            }
        }
    }
    var steps = 1;
    for (var i = 0; i < 100000; i++) {
        var planning = new Map, valid = new Map, newMap = new Map, keys = mapping.keys();
        var checkDone = true;
        for (var j = 0; j < mapping.size; j++) {
            var curr = keys.next().value, res = findDirection(mapping, curr, i);
            planning.set(curr, res + curr);
            if (!valid.has(res + curr)) {
                valid.set(res + curr, true);
            }
            else {
                valid.set(res + curr, false);
            }
        }
        keys = mapping.keys();
        for (var j = 0; j < mapping.size; j++) {
            var curr = keys.next().value;
            if (valid.get(planning.get(curr)) && planning.get(curr) != curr) {
                newMap.set(planning.get(curr), true);
                checkDone = false;
            }
            else {
                newMap.set(curr, true);
            }
        }
        mapping = newMap;
        if (checkDone) {
            break;
        }
        steps += 1;
    }
    return steps;
}
console.log(part1());
console.log(part2());
