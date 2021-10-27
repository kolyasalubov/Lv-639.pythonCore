users={'admin':['admin',999],'Andriy':['123456',3],'Oleg':['654321',8],'Olya':['09876',0]}
while (True):
    case=int(input('''Options:
        1. Register as a new user.
        2. Login to your account. 
        3. Exit
        Choose your option = '''))
    if case == 1:
        print("Your choose register.")
        login = input("Enter your login = ")
        if login in users == True:
            print("Error, this user has already registered. Choose another login or use form 'login'.")
            continue
        password = input("Enter your password = ")
        users.update({login:[password,0]})
        print("New user was registered.")
    elif case == 2:
        print("Your choose login.")
        login = input("Enter your login = ")
        password = input("Enter your password = ")
        if login in users and users[login][0] == password:
            if users[login][1] == 0:
                print(f"Congratulation. It`s your first login, {login}")
            elif users[login][1] > 0:
                users[login][1]+=1
                users.update({login: [password, users[login][1]]})
                print(f"You was logined. It`s your {users[login][1]} time.")
        elif login not in users:
            print("Error, this user hasn`t registered. Try again.")
            continue
        elif login in users and users[login][0] != password:
            print("Password is invalid or not correct. ")
            continue
    elif case == 3:
        print("EXIT")
        break
    else:
        print("We don`t have this options. Try aqain :(")