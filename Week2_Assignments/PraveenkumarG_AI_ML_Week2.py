# Task 1: Python Basics & Operators

# 1. Create a Python script that accepts two numbers from the user. 
# 2. Perform all basic arithmetic operations (add, subtract, multiply, divide, modulus, power). 
# 3. Demonstrate use of comparison and logical operators (>, <, ==, !=, and, or, not). 
# 4. Print results clearly using formatted output (f-strings). 
# Taking user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
print("\n--- Arithmetic Operations ---")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")
print(f"Power: {num1 ** num2}")

# Comparison & logical operators
print("\n--- Comparison & Logical Operators ---")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")

print("Logical AND:", (num1 > 0) and (num2 > 0))
print("Logical OR:", (num1 > 0) or (num2 > 0))
print("Logical NOT:", not(num1 < 0))


