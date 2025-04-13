
class Rectangle:
    count = 0
    def __init__(self, l, b):
        self.l = l
        self.b = b
        Rectangle.count += 1

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

    @classmethod
    def countRect(cls):
        print(cls.count)

    @staticmethod
    def isSquare(l,b):
        return l == b

r = Rectangle(30,23)
print(r.area())
print(r.isSquare(30,23))
print(dir(r))
r1 = Rectangle(10,20)
print(r.isSquare(30,23))
r1.countRect()
Rectangle.countRect()