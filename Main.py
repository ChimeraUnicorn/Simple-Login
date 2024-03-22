import time
import sys
from Signup import signup
from Login import login

while 1:
    print("********* Login System *********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("bye")
        sys.exit()
    else:
        print("Wrong Choice!")
