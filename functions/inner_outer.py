# Nested function

def Outer() :
    def Inner() :
        print("Inner function")
    Inner()

Outer()