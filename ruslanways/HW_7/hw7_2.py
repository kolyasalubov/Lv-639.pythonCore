import re

while True:
    pattern = input("Enter password: ")

    result_1 = re.search("[a-z]", pattern)
    result_2 = re.search("[A-Z]", pattern)
    result_3 = re.search("\d", pattern)
    result_4 = re.search("\$|#|@", pattern)

    if 16>=len(pattern)>=6 and bool(result_1)==True and bool(result_2)==True and bool(result_3)==True and bool(result_4)==True:
        print("The password was successfully accepted!")
        break
    else:
        print(
            """
            Warning! 
            Your password must meets the temrs:
            at least 1 letter between [a-z] and 1 letter between [A-Z],
            at least 1 number between [0-9],
            at least 1 character from [$#@],
            minimum length 6 characters,
            maximum length 16 characters.
            Try again!
            """
            )
