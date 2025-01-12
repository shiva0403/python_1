# Function as parameter

def display():
    print("Hello World")

def fun(d):
    d()

fun(display)

def add(x,y):
    print(x + y)

def sub(x,y):
    print( x - y)

def fun(f,x,y):
    f(x,y)

fun(add, 10, 20)
fun(sub, 10, 20)