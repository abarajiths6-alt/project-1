def calculator():
    """A simple calculator that performs basic arithmetic operations."""
    print("=== Simple Calculator ===")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)\n")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ").strip()
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print(f"Error: '{operation}' is not a valid operation.")
        return

    print(f"\nResult: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    calculator()