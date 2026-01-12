# Write a program that handles invalid input by using try and except blocks.

a = str(input("enter any name: "))

if not type(a) is int:
    raise TypeError("only enter integers value")
    

