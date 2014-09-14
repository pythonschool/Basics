# Football scoring program


def football():
    #Write a program that asks for two football team names, and then the score for each team
    #You program should then say if the teams get 3 points, 1 point or 0 points for the result
    print("This program will tell you how many points each football team scored based on the result")
    teamOne = input("Please enter the name of team one: ")
    teamTwo = input("Please enter the name of team two: ")
    teamOneScore = input("Please enter the score for {0}: ".format(teamOne)) 
    teamTwoScore = input("Please enter the score for {0}: ".format(teamTwo))



    if teamOneScore > teamTwoScore:
        print("{0} score 3 points and {1} score 0 points".format(teamOne,teamTwo))
    elif teamOneScore < teamTwoScore:
        print("{0} score 3 points and {1} score 0 points".format(teamTwo,teamOne))
    else:   #Game must be a draw if the previous two if statements are false
        print("Both {0} and {1} score 1 points.".format(teamOne,teamTwo))
