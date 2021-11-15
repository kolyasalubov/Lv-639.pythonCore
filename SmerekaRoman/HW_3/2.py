number = int(input("Enter the number:"))


reversed_number = str(number)
print("Reversed number is:", reversed_number[::-1])

print("Sorted number is:", sorted(str(number)))

prod=1
while number>0:
    digit = number%10
    prod *= digit
    number //= 10
print("The product of all numbers", prod)