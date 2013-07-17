with open("shopping.txt", mode="r",encoding="utf-8") as my_file:
    shopping_list = my_file.read().splitlines()
print("My Shopping List")
print()
for count,item in enumerate(shopping_list):
    print("{0}. {1}".format(count+1,item))
