name = input('Please, enter your name! ')
values = int(input('Please, enter how much values you\'d like \
to contain in a list: '))
list_of_el = []
for x in range(1, values + 1):
    x = int(input('Enter your numbers: '))
    list_of_el.append(x)
print(f"Here's your list of integers: \n{list_of_el}")
changed_list = []
for float_number in list_of_el:
    list_of_el = float(float_number)
    changed_list.append(list_of_el)
print(f'The integers were converted to float: \n{changed_list}')
print(f'Thank you for using our program, {name}')