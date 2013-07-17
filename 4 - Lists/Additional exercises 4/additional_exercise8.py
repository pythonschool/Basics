#6-2-2012
#additional exercise 8
#sample solution
import random

print("Connect 4")
print("This game is Connect 4 for two players")
print()
#create the board
#connect 4 board is 7 columns of 6
board = []
for column in range(7):
    board.append([])
    for row in range(6):
        board[column].append("O")

#set-up game
players = []
for player in range(2):
    tempPlayer = input("Please enter your name: ")
    players.append(tempPlayer)

#decide who plays first
if (random.randint(1,10) % 2) == 0:
    startPlayer = 0
else:
    startPlayer = 1

print()
print("{0} you get to start!".format(players[startPlayer]))

token = input("Whould you like to play as (R)ed or (Y)ellow: ")
if token == "R":
    tokens = ["R","Y"]
else:
    tokens = ["Y","R"]


gameWon = False

while not gameWon:
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

    #get go
    print("It is {0}'s turn...".format(players[startPlayer]))
    shot = input("Which column do you want to place a counter in: ")
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
    #switch to next player
    if not gameWon:
        if startPlayer == 0:
            startPlayer = 1
        else:
            startPlayer = 0
#game won
print()
print("The final board: ")
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
print("{0} you connected 4 - well done!".format(players[startPlayer]))
