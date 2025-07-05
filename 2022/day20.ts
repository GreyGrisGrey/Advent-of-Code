import * as fs from "fs"

class Node {
    val: number
    name: number
    steps: number
    left: Node
    right: Node

    constructor(num: number, label: number, step: number) {
        this.val = num
        this.name = label
        this.steps = step
    }

    setPos(newLeft: Node, newRight: Node): void {
        this.setLeft(newLeft)
        this.setRight(newRight)
    }

    setLeft(newLeft: Node): void {
        this.left = newLeft
    }

    setRight(newRight: Node): void {
        this.right = newRight
    }

    swapStep1(): void {
        this.left.setRight(this.right)
        this.right.setLeft(this.left)
    }

    swapStep2(newLeft: Node, newRight: Node): void {
        newLeft.setRight(this)
        newRight.setLeft(this)
        this.setPos(newLeft, newRight)
    }

    getName(): number {
        return this.name
    }

    getSteps(): number {
        return this.steps
    }

    getLeft(): Node {
        return this.left
    }

    getRight(): Node {
        return this.right
    }
}

function partBoth(mult: number, cycles: number): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), nodes = new Map<number, Node>, firstFlag = true, curr: Node, first: Node, find: Node
    for (let i = 0; i < data.length; i++) {
        if (firstFlag) {
            first = new Node(i, (parseInt(data[i]) * mult) % (data.length - 1), parseInt(data[i]) * mult), curr = first
            firstFlag = false
        } else {
            let newNode = new Node(i, (parseInt(data[i]) * mult) % (data.length - 1), parseInt(data[i]) * mult)
            curr.setRight(newNode)
            newNode.setLeft(curr)
            curr = newNode
            if (parseInt(data[i]) == 0) {
                find = newNode
            }
        }
        nodes.set(i, curr)
    }
    first.setLeft(curr)
    curr.setRight(first)
    for (let i = 0; i < data.length * cycles; i++) {
        let curr = nodes.get(i % data.length), steps = curr.getName(), start = curr
        if (steps <= 0) {
            curr = curr.getLeft()
        }
        start.swapStep1()
        while (steps != 0) {
            curr = steps > 0 ? curr.getRight() : curr.getLeft()
            steps += steps > 0 ? -1 : 1
        }
        start.swapStep2(curr, curr.getRight())
    }
    let res = 0
    for (let i = 0; i < 3001; i++) {
        if (i % 1000 == 0) {
            res += find.getSteps()
        }
        find = find.getRight()
    }
    return res
}

console.log(partBoth(1, 1), partBoth(811589153, 10))