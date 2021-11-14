required_log = 'First'
login = input('Please, enter your login: ')
while required_log == login:
    print(f'You may start your work, {login}')
    break
if login != 'First':
    print('You\'ve entered a wrong login. \
    \nPlease, try again!')
