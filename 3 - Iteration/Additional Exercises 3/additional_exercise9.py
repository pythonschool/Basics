#25-01-2012
#additional exercises 3, question 9
#sample solution

print("Hexadecimal to Denary Conversion")
print("This program converts a given hexadecimal number into the")
print("equivalent denary number.")
print()
hexNumber = input("Please enter a hex number to convert: ")

#get lenth of number
lengthHex = len(hexNumber)
print(lengthHex)
denary = 0
for element in range(lengthHex):
    #print(element)
    hexSeg = hexNumber[element]
    
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

    #work out the place value power of 16
    placePower = 16**(lengthHex-(element+1))
    hexSeg = hexSeg * placePower
    denary = denary + hexSeg
    
print(denary)
    

