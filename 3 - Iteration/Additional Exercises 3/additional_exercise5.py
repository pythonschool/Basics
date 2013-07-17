#25-01-2012
#additional exercises 3, question 5
#sample solution

print("Linear Search")
print("This program locates a specific character in a string")
print("using linear search.")
print()
targetStr = input("Please enter a string: ")
character = input("Please enter a character to find in the string: ")
found = False
for eachChar in targetStr:
    if eachChar == character:
        print("The character {0} is present in the string {1}".format(character,targetStr))
        found = True
if not found:
    print("The character {0} is not in the string {1}".format(character,targetStr))
    

