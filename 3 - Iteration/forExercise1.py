# For loop example

# Write a program that will ask the user for a message
# and the number of times they
# want that message displayed. Then output the message that number of times.

def messageLoop():
    message = input("Enter your message ")
    numberOfTimes = int(input("How many times do you want to see this message? "))
    for count in range(numberOfTimes):
        print(message)
        
