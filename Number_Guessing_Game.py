#Number Guessing Game Using Python

import random 

print("Welcome to number Guessing Game\nPlease choose a number between 1 -10\n")
computer_guess = random.randint(1,10)

while True:
    user_guess = int(input("Enter Your Guess : "))

    if user_guess > computer_guess:
        print("Too High, Try again!")
    elif user_guess < computer_guess:
        print("Too Low, Try again!")
    else:
        print("Congratulations! You Won.")
        break