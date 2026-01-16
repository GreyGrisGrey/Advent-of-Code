class Node:
    def __init__(self, name):
        self.name = name
        self.ins = []
        self.outs = []
        self.vals = None
        self.good = False
    
    
    def getGood(self):
        return self.good
    
    
    def getVals(self):
        return self.vals.copy()
    
    
    def checkGood(self):
        if self.name == "out":
            self.vals = [0, 0, 0, 1]
            self.good = True
            for i in self.ins:
                i.checkGood()
            return
        proceed = True
        for i in self.outs:
            if not i.getGood():
                proceed = False
        if proceed:
            self.changeVals()
            self.good = True
            for i in self.ins:
                i.checkGood()
            
    
    def changeVals(self):
        self.vals = [0, 0, 0, 0]
        for i in self.outs:
            newVals = i.getVals()
            for j in range(4):
                if self.name == "fft":
                    newVals[1] += newVals[3]
                    newVals[0] += newVals[2]
                    newVals[2] = newVals[3] = 0
                if self.name == "dac":
                    newVals[2] += newVals[3]
                    newVals[0] += newVals[1]
                    newVals[1] = newVals[3] = 0
                self.vals[j] += newVals[j]
    
    
    def addIn(self, new):
        self.ins.append(new)
    
    
    def addOut(self, new):
        self.outs.append(new)
                

def part1():
    nodesLists = []
    nameDict = {"out": -1}
    nodeDict = {}
    nodeDict["out"] = Node("out")
    for pos, data in enumerate(open("in.txt").read().split("\n")):
        data = data.split(" ")
        nameDict[pos] = data[0].strip(":")
        nodesLists.append(data[1::])
        nodeDict[data[0].strip(":")] = Node(data[0].strip(":"))
    for pos, data in enumerate(nodesLists):
        curr = nodeDict[nameDict[pos]]
        for i in data:
            adj = nodeDict[i]
            curr.addOut(adj)
            adj.addIn(curr)
    nodeDict["out"].checkGood()
    return sum(nodeDict["you"].getVals())


def part2():
    nodesLists = []
    nameDict = {"out": -1}
    nodeDict = {}
    nodeDict["out"] = Node("out")
    for pos, data in enumerate(open("in.txt").read().split("\n")):
        data = data.split(" ")
        nameDict[pos] = data[0].strip(":")
        nodesLists.append(data[1::])
        nodeDict[data[0].strip(":")] = Node(data[0].strip(":"))
    for pos, data in enumerate(nodesLists):
        curr = nodeDict[nameDict[pos]]
        for i in data:
            adj = nodeDict[i]
            curr.addOut(adj)
            adj.addIn(curr)
    nodeDict["out"].checkGood()
    return nodeDict["svr"].getVals()[0]
        
        

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())