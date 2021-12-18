import re

while True:

    password = input('Please, insert your password: \n')

    condition_one = re.findall('[A-Z]', password)
    condition_two = re.findall('[a-z]', password)
    condition_three = re.findall('0-9', password)
    condition_four = re.findall('[$#@]', password)

    if 5 < len(password) <= 16:
        len(condition_one) > 0 and len(condition_two) > 0 and len(condition_three) > 0 and len(condition_four) > 0
        print("You\'ve entered a right password.")
        break

    else:
        print("Try again")
        