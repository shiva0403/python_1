from classes.Bird import Bird


class Duck(Bird):
    def __init__(self,color, name, species):
        super().__init__(name, species)
        self.color = color

    def quack(self):
        return "Quack!"

    def swim(self):
        return f"{self.name} is swimming!"

d = Duck( "yellow",'Daffy', 'Mallard')
print(d.quack())