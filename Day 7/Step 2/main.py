import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a "placeholder" with the same number of blanks as the
#  chosen_word

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

# Create a "display" that puts the guess letter in the right
#  positions and _ in the rest of the string.

# Method 1 (more complicated)
# display = list(placeholder)
# for i, letter in enumerate(chosen_word):
#     if letter == guess:
#         display[i] = letter
#
# print(''.join(display))

# Method 2 (Simpler)
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
