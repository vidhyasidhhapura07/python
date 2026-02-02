# # Write a number guessing game that generates a random number and asks the user to guess it.

import random

number = random.randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number :
        print("🎉 Correct! You guessed it.")
        print("The number was:", number)
        break 

    else:
        print("❌ Wrong guess. Try again.")
        print("The number was:", number)
        continue 
