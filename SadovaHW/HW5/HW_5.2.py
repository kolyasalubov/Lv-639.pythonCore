login="First"
user_login=input("Enter your login ")
while user_login == login:
    print("Your authentication is successful, congrats!")
    break
if user_login != login:
    print("Your login an incorrect,sorry")