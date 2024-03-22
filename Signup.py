#This script covers the Signup/registration section of the application


from PassGen import passgen

def signup():
    user = input("Enter Username: ")

    #ensures the user cannot make a second admin account
    if user == "admin":
        print ("Can't use that Username\n")
        return
    
    #if inputed usernam is not admin allows the user to set a password 
    else:
        while True:
            auto_pass = input("Would you like an automatically generated password (Y/n): ")

            if auto_pass.lower() in ['y', 'yes']:
                pwd = passgen()
            elif auto_pass.lower() in ['n', 'no']:
                pwd = input("Enter Password: ")
            else:
                print('Invalid Choice!\n')
                continue

            with open("accounts.txt", "a") as file:
                file.write(f"\n{user} {pwd}")

            return print("You have registered successfully!")