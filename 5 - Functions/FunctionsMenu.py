# FunctionsMenu.py
#menu program


def mainmenu ():
    choice = 0
    while choice != "4":
        
        print()
        print()
        print("Choose from this menu")
        print()
        print("1 - Maze Game")
        print("2 - Guessing Game")
        print("3 - Quiz")
        print("4 - Exit")
        print ()
        choice = input("Enter 1,2,3 or 4")

        if choice == "1":
             mazeGame()
        elif choice == "2":
             numberGuesser()
        elif choice == "3":
             quiz()
        elif choice == "4":
                print ("Thanks for using the program.")
        else:
            print("Please enter 1,2,3 or 4 only")


def mazeGame():
    print("Now running Maze game...")
def numberGuesser():
    print("Now running Guessing game")
def quiz():
    print("Now running quiz")
              






