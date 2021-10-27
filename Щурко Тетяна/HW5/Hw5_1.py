even_numbers = [i for i in range(11) if i % 2 == 0]
odd_numbers = [i for i in range(11) if i % 3 == 0]
numbers_not_divide_two_tree = [i for i in range(11) if i % 2 == 1 and i % 3 == 1]
print(f"All even numbers in range [0,10] are {even_numbers}")
print(f"All odd numbers in range [0,10] are {odd_numbers}")
print(f"All numbers that don`t divide to 2 and 3 in range [0,10] are {numbers_not_divide_two_tree}")