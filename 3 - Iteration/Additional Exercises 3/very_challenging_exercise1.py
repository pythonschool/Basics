#25-01-2012
#additional exercises 3, question 7
#sample solution

print("Decimal to Binary Conversion")
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
        
    

