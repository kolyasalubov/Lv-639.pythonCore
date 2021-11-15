def choice():
    print('Figure 1: a rectangle\
        \nFigure 2: a circle\
        \nFigure 3: a triangle')
    return int(input('Please, enter the number of the chosen figure: '))

def rectange_sqr(num1:float, num2:float):
    return num1 * num2

def triangle_sqr(num1:float, num2:float, num3:float):
    per = (num1 + num2 + num3) / 2
    return (per * (per - num1) * (per - num2) * (per-num3))**(0.5)

def circle_sqr(num1:float):
    PI = 3.14
    return PI * num1

users_decision = choice()

while 3 < users_decision <= 0:
    users_decision = choice()
else:

    if users_decision == 1:
        rect_length = float(input('Please, enter the length of your rectangle: '))
        rect_width = float(input('Please, enter the width of your rectangle: '))
        print('{} is the square of your rectangle.'\
        .format(rectange_sqr(rect_length, rect_width)))

    elif users_decision == 2:
        radius = float(input('Please, enter your circle\'s radius: '))
        circle = circle_sqr(radius)
        print('{} is the square of your circle'\
        .format(circle_sqr(radius)))

    else:
        cat_one = float(input('Please, enter your first cathetus: '))
        cat_two = float(input('Please, enter your second cathetus: '))
        hyp = float(input('Please, enter your hypotenuse: '))
        print('{} is the square of your triangle.'\
        .format(triangle_sqr(cat_one, cat_two, hyp)))