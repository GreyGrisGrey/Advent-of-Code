class Wire:
    def __init__(self, name, value=None):
        self.left = None
        self.right = None
        self.operation = None
        self.name = name
        if value == "1":
            self.value = True
        elif value == "0":
            self.value = False
        else:
            self.value = None
    
    def runOp(self):
        if self.value != None:
            return self.value
        else:
            leftVal = self.left.runOp()
            rightVal = self.right.runOp()
            if self.operation == "XOR":
                self.value = rightVal != leftVal
            elif self.operation == "AND":
                self.value = (rightVal and leftVal)
            elif self.operation == "OR":
                self.value = (rightVal or leftVal)
            return self.value
    
    def setInputs(self, left, right, input):
        self.left = left
        self.right = right
        self.operation = input
    
    def printSelf(self):
        print("WIRE")
        print(self.name, self.value)
        if self.left != None:
            print(self.left.getName(), " ", self.operation, " ", self.right.getName())
    
    def getName(self):
        return self.name
    
    def backTrack(self):
        returnList = set()
        if self.left != None:
            lefts = self.left.backTrack()
            rights = self.right.backTrack()
            for i in lefts:
                returnList.add(i)
            for i in rights:
                returnList.add(i)
            returnList.add(self.name)
            return returnList
        else:
            return [self.name]
    
    def prevStep(self):
        if self.left != None:
            return [self.left.name, self.right.name]
        else:
            return None
    
    def getOperation(self):
        return self.operation

def part1():
    wireDict = {}
    inputs = True
    maxZ = 0
    for i in open("input.txt"):
        if i == "\n":
            inputs = False
        elif inputs:
            newWireVals = i.split(": ")
            wireDict[newWireVals[0]] = Wire(newWireVals[0], newWireVals[1].strip())
        else:
            line = i.split(" ")
            left = line[0]
            right = line[2]
            out = line[4].strip()
            if line[0] not in wireDict:
                wireDict[line[0]] = Wire(line[0])
            if line[2] not in wireDict:
                wireDict[line[2]] = Wire(line[2])
            if out not in wireDict:
                wireDict[out] = Wire(out)
            wireDict[out].setInputs(wireDict[left], wireDict[right], line[1])
            if out[0] == "z" and int(out[1::]) > maxZ:
                maxZ = int(out[1::])
    for i in wireDict:
        wireDict[i].runOp()
    outstring = ""
    for i in range(maxZ+1):
        rightStr = str((maxZ) - i)
        if len(rightStr) == 1:
            rightStr = "0" + rightStr
        if wireDict["z" + rightStr].runOp():
            outstring += "1"
        else:
            outstring += "0"
    print(int(outstring, 2))

