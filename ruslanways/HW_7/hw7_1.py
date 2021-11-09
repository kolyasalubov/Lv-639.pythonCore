import figure_squares

while True:
    print("Please make a chiose what figure do you want to calculate?")
    answer = input("type 'r' if reclangle, 't' if triangle, 'c' if circle or type 'q' to exit: ")
    print('\n')
    if answer == 'r':
        a = float(input("please enter the lenght: "))
        b = float(input("please enter the width: "))
        print(f"the square of your rectanlge: {figure_squares.square_rectangle(a, b)}\n")
    elif answer == 't':
        a = float(input("please enter the base: "))
        h = float(input("please enter the heigh: "))
        print(f"the square of your triangle: {figure_squares.square_triangle(a, h)}\n")
    elif answer == 'c':
        r = float(input("please enter the radius: "))
        print(f"the square of your circle: {figure_squares.square_circle(r)}\n")
    elif answer == 'q':
        break
    else:
        print("please type only aforesaid symbols!\n")
