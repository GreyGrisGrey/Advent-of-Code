"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var Node = /** @class */ (function () {
    function Node(num, label, step) {
        this.val = num;
        this.name = label;
        this.steps = step;
    }
    Node.prototype.setPos = function (newLeft, newRight) {
        this.setLeft(newLeft);
        this.setRight(newRight);
    };
    Node.prototype.setLeft = function (newLeft) {
        this.left = newLeft;
    };
    Node.prototype.setRight = function (newRight) {
        this.right = newRight;
    };
    Node.prototype.swapStep1 = function () {
        this.left.setRight(this.right);
        this.right.setLeft(this.left);
    };
    Node.prototype.swapStep2 = function (newLeft, newRight) {
        newLeft.setRight(this);
        newRight.setLeft(this);
        this.setPos(newLeft, newRight);
    };
    Node.prototype.getName = function () {
        return this.name;
    };
    Node.prototype.getSteps = function () {
        return this.steps;
    };
    Node.prototype.getLeft = function () {
        return this.left;
    };
    Node.prototype.getRight = function () {
        return this.right;
    };
    return Node;
}());
function partBoth(mult, cycles) {
    var data = fs.readFileSync("in.txt", "utf8").split("\r\n"), nodes = new Map, firstFlag = true, curr, first, find;
    for (var i = 0; i < data.length; i++) {
        if (firstFlag) {
            first = new Node(i, (parseInt(data[i]) * mult) % (data.length - 1), parseInt(data[i]) * mult), curr = first;
            firstFlag = false;
        }
        else {
            var newNode = new Node(i, (parseInt(data[i]) * mult) % (data.length - 1), parseInt(data[i]) * mult);
            curr.setRight(newNode);
            newNode.setLeft(curr);
            curr = newNode;
            if (parseInt(data[i]) == 0) {
                find = newNode;
            }
        }
        nodes.set(i, curr);
    }
    first.setLeft(curr);
    curr.setRight(first);
    for (var i = 0; i < data.length * cycles; i++) {
        var curr_1 = nodes.get(i % data.length), steps = curr_1.getName(), start = curr_1;
        if (steps <= 0) {
            curr_1 = curr_1.getLeft();
        }
        start.swapStep1();
        while (steps != 0) {
            curr_1 = steps > 0 ? curr_1.getRight() : curr_1.getLeft();
            steps += steps > 0 ? -1 : 1;
        }
        start.swapStep2(curr_1, curr_1.getRight());
    }
    var res = 0;
    for (var i = 0; i < 3001; i++) {
        if (i % 1000 == 0) {
            res += find.getSteps();
        }
        find = find.getRight();
    }
    return res;
}
console.log(partBoth(1, 1), partBoth(811589153, 10));
