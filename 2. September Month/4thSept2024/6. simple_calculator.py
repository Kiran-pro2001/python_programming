# Simple Calculator 
# Write a Python program that asks the user to input two numbers and an arithmetic operation (+, -, *, /). Use if-else statements to perform the operation and print the result.


num1 = int(input("Enter a number 1 :")) # 5
num2 = int(input("Enter a number 2 :"))  # 5
operation = input("Enter an operation (+,-,*,/)") # '+' -- +

if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
else:
    print(num1/num2)  # True Division - Always return quotient in float value.