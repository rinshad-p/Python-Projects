#Number Guessing Game Using Python

import random 

print("Welcome to Number Guessing Game\nPlease choose a number between 1-10\n")
computer_guess = random.randint(1,10)
attempt_left = 5

count = 0
while attempt_left!=0:
    user_guess = int(input("Enter Your Guess : "))
    count +=1
    if user_guess > computer_guess:
        print("Too High, Try again!")
    elif user_guess < computer_guess:
        print("Too Low, Try again!")
    else:
        print(f"Congratulations! You Won in {count} attempts.")
        break
    attempt_left -=1
    print(f"You have only {attempt_left} attempts left!!!\n")
    if attempt_left <=0:
        print(f"Your attempts are over!\nThe correct number was {computer_guess}.\nYou lost, better luck next time!")
