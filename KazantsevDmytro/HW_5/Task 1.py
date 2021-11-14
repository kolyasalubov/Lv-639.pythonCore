# list comprehension
even_num = [even_values for even_values in range(1, 11) if even_values % 2 == 0]
odd_num = [odd_values for odd_values in range(1, 11) if odd_values % 3 == 0]
other_odd = [other_odd for other_odd in range(1, 11) if other_odd % 2 != 0 and other_odd % 3 != 0]
print(f'The list of even numbers from 1 to 10 is {even_num}')
print(f'The list of odd numbers that can be divided by 3 is {odd_num}')
print(f'The list of odd numbers that are not divided by 3 is {other_odd}')

# typical solution
list_of_even = []
list_of_odd = []
list_of_other = []
for value in range(1, 11):
    if value % 2 != 0 and value % 3 != 0:
        list_of_other.append(value)
    elif value % 3 == 0:
        list_of_odd.append(value)
    else:
        list_of_even.append(value)
print(f'The list of even numbers is {list_of_even}')
print(f'The list of odd numbers is {list_of_odd}')
print(f'The list of odd numbers not divided by 2 and \
3 is {list_of_other}')
