def rectarea ():
    """This function calculates the area of ​​a rectangle"""
    
    length = float(input("Enter the length: "))
    widht = float(input("Enter the widht: "))

    area = length * widht
    return area

def triangarea ():
    """This function calculates the area of ​​a triangle"""
    
    side_1 = float(input("Enter the first side of a triangle: "))
    side_2 = float(input("Enter the second side of a triangle: "))
    side_3 = float(input("Enter the third side of a triangle: "))

    s = (side_1 + side_2 + side_3) / 2
    area = (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5
    return area

def circarea ():
    """This function calculates the area of ​​a circle"""
    
    radius = float(input("Enter the radius of circle: "))

    p = 3.14
    area = p * (radius**2)
    return area

hello_message = """
********************************** Hello! **********************************
   This program can calculate the area of ​​a rectangle, triangle and circle.
   Make a choice what do you want to calculate by answer a question below!
****************************************************************************"""
fig_types = "********************** rectangle | triangle | circle ***********************"

print(hello_message)
print(fig_types)
answer = (input("\nWrite what type of figure you want to calculate: ")).lower()

while answer!="rectangle" and answer!="triangle" and answer!="circle":
    print(f'\nSorry, but i don\'t understand what is "{answer}"! Maybe you made a mistake while typing... Try again!')
    answer = (input("\nWrite what type of figure you want to calculate: ")).lower()

else:
    if answer=="rectangle":
        print("\nOk. You want to calculate the area of rectangle.\n")
        print(f"\nThe area of ​​a rectangle is: {rectarea()}")
    
    elif answer=="triangle":
        print("\nOk. You want to calculate the area of triangle.\n")
        print(f"\nThe area of ​​a triangle is: {triangarea()}")

    elif answer=="circle":
        print("\nOk. You want to calculate the area of circle.\n")
        print(f"\nThe area of ​​a circle is: {circarea()}")
        
input()
