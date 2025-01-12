
def closure():
    msg = "Hello"
    def display():
        print("*" * 11)
        print(msg)
        print("*" * 11)
    return display

d = closure()
d()