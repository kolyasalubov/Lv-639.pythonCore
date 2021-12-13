import math


def triangle_area(height,side):
    area = round(0.5*height*side,2)
    message = f"Area yours triangle = {area}"
    return message

def rectangle_square(first_side,second_side):
    area = round(first_side * second_side,2)
    message = f"Area of your rectangle = {area}"
    return message

def round_square(radius):
    area = round(math.pi * math.pow(radius,2)*2,2)
    message = f"Area yours round = {area}"
    return message
