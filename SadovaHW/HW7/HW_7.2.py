import re

user_msg = input("Please enter password: ")

request_1 = re.findall("[A-Z]", user_msg)
request_2 = re.findall("[a-z]", user_msg)
request_3 = re.findall("[\d]", user_msg)
request_4 = re.findall("[$#@]", user_msg)

while True:
    if 6 <= len(user_msg) <= 16:
        len(request_1) > 0 and len(request_2) > 0 and len(request_3) > 0 and len(request_4) > 0
        print("Password is correct")
        break
    else:
        print("Password incorrect")
        break