#23-2-2012
#additional exercise 4
#sample solution

def displayInfo():
    print("Shopping List")
    print("this program stores your shopping list and then displays it")

def getNewItem():
    tempItem = input("Please enter an item for your list: ")
    return tempItem


def addToList(shoppingList,item):
    shoppingList.append(item)
    #notice that there is no return value here for the list...

def displayList(shoppingList):
    #display list
    print()
    print("Shopping List")
    print()
    for item in shoppingList:
        print(item)


def shoppingList():
    #empty list
    shoppingList = []
    finished = False
    while not finished:
        newItem = getNewItem()
        if len(newItem) == 0:
            finished = True
        else:
            addToList(shoppingList,newItem)
    displayList(shoppingList)


    
