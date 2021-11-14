import re
def validation(value):
    if len(value) >= 6 and len(value) <= 16:
        condition_1 = "[a-z]+"
        condition_2 = "[A-Z]+"
        condition_3 = "[0-9]+"
        condition_4= "[!@#$%^&*]+"
        if len(re.findall(condition_1,value)) > 0 and len(re.findall(condition_2,value)) > 0 \
                and len(re.findall(condition_3,value)) > 0 and len(re.findall(condition_4,value)) > 0:
            print("Congratulations!!! Password is valid.")
        else:
            print("Password is invalid")
    else:
        print("Password is invalid")

password=input("Enter your password = ")
validation(password)
