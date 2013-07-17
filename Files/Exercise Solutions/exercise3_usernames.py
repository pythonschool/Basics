users = []
with open("usernames_passwords.txt", mode="r",encoding="utf-8") as my_file:
    for line in my_file:
        users.append(line.rstrip("\n").split(','))
print(users)
attempts = 3
logged_in = False
while attempts > 0 and not logged_in:
    username_found = False
    password_found = False
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for details in users:
        if username == details[0] and password == details[1]:
            logged_in = True
        elif username == details[0]:
            username_found = True
    if not logged_in and username_found:
        print("Incorrect password")
    elif not logged_in and not username_found:
        print("This username does not exist")
    attempts -= 1
if logged_in:
    print("Login successful")
else:
    print("You did not login succesfully after 3 attempts")
        

        

