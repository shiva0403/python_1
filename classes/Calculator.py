class Calculator:
    def __init__(self):
        pass
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

print(Calculator.add(1, 2))