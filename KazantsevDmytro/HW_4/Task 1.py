number = int(input('Please, enter your value in order \
to calculate the factorial: '))
if number == 0:
    print(f'The factorial for {number} is always 1.')
elif number > 0:
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    print('The factorial for {1} is {0}.'.format
    (factorial, number))
else:
    print('We can\'t calculate the factorial of your number.')
print('Have a nice day!')