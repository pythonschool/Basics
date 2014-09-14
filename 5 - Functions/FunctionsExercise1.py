# FunctionsExercise1.py

def inputData():
    number = int(input("Enter a number   "))
    return number

def processData(number):
    if number % 7 == 0:
        # divisible by 7
        return True
    else:
        return False

def outputData(number,result):
    if result:
        print("The number {0} is divisible by 7".format(number))
    else:
        print("The number {0} is not divisible by 7".format(number))

def main():
    userNumber = inputData()
    result = processData(userNumber)
    outputData(userNumber,result)

    
