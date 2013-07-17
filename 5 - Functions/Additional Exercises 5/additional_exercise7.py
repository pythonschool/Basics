#23-2-2012
#additional exercise 7
#sample solution

def displayInfo():
    print("Shopping List")
    print("this program can add items to a shopping list and also sort and delete the")
    print("the list.")

def displayMenu():
    #display menu
    print()
    print("1. Add items to your list")
    print("2. Sort the list")
    print("3. Display the list")
    print("4. Delete the list")
    print()
    print("0. Exit the program")
    print()
    menuChoice = int(input("Please select an option: "))
    return menuChoice

def addItems(shoppingList):
    finished = False
    while not finished:
        tempItem = input("Please enter an item for your list: ")
        if len(tempItem) == 0:
            finished = True
        else:
            shoppingList.append(tempItem)
    print()
    print("Items added")
    print()

def bubbleSort(shoppingList):
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

def displayList(shoppingList):
    #display list
    print()
    print("Your current shopping list:")
    if len(shoppingList) > 0:
        for item in shoppingList:
            print(item)
    else:
        print("the list is currently empty")
    print()
    temp = input("Press any key to continue: ")
    print()

def deleteList(shoppingList):
    del shoppingList[:]
    print()
    print("List deleted")
    print()

def listProgram():
    shoppingList = []
    exitList = False
    while not exitList:
        menuChoice = displayMenu()
        if menuChoice == 1:
            addItems(shoppingList)
        elif menuChoice == 2:
            bubbleSort(shoppingList)
        elif menuChoice == 3:
            displayList(shoppingList)
        elif menuChoice == 4:
            deleteList(shoppingList)
        elif menuChoice == 0:
            exitList = True
        else:
            print("That was not a valid choice, please try again")

    
