class Polygon:
    """Initialisation polygon"""
    def __init__(self,  numberSides, sides=[0 for i in range(4)]):
        self.numberSides=numberSides
        self.sides=sides
    def input_sides(self):
        self.sides=[float(input(f"Enter {i+1} side = ")) for i in range(self.numberSides)]
    def display_sides(self):
        for i in range(self.numberSides):
            print(f"Side {i+1} is {self.sides[i]}")

class Rectangle(Polygon):
    """Initialisation rectangle"""
    def __init__(self):
        Polygon.__init__(self,2)

    def find_square(self):
        a,b = self.sides[0], self.sides[1]
        print(f"Square of rectangle is {2*a*b}")

rectangle_1=Rectangle()
rectangle_1.input_sides()
rectangle_1.display_sides()
rectangle_1.find_square()
