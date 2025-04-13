class Arith:
    def sum(self , x,y,z=None):
        a = x + y
        if(z is not None):
            a += z
        return a
    # def sum(self, x, y, z):
    #     return x + y + z

a = Arith()
print(a.sum(1,2))
print(a.sum(1.3,3.4))
print(a.sum('hello', 'world'))
print(a.sum(1,2,3))