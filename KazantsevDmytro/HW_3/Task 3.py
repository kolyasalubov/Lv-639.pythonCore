val_first = input('Please, enter your first value ')
val_second = input('Please, enter your second value ')
print('%f is your first entered value. \n%f is the second' 
    % (float(val_first), float(val_second)))
val_first, val_second = val_second, val_first
print('The values were exchanged. Now {1} is the first value, \
and {0} is the second one'.format (val_second, val_first))