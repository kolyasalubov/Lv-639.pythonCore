print('C L A S S I C   S O L U T I O N')
range_of_numbers = []
div_by_2 = []
div_by_3 = []
other_numbers = []
for i in range(1,11):
    range_of_numbers.append(i)
    if i%2 == 0:
        div_by_2.append(i)
    elif i%3 == 0:
        div_by_3.append(i)
    else:
        other_numbers.append(i)
print('The range of numbers is: ', range_of_numbers)
print('')
print('The even numbers that are divisible by 2: ',div_by_2)
print('The odd numbers, which are divisible by 3: ', div_by_3)
print('The numbers, that are not divisible by 2 and 3: ', other_numbers)
print('')
print('')
print('L I S T   C O M P R E H E N S I O N')
range_of_numbers = [i for i in range (1, 11)]
div_by_2 = [i for i in range (1, 11) if i % 2 == 0 ]
div_by_3 = [i for i in range (1, 11) if i % 2 == 1 and i % 3 == 0]
other_numbers = [i for i in range (1, 11) if i % 2 == 1 and i % 3 == 1]
print('The range of numbers is: ', range_of_numbers)
print('')
print('The even numbers that are divisible by 2: ',div_by_2)
print('The odd numbers, which are divisible by 3: ', div_by_3)
print('The numbers, that are not divisible by 2 and 3: ', other_numbers)