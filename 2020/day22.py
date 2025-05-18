class Queue:
    def __init__(self):
        self.list = []
        self.items = 0
    
    def append(self, item):
        self.list.append(item)
        self.items += 1
    
    def remove(self):
        if self.items != 0:
            self.items -= 1
            temp = self.list[0]
            del self.list[0]
            return temp
        return None
    
    def stringify(self):
        string = ""
        for i in self.list:
            string += str(i) + ":"
        return string.strip(":")
    
    def calcVal(self):
        total = 0
        for i in self.list:
            total += i * self.items
            self.items -= 1
        return total
    
    def getItems(self):
        return self.items
    
    def clone(self, depth):
        newQueue = Queue()
        for i in range(depth):
            temp = self.list[i]
            newQueue.append(temp)
        return newQueue


def part1():
    p1 = Queue()
    p2 = Queue()
    p1Done = False
    for i in open("in.txt", "r"):
        if i[0] == "P" and p1Done:
            curr = p2
        elif i[0] == "P":
            curr = p1
        elif i[0] == "\n":
            p1Done = True
        else:
            curr.append(int(i.strip("\n")))
    while p1.getItems() != 0 and p2.getItems() != 0:
        p1Card = p1.remove()
        p2Card = p2.remove()
        if p1Card > p2Card:
            p1.append(p1Card)
            p1.append(p2Card)
        else:
            p2.append(p2Card)
            p2.append(p1Card)
    return max(p1.calcVal(), p2.calcVal())

def recurseGame(p1, p2):
    cache = {}
    while p1.getItems() != 0 and p2.getItems() != 0:
        p1String = p1.stringify()
        p2String = p2.stringify()
        if p1String in cache or p2String in cache:
            return 1
        cache[p1String] = True
        cache[p2String] = True
        p1Card = p1.remove()
        p2Card = p2.remove()
        if p1.getItems() >= p1Card and p2.getItems() >= p2Card:
            copyA = p1.clone(p1Card)
            copyB = p2.clone(p2Card)
            res = recurseGame(copyA, copyB)
            if res == 1:
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)
        else:
            if p1Card > p2Card:
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)
    if p1.getItems() != 0:
        return 1
    return 2

def part2():
    p1 = Queue()
    p2 = Queue()
    p1Done = False
    for i in open("in.txt", "r"):
        if i[0] == "P" and p1Done:
            curr = p2
        elif i[0] == "P":
            curr = p1
        elif i[0] == "\n":
            p1Done = True
        else:
            curr.append(int(i.strip("\n")))
    res = recurseGame(p1, p2)
    return max(p1.calcVal(), p2.calcVal())

print(part1())
print(part2())
