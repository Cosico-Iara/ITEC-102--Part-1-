# 6. break and continue Together with for-else
# continue – Skips an empty input and goes to the next attempt.
# break – Stops the loop once the correct password is entered.
# else on a loop – Runs only if the loop finished WITHOUT a break.
# Here, the else block means all attempts were used and the password was never correct.

# Code_Example:
correct_password = "python123"

print("Password check (3 attempts):")
for attempt in range(1, 4):
    guess = input(f"Attempt {attempt}: ")
    if guess == "":
        print("Empty input, try again.")
        continue
    if guess == correct_password:
        print("Access granted!")
        break
    print("Wrong password.")
else:
    # runs only if the loop finished WITHOUT a break
    print("Too many failed attempts. Locked out.")