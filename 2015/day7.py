from queue import Queue
class Wire:
    def __init__(self, name, parameters, operation):
        self.name = name
        self.operation = operation
        self.parameters = parameters
        self.next = []
        self.value = None
        try:
            self.parameters[0] = self.assignVal("{0:b}".format(int(self.parameters[0]))[::-1])
        except:
            self.next = []
        try:
            self.parameters[1] = self.assignVal("{0:b}".format(int(self.parameters[1]))[::-1])
        except:
            self.next = []
    
    def assignVal(self, z):
        num = []
        for i in range(16):
            if i < 16 - len(z):
                num.append("0")
            else:
                num.append(z[15-i])
        return num
    
    def checkToAssign(self):
        check = False
        if (len(self.parameters) == 2) and (type(self.parameters[0]) is list) and (type(self.parameters[1]) is list):
            check = True
        elif (len(self.parameters) == 1) and type(self.parameters[0]) is list:
            check = True
        if check:
            match self.operation:
                case "ASSIGN":
                    self.assignFunction()
                case "NOT":
                    self.notFunction()
                case "AND":
                    self.andFunction()
                case "OR":
                    self.orFunction()
                case "LSHIFT":
                    self.lShiftFunction()
                case "RSHIFT":
                    self.rShiftFunction()
            return True
        else:
            return False

    def notFunction(self):
        self.value = []
        for i in self.parameters[0]:
            if i == "0":
                self.value.append("1")
            else:
                self.value.append("0")
        pass

    def assignFunction(self):
        self.value = []
        for i in self.parameters[0]:
            self.value.append(i)
        pass

    def andFunction(self):
        self.value = []
        for i in range(16):
            if self.parameters[0][i] == self.parameters[1][i] == "1":
                self.value.append("1")
            else:
                self.value.append("0")
        pass

    def orFunction(self):
        self.value = []
        for i in range(16):
            if self.parameters[0][i] == "1" or self.parameters[1][i] == "1":
                self.value.append("1")
            else:
                self.value.append("0")
        pass

    def lShiftFunction(self):
        self.value = []
        shift = 0
        for i in range(16):
            shift += (2 ** (15-i)) * (int(self.parameters[1][i]))
        for i in range(16):
            if i+shift <16:
                self.value.append(self.parameters[0][i+shift])
            else:
                self.value.append("0")
        pass

    def rShiftFunction(self):
        self.value = []
        shift = 0
        for i in range(16):
            shift += (2 ** (15-i)) * (int(self.parameters[1][i]))
        for i in range(16):
            if i-shift >= 0:
                self.value.append(self.parameters[0][i-shift])
            else:
                self.value.append("0")
        pass

commands = ["assign", "not", "lshift", "rshift", "and", "or"]
f = open("input.txt")
wires = []
endWire = None
for i in f:
    command = i.split()
    if len(command) == 3:
        newWire = Wire(command[2], [command[0]], "ASSIGN")
        wires.append(newWire)
    elif len(command) == 4:
        newWire = Wire(command[3], [command[1]], "NOT")
        wires.append(newWire)
    else:
        newWire = Wire(command[4], [command[0], command[2]], command[1])
        wires.append(newWire)
    if newWire.name == "a":
        endWire = newWire
for i in wires:
    for j in wires:
        if i.name in j.parameters:
            i.next.append(j)
nextSet = Queue()
for i in wires:
    try:
        if len(i.parameters) == 1 and type(i.parameters[0]) is list:
            i.value = i.parameters[0]
            for j in i.next:
                if len(j.parameters) == 1:
                    j.parameters[0] = i.value
                elif type(j.parameters[0]) == list:
                    j.parameters[1] = i.value
                elif type(j.parameters[1]) == list:
                    j.parameters[0] = i.value
                elif j.parameters[0] == i.name:
                    j.parameters[0] = i.value
                else:
                    j.parameters[1] = i.value
                nextSet.put(j)
        else:
            try:
                i.parameters[0] = int(i.parameters[0])
            except:
                try:
                    i.parameters[1] = int(i.parameters[1])
                except:
                    pass
    except:
        pass
count = 1000000
while not nextSet.empty():
    nextWire = nextSet.get()
    if nextWire.value != None:
        pass
    elif nextWire.checkToAssign():
        for i in nextWire.next:
            if len(i.parameters) == 1:
                i.parameters[0] = nextWire.value
            elif type(i.parameters[0]) == list:
                i.parameters[1] = nextWire.value
            elif type(i.parameters[1]) == list:
                i.parameters[0] = nextWire.value
            elif i.parameters[0] == nextWire.name:
                i.parameters[0] = nextWire.value
            else:
                i.parameters[1] = nextWire.value
            nextSet.put(i)
    else:
        nextSet.put(nextWire)
for i in wires:
    newParameters = []
    newValue = ""
    for j in i.parameters:
        newLine = ""
        for k in j:
            newLine = newLine + k
        newParameters.append(newLine)
    for j in i.value:
        newValue = newValue + j
    print(newParameters, i.operation, newValue, i.name)
print("done", endWire.value, endWire.name)
# options
# has two parameters, 1 is an int
# has two parameters, both are wires
# has one parameter, a wire