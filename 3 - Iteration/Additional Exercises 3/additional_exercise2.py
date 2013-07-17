#25-01-2012
#additional exercises 3, question 2
#sample solution

print("Times Tables")
print("This program asks the user for a number and then prints out")
print("the times table for that number")
print()
number = int(input("Please enter a number: "))
print()
for eachNumber in range(1,13):
    print("{0} x {1:>2} = {2:>3}.".format(number,eachNumber,eachNumber*number))
