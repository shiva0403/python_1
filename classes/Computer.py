class Computer:
    def __init__(self, name, cpu, os):
        self.name = name
        self.cpu = self.CPU(cpu)
        self.os = self.OS(os)

    def __str__(self):
        return f"Computer Name: {self.name}, CPU: {self.cpu}, OS: {self.os}"

    class CPU:
        def __init__(self, brand):
            self.brand = brand

        def __str__(self):
            return f"CPU Brand: {self.brand}"

        def get_brand(self):
            return self.brand

    class OS:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"OS name: {self.name}"


c1 = Computer("Dell", "Intel", "Windows")

print(c1)