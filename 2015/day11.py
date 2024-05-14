f = open("input.txt")
def increment(password):
    done = False
    index = 7
    As = 8
    while not done:
        if password[index] == "z" and index > -1:
            As = index
            index -= 1
        else:
            change = chr(ord(password[index])+1)
            changeIndex = index
            done = True
    newPassword = ""
    for i in range(8):
        if changeIndex == i:
            newPassword = newPassword + change
        elif(i >= As):
            newPassword = newPassword + "a"
        else:
            newPassword = newPassword + (password[i])
    return newPassword

def checkValid(password):
    for i in password:
        if i == "l" or i == "o" or i == "i":
            return False
    pair1 = None
    pair2 = None
    straight = False
    count = 0
    prevPair = None
    prevStraight1 = password[0]
    prevStraight2 = password[1]
    while count < 8:
        if count > 1 and not straight:
            if ord(prevStraight1)+2 == ord(prevStraight2)+1 == ord(password[count]):
                straight = True
            else:
                prevStraight1 = prevStraight2
                prevStraight2 = password[count]
        if (prevPair == password[count]) and (pair1 != None) and (prevPair != pair1):
            pair2 = True
            prevPair = None
        elif prevPair == password[count]:
            pair1 = prevPair
            prevPair = None
        else:
            prevPair = password[count]
        count += 1
    if pair1 != None and pair2 != None and straight:
        return True
    return False


valid = False
password = f.readline()
password = "cqjxxyzz"
while not valid:
    password = increment(password)
    valid = checkValid(password)
print(password)