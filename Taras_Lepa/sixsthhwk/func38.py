def triangle_square(first_side,second_side):
    triangles_square = round(0.5 * first_side * second_side,2)
    return f"Square of your triangle is {triangles_square}"

def rectangle_square(first_side,second_side):
    rectangles_square = round(first_side * second_side,2)
    return f"Square of your rectangle is {rectangles_square}"

def round_square(radius):
    PI = 3.14
    rounds_square = round(PI*pow(radius,2),2)
    return f"Square of your round is {rounds_square}"



answers = input("Why fugures we will match? 1 - for triangle, 2 - for rectangle, 3 - for round. For exit, use any button")
if answers =="1":
    first_side= float(input("input first side "))
    second_side = float(input("input second side "))
    print(triangle_square(first_side,second_side))

elif answers =="2":
    first_side= float(input("input first side "))
    second_side = float(input("input second side "))
    print(rectangle_square(first_side,second_side))
elif answers =="3":
    radius= float(input("Input the radius"))
    print(round_square(radius))
else:
    print("Good day")
