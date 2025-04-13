
def Driver(car):
    car.drive()

class Honda:
    def drive(self):
        print("Honda is driving")

class Toyota:
    def drive(self):
        print("Toyota is driving")

h = Honda()
Driver(h)
t = Toyota()
Driver(t)