number_1=1234
number_str=str(number_1)
multiply_numbers=1
for i in range(len(number_str)):
        multiply_numbers*=int(number_str[i])
print(f"Multiply numbers is {multiply_numbers}")
print(f"Reverse numbers is {number_str[::-1]}")
print(f"Sorted numbers is {sorted(number_str)}")