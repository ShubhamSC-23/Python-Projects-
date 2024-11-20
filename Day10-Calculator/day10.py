"""
 _____________________
|  _________________  |
| | CALULATOR       | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""




def add(num1, num2):
    """Adds two numbers together (num1 and num2)"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts num2 from num1"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies num1 by num2"""
    return num1 * num2


def divide(num1, num2):
    """Divides num1 by num2"""
    return num1 / num2


calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    first_number = float(input("What is your first number?\n"))

    print("List of operations you can perform:\n")
    for operation in calculator_operations:
        print(operation)

    operation = input("What operation would you like to perform?\n")

    second_number = float(input("What is your second number?\n"))

    result = calculator_operations[operation](first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")

    continue_calculator = input(
        f"Continue using calculator with current result ({result})? Type 'y' to continue, 'n' "
        f"to start a new calculator, or 'exit' to quit the program: \n")

    while continue_calculator == 'y':
        new_first_number = result
        for operation in calculator_operations:
            print(operation)
        operation = input("What operation would you like to perform?\n")
        new_second_number = float(input("What is your second number?\n"))
        result = calculator_operations[operation](new_first_number, new_second_number)
        print(f"{new_first_number} {operation} {new_second_number} = {result}")
        continue_calculator = input(
            f"Continue using calculator with current result ({result})? Type 'y' to continue, "
            f"'n' to start a new calculator, or 'exit' to quit the program: \n")

    if continue_calculator == 'n':
        calculator()

    if continue_calculator == 'exit':
        print("Exiting program. See you!")

calculator()