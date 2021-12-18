class Polygon:

    def __init__(self, no_of_sides):
        self.no = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter {i+1} side = ")) for i in range(self.no)]

    def disp_sides(self):
            for i in range(self.no):
                print("Side",i+1,"is",self.sides[i])
    
class Rectangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 2)

    def find_square(self):
        side_one, side_two = self.sides
        square = side_one * side_two
        print('The rectangle\'s square is {}'.format(round(square, 2)))

rectangle_test = Rectangle()
rectangle_test.input_sides()
rectangle_test.disp_sides()
rectangle_test.find_square()



