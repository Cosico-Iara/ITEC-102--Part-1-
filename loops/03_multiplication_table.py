# 3. Multiplication Table using a For Loop
# A for loop with range(1, 11) repeats the multiplication 10 times.
# input() reads what the user types, and int() converts it to a whole number.
# f-strings (f"...") put variable values directly inside the text.
# {i:>2} and {number * i:>3} right-align the values so the columns line up.

# Code_Example:
number = int(input("Enter a number for its multiplication table: "))

print(f"\nMultiplication table of {number}")
print("-" * 25)  # prints a line of 25 dashes
for i in range(1, 11):
    print(f"{number} x {i:>2} = {number * i:>3}")