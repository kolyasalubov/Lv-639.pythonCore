users_number = int(input('Please, enter your value: '))
fibonacci = [0, 1]
while fibonacci[-1] < users_number:
    if fibonacci[-1] + fibonacci[-2] > users_number:
      break
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print('Your fibonacci sequence is: {}'.format(fibonacci))