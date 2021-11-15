def bigger ():
    """This function returns the largest number of two numbers
    that are entered by user."""
    
    arg1 = int(input("Enter your first number: "))
    arg2 = int(input("Enter your second number: "))

    if arg1 < arg2:
        arg = f"\n{arg2} is larger than {arg1}"
    elif arg1 > arg2:
        arg = f"\n{arg1} is larger than {arg2}"
    return arg

hello_message = """
********************************** Hello! **********************************
 This program returns the largest number of two numbers that you will enter
****************************************************************************"""

print(hello_message)
print(f"{bigger()}")

input()
