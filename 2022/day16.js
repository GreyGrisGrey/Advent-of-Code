"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var Valve = /** @class */ (function () {
    function Valve(inputs, pressure, name) {
        this.adjacent = inputs;
        this.pressure = pressure;
        this.name = name;
    }
    Valve.prototype.addPressure = function (time) {
        return (time - 1) * this.pressure;
    };
    Valve.prototype.getAdj = function () {
        return this.adjacent;
    };
    Valve.prototype.getAdjMap = function () {
        return this.adjacentMap;
    };
    Valve.prototype.setAdj = function (newMap) {
        this.adjacentMap = newMap;
        return;
    };
    return Valve;
}());
function BFS(start, valves, opens) {
    var currOpen = [[start, 0]], dones = new Map, checked = new Array();
    while (dones.size < opens.length) {
        var nextOpen = valves.get(currOpen[0][0]).getAdj();
        if (opens.includes(currOpen[0][0]) && !checked.includes(currOpen[0][0])) {
            dones.set(currOpen[0][0], currOpen[0][1]);
        }
        checked.push(currOpen[0][0]);
        for (var i = 0; i < nextOpen.length; i++) {
            if (!checked.includes(nextOpen[i])) {
                currOpen.push([nextOpen[i], currOpen[0][1] + 1]);
            }
        }
        currOpen = currOpen.slice(1, currOpen.length);
    }
    valves.get(start).setAdj(dones);
    return;
}
function recurse1(currValve, currNum, valves, opens, time, closed) {
    if (time <= 0) {
        return currNum;
    }
    else if (closed.includes(currValve)) {
        return currNum;
    }
    if (opens.includes(currValve)) {
        currNum += valves.get(currValve).addPressure(time);
        closed.push(currValve);
        time -= 1;
    }
    var mapping = valves.get(currValve).getAdjMap(), best = currNum;
    for (var i = 0; i < opens.length; i++) {
        var newClosed = closed.slice();
        var newStep = recurse1(opens[i], currNum, valves, opens, time - mapping.get(opens[i]), newClosed);
        if (newStep > best) {
            best = newStep;
        }
    }
    return best;
}
// this will take a while but it will do it
function recurse2(currValves, currNum, valves, opens, time, currTime, closed) {
    if (currTime == time - 1) {
        return currNum;
    }
    if ((closed.includes(currValves[0][0]) || closed.includes(currValves[1][0])) && (currValves[0][0] != "AA") && (currValves[1][0] != "AA")) {
        return currNum;
    }
    var best = 0;
    if (currTime == currValves[0][1]) {
        if (!closed.includes(currValves[0][0])) {
            currNum += valves.get(currValves[0][0]).addPressure(time - currTime + 1);
            closed.push(currValves[0][0]);
        }
        var mapping = valves.get(currValves[0][0]).getAdjMap();
        for (var i = 0; i < opens.length; i++) {
            if (opens[i] != currValves[0][0]) {
                var newClosed = closed.slice();
                var newStep = recurse2([[opens[i], currTime + mapping.get(opens[i]) + 1], currValves[1]], currNum, valves, opens, time, currTime, newClosed);
                if (newStep > best) {
                    best = newStep;
                }
            }
        }
    }
    else if (currTime == currValves[1][1]) {
        if (!closed.includes(currValves[1][0])) {
            currNum += valves.get(currValves[1][0]).addPressure(time - currTime + 1);
            closed.push(currValves[1][0]);
        }
        var mapping = valves.get(currValves[1][0]).getAdjMap();
        for (var i = 0; i < opens.length; i++) {
            if (opens[i] != currValves[1][0]) {
                var newClosed = closed.slice();
                var newStep = recurse2([currValves[0], [opens[i], currTime + mapping.get(opens[i]) + 1]], currNum, valves, opens, time, currTime, newClosed);
                if (newStep > best) {
                    best = newStep;
                }
            }
        }
    }
    else {
        best = recurse2(currValves, currNum, valves, opens, time, currTime + 1, closed);
    }
    return best;
}
function partBoth(first) {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), valves = new Map, opens = new Map, opensArr = new Array();
    for (var i = 0; i < data.length; i++) {
        var line = data[i].split(" "), important = [line[1], parseInt(line[4].slice(0, line[4].length - 1).split("=")[1])];
        var adj = new Array();
        for (var j = 9; j < line.length; j++) {
            if (j != line.length - 1) {
                adj.push(line[j].slice(0, line[j].length - 1));
            }
            else {
                adj.push(line[j]);
            }
        }
        var newValve = new Valve(adj, important[1], important[0]);
        valves.set(important[0], newValve);
        if (important[1] != 0) {
            opens.set(important[0], newValve);
            opensArr.push(important[0]);
        }
    }
    for (var i = 0; i < opensArr.length; i++) {
        BFS(opensArr[i], valves, opensArr);
    }
    BFS("AA", valves, opensArr);
    if (first) {
        return recurse1("AA", 0, valves, opensArr, 30, new Array());
    }
    return recurse2([["AA", 0], ["AA", 0]], 0, valves, opensArr, 26, 0, new Array());
}
console.log(partBoth(true), partBoth(false));
