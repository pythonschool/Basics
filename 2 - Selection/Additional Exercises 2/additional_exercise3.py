#23-01-2012
#additional exercises 2, program 3
#sample solution

print("Seasons")
print("This program asks for a month number and then displays the season")
print()
month = int(input("Please enter the month number: "))
print()
if month == 1 or month == 2 or month == 12:
    print("This month is in Winter")
elif month == 3 or month == 4 or month == 5:
    print("This month is in Spring")
elif month == 6 or month == 7 or month == 8:
    print("This month is in Summer")
elif month == 9 or month == 10 or month == 11:
    print("This month is in Autumn")
else:
    print("You have entered an invalid month number")
    
