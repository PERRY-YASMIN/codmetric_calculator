# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

print("Welcome to Codmetric Calculator!")
print("Operations: +  -  *  /")
print("Type 'exit' to quit.\n")

while True:
    try:
        num1 = input("Enter first number (or type 'exit'): ")
        if num1.lower() == "exit":
            print("Thank you for using Codmetric Calculator!")
            break
        num1 = float(num1)

        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator! Please choose +, -, *, /")
            continue

        print(f"Result: {num1} {operator} {num2} = {result:.2f}\n")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")
    except ZeroDivisionError as e:
        print(f"❌ Error: {e}\n")
