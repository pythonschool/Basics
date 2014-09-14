# For loop example

# Write a program that will calculate the average (mean)
##of a set of numbers. This time, the user is to be asked
##how many numbers are to be averaged, they must then enter
##this number of numbers.
##Your program will calculate and display the average of those numbers. 

def averaging():
    numberOfnumbers = int(input("How many numbers do you want to be averaged?"))
    runningTotal = 0
    # don't forget to initialise the running total before you start
    for count in range(numberOfnumbers):
        nextNumber = int(input("Enter the next number  "))
        runningTotal = runningTotal + nextNumber
    average = runningTotal/numberOfnumbers
    print("The average of your numbers is {0}.".format(average))
    
        
