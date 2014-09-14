# ListsExercises1.py

def largest():
    maxNumber = 0
    numberList = [15,4,26,1,9,21,3,6,13]
    for each in numberList:
        if each>maxNumber:
            maxNumber = each
    print("The largest number in the list is {0}".format(maxNumber))
    
