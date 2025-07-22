#Number Guessing Game Using Python
import random

def generate_number():
    number_choice = input("Would you like to set your own number range? (y/n) : ").strip().lower()

    if number_choice == "y":
        min_limit = int(input("Please enter your minimum limit : "))
        max_limit = int(input("Please enter your maximum limit : "))
        target_number = random.randint(min_limit, max_limit)
        return target_number, min_limit, max_limit
    elif number_choice == "n":
        print("Using the default range (1-10)")
        target_number = random.randint(1, 10)
        return target_number, 1, 10
    else:
        print("Invalid Choice!!\nPlease Choose a correct option!!")
        return generate_number()

def generate_limit():
    limit_choice = input("\nWould you like to set your own guess limit? (y/n) : ").strip().lower()

    if limit_choice == "y":
        attempt = int(input("How many guesses would you like? : "))
        return attempt
    elif limit_choice == "n":
        print("Using the default attempt limit (5)")
        attempt = 5
        return attempt
    else:
        print("Invalid Choice!!\nPlease Choose a correct option!!")
        return generate_limit()


def main():
    print("Welcome to the Number Guessing Game.\n")
    target_number, min_limit, max_limit = generate_number()
    attempt_left = generate_limit()
    count = 0
    print(f"\nGuess a number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
    while attempt_left > 0:
        user_guess = int(input("Enter Your Guess : "))
        count +=1
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
            print(f"Sorry, you didn't guess the number. It was {target_number}.")


if __name__ == "__main__":
    main()
