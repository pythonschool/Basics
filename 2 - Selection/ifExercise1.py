# Exercise 1 if statements
# Write a function that asks the user how old they are.
# Tell them if they are old enough to vote. Then extend the program
# to tell them how many years it is until they can retire (assume at age 65).

def main():
    yourAge = int(input("How old are you? "))
    if yourAge >= 18:
        print("You are old enough to vote")
    else:
        ageToVote = 18- yourAge
        print("You can vote in {0} years ".format(ageToVote))
        
def extension():
    yourAge = int(input("How old are you? "))
    if yourAge >= 18:
        print("You are old enough to vote")
    else:
        ageToVote = 18- yourAge
        print("You can vote in {0} years ".format(ageToVote))
    if yourAge < 65:
        ageToRetire = 65- yourAge
        print("You can retire in {0} years.".format(ageToRetire))
        
    
