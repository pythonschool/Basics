#2-2-2012
#additional exercise 1
#sample solution

print("Shopping List")
print("this program stores your shopping list and then displays it")

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
for item in shoppingList:
    print(item)
    
