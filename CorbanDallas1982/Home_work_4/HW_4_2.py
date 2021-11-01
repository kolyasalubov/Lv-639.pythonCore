list_of_integer_types=[1,2,3,4,5,6,7,8,9,10]
print('Initial list (integer types):\n', list_of_integer_types)
print('')
for i in range(len(list_of_integer_types)):
    list_of_integer_types[i]=float(list_of_integer_types[i])
print('Chganged list (float types):\n', list_of_integer_types)