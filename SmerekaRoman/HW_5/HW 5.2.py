login_user = input("Please input your login: ")
while login_user != "First": 
    print("Wrong user name")
    login_user = input("Please input another logn: ")
else:
    print("Hello First!")