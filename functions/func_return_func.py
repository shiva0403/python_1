# Function returning function

def outer():
    def display():
        print("Hello World")
    return display

d = outer()
d()