class Angle:
    def __init__(self, degrees: float = 0.0):
        self.degrees = degrees

    def __str__(self):
        return f"{self.degrees} degrees"

    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.degrees + other.degrees)
        return NotImplemented
a1 = Angle(30)
a2 = Angle(45)
a3 = a1 + a2
print(a3)  # Output: 75 degrees
a4 = a3.__add__(a3)
print(a4)
