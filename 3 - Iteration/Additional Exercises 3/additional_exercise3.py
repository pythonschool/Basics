#25-01-2012
#additional exercises 3, question 3
#sample solution

print("Adding until rogue value")
print("This program adds up values until a rogue values is entered")
print("it then displays the total of the entered values")
print()
enteredValue = None
runningTotal = 0
while enteredValue != 0:
    print("The running total is: {0}.".format(runningTotal))
    print()
    enteredValue = int(input("Please enter a value to add to the running total: "))
    runningTotal = runningTotal + enteredValue
print()
print("The final total is: {0}.".format(runningTotal))
