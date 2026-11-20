# 7. Diamond Pattern using Two Loops
# The top half grows from 1 star to rows stars.
# The bottom half shrinks back down, starting at rows - 1 so the widest row is not repeated.
# "* " * i repeats the star and space i times, and the spaces in front keep the shape centered.

# Code_Example:
rows = 5

for i in range(1, rows + 1):  # top half
    print(" " * (rows - i) + "* " * i)

for i in range(rows - 1, 0, -1):  # bottom half
    print(" " * (rows - i) + "* " * i)