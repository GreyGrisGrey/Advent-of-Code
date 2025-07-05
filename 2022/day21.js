"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var Monkey = /** @class */ (function () {
    function Monkey(first, second, third) {
        if (first == "VAL") {
            this.val = parseInt(second);
            this.done = true;
        }
        else {
            this.left = first;
            this.operation = second;
            this.right = third;
            this.done = false;
        }
    }
    Monkey.prototype.checkDone = function () {
        return this.done;
    };
    Monkey.prototype.getVal = function () {
        return this.val;
    };
    Monkey.prototype.setVal = function (newNum) {
        this.val = newNum;
        this.done = true;
    };
    Monkey.prototype.getOp = function () {
        return this.operation;
    };
    Monkey.prototype.getPrevs = function () {
        return [this.left, this.right];
    };
    return Monkey;
}());
function generate(file, humn) {
    if (humn === void 0) { humn = -1; }
    var data = fs.readFileSync(file, "utf8").split("\r\n"), nameMap = new Map;
    for (var i = 0; i < data.length; i++) {
        var curr = data[i].split(" "), key = curr[0].slice(0, 4), newMonk = void 0;
        if (curr.length == 2) {
            if (humn != -1 && key == "humn") {
                newMonk = new Monkey("VAL", humn.toString(), "a");
            }
            else {
                newMonk = new Monkey("VAL", curr[1], "a");
            }
            nameMap.set(key, newMonk);
        }
        else {
            newMonk = new Monkey(curr[1], curr[2], curr[3]);
            nameMap.set(key, newMonk);
        }
    }
    return nameMap;
}
function recurse(curr, nameMap) {
    var currMonk = nameMap.get(curr);
    if (currMonk.checkDone()) {
        return currMonk.getVal();
    }
    var prevs = currMonk.getPrevs(), val = [recurse(prevs[0], nameMap), recurse(prevs[1], nameMap)], newVal;
    if (currMonk.getOp() == "*") {
        newVal = val[0] * val[1];
    }
    else if (currMonk.getOp() == "+") {
        newVal = val[0] + val[1];
    }
    else if (currMonk.getOp() == "/") {
        newVal = val[0] / val[1];
    }
    else if (currMonk.getOp() == "-") {
        newVal = val[0] - val[1];
    }
    currMonk.setVal(newVal);
    return newVal;
}
function partBoth() {
    var results = new Array;
    for (var i = 0; i < 2; i++) {
        var newMap = generate("in.txt", i), prevs = newMap.get("root").getPrevs(), val = [recurse(prevs[0], newMap), recurse(prevs[1], newMap)];
        results.push(val[0]);
        results.push(val[1]);
    }
    return [recurse("root", generate("in.txt")), (results[0] - results[1]) / (results[0] - results[2])];
}
console.log(partBoth());
