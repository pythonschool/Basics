#16-01-2012
#additional exercise 6
#sample solution

print("Foreign Currency")
print("This program asks for your holiday money (in pounds)")
print("and the current exchange rate then displays the number of")
print("euros you will recieve.")
print()
holidayMoney = int(input("Please enter amount of money you will take on holiday: "))
exchangeRate = float(input("Please enter the current pound-euro exchange rate: "))
print()
#this is a div calculation
euroHolidayMoney = holidayMoney//exchangeRate
print("You will receive {0} Euros for your holiday.".format(euroHolidayMoney))
