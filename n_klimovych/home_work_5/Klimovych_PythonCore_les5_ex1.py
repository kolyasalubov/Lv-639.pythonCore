hello_message = """
********************************** Hello! **********************************
 This small programm will sort all numbers in range you'll enter for:
  • Even numbers that are divisible by 2;
  • Odd numbers, which are divisible by 3;
  • Numbers that are not divisible by 2 and 3.
****************************************************************************
"""
print(hello_message)
user_range = int(input("Enter a random range of numbers you want to sort: "))

even_num = []
odd_num = []
other_num =[]

for num in range (1, user_range + 1):
    if num % 2 == 0:
        even_num.append(num)
    elif num % 3 == 0:
        odd_num.append(num)
    else:
        other_num.append(num)

################################# List comprehension ###################################

# even_num = [num for num in range (1, user_range + 1) if num % 2 == 0]
# odd_num = [num for num in range (1, user_range + 1) if num % 3 == 0 and num % 2 == 1]
# other_num = [num for num in range (1, user_range + 1) if num % 2 != 0 and num  % 3 != 0]

########################################################################################
print(f"""
In a range from 1 to {user_range}:
\nEven numbers that are divisible by 2:\n{even_num}
\nOdd numbers, which are divisible by 3:\n{odd_num}
\nNumbers that are not divisible by 2 and 3:\n{other_num}""")

print("\n********************************** Thanks! *********************************")
input()
