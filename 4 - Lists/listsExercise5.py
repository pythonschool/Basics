# listsExercise5.py

def diceThrowing():
    # tallychart program
    import random
    tally = [0,0,0,0,0,0]
    for counter in range(30):
        score = random.randint(1, 6)
        tally[score-1] = tally[score-1] + 1 #update tally chart
    print("|{0:<8} | {1:<10}|".format("Number","Frequency"))

    for counter in range(1,7):
        print("|{0:^8} | {1:^10}|".format(counter,tally[counter-1]))
        
              
