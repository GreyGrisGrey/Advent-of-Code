"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function splitList(val) {
    var index = 0, layers = 0, newArr = new Array;
    for (var i = 0; i < val.length; i++) {
        if (val[i] == "[") {
            layers += 1;
        }
        else if (val[i] == "]") {
            layers -= 1;
        }
        else if (val[i] == "," && layers == 0) {
            newArr.push(val.slice(index, i));
            index = i + 1;
        }
        if (i == val.length - 1) {
            newArr.push(val.slice(index, i + 1));
        }
    }
    return newArr;
}
function firstNum(val) {
    var num = 0, index = 0, flag = false, startIndex = -1;
    while (num == 0) {
        if (index == val.length) {
            return 0;
        }
        if (val[index] != "[" && val[index] != "]" && val[index] != ",") {
            flag = true;
            startIndex = index;
        }
        else if ((val[index] == "[" || val[index] == "]" || val[index] == ",") && flag) {
            num = parseInt(val.slice(startIndex, index));
        }
        index += 1;
    }
    return num;
}
function compareVals(valA, valB) {
    if (!(valA[0] == "[" || valB[0] == "[")) {
        if (parseInt(valA) > parseInt(valB)) {
            return 0;
        }
        else if (parseInt(valA) < parseInt(valB)) {
            return 2;
        }
        else {
            return 1;
        }
    }
    if (valA[0] != "[") {
        valA = "[".concat(valA, "]");
        return compareVals(valA, valB);
    }
    else if (valB[0] != "[") {
        valB = "[".concat(valB, "]");
        return compareVals(valA, valB);
    }
    else {
        var newA = splitList(valA.slice(1, valA.length - 1)), newB = splitList(valB.slice(1, valB.length - 1)), index = 0;
        while (index < newA.length) {
            if (index >= newB.length) {
                return 0;
            }
            var res = compareVals(newA[index], newB[index]);
            if (res != 1) {
                return res;
            }
            index += 1;
        }
        if (newA.length == newB.length) {
            return 1;
        }
        return 2;
    }
}
function part1() {
    var index = 0, step = 1, left = "", right = "", total = 0, data = fs.readFileSync("in.txt", "utf8").split("\r\n");
    for (var i = -1; i < data.length; i++) {
        if (index == 0) {
            left = data[i + 1];
        }
        else if (index == 1) {
            right = data[i + 1];
        }
        else {
            index = -1;
            if (compareVals(left, right) == 2) {
                total += step;
            }
            step += 1;
        }
        index += 1;
    }
    return total;
}
function part2() {
    var index = 0, step = 1, left = "", right = "", total = 1, data = fs.readFileSync("in.txt", "utf8").split("\r\n"), ordering = new Array;
    for (var i = 0; i < data.length; i++) {
        if (data[i].length > 0) {
            ordering.push(data[i]);
        }
    }
    ordering.push("[[2]]");
    ordering.push("[[6]]");
    for (var i = 0; i < ordering.length; i++) {
        for (var j = 0; j < ordering.length - 1; j++) {
            var res = compareVals(ordering[j], ordering[j + 1]);
            if (res == 0) {
                var temp = ordering[j];
                ordering[j] = ordering[j + 1];
                ordering[j + 1] = temp;
            }
        }
    }
    var nextNum = 1;
    index = 1;
    for (var i = 0; i < ordering.length; i++) {
        if (ordering[i] == "[[2]]") {
            total *= index;
        }
        else if (ordering[i] == "[[6]]") {
            total *= index;
        }
        index += 1;
    }
    return total;
}
console.log(part1());
console.log(part2());
