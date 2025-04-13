
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age


p = Person("shiva", 42)
print(p.getName())
p.setName("krishna")
print(p.getName())