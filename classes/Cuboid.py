
class Cuboid:
    def __init__(self, length: float, width: float, height: float):
        print(id(self))
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height

    def surface_area(self) -> float:
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

c = Cuboid(1, 2, 3)
print(c.volume())
print(id(c))
c2 = Cuboid(2, 3, 4)
print(c2.volume())