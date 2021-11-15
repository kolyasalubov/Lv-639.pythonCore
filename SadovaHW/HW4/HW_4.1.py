factorial_number = int(input("Enter the number: "))
factorial = 1
for i in range(1, factorial_number+1):
    factorial *= i
print(factorial)