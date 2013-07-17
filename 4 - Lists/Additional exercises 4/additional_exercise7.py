#6-2-2012
#additional exercise 7
#sample solution

print("Shopping List")
print("this program can add items to a shopping list and also sort and delete the")
print("the list.")
shoppingList = []
exitList = False
print()
while not exitList:
    #display menu
    print("1. Add items to your list")
    print("2. Sort the list")
    print("3. Display the list")
    print("4. Delete the list")
    print()
    print("0. Exit the program")
    print()
    menuChoice = int(input("Please select an option: "))
    if menuChoice == 1:
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
    elif menuChoice == 2:
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
        print()
        print("List sorted")
        print()
    elif menuChoice == 3:
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
    elif menuChoice == 4:
        shoppingList = []
        print()
        print("List deleted")
        print()
    elif menuChoice == 0:
        exitList = True
    else:
        print("That was not a valid choice, please try again")

    
