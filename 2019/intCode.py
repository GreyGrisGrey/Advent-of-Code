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
                noun, verb = getWords(self.index, self.spaces)
                self.spaces[self.spaces[self.index + 3]] = noun + verb
                self.index += 4
            # Multiply locations i+1 and i+2, write to location i+3
            case 2: 
                noun, verb = getWords(self.index, self.spaces)
                self.spaces[self.spaces[self.index + 3]] = noun * verb
                self.index += 4
            # Write input to target location
            # Known issue: Currently inserts "None" into self.spaces if called without input
            case 3:
                self.spaces[self.spaces[self.index + 1]] = self.inputs[0]
                self.index += 2
                if self.delFlag:
                    del self.inputs[0]
            # Output target location
            case 4:
                self.out = [True, self.spaces[self.spaces[self.index + 1]]]
                self.index += 2
            # Jump if i+1 isn't 0
            case 5:
                noun, verb = getWords(self.index, self.spaces)
                self.index = verb if noun != 0 else self.index + 3
            # Jump if i+1 is 0
            case 6:
                noun, verb = getWords(self.index, self.spaces)
                self.index = verb if noun == 0 else self.index + 3
            # Set register to 1 if i+1 < i+2, otherwise 0
            case 7:
                noun, verb = getWords(self.index, self.spaces)
                self.spaces[self.spaces[self.index + 3]] = 1 if noun < verb else 0
                self.index += 4
            # Set register to 1 if i+1 == i+2, otherwise 0
            case 8:
                noun, verb = getWords(self.index, self.spaces)
                self.spaces[self.spaces[self.index + 3]] = 1 if noun == verb else 0
                self.index += 4
            # Unknown Opcode, error
            case _:
                print("Error: Unknown Opcode")
                print("Opcode:", self.spaces[self.index], "Location:", self.index)
                self.state = 2


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

# Gets first two target locations following specified index
def getWords(index, spaces):
    noun = spaces[spaces[index + 1]] if getDigit(spaces[index], 2) == 0 else spaces[index + 1]
    verb = spaces[spaces[index + 2]] if getDigit(spaces[index], 3) == 0 else spaces[index + 2]
    return noun, verb