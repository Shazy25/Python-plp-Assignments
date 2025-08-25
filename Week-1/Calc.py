# Basic Calculator Program

# Ask the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Perform the operation and print the result
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
    
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2!= 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")

