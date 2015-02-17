#25-01-2012
#additional exercises 3, question 1
#sample solution

print("Squared Numbers")
print("This program asks the user for a number and then prints out")
print("the squares of all numbers between 1 and the entered number")
print()
number = int(input("Please enter a number: "))
print()
for eachNumber in range(number+1):
    print("{0} squared is {1}.".format(eachNumber,eachNumber*eachNumber))
