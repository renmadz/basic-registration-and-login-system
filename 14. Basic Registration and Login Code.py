# Registration and Log in Page Code

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open ("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("\nSuccessfully registered!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open ("users.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")

            if username == stored_user and password == stored_pass:
                print(f"\nWelcome back {username}!")
                print("It worked!")
                return

    print("Invalid credentials, please try again.")

while True:
    print("\nLogin and Registration.")
    print("[1] Register.")
    print("[2] Login.")
    print("[3] Exit.")
    print("=======================\n")

    option = int(input("Select an option: \n"))

    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

# Wrote with the help of AI (specifically the file handling).
# I learned the process of file handling and how it worked.
# I also made the mistake of not paying attention to the text file name I used, leading to confusion on why it was not reading what was registered.
# Make sure that the file name, in this case it is 'users.txt' matches between the registration and login function.