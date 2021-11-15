import math

def circsqr():
    """This function calculates the area of ​​a circle"""
    
    radius = float(input("Enter the radius of circle: "))
    circarea = (math.pi) * (math.pow(radius, 2))
    return circarea

def rectsqr():
    """This function calculates the area of ​​a rectangle"""

    length = float(input("Enter the length: "))
    widht = float(input("Enter the widht: "))
    reactarea = length * widht
    return reactarea

def triangsqr():
    """This function calculates the area of ​​a triangle"""

    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    triangarea = 0.5 * base * height
    return triangarea

def sqrerror():
    """This function returns input error"""

    error = print("\nInput error! Try again!")
    return error
