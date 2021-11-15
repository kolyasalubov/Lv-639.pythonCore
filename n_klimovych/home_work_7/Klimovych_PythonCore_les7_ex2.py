import re

def validation():
    """ This function checks password for following this rules:
        - At least 1 letter between [a-z] and 1 letter between [A-Z].
        - At least 1 number between [0-9].
        - At least 1 character from [$#@].
        - Minimum length 6 characters.
        - Maximum length 16 characters. """

    while  True:
        password = input("Enter your password: ")
        special_symb = ['$','#','@']

        if len(password) < 6:
            print ("Minimum length is 6!")
            continue
        elif len(password) > 16:
            print("Maximum length is 16!")
        elif re.search ("[0-9]", password) is None:
            print("You need to add at least one number!")
        elif re.search ("[A-Z]", password) is None:
            print("You need to add at least one uppercase symbol!")
        elif not any(char in special_symb for char in password):
            print("You need to add at least one of this special symbols: '$', '#', '@'")
        else:
            print("Your password passed validation! Thank you!")
            break
    return password

validation()
