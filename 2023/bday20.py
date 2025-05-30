class Node:
    def __init__(self, name, type = "flip"):
        self.ins = []
        self.name = name
        self.inMemories = []
        self.outs = []
        self.type = type
        self.on = False
    
    def addInput(self, input):
        self.ins.append(input)
        self.inMemories.append(False)
    
    def addOutput(self, output):
        self.outs.append(output)
    
    def receiveSignal(self, input, high):
        if self.type == "flip":
            if not high:
                self.on = not self.on
                return self.send(self.on)
            return None
        elif self.type == "conj":
            for i in range(len(self.ins)):
                if self.ins[i] == input:
                    self.inMemories[i] = high
            checker = True
            for i in self.inMemories:
                if not i:
                    checker = False
                    break
            if checker:
                return self.send(False)
            else:
                return self.send(True)
        else:
            return self.send(high)
    
    def send(self, high):
        output = []
        for i in self.outs:
            output.append([i, high, self])
        return output
    
    def getName(self):
        return self.name
    
    def printSelf(self):
        print(self.name)
        ins = []
        outs = []
        for i in self.ins:
            ins.append(i.getName())
        for i in self.outs:
            outs.append(i.getName())
        print(ins)
        print(outs)


def part1():
    nodeDict = {}
    lineList = []
    typeMap = {"%":"flip", "&":"conj", "b":"broadcast"}
    for i in open("in.txt"):
        res = i.strip("\n").split(" -> ")
        lineList.append(res)
        nodeDict[res[0][1::]] = Node(res[0], typeMap[res[0][0]])
    for i in lineList:
        base = nodeDict[i[0][1::]]
        for j in i[1].split(", "):
            if j not in nodeDict:
                nodeDict[j] = Node(j)
            base.addOutput(nodeDict[j])
            nodeDict[j].addInput(base)
    total = [0, 0]
    for i in range(1000):
        liveSignals = [[nodeDict["roadcaster"], False, None]]
        while len(liveSignals) > 0:
            if liveSignals[0][1] == False:
                total[0] += 1
            else:
                total[1] += 1
            res = liveSignals[0][0].receiveSignal(liveSignals[0][2], liveSignals[0][1])
            if res != None:
                for j in res:
                    liveSignals.append(j)
            del liveSignals[0]
    return total[0] * total[1]

print(part1())