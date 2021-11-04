import Hw7_1_1
case=int(input("1. Rectangle. \n2. Triangle. \n3. Circle. \nChoose your figure = "))
if case == 1:
    length=int(input("Enter length = "))
    width = int(input("Enter width = "))
    print(f"Square of rectangle is {Hw7_1_1.squareRectangle(length,width)}")
elif case == 2:
    heigth = int(input("Enter heigth = "))
    base = int(input("Enter base = "))
    print(f"Square of triangle is {Hw7_1_1.squareTriangle(heigth, base)}")
elif case == 3:
    radius = int(input("Enter radius = "))
    print(f"Square of circle is {Hw7_1_1.squareCircle(radius)}")