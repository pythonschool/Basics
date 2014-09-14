## ListsExercise4.py



def farmList():
    print("Please enter six farming terms")
    termList = []
    for counter in range(6):
        term = input("Enter the next term ")
        termList.append(term)
    print(termList)

def farmList2():
    print("Please enter six farming terms")
    termList = []
    for counter in range(6):
        term = input("Enter the next term ")
        termList.append(term)
    reverseOrder = input("Do you want it printed out in reverse? (y/n)")
    if reverseOrder == "y":
        print(termList[::-1])
    else:
        print(termList)


def farmList3():
    print("Please enter six farming terms")
    termList = []
    for counter in range(6):
        term = input("Enter the next term ")
        termList.append(term)
    reverseOrder = input("Do you want it printed out in reverse? (y/n)")
    if reverseOrder == "y":
        print(termList[::-1])
    else:
        print(termList)
    whichTerm = int(input("Which term (1-6) would you like to see again? "))
    print(termList[whichTerm-1])  # minus 1 as our list starts at 0
