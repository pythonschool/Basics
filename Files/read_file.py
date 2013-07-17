with open("animals.txt", mode="r",encoding="utf-8") as my_file:
    animals = my_file.read().splitlines()
print(animals)