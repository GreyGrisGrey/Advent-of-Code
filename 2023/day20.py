from math import gcd

class Node:
    def __init__(self, name, type = "flip"):
        self.ins = []
        self.name = name
        self.inMemories = []
        self.outs = []
        self.type = type
        self.on = False
        self.lowSig = False
    
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
                self.lowSig = True
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
    
    def getLarge(self):
        if self.type == "conj" and len(self.ins) + len(self.outs) > 6:
            return True
        return False


def partBoth():
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
    conj, nums = [], []
    for i in nodeDict:
        if nodeDict[i].getLarge():
            conj.append(nodeDict[i].getName()[1::])
            nums.append(-1)
    for i in range(30000):
        if i == 1000:
            res1 = total[0] * total[1]
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
        checked = True
        for j in range(len(nums)):
            if nums[j] == -1 and nodeDict[conj[j]].lowSig:
                nums[j] = i + 1
            elif not nodeDict[conj[j]].lowSig:
                checked = False
        if checked and i >= 1000:
            break
    leastCommonMult = nums[0]
    for i in range(len(nums)-1):
        leastCommonMult *= int(nums[i+1]/gcd(leastCommonMult, nums[i+1]))
    return res1, leastCommonMult

print(partBoth())