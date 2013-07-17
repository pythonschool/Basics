#23-2-2012
#additional exercise 8
#sample solution
import random

def displayInfo():
    print("Connect 4")
    print("This game is Connect 4 for two players")
    print()

def createBoard():
    #create the board
    #connect 4 board is 7 columns of 6
    board = []
    for column in range(7):
        board.append([])
        for row in range(6):
            board[column].append("O")
    return board

def getPlayerNames():
    #set-up game
    players = []
    for player in range(2):
        tempPlayer = input("Please enter your name: ")
        players.append(tempPlayer)
    return players

def getStartPlayer():
    #decide who plays first
    if (random.randint(1,10) % 2) == 0:
        startPlayer = 0
    else:
        startPlayer = 1
    return startPlayer

def getStartPlayerToken(startPlayer):
    token = input("Whould you like to play as (R)ed or (Y)ellow: ")
    if token == "R" and startPlayer == 0:
        tokens = ["R","Y"]
    elif token == "R" and startPlayer == 1:
        tokens = ["Y","R"]
    elif token == "Y" and startPlayer == 0:
        tokens = ["Y","R"]
    else:
        tokens = ["R","Y"]
    return tokens

def orderPlayers():
    players = getPlayerNames()
    startPlayer = getStartPlayer()
    print()
    print("{0} you get to start!".format(players[startPlayer]))
    tokens = getStartPlayerToken(startPlayer)
    return players,startPlayer,tokens

def setUpGame():
    board = createBoard()
    playerSettings = orderPlayers()
    return board, playerSettings

def displayCurrentBoard(board):
    print()
    print("The board currently looks like this: ")
    print()
    for row in range(6):
        for column in range(7):
            if column < 6:
                print("{0} ".format(board[column][row]),end=" ")
            else:
                print("{0}".format(board[column][row]))
    print()
    print("A  B  C  D  E  F  G")
    print()

def getTurn(players,startPlayer):
    #get go
    print("It is {0}'s turn...".format(players[startPlayer]))
    shot = input("Which column do you want to place a counter in: ")
    return shot

def playCounter(shot,board,tokens,startPlayer):
    print("tokens {0}".format(tokens))
    print("startPlayer {0}".format(startPlayer))
    #play counter
    if shot == "A":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[0][counter] == "O":
                board[0][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "B":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[1][counter] == "O":
                board[1][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "C":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[2][counter] == "O":
                board[2][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "D":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[3][counter] == "O":
                board[3][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "E":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[4][counter] == "O":
                board[4][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "F":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[5][counter] == "O":
                board[5][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1
    elif shot == "G":
        played = False
        counter = 5
        while not played and counter >= 0:
            if board[6][counter] == "O":
                board[6][counter] = tokens[startPlayer]
                played = True
            else:
                counter = counter - 1

def checkVerticalWin(board,startPlayer,tokens):
    gameWon = False
    #check to see if currentplayer has won vertically
    connect = 0
    for each in board:
        for item in each:
            if item == tokens[startPlayer]:
                connect = connect + 1
            else:
                connect = 0
            if connect == 4:
                gameWon = True
    return gameWon

def checkHorizontalWin(board,startPlayer,tokens):
    gameWon = False
    #check to see if currentplayer has won horizontally
    connect = 0
    for row in range(6):
        for column in range(7):
            if board[column][row] == tokens[startPlayer]:
                connect = connect + 1
            else:
                connect = 0
            if connect == 4:
                gameWon = True
    return gameWon

def checkForWin(board,startPlayer,tokens):
    win = checkVerticalWin(board,startPlayer,tokens)
    if win == False:
        win = checkHorizontalWin(board,startPlayer,tokens)
    return win

def setNextPlayer(startPlayer):
    #switch to next player
    if startPlayer == 0:
        startPlayer = 1
    else:
        startPlayer = 0
    return startPlayer

def playGame(board,playerSettings):
    players = playerSettings[0]
    startPlayer = playerSettings[1]
    print(startPlayer)
    tokens = playerSettings[2]
    gameWon = False
    while not gameWon:
        displayCurrentBoard(board)
        shot = getTurn(players,startPlayer)
        playCounter(shot,board,tokens,startPlayer)
        gameWon = checkForWin(board,startPlayer,tokens)
        if not gameWon:
            startPlayer = setNextPlayer(startPlayer)
    return board,startPlayer,players

def displayWinDetails(gameStats):
    board = gameStats[0]
    startPlayer = gameStats[1]
    players = gameStats[2]
    displayCurrentBoard(board)
    print()
    print("{0} you connected 4 - well done!".format(players[startPlayer]))


def connectFour():
    setup = setUpGame()
    gameStats = playGame(setup[0],setup[1])
    displayWinDetails(gameStats)
