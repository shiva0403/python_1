class Cust:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno

    def get_name(self):
        return self.name
    def get_phoneno(self):
        return self.phoneno
    def set_name(self, name):
        self.name = name


c = Cust("Krishna", "1234567890")
print(c.get_name())
print(c.get_phoneno())
print(c.set_name("John"))
print(c.get_name(

))