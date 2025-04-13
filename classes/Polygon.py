class Polygon:
    def __init__(self, no_of_sides, *sides):
        self.no_of_sides = no_of_sides
        self.sides = sides[:no_of_sides]

import math
class Triangle(Polygon):

    def __init__(self,  *sides):
        Polygon.__init__(self, 3, *sides)

    def area(self ):
        a,b,c = self.sides
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

t1 = Triangle(3, 4,  5, 7)
print(t1.area())