#Check number is devisible by 3 or not.

value=int(input("enter a value"))

def divide(value):
    if (value%3==0):
        print("yes, this is divisable by 3.")
    else:
     print("no, this is not divisable by 3.")

divide(value)