#Rectangle class


class Polygon:
    def __init__(self, match_size):
        self.match_size = match_size
        self.sides = [0 for i in range(match_size)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.match_size)]

    def dispSides(self):
        for i in range(self.match_size):
            print("Side",i+1,"is",self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)  

    def findArea(self):
        first_size, second_size = self.sides
        s = first_size * second_size
        print(f"The area of the rectangle is {round(s,2)}")

example = Rectangle()
example.inputSides()
example.dispSides()
example.findArea()