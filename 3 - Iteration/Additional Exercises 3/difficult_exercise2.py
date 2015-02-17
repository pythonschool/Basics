#25-01-2012
#additional exercises 3, question 11
#sample solution

import random

print("Hangman")
print("This program plays hangman between two players")
print()
player1 = input("Please enter the name of player one: ")
player2 = input("Please enter the name of player two: ")
#decide which player will be guessing
startPlayer = random.randint(1,2)
if startPlayer == 1:
    print()
    print("{0} you get to set the word to guess.".format(player1))
    print()
    splayer = player1
    gplayer = player2
else:
    print()
    print("{0} you get to set the word to guess.".format(player2))
    print()
    splayer = player2
    gplayer = player1

#get the word from the user
targetStr = input("{0}, please enter a string: ".format(splayer))
guesses = int(input("{0}, how many guesses should {1} get?: ".format(splayer,gplayer)))
print()
print()
character = None
#create a blank string for output
outputStr = ""
#counter for guesses
noOfGuesses = 0
wordFound = False
while noOfGuesses < guesses and wordFound == False:
    noOfGuesses = noOfGuesses + 1
    character = input("{0}, please enter a character to find in the string: ".format(gplayer))
    found = False
    for eachChar in range(len(targetStr)):
        if targetStr[eachChar] == character:
            if outputStr == None:
                outputStr = character
                found = True
            elif len(outputStr) == len(targetStr):
                #get the OutputStr up to the character before the character to add
                #add the character to this string and then add the Output string from
                #the character after the character we add
                outputStr = outputStr[:eachChar] + character + outputStr[eachChar+1:]
                found = True
            else:
                outputStr = outputStr + character
                found = True
        else:
            if len(outputStr) < len(targetStr):
                outputStr = outputStr + "_"
    if found:
        print()
        print("The letter {0} was in the string".format(character))
        print("the string is now {0}".format(outputStr))
        print()
    else:
        print()
        print("The letter {0} was not in the string".format(character))
        print("the string is still {0}".format(outputStr))
        print()
    print("You have {0} guesses remaining.".format(guesses-noOfGuesses))
    print()
    print(outputStr)
    #decide if the word has been found
    if outputStr == targetStr:
        wordFound = True

if wordFound:
    print("Well done {0}, you have guessed that the word is {1}".format(gplayer,targetStr))
    print("You took {0} guesses".format(noOfGuesses))
else:
    print("Sorry {0}, you didn't get the word {1} in {2} guesses".format(gplayer,targetStr,guesses))
    

