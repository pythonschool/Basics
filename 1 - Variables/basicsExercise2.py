# Exercise 2 Basics
# Write a program to input two whole numbers,
# add them together and print the result to the screen. 

def main():
    number1= int(input("Enter your first number "))
    number2= int(input("Enter your second number "))
    sumOfNumbers = number1 + number2
    print("{0} + {1} = {2}".format(number1,number2,sumOfNumbers))
    
