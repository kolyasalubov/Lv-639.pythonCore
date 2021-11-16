from math import pi
PI=3.14

figure = input("1-rectangle, 2-triangle, 3-circle: ")
if figure == "1":
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    print("Square= {}".format(a*b))
elif figure =="2":
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    print("Square= {}".format(0.5*a*h))
elif figure =="3":
    r= float(input("Input radius: "))
    print("Square= {}".format(PI*r**2))
else:
    print("Input error")