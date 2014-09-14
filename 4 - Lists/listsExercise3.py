# ListsExercise3.py

# Write a function which finds the averages of a list of number using a for loop

def averageProg():
    runningTotal = 0
    listOfNumbers = [4,7,9,1,8,6]
    for each in listOfNumbers:
        runningTotal = runningTotal + each
        # each time round the loop add the next item to the running total
    average = runningTotal/len(listOfNumbers)
    # the average is the runningTotal at the end / how many numbers
    print(listOfNumbers)
    print("The average of these numbers is {0:.2f}".format(average))
    
    
