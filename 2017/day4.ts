import * as fs from "fs";

function part1(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let total = 0
    for (let i = 0; i < data.length; i++) {
        let wordMap: Map<string, boolean> = new Map()
        let words = data[i].split(" ")
        let good = true;
        for (let j = 0; j < words.length; j++) {
            if (wordMap.has(words[j])) {
                good = false
            } else {
                wordMap.set(words[j], true)
            }
        }
        if (good) {
            total += 1
        }
    }
    return total
}

function wordToCount(word: string): string {
    let numMap: Map<string, number> = new Map()
    let newString = ""
    for (let i = 97; i < 123; i++) {
        numMap.set(String.fromCharCode(i), 0)
    }
    for (let i = 0; i < word.length; i++) {
        numMap.set(word[i], numMap.get(word[i])! + 1)
    }
    for (let i = 97; i < 123; i++) {
        newString += numMap.get(String.fromCharCode(i))!.toString()
    }
    return newString
}

function part2(): number {
    let data = fs.readFileSync("in.txt", "utf8").split("\r\n")
    let total = 0
    for (let i = 0; i < data.length; i++) {
        let wordMap: Map<string, boolean> = new Map()
        let words = data[i].split(" ")
        let good = true;
        for (let j = 0; j < words.length; j++) {
            let newWord = wordToCount(words[j])
            if (wordMap.has(newWord)) {
                good = false
            } else {
                wordMap.set(newWord, true)
            }
        }
        if (good) {
            total += 1
        }
    }
    return total
}

console.log("Part 1:", part1())
console.log("Part 2:", part2())