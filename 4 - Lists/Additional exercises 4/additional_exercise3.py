#6-2-2012
#additional exercise 3
#sample solution

print("Easier Hangman")
print("This program is a simpler verision of hangman using a list")
print()
word = input("Please enter a word for the other player to guess: ")
chances = int(input("How many chances should they get to guess the word: "))

#empty list
hangman = []
for each in word:
    hangman.append(each)

#set up list for guesses
guessedCharacters = []
for each in hangman:
    guessedCharacters.append("_")
    

guessed = False
while not guessed and chances > 0:
    print()
    print(guessedCharacters)
    print("you have {0} chances remaining.".format(chances))
    print()
    currentGuess = input("please enter a character to guess: ")
    #check guess
    for each in range(len(hangman)):
        if hangman[each] == currentGuess:
            guessedCharacters[each] = currentGuess
    chances = chances - 1
    #check to see if whole word guessed
    if guessedCharacters == hangman:
        guessed = True
print()
if guessed:
    print("Well done - you guessed the word!")
else:
    print("Sorry you didn't guess that the word was {0}.".format(word))
