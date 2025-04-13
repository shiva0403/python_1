class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.q + self.q * other.p, self.q * other.q)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.q - self.q * other.p, self.q * other.q)
        return NotImplemented
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.p * other.p, self.q * other.q)
        return NotImplemented
    def __str__(self):
        return f"{self.p}/{self.q}"

r = Rational(1, 2)
r2 = Rational(3, 4)
print(r + r2)  # Rational(10, 8)