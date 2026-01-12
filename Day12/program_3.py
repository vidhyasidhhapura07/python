# Create a program that divides two numbers and handles division by zero.

num1 = int(input("enter a number1: "))
num2 = int(input("enter a number2: "))

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print ("you can't division by zero")
    

