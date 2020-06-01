class Calculator():
    PI = 3.14159265

    def __init__(self):
        self.operation_log = []

    def add(self, num1, num2):
        result = num1 + num2
        self.operation_log.append(f'{num1} added to {num2} result: {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.operation_log.append(f'{num1} multiplied by {num2} result: {result}')
        return result

    def print_operations(self):
        print(self.operation_log)

    @staticmethod
    def compute_circle_area(r):
        return Calculator.PI * r ** 2


if __name__ == '__main__':
    c = Calculator()
    print(c.add(2, 2))
    print(c.add(213, 2))
    print(c.multiply(2, 123))
    print(c.multiply(2, 2))
    print(c.add(123, 2))
    print(c.add(2, 2))
    print(c.add(2, 2))
    print(c.multiply(2, 3))
    print(c.compute_circle_area(10))
