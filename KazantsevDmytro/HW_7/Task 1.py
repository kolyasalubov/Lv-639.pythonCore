import script_for_figures

while True:

    print('Please, choose a figure in order to calculate the square!\
    \nWrite \'r\' for rectangle, \'t\' for triangle or \'c\' for circle!\
    \nIf you want to stop the execution, write down \'q\'.')
    users_choice = input('Your choice: \n')

    if users_choice.lower() == 'r':
        lenght = int(input('Please, enter length:\n'))
        width = int(input('Please, enter width: \n'))
        print(f'The square of your rectangle is {script_for_figures.rect_square(lenght, width)}.')

    elif users_choice.lower() == 't':
        height = int(input('Please, enter your triangle\'s height: \n'))
        base = int(input('Please, enter the base of your triangle: \n'))
        print(f'Your triangle\'s square is {script_for_figures.trian_square(height, base)}.')

    elif users_choice.lower() == 'c':
        rad = int(input('Please, enter your circle\'s radius: \n'))
        print(f'Your circle\'s square is {script_for_figures.circ_square(rad)}.')

    elif users_choice.lower() == 'q':
        print('Thank you for using my program!')
        break

    else:
        print('You\'ve entered a wrong input!')


    