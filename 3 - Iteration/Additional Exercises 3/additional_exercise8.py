#25-01-2012
#additional exercises 3, question 8
#sample solution

print("Decimal to Hexadecimal Conversion")
print("This program converts a given decimal number into the")
print("equivalent hexadecimal number.")
print()
decimalNumber = int(input("Please enter a number to convert: "))
#keep a copy so that we can print it later as we will be using decimal number
decimalNumberCopy = decimalNumber
binaryString = ""
if decimalNumber == 0:
    binaryString = "00000000"
else:
    while decimalNumber > 0:
        #work out whether a 0 or 1 goes in the next position
        positionValue = str(decimalNumber % 2)
        print(positionValue)
        #append to string
        binaryString = positionValue + binaryString
        #
        decimalNumber = decimalNumber // 2
        
#make sure number has eight bits
if len(binaryString) < 8:
    addZeros = 8 - len(binaryString)
    for eachZero in range(addZeros):
        binaryString = "0" + binaryString
print()
print("The binary equivalent is {0}".format(binaryString))
#
#get hex segments
hexA = binaryString[:4]
hexB = binaryString[4:]
finalhex = ""
for eachSegment in (hexA, hexB):
    denary = int(eachSegment[0])*8 + int(eachSegment[1])*4 + int(eachSegment[2])*2 + int(eachSegment[3])*1
    print(denary)
    if denary == 10:
        denary = 'A'
    elif denary == 11:
        denary = 'B'
    elif denary == 12:
        denary = 'C'
    elif denary == 13:
        denary = 'D'
    elif denary == 14:
        denary = 'E'
    elif denary == 15:
        print('got here')
        denary = 'F'
    print(denary)
    finalhex = finalhex + str(denary)
print()
print("{0} in hexadecimal is {1}".format(decimalNumberCopy,finalhex))
        
    

