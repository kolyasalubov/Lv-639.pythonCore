import base

answers = input("Why fugures we will match? 1 - for triangle, 2 - for rectangle, 3 - for round. For exit, use any button ")
if answers =="1":
    height= float(input("input height "))
    side = float(input("input side "))
    print(base.triangle_area(height,side))

elif answers =="2":
    first_side= float(input("input first side "))
    second_side = float(input("input second side "))
    print(base.rectangle_square(first_side,second_side))
elif answers =="3":
    radius= float(input("Input the radius"))
    print(base.round_square(radius))
else:
    print("Good day")


if __name__ == "__main__":
    answers