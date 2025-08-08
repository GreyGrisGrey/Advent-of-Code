from math import floor

class intMachine:
    def __init__(self, day, fileName = "in.txt"):
        self.day = day
        self.spaces = initializeMapping(fileName)
        self.index = 0
        self.state = 0
        self.out = [False, 0]
        self.inputs = []
        self.delFlag = True
        self.rel = 0
    
    def clone(self):
        newMachine = intMachine(self.day)
        for i in self.spaces:
            newMachine.setIndex(i, self.spaces[i])
        newMachine.addInputs(self.inputs)
        newMachine.index = self.index
        newMachine.state = self.state
        newMachine.delFlag = self.delFlag
        newMachine.rel = self.rel
        return newMachine
    
    def deleteInputs(self, newDel):
        self.delFlag = newDel
    
    def addInputs(self, newInputs):
        self.inputs.extend(newInputs)
    
    def addInput(self, newInput):
        self.inputs.append(newInput)
    
    def getIndex(self, index):
        return self.spaces[index]
    
    def setIndex(self, index, newVal):
        self.spaces[index] = newVal
    
    def run(self, printOuts = False, getOuts = False):
        while self.state == 0:
            self.step()
            if self.out[0] and printOuts:
                print(self.out[1])
            if self.out[0] and getOuts:
                return [self.state, self.out[1]]
        return [self.state, None]
    
    def step(self):
        if self.state == 0:
            if self.out[0]:
                self.out = [False, 0]
            self.runOp()
            if self.out[0]:
                return [0, self.out[1]]
        return [self.state, None]
    
    # Runs singular code step
    def runOp(self):
        instruct = getInstruct(self.spaces[self.index])
        match instruct:
            # End Program
            case 99:
                self.state = 1
            # Add locations i+1 and i+2, write to location i+3
            case 1:
                self.spaces[self.getTarget(2)] = self.getWord(0) + self.getWord(1)
                self.index += 4
            # Multiply locations i+1 and i+2, write to location i+3
            case 2: 
                self.spaces[self.getTarget(2)] = self.getWord(0) * self.getWord(1)
                self.index += 4
            # Write input to target location
            # Known issue: Currently inserts "None" into self.spaces if called without input
            case 3:
                if len(self.inputs) == 0:
                    print("Error: Requested input without providing input")
                    print("Location:", self.index)
                    self.state = 3
                    return
                self.spaces[self.getTarget(0)] = self.inputs[0]
                self.index += 2
                if self.delFlag:
                    del self.inputs[0]
            # Output target location
            case 4:
                noun = self.getWord(0)
                self.out = [True, noun]
                self.index += 2
            # Jump if i+1 isn't 0
            case 5:
                noun, verb = self.getWord(0), self.getWord(1)
                self.index = verb if noun != 0 else self.index + 3
            # Jump if i+1 is 0
            case 6:
                noun, verb = self.getWord(0), self.getWord(1)
                self.index = verb if noun == 0 else self.index + 3
            # Set register to 1 if i+1 < i+2, otherwise 0
            case 7:
                noun, verb = self.getWord(0), self.getWord(1)
                self.spaces[self.getTarget(2)] = 1 if noun < verb else 0
                self.index += 4
            # Set register to 1 if i+1 == i+2, otherwise 0
            case 8:
                noun, verb = self.getWord(0), self.getWord(1)
                self.spaces[self.getTarget(2)] = 1 if noun == verb else 0
                self.index += 4
            case 9:
                self.rel += self.getWord(0)
                self.index += 2
            # Unknown Opcode, error
            case _:
                print("Error: Unknown Opcode")
                print("Opcode:", self.spaces[self.index], "Location:", self.index)
                self.state = 2
    
    # Retrieves data associated with index + parse code
    def getWord(self, adder):
        return self.checkVal(self.spaces[self.getTarget(adder)])
    
    # Retrieves location associated with index + parse code
    def getTarget(self, adder):
        match getDigit(self.spaces[self.index], 2 + adder):
            case 0:
                targ = self.checkVal(self.spaces[self.checkVal(self.index + 1 + adder)])
            case 1:
                targ = self.checkVal(self.index + 1 + adder)
            case 2:
                targ = self.checkVal(self.spaces[self.checkVal(self.index + 1 + adder)] + self.rel)
        return targ
    
    # Checks if a given index has a memory address, adds a memory address for it if not. Returns index checked.
    def checkVal(self, val):
        if val not in self.spaces:
            self.spaces[val] = 0
        return val


# Several functions currently outside class on the basis that they may have uses outside the class.
# Remains to be seen.

# Generates registry from filename
def initializeMapping(filename = "in.txt"):
    spaces = {}
    curr = 0
    for i in open(filename).read().split(","):
        spaces[curr] = int(i)
        curr += 1
    return spaces
    
def getDigit(num, index):
    return floor(num/10**index) % 10

def getInstruct(num):
    return num % 100