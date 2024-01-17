def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_input():
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

def calculator():
    print("Simple Calculator App with Data Validation Checks")
    
    while True:
        try:
            num1 = get_number_input("Enter the first number: ")
            num2 = get_number_input("Enter the second number: ")
            operation = get_operation_input()

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}")

        user_choice = input("Do you want to perform another calculation? (yes/no): ")
        if user_choice.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
