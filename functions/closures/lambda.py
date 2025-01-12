
def miles2km(miles):
    return 1.60934 * miles

k = lambda miles: 1.60934 * miles

print(miles2km(10)) # 16.0934
print(k(10)) # 16.0934


#********************************

def add(x,y):
    return x + y

a = lambda x,y: x + y

print(add(1,2)) # 3
print(a(22,4))