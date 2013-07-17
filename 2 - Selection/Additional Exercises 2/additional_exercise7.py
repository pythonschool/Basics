#23-01-2012
#additional exercises 2, program 7
#sample solution

print("Date Formatter")
print("This program asks for the date as three numbers and formats it correctly")
print()
year = int(input("Please enter the year (YYYY): "))
month = int(input("Please enter the month (MM): "))
day = int(input("Please enter the day (DD): "))
print()
if day in (1,21,31):
    dayStr = "{0}st".format(day)
elif day in (2,22):
    dayStr = "{0}nd".format(day)
else:
    dayStr = "{0}th".format(day)

if month == 1:
    monthStr = "January"
elif month == 2:
    monthStr = "February"
elif month == 3:
    monthStr = "March"
elif month == 4:
    monthStr = "April"
elif month == 5:
    monthStr = "May"
elif month == 6:
    monthStr = "June"
elif month == 7:
    monthStr = "July"
elif month == 8:
    monthStr = "August"
elif month == 9:
    monthStr = "September"
elif month == 10:
    monthStr = "October"
elif month == 11:
    monthStr = "November"
elif month == 12:
    monthStr = "December"

print("The date is {0} {1} {2}.".format(dayStr,monthStr,year))
    
