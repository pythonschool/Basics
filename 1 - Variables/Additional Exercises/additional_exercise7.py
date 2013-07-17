#16-01-2012
#additional exercise 7
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
print("This will be made up of:")
euro50s = int(euroHolidayMoney // 50)
#this is a mod calculation
remainingEuros = euroHolidayMoney % 50
euro20s = int(remainingEuros // 20)
remainingEuros = remainingEuros % 20
euro10s = int(remainingEuros // 10)
remainingEuros = remainingEuros % 10
euro5s = int(remainingEuros // 5)
remainingEuros = remainingEuros % 5
print("{0} 50 Euro notes.".format(euro50s))
print("{0} 20 Euro notes.".format(euro20s))
print("{0} 10 Euro notes.".format(euro10s))
print("{0} 5 Euro notes.".format(euro5s))
print("and {0} in coins.".format(remainingEuros))
