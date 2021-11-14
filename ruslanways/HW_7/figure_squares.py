from math import pow, pi

def square_rectangle(a, b):
    return a*b

def square_triangle(a, h):
    return 0.5*a*h

def square_circle(r):
    return round(pi*pow(r, 2), 2)
