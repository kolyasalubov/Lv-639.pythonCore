import re

pattern = input("Please insert password: ")

result_1 = re.findall("[A-Z]", pattern)
result_2 = re.findall("[a-z]", pattern)
result_3 = re.findall("[\d]", pattern)
result_4 = re.findall("[$#@]", pattern)

while True:
    if 5 < len(pattern) <= 16:
        len(result_1) > 0 and len(result_2) > 0 and len(result_3) > 0 and len(result_4) > 0
        print("Correct")
        break
    else:
        print("Try again")