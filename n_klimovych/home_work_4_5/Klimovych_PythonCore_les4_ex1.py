hello_message = "******** Hello! I can calculate factorial of any number! Let's try! ********"

print(hello_message)
number = int(input("\nEnter a number: "))

factorial = 1
if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")
input()
