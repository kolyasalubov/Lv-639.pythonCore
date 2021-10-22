integer_list = [7, 4, 16, 1, 32, 8, 11, 264, 15]

print(f"Integer list:\n{integer_list}")
print("\nType of these elements became floating:")

for number in integer_list:
    number = float(number)
    print(number)
input()