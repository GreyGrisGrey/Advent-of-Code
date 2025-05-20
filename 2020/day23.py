#562893147
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def addLeft(self, left):
        self.left = left
    
    def addRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getVal(self):
        return self.val

def printOrder(node):
    while node.getVal() != 1:
        node = node.getRight()
    string = ""
    node = node.getRight()
    while node.getVal() != 1:
        string += str(node.getVal())
        node = node.getRight()
    return string

def part1():
    nums = open("in.txt").readline()
    first = Node(int(nums[0]))
    old = first
    for i in range(len(nums)-1):
        new = Node(int(nums[i+1]))
        old.addRight(new)
        new.addLeft(old)
        old = new
    first.addLeft(new)
    new.addRight(first)
    curr = first
    for i in range(100):
        moved = [curr.getRight()]
        moved.append(moved[0].getRight())
        moved.append(moved[1].getRight())
        forbidden = [moved[0].getVal(), moved[1].getVal(), moved[2].getVal()]
        dest = curr.getVal() - 1
        while dest in forbidden or dest == 0:
            dest -= 1
            if dest <= 0:
                dest = 9
        destCup = curr
        while destCup.getVal() != dest:
            destCup = destCup.getLeft()
            dest
        destNext = destCup.getRight()
        destCup.addRight(moved[0])
        moved[0].addLeft(destCup)
        curr.addRight(moved[2].getRight())
        moved[2].getRight().addLeft(curr)
        moved[2].addRight(destNext)
        destNext.addLeft(moved[2])
        curr = curr.getRight()
    while curr.getVal() != 1:
        curr = curr.getRight()
    return printOrder(curr)

def part2(size, turns):
    nums = open("in.txt").readline()
    first = Node(int(nums[0]))
    old = first
    destDict = {}
    destDict[int(nums[0])] = first
    for i in range(len(nums)-1):
        new = Node(int(nums[i+1]))
        destDict[int(nums[i+1])] = new
        old.addRight(new)
        new.addLeft(old)
        old = new
    for i in range(size-len(nums)):
        new = Node(i+10)
        destDict[i+10] = new
        old.addRight(new)
        new.addLeft(old)
        old = new
    first.addLeft(new)
    new.addRight(first)
    curr = first
    for i in range(turns):
        moved = [curr.getRight()]
        moved.append(moved[0].getRight())
        moved.append(moved[1].getRight())
        forbidden = [moved[0].getVal(), moved[1].getVal(), moved[2].getVal()]
        dest = curr.getVal() - 1
        while dest in forbidden or dest == 0:
            dest -= 1
            if dest <= 0:
                dest = size
        destCup = destDict[dest]
        destNext = destCup.getRight()
        destCup.addRight(moved[0])
        moved[0].addLeft(destCup)
        curr.addRight(moved[2].getRight())
        moved[2].getRight().addLeft(curr)
        moved[2].addRight(destNext)
        destNext.addLeft(moved[2])
        curr = curr.getRight()
    one = destDict[1]
    first = one.getRight()
    second = first.getRight()
    return first.getVal() * second.getVal()
        



print(part1())
print(part2(1000000, 10000000))