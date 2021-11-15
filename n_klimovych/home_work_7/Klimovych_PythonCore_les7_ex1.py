import square

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
    square.sqrerror()
    answer = (input("\nWrite what type of figure you want to calculate: ")).lower()
else:
    if answer=="rectangle":
        print("\nOk. You want to calculate the area of rectangle.\n")
        print(f"\nThe area of ​​a rectangle is: {square.rectsqr()}")
    
    elif answer=="triangle":
        print("\nOk. You want to calculate the area of triangle.\n")
        print(f"\nThe area of ​​a triangle is: {square.triangsqr()}")

    elif answer=="circle":
        print("\nOk. You want to calculate the area of circle.\n")
        print(f"\nThe area of ​​a circle is: {square.circsqr()}")
