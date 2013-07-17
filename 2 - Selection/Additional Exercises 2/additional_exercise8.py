#23-01-2012
#additional exercises 2, program 8
#sample solution

print("Printer Problems")
print("This program helps you troubleshoot your printer")
print()
response = input("Is your printer turned on (Y or N)?: ")
response = response.upper()
if response == 'N':
    print("try making sure the printer is plugged in and the on switch has been pressed")
    response = input("Did this solve your problem (Y or N)?: ")
    if response == 'Y':
        solved = True
    else:
        solved = False
elif response == 'Y':
    solved = False
else:
    solved = False
    print("you need to enter either Y or N as your answer.")
#question 2
if not solved:
    response = input("Is the paper down open and there is paper in the printer?: ")
    if response == 'N':
        print("try opening the paper tray door and putting paper in the printer")
        response = input("Did this solve your problem (Y or N)?: ")
        if response == 'Y':
            solved = True
        else:
            solved = False
    elif response == 'Y':
        solved = False
#question 3 to question x
#you repeat the above

#final section
if not solved:
    print()
    print("sorry, this tool can't fix your printer - call technical support!")
    
