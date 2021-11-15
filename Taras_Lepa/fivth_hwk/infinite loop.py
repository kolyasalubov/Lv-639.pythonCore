#Infinite loop password




password = input("Please input your login: ")
while password != "First": 
    print ("Incorrect password.Check your CAPS LOCK button and try again")
    password = input("You can try again: ")
else:
    print("Hello First!")