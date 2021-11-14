def largest_num(argOne:int, argTwo:int):
    """
    name:         largest_num
    data type:    int    
    output:       biggest value out of two arguments
    """
    if argOne > argTwo:
        print('{} is bigger than {}'.format(argOne, argTwo))
    elif argOne < argTwo:
        print('{} is bigger than {}'.format(argTwo, argOne))
    else:
        print('Both {} and {} are equal'.format(argOne, argTwo))
    return print('Have a nice day!')

first_num = int(input('Please, enter your first number: '))
second_num = int(input('Please, enter your second number: '))
print(largest_num.__doc__)
large = largest_num(first_num, second_num)
