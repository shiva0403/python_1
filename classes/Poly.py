class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Cat Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print(f"{self.name} says Meow!")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Dog Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print(f"{self.name} says Woof!")

def my_pet(pet):
    pet.info()
    pet.make_sound()

c = Cat("Whiskers", 3)
c.info()
d = Dog("Buddy", 5)
d.info()

my_pet(c)
my_pet(d)