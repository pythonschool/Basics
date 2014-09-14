# Exercise 2 if statements
# Write a function that asks the user to input a number
# between 1 and 20. Give a response which indicates if the
# number is either within the range, too high or too low.


def main():
    number = int(input("Enter a number between 1 and 20 "))
    if number > 20:
        print("Your number is too high")
    elif number < 1:
        print("Your number is too low")
    else:
        print("Thank you!")
  
