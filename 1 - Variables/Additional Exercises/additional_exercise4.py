#16-01-2012
#additional exercise 4
#sample solution

("Dividing - improved")
print("This program asks for two numbers and then divides them,")
print("it then displays the number of times one goes into the other")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
print()
#many ways to do this
intans = num1 // num2
#intans = int(num1/num2)
#intans = int(round(num1/num2,0))
remainder = num1 % num2
print("{0}/{1} = {2}.".format(num1,num2,intans,remainder))
