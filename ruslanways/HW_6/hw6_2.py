def square_rectangle(a, b):
    return a*b

def square_triangle(a, h):
    return 0.5*a*h

def square_circle(r):
    return 3.14*r**2

answer = None
while answer != 'q':
    print("Please make a chiose what figure do you want to calculate?")
    answer = input("type 'r' if reclangle, 't' if triangle, 'c' if circle or type 'q' to exit: ")
    print('\n')
    if answer == 'r':
        a = float(input("please enter the lenght: "))
        b = float(input("please enter the width: "))
        print(f"the square of your rectanlge: {square_rectangle(a, b)}\n")
    elif answer == 't':
        a = float(input("please enter the base: "))
        h = float(input("please enter the heigh: "))
        print(f"the square of your triangle: {square_triangle(a, h)}\n")
    elif answer == 'c':
        r = float(input("please enter the radius: "))
        print(f"the square of your circle: {square_circle(r)}\n")
    else:
        print("please type only aforesaid symbols!\n")
