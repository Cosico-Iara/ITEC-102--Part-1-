# 2. While Loop
# Used to repeat a block of code as long as a condition is True.
# The condition is checked before every repeat.
# The counter must be updated inside the loop, or it will run forever (infinite loop).

# Code_Example:
count = 10  # starting value

while count > 0:  # condition is checked before every repeat
    print(count)
    count -= 1  # update the counter, or the loop never ends!

print("Liftoff!")