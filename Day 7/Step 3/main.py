import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
matched_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Change the for loop so that you keep the previous
    #  correct letters in display.

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            matched_letters.append(letter)
        elif letter in matched_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You won.")
