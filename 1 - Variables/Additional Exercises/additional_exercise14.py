#16-01-2012
#additional exercise 14
#sample solution

print("Quote Formatter")
print("This program displays a given quote in different formats")
print()
quote = input("Please enter a quote to format: ")
print(quote)
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.title())
replaceWord = input("Which word in the quote would you like to replace: ")
replaceWith = input("Please enter the word to replace it with: ")
print("The original quote is: {0}".format(quote))
print("The new quote is: {0}".format(quote.replace(replaceWord,replaceWith)))


