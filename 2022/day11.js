"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function part1() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), index = 0, monkies = new Map(), step = 0, objCount = [];
    for (var i = 0; i < data.length; i++) {
        data[i] = data[i].trim();
        if (data[i] == "") {
            index += 1;
            step = 0;
        }
        else if (step == 0) {
            step += 1;
            monkies.set(index, new Array());
            objCount.push(0);
        }
        else if (step == 1) {
            var currString = data[i].split(": ")[1].split(", "), newAr = new Array();
            for (var j = 0; j < currString.length; j++) {
                newAr.push(parseInt(currString[j]));
            }
            monkies.get(index).push(newAr);
            step += 1;
        }
        else if (step == 2) {
            var currString = data[i].split(" "), newAr = new Array();
            newAr.push(currString[4]);
            if (currString[5] == "old") {
                newAr.push(-1);
            }
            else {
                newAr.push(parseInt(currString[5]));
            }
            monkies.get(index).push(newAr);
            step += 1;
        }
        else if (step == 3) {
            monkies.get(index).push(parseInt(data[i].split(" ")[3]));
            step += 1;
        }
        else if (step == 4) {
            var newAr = new Array();
            newAr.push(parseInt(data[i].split(" ")[5]));
            monkies.get(index).push(newAr);
            step += 1;
        }
        else {
            monkies.get(index)[3].push(parseInt(data[i].split(" ")[5]));
        }
    }
    for (var i = 0; i < 20; i++) {
        for (var j = 0; j < index + 1; j++) {
            var newAr = new Array(), curr = monkies.get(j);
            for (var k = 0; k < curr[0].length; k++) {
                objCount[j] += 1;
                var newNum = 0;
                if (curr[1][0] == "+") {
                    newNum = curr[0][k] + curr[1][1];
                }
                else if (curr[1][1] != -1) {
                    newNum = curr[0][k] * curr[1][1];
                }
                else {
                    newNum = curr[0][k] * curr[0][k];
                }
                newNum = Math.floor(newNum / 3);
                if ((newNum % curr[2]) == 0) {
                    monkies.get(curr[3][0])[0].push(newNum);
                }
                else {
                    monkies.get(curr[3][1])[0].push(newNum);
                }
            }
            curr[0] = new Array();
        }
    }
    var maximums = [0, 0];
    for (var i = 0; i < objCount.length; i++) {
        var temp = objCount[i], swap = 0;
        if (temp > maximums[0]) {
            swap = temp;
            temp = maximums[0];
            maximums[0] = swap;
        }
        if (temp > maximums[1]) {
            swap = temp;
            temp = maximums[1];
            maximums[1] = swap;
        }
    }
    return (maximums[0] * maximums[1]);
}
function part2() {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), index = 0, monkies = new Map(), step = 0, objCount = [], gcd = 1;
    for (var i = 0; i < data.length; i++) {
        data[i] = data[i].trim();
        if (data[i] == "") {
            index += 1;
            step = 0;
        }
        else if (step == 0) {
            step += 1;
            monkies.set(index, new Array());
            objCount.push(0);
        }
        else if (step == 1) {
            var currString = data[i].split(": ")[1].split(", "), newAr = new Array();
            for (var j = 0; j < currString.length; j++) {
                newAr.push(parseInt(currString[j]));
            }
            monkies.get(index).push(newAr);
            step += 1;
        }
        else if (step == 2) {
            var currString = data[i].split(" "), newAr = new Array();
            newAr.push(currString[4]);
            if (currString[5] == "old") {
                newAr.push(-1);
            }
            else {
                newAr.push(parseInt(currString[5]));
            }
            monkies.get(index).push(newAr);
            step += 1;
        }
        else if (step == 3) {
            monkies.get(index).push(parseInt(data[i].split(" ")[3]));
            gcd *= parseInt(data[i].split(" ")[3]);
            step += 1;
        }
        else if (step == 4) {
            var newAr = new Array();
            newAr.push(parseInt(data[i].split(" ")[5]));
            monkies.get(index).push(newAr);
            step += 1;
        }
        else {
            monkies.get(index)[3].push(parseInt(data[i].split(" ")[5]));
        }
    }
    for (var i = 0; i < 10000; i++) {
        for (var j = 0; j < index + 1; j++) {
            var newAr = new Array(), curr = monkies.get(j);
            for (var k = 0; k < curr[0].length; k++) {
                objCount[j] += 1;
                var newNum = 0;
                if (curr[1][0] == "+") {
                    newNum = curr[0][k] + curr[1][1];
                }
                else if (curr[1][1] != -1) {
                    newNum = curr[0][k] * curr[1][1];
                }
                else {
                    newNum = curr[0][k] * curr[0][k];
                }
                while (newNum > gcd) {
                    newNum -= gcd;
                }
                if ((newNum % curr[2]) == 0) {
                    monkies.get(curr[3][0])[0].push(newNum);
                }
                else {
                    monkies.get(curr[3][1])[0].push(newNum);
                }
            }
            curr[0] = new Array();
        }
    }
    var maximums = [0, 0];
    for (var i = 0; i < objCount.length; i++) {
        var temp = objCount[i], swap = 0;
        if (temp > maximums[0]) {
            swap = temp;
            temp = maximums[0];
            maximums[0] = swap;
        }
        if (temp > maximums[1]) {
            swap = temp;
            temp = maximums[1];
            maximums[1] = swap;
        }
    }
    return (maximums[0] * maximums[1]);
}
console.log(part1());
console.log(part2());
