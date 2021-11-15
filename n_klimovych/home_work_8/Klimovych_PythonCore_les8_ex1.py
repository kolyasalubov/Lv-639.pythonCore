class Polygon:
    """This class calculates the polygon area"""
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def polarea(self):
        """This method calculates the polygon area"""
        from math import tan, pi
        area = self.sides * (self.length ** 2) / (4 * tan (pi / self.sides))
        print(f"The area of the polygon is: {area}")
        return area

class Rectangle(Polygon):
    """This class inherits from the Polygon class"""
    def __init__(self, sides, length):
        """This method calculates the rectangle area"""
        super().__init__(sides, length)

    def rectarea(self):
        """This method calculates the reactangle area"""
        area = self.length ** 2
        print(f"The area of the rectangle is: {area}")
        return area

area = Polygon(6, 13)
area.polarea()
area = Rectangle(4, 13)
area.rectarea()
