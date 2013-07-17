#23-2-2012
#additional exercise 5
#sample solution

def displayInfo():
    print("Easier Hangman")
    print("This program is a simpler verision of hangman using a list")
    print()

def getWord():
    word = input("Please enter a word for the other player to guess: ")
    return word

def getChances():
    chances = int(input("How many chances should they get to guess the word: "))
    return chances

def constructHangmanList(word):
    #empty list
    hangman = []
    for each in word:
        hangman.append(each)
    return hangman

def constructGuessedCharacterList(hangman):
    #set up list for guesses
    guessedCharacters = []
    for each in hangman:
        guessedCharacters.append("_")
    return guessedCharacters

def setUpGame():
    word = getWord()
    chances = getChances()
    hangman = constructHangmanList(word)
    guessedCharacters = constructGuessedCharacterList(hangman)
    return word,chances,hangman,guessedCharacters


def getGuessCharacter(guessedCharacters,chances):
    print()
    print(guessedCharacters)
    print("you have {0} chances remaining.".format(chances))
    print()
    currentGuess = input("please enter a character to guess: ")
    return currentGuess

def checkGuessCharacter(currentGuess,hangman,guessedCharacters):
    #check guess
    for each in range(len(hangman)):
        if hangman[each] == currentGuess:
            guessedCharacters[each] = currentGuess

def checkWin(guessedCharacters,hangman):
    if guessedCharacters == hangman:
        return True
    else:
        return False

def displayResult(result):
    guessed = result[0]
    word = result[1]
    if guessed:
        print("Well done - you guessed the word!")
    else:
        print("Sorry you didn't guess that the word was {0}.".format(word))
    
def playGame(setUpValues):
    word = setUpValues[0]
    chances = setUpValues[1]
    hangman = setUpValues[2]
    guessedCharacters = setUpValues[3]
    hangman = constructHangmanList(word)
    guessed = False
    while not guessed and chances > 0:
        currentGuess = getGuessCharacter(guessedCharacters,chances)
        checkGuessCharacter(currentGuess,hangman,guessedCharacters)
        chances = chances - 1
        guessed = checkWin(guessedCharacters,hangman)
    return guessed,word

def hangman():
    setUpValues = setUpGame()
    result = playGame(setUpValues)
    displayResult(result)
