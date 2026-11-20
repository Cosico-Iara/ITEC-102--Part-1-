# 8. Number Guessing Game
# Combines many loop concepts in one program.
# import random – Lets the program use the random module.
# random.randint(1, max_number) – Picks a random whole number, including both ends.
# while attempts < max_attempts – Repeats until the player runs out of attempts.
# str.isdigit() – Checks if the input contains only digits, used for input validation.
# continue – Skips an invalid input, so it does not use up an attempt.
# return True – Ends the function as soon as the player guesses correctly.
# The outer while True loop lets the player play again, and break stops it when the answer is not "y".

# Code_Example:
import random


def play_round(max_number=100, max_attempts=7):
    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess_text = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ")

        # Input validation
        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue  # invalid input does not use an attempt

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempt(s).")
            return True

    print(f"Out of attempts. The number was {secret}.")
    return False


wins = 0
rounds = 0

while True:
    rounds += 1
    if play_round():
        wins += 1

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

print(f"\nThanks for playing! You won {wins} of {rounds} round(s).")