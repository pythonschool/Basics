#16-01-2012
#additional exercise 3
#sample solution

print("Dividing")
print("This program asks for two numbers and then divides them,")
print("it then displays the number of times one goes into the other and")
print("the remainder")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
print()
intans = num1 // num2
remainder = num1 % num2
print("{0}/{1} = {2} remainder {3}.".format(num1,num2,intans,remainder))
