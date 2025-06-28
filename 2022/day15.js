"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function part1() {
    var total = 0, dists = new Map(), sensors = new Map(), data = fs.readFileSync("in.txt", "utf8").split("\r\n"), curr = 0, checked = new Map();
    var target = 2000000;
    for (var i = 0; i < data.length; i++) {
        var line = data[i].split(" "), sensor = [parseInt(line[2].slice(2, line[2].length - 1)), parseInt(line[3].slice(2, line[3].length - 1))];
        var dist = [parseInt(line[8].slice(2, line[8].length - 1)), parseInt(line[9].slice(2, line[9].length))];
        if (dist[1] == target && (!checked.has(dist[0] * 100000000 + dist[1]))) {
            total -= 1;
            checked.set(dist[0] * 100000000 + dist[1], true);
        }
        sensors.set(curr, sensor);
        dists.set(curr, Math.abs(sensor[0] - dist[0]) + Math.abs(sensor[1] - dist[1]));
        curr += 1;
    }
    for (var i = 0; i < 10 * target; i++) {
        var step = [i - (5 * target), target];
        for (var j = 0; j < curr; j++) {
            if (Math.abs(step[0] - sensors.get(j)[0]) + Math.abs(step[1] - sensors.get(j)[1]) <= dists.get(j)) {
                total += 1;
                break;
            }
        }
    }
    return total;
}
function checkValid(val, target) {
    if (val[0] < 0 || val[1] < 0 || val[0] > target || val[1] > target) {
        return false;
    }
    return true;
}
function part2() {
    var total = 0, data = fs.readFileSync("in.txt", "utf8").split("\r\n"), options = new Array(), curr = 0;
    var dists = new Map(), sensors = new Map();
    var target = 4000000;
    for (var i = 0; i < data.length; i++) {
        var line = data[i].split(" "), sensor = [parseInt(line[2].slice(2, line[2].length - 1)), parseInt(line[3].slice(2, line[3].length - 1))];
        var beacon = [parseInt(line[8].slice(2, line[8].length - 1)), parseInt(line[9].slice(2, line[9].length))];
        var dist = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
        for (var j = 0; j < ((dist + 1) * 2) + 1; j++) {
            var newY = sensor[1] + (dist + 1) - j;
            if (j < dist + 2) {
                var coordsA = [sensor[0] + j, newY], coordsB = [sensor[0] - j, newY];
                if (coordsA[0] != coordsB[0]) {
                    if (checkValid(coordsB, target)) {
                        options.push(coordsB);
                    }
                }
                if (checkValid(coordsA, target)) {
                    options.push(coordsA);
                }
            }
            else {
                var coordsA = [sensor[0] + ((dist + 1) * 2) - j, newY], coordsB = [sensor[0] - ((dist + 1) * 2) + j, newY];
                if (coordsA[0] != coordsB[0]) {
                    if (checkValid(coordsB, target)) {
                        options.push(coordsB);
                    }
                }
                if (checkValid(coordsA, target)) {
                    options.push(coordsA);
                }
            }
        }
        dists.set(curr, dist);
        sensors.set(curr, sensor);
        curr += 1;
    }
    for (var i = 0; i < options.length; i++) {
        var goodFlag = true;
        for (var j = 0; j < sensors.size; j++) {
            if (Math.abs(options[i][0] - sensors.get(j)[0]) + Math.abs(options[i][1] - sensors.get(j)[1]) <= dists.get(j)) {
                goodFlag = false;
                break;
            }
        }
        if (goodFlag) {
            return options[i][0] * 4000000 + options[i][1];
        }
    }
    return 1;
}
console.log(part1());
console.log(part2());