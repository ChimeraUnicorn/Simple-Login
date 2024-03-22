#This script covers the login portion of the application


def login():
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")
    
    #Opens and reads the accounts.txt file
    with open("accounts.txt", "r") as file:
        users = dict(line.split() for line in map(str.strip, file) if line)

    #checks to see if the username and passwords are correct
    if user in users and pwd == users[user]:
        print("Logged in successfully!")

        #detects if user is an admin and gives them specified admin privileges
        if user == "admin":
            accounts = input("Would you like to view all user accounts Y/n: ")

            if accounts.lower() in ["y", "yes"]:
                with open("accounts.txt", "r") as file:
                    for line in file:
                        print(line.strip())
            
            else:
                print ("You've been logged out\n")
                return
    else:
        print("Login Failed! \n")