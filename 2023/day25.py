class Connection:
    def __init__(self):
        self.count = 0
        self.adj = []
    
    def increment(self, num=1):
        self.count += num
    
    def addAdj(self, adj):
        self.adj.append(adj)
    
    def getAdj(self):
        return self.adj
    
    def getCount(self):
        return self.count

class Node:
    def __init__(self, name):
        self.adj = {}
        self.name = name
    
    def addAdj(self, adj, con):
        self.adj[adj] = con
    
    def getName(self):
        return self.name
    
    def getAdj(self):
        return self.adj

def BFS(start, end):
    curr = start
    open = [[start, {}]]
    closed = [curr]
    while len(open) != 0:
        curr = open[0][0]
        if curr == end:
            for i in open[0][1]:
                open[0][1][i].increment()
            break
        closed.append(curr)
        poss = curr.getAdj()
        for i in poss:
            if i not in closed:
                copy = open[0][1].copy()
                copy[i] = poss[i]
                open.append([i, copy])
        del open[0]

def scan(curr, done, blacklist):
    poss = curr.getAdj()
    total = 1
    done[curr] = True
    for i in poss:
        if i not in done and poss[i] not in blacklist:
            total += scan(i, done, blacklist)
    return total

# probabilistic, but it works with high probability, so good enough
from random import randint
def part1():
    connections = {}
    nodes = {}
    nodeNums = {}
    index = 0
    for i in open("in.txt"):
        start, ends = i.strip().split(": ")
        ends = ends.split(" ")
        if start not in nodes:
            nodes[start] = Node(start)
            nodeNums[index] = start
            index += 1
        for j in ends:
            if j not in nodes:
                nodes[j] = Node(j)
                nodeNums[index] = j
                index += 1
            newCon = Connection()
            newCon.addAdj(nodes[start])
            newCon.addAdj(nodes[j])
            connections[start + ":" + j] = newCon
            nodes[start].addAdj(nodes[j], newCon)
            nodes[j].addAdj(nodes[start], newCon)
    for i in range(250):
        if i % 10 == 0:
            print(i)
        BFS(nodes[nodeNums[randint(0, len(nodes)-1)]], nodes[nodeNums[randint(0, len(nodes)-1)]])
    counts = []
    for i in connections:
        counts.append([connections[i].getCount(), i])
    counts = sorted(counts, key = lambda x: x[0])
    blackList = [connections[counts[len(counts)-1][1]], connections[counts[len(counts)-2][1]], connections[counts[len(counts)-3][1]]]
    res = scan(nodes[counts[len(counts)-1][1].split(":")[0]], {}, blackList), scan(nodes[counts[len(counts)-1][1].split(":")[1]], {}, blackList)
    return res[0] * res[1]
    
print(part1())