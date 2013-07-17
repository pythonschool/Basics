#22-02-2012
#additional exercises 2, question 2
#sample solution

def linearSearch(findItem,searchItem):
    element = 0
    found = False
    lengthOfList = len(searchItem)
    while found == False and element < lengthOfList:
        if findItem == searchItem[element]:
            found = True
        else:
            element = element + 1
    return found

def displayInfo():
    print("Linear Search")
    print("This program locates a specific character in a string")
    print("using linear search.")
    print()

def getString():
    targetStr = input("Please enter a string: ")
    return targetStr

def getSearchCharacter():
    character = input("Please enter a character to find in the string: ")
    return character

def displayResult(character,targetStr,result):
    if result == True:
        print("The character {0} is present in the string {1}".format(character,targetStr))
    else:
        print("The character {0} is not in the string {1}".format(character,targetStr))        

def searchString():
    displayInfo()
    searchStr = getString()
    searchChar = getSearchCharacter()
    result = linearSearch(searchChar,searchStr)
    displayResult(searchChar,searchStr,result)
    
    

