with open("animals.txt", mode="r",encoding="utf-8") as my_file:
    for line in my_file:
        print(line.rstrip('\n'))