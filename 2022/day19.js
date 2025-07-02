"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function canBuild(costMap, currResource, currBots, maximums) {
    var res = new Array;
    for (var i = 0; i < costMap.size; i++) {
        var costs = costMap.get(i), check = true;
        if (currBots[i] >= maximums[i]) {
            check = false;
        }
        for (var j = 0; j < currResource.length; j++) {
            if (currResource[j] < costs[j]) {
                check = false;
            }
        }
        res.push(check);
    }
    return res;
}
function build(index, costMap, currResource, currBots) {
    var costs = costMap.get(index), result = [currResource.slice(), currBots.slice()];
    for (var i = 0; i < currResource.length - 1; i++) {
        result[0][i] -= costs[i];
    }
    result[1][index] += 1;
    return result;
}
function recurse1(costMap, currResource, currBots, time, maxTime, best, maximums, cache) {
    if (time == maxTime) {
        return currResource[3];
    }
    if ((maxTime - time) * (currBots[3] + 2) + currResource[3] < best) {
        return 0;
    }
    var options = canBuild(costMap, currResource, currBots, maximums);
    for (var i = 0; i < 4; i++) {
        currResource[i] += currBots[i];
    }
    for (var i = 0; i < 4; i++) {
        if (options[3 - i]) {
            var newArrs = build(3 - i, costMap, currResource, currBots), res_1 = recurse(costMap, newArrs[0], newArrs[1], time + 1, maxTime, best, maximums, cache);
            best = res_1 > best ? res_1 : best;
        }
    }
    var res = recurse(costMap, currResource, currBots, time + 1, maxTime, best, maximums, cache);
    return (res > best) ? res : best;
}
function recurse(costMap, currResource, currBots, time, maxTime, best, maximums, cache) {
    if (time == maxTime) {
        return currResource[3];
    }
    if (currResource[3] + (currBots[3] * (maxTime - time)) + ((maxTime - time - 1) * (maxTime - time) / 2) < best) {
        return 1;
    }
    var key = currBots.join().concat(",", currResource.join(), ",", time.toString());
    if (cache.has(key)) {
        return cache.get(key);
    }
    var options = canBuild(costMap, currResource, currBots, maximums);
    for (var i = 0; i < 4; i++) {
        currResource[i] += currBots[i];
    }
    for (var i = 0; i < 4; i++) {
        if (options[3 - i]) {
            var newArrs = build(3 - i, costMap, currResource, currBots), res_2 = recurse(costMap, newArrs[0], newArrs[1], time + 1, maxTime, best, maximums, cache);
            best = res_2 > best ? res_2 : best;
        }
    }
    var res = recurse(costMap, currResource, currBots, time + 1, maxTime, best, maximums, cache);
    best = res > best ? res : best;
    cache.set(key, best);
    return best;
}
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), end = 0;
    for (var i = 0; i < data.length; i++) {
        var robotCost = new Map, dataSplit = data[i].split(" ");
        robotCost.set(0, [parseInt(dataSplit[6]), 0, 0]);
        robotCost.set(1, [parseInt(dataSplit[12]), 0, 0]);
        robotCost.set(2, [parseInt(dataSplit[18]), parseInt(dataSplit[21]), 0]);
        robotCost.set(3, [parseInt(dataSplit[27]), 0, parseInt(dataSplit[30])]);
        var maximums = [Math.max(parseInt(dataSplit[12]), parseInt(dataSplit[18]), parseInt(dataSplit[27])), parseInt(dataSplit[21]), parseInt(dataSplit[30]), 90];
        end += recurse(robotCost, [0, 0, 0, 0], [1, 0, 0, 0], 0, 24, 0, maximums, new Map) * (i + 1);
    }
    return end;
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), end = 1;
    for (var i = 0; i < 3; i++) {
        var robotCost = new Map, dataSplit = data[i].split(" ");
        robotCost.set(0, [parseInt(dataSplit[6]), 0, 0]);
        robotCost.set(1, [parseInt(dataSplit[12]), 0, 0]);
        robotCost.set(2, [parseInt(dataSplit[18]), parseInt(dataSplit[21]), 0]);
        robotCost.set(3, [parseInt(dataSplit[27]), 0, parseInt(dataSplit[30])]);
        var maximums = [Math.max(parseInt(dataSplit[12]), parseInt(dataSplit[18]), parseInt(dataSplit[27])), parseInt(dataSplit[21]), parseInt(dataSplit[30]), 30];
        end *= recurse(robotCost, [0, 0, 0, 0], [1, 0, 0, 0], 0, 32, 0, maximums, new Map);
    }
    return end;
}
console.log(part1());
console.log(part2());