#doesn't autofix, but does help
def part2():
    wireDict = {}
    inputs = True
    maxZ = 0
    for i in open("input.txt"):
        if i == "\n":
            inputs = False
        elif inputs:
            newWireVals = i.split(": ")
            wireDict[newWireVals[0]] = Wire(newWireVals[0], newWireVals[1].strip())
        else:
            line = i.split(" ")
            left = line[0]
            right = line[2]
            out = line[4].strip()
            if line[0] not in wireDict:
                wireDict[line[0]] = Wire(line[0])
            if line[2] not in wireDict:
                wireDict[line[2]] = Wire(line[2])
            if out not in wireDict:
                wireDict[out] = Wire(out)
            wireDict[out].setInputs(wireDict[left], wireDict[right], line[1])
            if out[0] == "z" and int(out[1::]) > maxZ:
                maxZ = int(out[1::])
    for i in wireDict:
        wireDict[i].runOp()
    for i in range(maxZ):
        if i < 10:
            nextCheck = "z0" + str(i)
            nextX = "x0" + str(i)
            nextY = "y0" + str(i)
            prevX = "x0" + str(i-1)
            prevY = "y0" + str(i-1)
        else:
            nextCheck = "z" + str(i)
            nextX = "x" + str(i)
            nextY = "y" + str(i)
            if i == 10:
                prevX = "x0" + str(i-1)
                prevY = "y0" + str(i-1)
            else:
                prevX = "x" + str(i-1)
                prevY = "y" + str(i-1)
        checkList = wireDict[nextCheck].backTrack()
        if len(checkList) != 1 + (6*i) and i != 1 and i != 0:
            print("Error on ", str(nextCheck), ", wrong set length.")
            print("Should be :", str(1 + (6*i)), " Is :", str(len(checkList)))
            firstCarry = findOutput(prevX, prevY, "AND", wireDict)
            doubleCarry = findOutput(xor, carry, "AND", wireDict)
            orCarry = findOutput(doubleCarry, firstCarry, "OR", wireDict)
            print(firstCarry, doubleCarry, orCarry)
            print("Possibilities:")
            for j in wireDict:
                if wireDict[j].prevStep() != None and orCarry in wireDict[j].prevStep():
                    print(j)
            print("Second possibilities:")
            test = wireDict[nextCheck].prevStep()
            test2 = wireDict[test[0]].prevStep()
            test3 = wireDict[test[1]].prevStep()
            print(test2, test3)
            if "x31" in test2:
                print(findOutput(test3[0], test3[1], "XOR", wireDict))
            else:
                print(findOutput(test2[0], test2[1], "XOR", wireDict))
            break
        if i == 0:
            if not ("z00" in checkList and "x00" in checkList and "y00" in checkList):
                print("Error on z00, x00 XOR y00 mapped wrong")
        elif i == 1:
            for j in checkList:
                if j != "x00" and j != "x01" and j != "y01" and j != "y00" and j != "z01":
                    newCheck = wireDict[j].backTrack()
                    if len(newCheck) == 3 and "x01" in newCheck and "y01" in newCheck:
                        xor = j
                    elif len(newCheck) == 3 and "x00" in newCheck and "y00" in newCheck:
                        carry = j
            if xor == None:
                print("Error on z01, no appropriate XOR gate")
            if carry == None:
                print("Error on z01, no appropriate carry AND gate")
            prevCheckList = checkList
        else:
            newChecks = checkList - prevCheckList
            prevCheckList = newChecks | checkList
            remove = set()
            firstCarry = None
            doubleCarry = None
            orCarry = None
            newXor = None
            for j in newChecks:
                if j[0] == "x" or j[0] == "y" or j[0] == "z":
                    remove.add(j)
                else:
                    testVals = wireDict[j].prevStep()
                    if testVals != None:
                        currOperation = wireDict[j].getOperation()
                        if currOperation == "XOR" and nextX in testVals and nextY in testVals:
                            newXor = j
                        elif currOperation == "AND" and prevX in testVals and prevY in testVals:
                            firstCarry = j
                        elif currOperation == "AND" and xor in testVals and carry in testVals:
                            doubleCarry = j
                        elif currOperation == "OR":
                            checkBool = True
                            for k in testVals:
                                if k not in newChecks:
                                    checkBool = False
                            if checkBool:
                                orCarry = j
            if firstCarry == None:
                print("Error on ", str(nextCheck), ", missing firstCarry")
                print(newChecks, orCarry, doubleCarry, firstCarry, newXor)
                print("Incorrect output:", prevX, prevY)
                print(findOutput(prevX, prevY, "AND", wireDict))
                break
            if newXor == None:
                print("Error on ", str(nextCheck), ", missing newXor")
                print(newChecks, orCarry, doubleCarry, firstCarry, newXor)
                print("Incorrect output:", nextX, nextY)
                print(findOutput(nextX, nextY, "XOR", wireDict))
                break
            if doubleCarry == None:
                print("Error on ", str(nextCheck), ", missing doubleCarry")
                print(newChecks, orCarry, doubleCarry, firstCarry, newXor)
                print("Incorrect output:")
                print(findOutput(xor, carry, "AND", wireDict))
                break
            if orCarry == None:
                print("Error on ", str(nextCheck), ", missing orCarry")
                print(newChecks, orCarry, doubleCarry, firstCarry, newXor)
                print("Incorrect output:", firstCarry, doubleCarry)
                print(findOutput(firstCarry, doubleCarry, "OR", wireDict))
                break
            if findOutput(newXor, orCarry, "XOR", wireDict) != nextCheck:
                print("Error on ", str(nextCheck), ", wrong check")
                print("Issue at : ")
                print(newXor, orCarry, findOutput(newXor, orCarry, "XOR", wireDict))
                break
            newChecks = newChecks - remove
            xor = newXor
            carry = orCarry

def findOutput(left, right, operation, mapping):
    for i in mapping:
        tests = mapping[i].prevStep()
        if tests != None and left in tests and right in tests and mapping[i].getOperation() == operation:
            return i
    return


part1()
part2()