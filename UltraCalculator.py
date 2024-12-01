# Calculator Header
class Calculations:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    # First function which adds 2 values
    def add(self):                                          
        print(self.number1 + self.number2)

    def subtract(self):
        print(self.number1 - self.number2)

    def multiply(self):                                     
        print(self.number1 * self.number2)

    def divide(self):
        print(self.number1 / self.number2)            

    def menu(self):
        print('''Choose one of the options below:
[1]Addition
[2]Subtraction
[3]Multiplication
[4]Division''')

# Apply information to the variables in Calculations
x = Calculations(int(input('Number1: ')), int(input('Number2: ')))
x.menu()

user_choice = int(input('...'))

# Executes a function from the Calculations class to perform the operations
if user_choice == 1:
    x.add()
elif user_choice == 2:
    x.subtract()
elif user_choice == 3:
    x.multiply()
elif user_choice == 4:
    x.divide()
