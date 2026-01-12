# Write a program to handle invalid user input

try:
    num = int(input("enter a value: "))
    print("you entered : ",num)
except ValueError:
    print("Invalid input! Please enter a valid integer value.")

