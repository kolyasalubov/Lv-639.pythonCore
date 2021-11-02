def square_rectangle(a = int, b = int):
    return a*b

def square_triangle(a,h):
    return a*h / 2

def square_circle(r):
    PI = 3.14
    return r**2 * PI

menu = int(input('''Choose the figure: 
                        1. Rectangle
                        2. Triangle
                        3. Circle
                        '''))
if menu == 1:
    a = int(input("Please input height (cm): "))
    b = int(input("Please input width (cm): "))
    print (f"Square of rectangle is: {square_rectangle(a,b)} см²")
elif menu == 2:
        a = int(input("Please input basic side (cm): "))
        h = int(input("Please input height of triangle (cm): "))
        print (f"Square of rectangle is: {square_triangle(a,h)} см²")
elif menu == 3:
        r = int(input("Please the radius of circle (cm): "))
        print (f"Square of rectangle is: {square_circle(r)} см²")
else:
    print("Wrong input")
    