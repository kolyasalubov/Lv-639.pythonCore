hello_message = """
********************************** Hello! **********************************
I am a program that can do cool stuf with large integer numbers. So you can 
enter your phone number or any other and I will do a magic. Don't worry!
I'll keep it a secret! But remember: ignore '0'. It has no magic!
****************************************************************************"""

print(hello_message)
input_number = input("Enter your mega secret magic number: ")

# task 1: Find the product of the digits of entered number
digit = int(input_number)
product = 1

while(digit != 0):
    product = product * (digit % 10)
    digit = int(digit / 10)
print(f"\nProduct of all digits in '{input_number}': {product}")
print(input("Want some more? Press any key"))

# task 2: Write the number in reverse order
print(f"Let's try to read it backwards: {input_number[::-1]}\nLooks cool, huh?!")
print(input("A little more magic? Press any key"))

# task 3: Sort the digits included in entered number
print(f"Now you will see the real magic!!! (joke)\nLet's sort your number:\n{sorted(input_number)}")
print("\n**********************************_THANKS_**********************************")
input()
