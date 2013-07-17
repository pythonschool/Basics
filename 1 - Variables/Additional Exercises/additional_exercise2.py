#16-01-2012
#additional exercise 2
#sample solution

print("Number Multiply and Divsion")
print("This program asks for three numbers, adds the first two together")
print("then divides the total by the third number before displaying the answer")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
num3 = int(input("Please enter a third number: "))
print()
ans = (num1 + num2) / num3
print("The total of ({0} + {1}) / {2} is {3}.".format(num1,num2,num3,ans))
