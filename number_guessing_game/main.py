#Number Guessing Game Using Python
import random

def generate_number(level_choice):
    if level_choice == 1:
        target_number = random.randint(1, 10)
        return target_number, 1, 10
    
    elif level_choice == 2:
        target_number = random.randint(1, 50)
        return target_number, 1, 50
    
    elif level_choice == 3:
        target_number = random.randint(1, 100)
        return target_number, 1, 100
    elif level_choice == 4:
        while True: #Keep asking until a valid custom range is entered
            min_limit = validate_number("Please enter your minimum limit: ")
            max_limit = validate_number("Please enter your maximum limit: ")
            if min_limit >= max_limit: #Check if minimum value is less than maximum
                print(f"\nYou select {min_limit} and {max_limit}\nMinimum limit must be less than maximum limit.\n")
                continue 
            target_number = random.randint(min_limit, max_limit)
            return target_number, min_limit, max_limit
    else:
        print("invalid")
        
#Validates that the user's input is a number
def validate_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid number. Please provide a valid number.\n")

#global variables
total_score = []
high_score = 0

#To calculate and updates the score
def calculate_score(result):
    global high_score 
    total_score.append(result)
    if result > high_score:
        high_score = result #Updates high score globally if current score is higher
    print(f"\nYour Highest Score is {high_score}")
    print("ScoreBoard: ") #Displays all previous scores
    for i in total_score:
        print(i, end=" ")
        
#Main Function
def main():
    while True:
        game_instruction = """
    Welcome to the Number Guessing Game!

    I will pick a secret number, and your goal is to guess it before you run out of tries.

    How to play:
    - Choose your difficulty level (Easy, Medium, Hard, or Custom).
    - In Custom mode, you pick your own number range and number of guesses.
    - I will let you know if your guess is too high or too low.
    - Each wrong guess lowers your remaining attempts and your current score.
    - Your final score is the number of guesses you had left when you found the secret number!
    - If you run out of attempts, you will see the correct answer.
    - After each round, your score is shown on the scoreboard (including your all-time high score!).

    Choose your difficulty level:
        1. Easy   --> Guess a number from 1 to 10  (5 attempts)
        2. Medium --> Guess a number from 1 to 50  (6 attempts)
        3. Hard   --> Guess a number from 1 to 100 (7 attempts)
        4. Custom --> Choose your own range and attempts

    Good luck and have fun!
    """
        print(game_instruction)
        while True:
            level_choice = validate_number("Which level would you like to try? : ")
                
            if level_choice == 1:
                target_number, min_limit, max_limit = generate_number(1)
                attempt_left = 5
                print(f"\nYou selected the Easy Level!\nTry to guess the number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
                break
            elif level_choice == 2:
                target_number, min_limit, max_limit = generate_number(2)
                attempt_left = 6
                print(f"\nYou picked Medium Level!\nGuess a number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
                break
            elif level_choice == 3:
                target_number, min_limit, max_limit = generate_number(3)
                attempt_left = 7
                print(f"\nYou picked Hard Level!\nGuess a number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
                break
            elif level_choice == 4:
                target_number, min_limit, max_limit = generate_number(4)
                attempt_left = validate_number("How many guesses woulhigh_score = 0d you like?")
                print(f"\nYou picked Custom Level!\nGuess a number between {min_limit} and {max_limit}.\nYou have {attempt_left} tries. Good luck!\n")
                break
            else:
                print("\nOops, that's not a valid level. Please pick a number from 1 to 4.\n")
                continue
        
        count = 0
        score = attempt_left
    
        while attempt_left > 0:
            user_guess = validate_number("Enter Your Guess : ")     
            if user_guess < min_limit or user_guess > max_limit:
                print(f"\nThat guess is  out of range,\nPlease enter a number between {min_limit} and {max_limit}\n")
            else:
                count += 1
                if user_guess == target_number:
                    print(f"Congratulations! You guessed the number in {count} tries!")
                    
                    break
                elif user_guess > target_number:
                    print("Too high! Try a lower number.")
                else:
                    print("Too low! Try a higher number.")
    
                attempt_left -= 1 #Decrease the number of remaining attempts
                score -= 1  #Decrese score
                print(f"You have only {attempt_left} attempt left\n")

                if attempt_left <= 0:
                    print("Game over! You have used all your attempts.")
                    print(f"The correct number was {target_number}.\nBetter luck next time!\n")
                    
        calculate_score(score) #Calculate and display score after the game ends
        
        while True:  #Playagain
            play_again = input("\n\nDo you want to play again (y/n): ").lower()

            if play_again == "y" or play_again == "n":
                break
            else:
                print("Invalid option!!, Please choose an valid answer (y/n)")
                continue

        if play_again == "y":
            continue
        else:
            print("\nThanks For Playing!!\n\nGood Bye\n")
            print(f"You Final Scoreboard {total_score} and your highest score is {high_score}\n")
            break
                
if __name__ == "__main__":
    main()
