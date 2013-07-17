#23-02-2012
#additional exercises 2, question 1
#sample solution

#clearly this solution isn't as nice as our earlier one (day one additional
#exerises 3, question 2) but it does demonstrate use of functions with parameters
#quite simply

def displayInfo():
    print("Times Tables")
    print("This program asks the user for a number and then prints out")
    print("the times table for that number")
    print()

def getTableNumber():
    number = int(input("Please enter a number: "))
    return number

def createTable(number):
    table = []
    for eachNumber in range(1,13):
        entry = (number, eachNumber,eachNumber*number)
        table.append(entry)
    return table

def displayTable(table):
    for entry in table:
        print("{0} x {1:>2} = {2:>3}".format(entry[0],entry[1],entry[2]))


def timesTable():
    displayInfo()
    number = getTableNumber()
    table = createTable(number)
    displayTable(table)
