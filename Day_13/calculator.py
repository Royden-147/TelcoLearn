# SIMPLE CALCULATOR

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    result = num1 + num2    
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        result = "Error! Division by zero."            
    else:
        result = num1 // num2
else:
    result = "Invalid operation!"

print("Result:", result)