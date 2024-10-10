from random import randint

from PIL.ImImagePlugin import number

import art

# global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, correct_answer, attempts_left):
    """Compares the guess value against the answer and returns the number
    of attempts left"""

    if user_guess > correct_answer:
        print("Too high.")
        return attempts_left - 1
    elif user_guess < correct_answer:
        print("Too low.")
        return attempts_left - 1
    else:
        print(f"You got it! The answer was {correct_answer}")


def choose_difficulty():
    """Lets user select level and returns the total attempts"""

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    # print(f"Psst, the correct answer is {number_to_guess}")
    turns = choose_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the "
              f"number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

# 1: Select a random number between 1 and 100 and assign to a variable

# 2: Create a variable to allow user input a guess number

# 3: Compare the guessed number with the answer and tell if it is
#  too low or too high

# 4: Create another variable to count the number of guesses.

# 5: If the guess is wrong, discount the total number of guesses.

# 6: Create a while loop that has total number of guesses, and will
#  stop when total guesses is 0.

# 7: Select if he wants to play easy or hard.

# 8: Create functions to make the program more modular.
