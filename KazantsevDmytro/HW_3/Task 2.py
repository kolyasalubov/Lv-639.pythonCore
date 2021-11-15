number = 2279
number_str = str(number)
list_of_el = sorted(number_str)
print(f'The reversed number is {number_str[::-1]}.\
    \nThe sorted elements are {list_of_el}')
sum_of_el = int(list_of_el[0]) + int(list_of_el[1]) +\
    int(list_of_el[2]) + int(list_of_el[3])
print('The sum of elements is {}'.format(sum_of_el))
