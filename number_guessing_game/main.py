# Number Guessing Game Using Python
import random

def generate_number():
    while True:
        number_choice = input(
            "Would you like to set your own number range? (y/n) : ").strip().lower()
        if number_choice == "y":
            while True:
                min_limit = validate_number("Please enter your minimum limit: ")
                max_limit = validate_number("Please enter your maximum limit: ")

                if min_limit >= max_limit:
                    print(f"\nYou select {min_limit} and {max_limit}\nMinimum limit must be less than maximum limit.\n")
                    continue
                target_number = random.randint(min_limit, max_limit)
                return target_number, min_limit, max_limit

        elif number_choice == "n":
            print("Using the default range (1-10)")
            target_number = random.randint(1, 10)
            return target_number, 1, 10

        else:
            print("Invalid Option! Please choose (y/n)\n")


def validate_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid number. Please provide a valid number.")


def generate_limit():
    while True:
        limit_choice = input(
            "\nWould you like to set your own guess limit? (y/n): ").strip().lower()
        if limit_choice == "y":
            # attempt = int(input("How many guesses would you like? : "))
            attempt = validate_number("How many guesses would you like?")
            return attempt

        elif limit_choice == "n":
            print("Using the default attempt limit (5)")
            return 5
        else:
            print("Invalid Choice!!\nPlease Choose a correct option.")


def main():
    instructions = """
Welcome to the Number Guessing Game!

*** HOW TO PLAY ***

1. At the start, you can choose your own number range or use the default (1-10).
2. Next, you can set how many guesses (attempts) you'd like, or use the default (5).
3. Try to guess the secret number within your selected range.
4. After each guess, you'll be told if your guess was too high or too low.
5. If you guess the number within your allowed attempts, you win!
6. If you run out of guesses, the game will reveal the secret number.

Good luck and have fun!
"""

    print(instructions)
    target_number, min_limit, max_limit = generate_number()
    attempt_left = generate_limit()
    count = 0
    print(
        f"\nGuess a number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
    while attempt_left > 0:
        user_guess = validate_number("Enter Your Guess : ")
        count += 1
        if user_guess == target_number:
            print(f"Congratulations! You guessed the number in {count} tries!")
            break
        elif user_guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print("Too low! Try a higher number.")
        attempt_left -= 1
        print(f"You have only {attempt_left} attempt left\n")

        if attempt_left <= 0:
            print("Your Attempts are OVER!!!")
            print(
                f"Sorry, you didn't guess the number. It was {target_number}.")


if __name__ == "__main__":
    main()
