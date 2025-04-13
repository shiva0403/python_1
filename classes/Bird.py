
class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        return f"{self.name} is flying!"