# Calculator Header
class Calculations:
    def __init__(self, num1, num2, format_style):
        self.number1 = num1
        self.number2 = num2
        self.formatting = format_style

    # First function which adds 2 values
    def add(self):
        total = self.number1 + self.number2
        formatted = format(total, ",").replace(",", ".")
        print(f'The result of adding {self.number1} + {self.number2} is: ', formatted)

    def subtract(self):
        total = self.number1 - self.number2
        formatted = format(total, ",").replace(",", ".")
        print(f'The result of subtracting {self.number1} - {self.number2} is: ', total)

    def multiply(self):
        total = self.number1 * self.number2
        formatted = format(total, ",").replace(",", ".")
        print(f'The result of multiplying {self.number1} x {self.number2} is: ', total)

    def divide(self):
        total = self.number1 / self.number2
        formatted = format(total, ",").replace(",", ".")
        print(f'The result of dividing {self.number1} ÷ {self.number2} is: ', total)

    def menu(self):
        print('''Choose one of the options below:
[1]Addition
[2]Subtraction
[3]Multiplication
[4]Division
[0]Exit''')

class Result(Calculations):
    def __init__(self, num1, num2, format_style, x):
        super().__init__(num1, num2, format_style)
        print("A")

    def execute(self):
        # Apply information to the variables in Calculations and display a menu to the user
        print('Below, enter two numbers that will be used next')
        x = Calculations(int(input('Number1: ')), int(input('Number2: ')), ",")
        x.menu()

        # This part collects the information about which operation will be executed below
        user_choice = int(input('...'))

        # Executes a function from the Calculations class to perform operations
        if user_choice == 1:
            x.add()
        elif user_choice == 2:
            x.subtract()
        elif user_choice == 3:
            x.multiply()
        elif user_choice == 4:
            x.divide()
        else:
            print(':)')
