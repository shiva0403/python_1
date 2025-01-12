# passing function as parameter
# nested function calling parameter function

def decorator(fun):
    def wrapper():
        print("*"* 11)
        fun()
        print("*"* 11)
    return wrapper

@decorator
def display():
    print("Hello World")
# when annotated we do not need below line
#d = decorator(display)

display()