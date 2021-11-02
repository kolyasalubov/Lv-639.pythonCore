from math import pi
squareRectangle = lambda length,width: 2*(length+width)
squareTriangle = lambda height,base: 0.5*(height*base)
squareCircle = lambda radius: pi*radius**2
case=int(input("1. Rectangle. \n2. Triangle. \n3. Circle. \nChoose your figure = "))
if case == 1:
    length=int(input("Enter length = "))
    width = int(input("Enter width = "))
    print(f"Square of rectangle is {squareRectangle(length,width)}")
elif case == 2:
    heigth = int(input("Enter heigth = "))
    base = int(input("Enter base = "))
    print(f"Square of triangle is {squareTriangle(heigth, base)}")
elif case == 3:
    radius = int(input("Enter radius = "))
    print(f"Square of circle is {squareCircle(radius)}")