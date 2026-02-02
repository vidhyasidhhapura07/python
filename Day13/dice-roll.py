# Use the random module to simulate a dice roll.

import random

while True:
    n = input("choose any one true or false: ")

    if n == "true":
        print(random.randint(1,6))
    elif n == "false":
        print("Game is died")
    else:
        print("Invalid Input...! please enter true or false")