#This script covers the auto-generated passwords
import string
import random

def passgen():
    possible_chars = ""

    #Adds digits to the possible_chars variable
    digits = input("Would you like to include numbers in your password Y/n: ")
    if digits.lower() in ['y', 'yes']:
        possible_chars += string.digits

    #Adds symbols to the posssible_chars variable
    symbol = input("Would you like to include Symbols in your password Y/n: ")
    if symbol.lower() in ['y', 'yes']:
        possible_chars += string.punctuation.replace(" ", "")

    #Adds letters to the possible_chars variable
    char = input("Would you like to include Letters in your password Y/n: ")
    if char.lower() in ['y', 'yes']:
        possible_chars += string.ascii_letters

    #Allows user to choose the length of the auto generated password
    length_choice = input("Would you like to use default password length (10char) Y/n: ")
    if length_choice.lower() in ['y', 'yes']:
        length = 10
    elif length_choice.lower() in ['n', 'no']:
        length = 0
        while True:
            try:
                length = int(input("Enter a number between 5-20: "))
                if length > 20 or length < 10:
                    print('Invalid Number, Try 5 - 20!\n')
                    continue
                return length
            except ValueError:
                print('Invalid Type, Use Number!\n')
    
    #Randomly joins all characters in the possible_chars variables at the specified length
    if len(possible_chars) > 0:
        return ''.join(random.choice(possible_chars) for _ in range(int(length)))
    else:
        return "No"
