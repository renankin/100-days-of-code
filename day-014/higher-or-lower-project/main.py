# Higher or Lower Game:

# Import game data and random module.
from game_data import data
import random
from art import logo, vs


def get_account():
    """Return a random account"""

    # From game data, get a random dictionary entry and assign to variable
    # and remove data.
    account = random.choice(data)
    data.remove(account)

    return account


def format_data(account):
    """Takes the account data and returns the printable format"""

    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def compare_followers(first_account, second_account):
    """Check which account has the largest followers and return "A" or "B"
    as answer depending on which account"""

    # Use a print statement to return the information from dictionary.
    print(f"Compare A: {format_data(first_account)}")
    print(vs)
    print(f"Against B: {format_data(second_account)}")

    if first_account["follower_count"] > second_account["follower_count"]:
        return "A"
    else:
        return "B"


def game():

    print(logo)

    # Get accounts
    account_a = get_account()
    account_b = get_account()

    answer = ""
    guess = ""
    score = 0
    while not guess != answer:
        # Compare number of followers and save answer.
        answer = compare_followers(account_a, account_b)

        # Ask the user to make a guess and compare the user's answer to the
        # final answer.
        guess = input("Who has more followers? Type 'A' or 'B' ").upper()

        # if user's right, add score, overwrite first variable with the
        # second one, and keep playing. If user's wrong, display final score
        # and end game.
        if guess == answer:
            score += 1
            print("\n" * 20 + logo)
            print(f"You're right! Current score: {score}")
            account_a = account_b
            account_b = get_account()
        else:
            print("\n" * 20 + logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return


game()
