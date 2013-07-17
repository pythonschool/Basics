#23-02-2012
#additional exercises 2, question 3
#sample solution

def convertToSegment(hexSeg):
    if hexSeg == 'A':
        hexSeg = 10
    elif hexSeg == 'B':
        hexSeg = 11
    elif hexSeg == 'C':
        hexSeg = 12
    elif hexSeg == 'D':
        hexSeg = 13
    elif hexSeg == 'E':
        hexSeg = 14
    elif hexSeg == 'F':
        hexSeg = 15
    else:
        hexSeg = int(hexSeg)
    return hexSeg

def displayInfo():
    print("Hexadecimal to Denary Conversion")
    print("This program converts a given hexadecimal number into the")
    print("equivalent denary number.")
    print()

def getHexNumber():
    hexNumber = input("Please enter a hex number to convert: ")
    return hexNumber

def convertToDenary(hexNumber):
    denary = 0
    #get lenth of number
    lengthHex = len(hexNumber)
    for element in range(lengthHex):
        #print(element)
        hexSeg = hexNumber[element]
        hexSeg = convertToSegment(hexSeg)
        #work out the place value power of 16
        placePower = 16**(lengthHex-(element+1))
        hexSeg = hexSeg * placePower
        denary = denary + hexSeg
    return denary

def displayDenaryValue(denary):
    print(denary)


def hexToDenary():
    displayInfo()
    hexNum = getHexNumber()
    denNum = convertToDenary(hexNum)
    displayDenaryValue(denNum)
    

