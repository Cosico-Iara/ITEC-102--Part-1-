# 4. Counting Vowels in a Sentence
# A loop can be combined with an if statement to count only certain characters.
# .lower() converts the text to lowercase so uppercase vowels are also counted.
# The in keyword checks if a character is found inside "aeiou".

# Code_Example:
sentence = "Looping through strings is fun"
vowel_count = 0

for char in sentence.lower():
    if char in "aeiou":
        vowel_count += 1  # add 1 for every vowel found

print(f"The sentence has {vowel_count} vowels.")