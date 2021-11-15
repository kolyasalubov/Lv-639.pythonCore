even_numbers = []
odd_numbers = []
other_numbers = []

for n in range(1,11):
    if n%2 == 0:
        even_numbers.append(n)
    elif n%3 == 0:
        odd_numbers.append(n)
    else:
        other_numbers.append(n)

print("The even numbers in range 1-10 are: ",even_numbers)
print("The odd numbers in range 1-10 are: ", odd_numbers)
print("The other numbers in range 1-10 are: ", other_numbers)

