#2-2-2012
#additional exercise 4
#sample solution

print("Shopping List")
print("this program stores your shopping list and then displays it in alphabetical order")

#empty list
shoppingList = []
finished = False
while not finished:
    tempItem = input("Please enter an item for your list: ")
    if len(tempItem) == 0:
        finished = True
    else:
        shoppingList.append(tempItem)

#display list
print()
print("Shopping List")
print()
#bubble sort list
noMoreSwaps = False
while not noMoreSwaps:
    noMoreSwaps = True
    for element in range(len(shoppingList)-1):
        if shoppingList[element] > shoppingList[element+1]:
            noMoreSwaps = False
            temp = shoppingList[element]
            shoppingList[element] = shoppingList[element+1]
            shoppingList[element+1] = temp

#print the list
for item in shoppingList:
    print(item)
    
