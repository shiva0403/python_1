import math

class Circle:
    def __init__(self, radius ):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(5)
print(int(c1.area()))
print(c1.perimeter())