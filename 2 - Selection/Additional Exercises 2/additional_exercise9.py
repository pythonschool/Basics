#23-01-2012
#additional exercises 2, program 9
#sample solution

print("Exam Grades")
print("This program tells you what grade you recieved and how many marks you would")
print("have needed for the next grade up")
print()
mark = int(input("What mark did you get out of 60: "))
gradeUp = True
print()
if mark > 48:
    print("You got an A!")
    gradeUp = False
elif mark > 42:
    print("You got a B!")
    nextGrade = 48 - mark
elif mark > 36:
    print("You got a C!")
    nextGrade = 42 - mark
elif mark > 30:
    print("You got a D!")
    nextGrade = 36 - mark
elif mark > 24:
    print("You got an E!")
    nextGrade = 36 - mark
else:
    print("You failed")
    nextGrade = 24 - mark
if gradeUp:
    print("You needed {0} additional marks to get the next grade up".format(nextGrade))

    
