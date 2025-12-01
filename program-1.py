class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operation"


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
op = input("Enter operation (add / subtract / multiply / divide): ")

calc = Calculator(a, b, op)
print("Result:", calc.calculate())
