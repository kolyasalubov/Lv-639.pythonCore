import my_squares

choose = int(input('''Please thoose the figure: 
                        1 - rectangle
                        2 - triangle
                        3 - circle  
                        '''))

if choose == 1:
    a = int(input("Please input height (cm): "))
    b = int(input("Please input width (cm): "))
    print (f"Square of rectangle is: {my_squares.square_rectangle(a,b)} см²")

elif choose == 2:
        a = int(input("Please input basic side (cm): "))
        h = int(input("Please input height of triangle (cm): "))
        print (f"Square of rectangle is: {my_squares.square_triangle(a,h)} см²")
elif choose == 3:
        r = int(input("Please the radius of circle (cm): "))
        print (f"Square of rectangle is: {my_squares.square_circle(r)} см²")
else:
    print("Wrong input")