print("Hello! Please answer a few questions:")
user_name = input("What is your name? ")
user_age = input("How old are you? ")
user_city = input("Where do you live? ")

print(f"""\nHello, {user_name.title()}!
Your age is {user_age},
You live in {user_city.title()}.""")
input()
