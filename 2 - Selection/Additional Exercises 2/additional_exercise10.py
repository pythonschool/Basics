#23-01-2012
#additional exercises 2, program 10
#sample solution

print("Seasons and Days of the month")
print("This program asks for a month number and then displays the season")
print("it also displays the number of days in the month")
print()
month = int(input("Please enter the month number: "))
year = int(input("Please enter the year: "))
print()
if month in (1,2,12):
    print("This month is in Winter")
elif month in (3,4,5):
    print("This month is in Spring")
elif month in (6,7,8):
    print("This month is in Summer")
elif month in (9,10,11):
    print("This month is in Autumn")
else:
    print("You have entered an invalid month number")

#days
if month == 2:
    if (year % 400) == 0:
        print('There are 29 days in this month')
    elif (year % 100) == 0:
        print('There are 28 days in this month')
    elif (year % 4) == 0:
        print('There are 29 days in this month')
    else:
        print('There are 28 days in this month')
elif month in (4,6,9,11):
    print("This month has 30 days")
elif month in (1,3,5,7,8,10):
    print("This month has 31 days")
    
