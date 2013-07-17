names = []
for count in range(6):
    name = input("Please enter a name: ")
    names.append(name)

with open("names.txt",mode="w",encoding="utf-8") as my_file:
    for name in names:
        my_file.write(name+"\n")