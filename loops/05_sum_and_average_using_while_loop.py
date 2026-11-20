# 5. Sum and Average using a While Loop
# while True creates a loop that keeps running until break is used.
# The loop asks for numbers and stops when the user types 0 (the sentinel value).
# break – Immediately exits the loop.
# Average = total / count, and :.2f rounds the result to 2 decimal places.

# Code_Example:
print("Enter numbers to add (type 0 to stop):")
running_total = 0
count = 0

while True:
    value = float(input("Number: "))
    if value == 0:  # sentinel value, stop the loop
        break
    running_total += value
    count += 1

if count > 0:  # avoids dividing by zero if nothing was entered
    print(f"Total   : {running_total}")
    print(f"Count   : {count}")
    print(f"Average : {running_total / count:.2f}")
else:
    print("No numbers were entered.")