import * as fs from "fs";
function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), index = 0, monkies = new Map(), step = 0, objCount = []
    for (let i = 0; i < data.length; i++) {
        data[i] = data[i].trim()
        if (data[i] == "") {
            index += 1
            step = 0
        } else if (step == 0) {
            step += 1
            monkies.set(index, new Array())
            objCount.push(0)
        } else if (step == 1) {
            let currString = data[i].split(": ")[1].split(", "), newAr = new Array()
            for (let j = 0; j < currString.length; j++) {
                newAr.push(parseInt(currString[j]))
            }
            monkies.get(index).push(newAr)
            step += 1
        } else if (step == 2) {
            let currString = data[i].split(" "), newAr = new Array()
            newAr.push(currString[4])
            if (currString[5] == "old") {
                newAr.push(-1)
            } else {
                newAr.push(parseInt(currString[5]))
            }
            monkies.get(index).push(newAr)
            step += 1
        } else if (step == 3) {
            monkies.get(index).push(parseInt(data[i].split(" ")[3]))
            step += 1
        } else if (step == 4) {
            let newAr = new Array()
            newAr.push(parseInt(data[i].split(" ")[5]))
            monkies.get(index).push(newAr)
            step += 1
        } else {
            monkies.get(index)[3].push(parseInt(data[i].split(" ")[5]))
        }
    }
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < index + 1; j++) {
            let newAr = new Array(), curr = monkies.get(j)
            for (let k = 0; k < curr[0].length; k++) {
                objCount[j] += 1
                let newNum = 0
                if (curr[1][0] == "+") {
                    newNum = curr[0][k] + curr[1][1]
                } else if (curr[1][1] != -1) {
                    newNum = curr[0][k] * curr[1][1]
                } else {
                    newNum = curr[0][k] * curr[0][k]
                }
                newNum = Math.floor(newNum / 3)
                if ((newNum % curr[2]) == 0) {
                    monkies.get(curr[3][0])[0].push(newNum)
                } else {
                    monkies.get(curr[3][1])[0].push(newNum)
                }
            }
            curr[0] = new Array()
        }
    }
    let maximums = [0, 0]
    for (let i = 0; i < objCount.length; i++) {
        let temp = objCount[i], swap = 0
        if (temp > maximums[0]) {
            swap = temp
            temp = maximums[0]
            maximums[0] = swap
        }
        if (temp > maximums[1]) {
            swap = temp
            temp = maximums[1]
            maximums[1] = swap
        }
    }
    return (maximums[0] * maximums[1])
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n"), index = 0, monkies = new Map(), step = 0, objCount = [], gcd = 1
    for (let i = 0; i < data.length; i++) {
        data[i] = data[i].trim()
        if (data[i] == "") {
            index += 1
            step = 0
        } else if (step == 0) {
            step += 1
            monkies.set(index, new Array())
            objCount.push(0)
        } else if (step == 1) {
            let currString = data[i].split(": ")[1].split(", "), newAr = new Array()
            for (let j = 0; j < currString.length; j++) {
                newAr.push(parseInt(currString[j]))
            }
            monkies.get(index).push(newAr)
            step += 1
        } else if (step == 2) {
            let currString = data[i].split(" "), newAr = new Array()
            newAr.push(currString[4])
            if (currString[5] == "old") {
                newAr.push(-1)
            } else {
                newAr.push(parseInt(currString[5]))
            }
            monkies.get(index).push(newAr)
            step += 1
        } else if (step == 3) {
            monkies.get(index).push(parseInt(data[i].split(" ")[3]))
            gcd *= parseInt(data[i].split(" ")[3])
            step += 1
        } else if (step == 4) {
            let newAr = new Array()
            newAr.push(parseInt(data[i].split(" ")[5]))
            monkies.get(index).push(newAr)
            step += 1
        } else {
            monkies.get(index)[3].push(parseInt(data[i].split(" ")[5]))
        }
    }
    for (let i = 0; i < 10000; i++) {
        for (let j = 0; j < index + 1; j++) {
            let newAr = new Array(), curr = monkies.get(j)
            for (let k = 0; k < curr[0].length; k++) {
                objCount[j] += 1
                let newNum = 0
                if (curr[1][0] == "+") {
                    newNum = curr[0][k] + curr[1][1]
                } else if (curr[1][1] != -1) {
                    newNum = curr[0][k] * curr[1][1]
                } else {
                    newNum = curr[0][k] * curr[0][k]
                }
                while (newNum > gcd) {
                    newNum -= gcd
                }
                if ((newNum % curr[2]) == 0) {
                    monkies.get(curr[3][0])[0].push(newNum)
                } else {
                    monkies.get(curr[3][1])[0].push(newNum)
                }
            }
            curr[0] = new Array()
        }
    }
    let maximums = [0, 0]
    for (let i = 0; i < objCount.length; i++) {
        let temp = objCount[i], swap = 0
        if (temp > maximums[0]) {
            swap = temp
            temp = maximums[0]
            maximums[0] = swap
        }
        if (temp > maximums[1]) {
            swap = temp
            temp = maximums[1]
            maximums[1] = swap
        }
    }
    return (maximums[0] * maximums[1])
}

console.log(part1())
console.log(part2())