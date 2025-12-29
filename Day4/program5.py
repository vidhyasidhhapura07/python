#  check no is odd or even

number = int(input("enter any number : "))

def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

odd_even(number)