# ListsExercises2.py

def wordsBegS():
    wordList = ["and","but","sausage","every","fish","sugar","pie","sultry"]
    numberSwords = 0

    for each in wordList:
        if each[0]=="s":
            print(each)
            numberSwords = numberSwords+1

    print("End of program")
    
