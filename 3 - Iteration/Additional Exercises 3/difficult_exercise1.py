#25-01-2012
#additional exercises 3, question 10
#sample solution

print("Linear Search")
print("This program locates a specific character in a string")
print("using linear search.")
print()
targetStr = input("Please enter a string: ")
character = None
#create a blank string for output
outputStr = ""
while character != 0:
    character = input("Please enter a character to find in the string: ")
    found = False
    for eachChar in range(len(targetStr)):
        if targetStr[eachChar] == character:
            if outputStr == None:
                outputStr = character
                found = True
            elif len(outputStr) == len(targetStr):
                #get the OutputStr up to the character before the character to add
                #add the character to this string and then add the Output string from
                #the character after the character we add
                outputStr = outputStr[:eachChar] + character + outputStr[eachChar+1:]
                found = True
            else:
                outputStr = outputStr + character
                found = True
        else:
            if len(outputStr) < len(targetStr):
                outputStr = outputStr + "_"
    if found:
        print()
        print("The letter {0} was in the string".format(character))
        print("the string is now {0}".format(outputStr))
        print()
    else:
        print()
        print("The letter {0} was not in the string".format(character))
        print("the string is still {0}".format(outputStr))
        print()
    print()
    print(outputStr)
    

