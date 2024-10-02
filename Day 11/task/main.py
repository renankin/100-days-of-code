import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO-1: Create a way of pulling up cards for the user and computer in
#  sequence while removing cards from the deck and storing the cards in a list

# TODO-2: Asks the user if he wants to play again and iterate over the loop


user_hand = []
computer_hand = []
for turn in range(2):
    # pull a card for user
    user_card = random.choice(cards)
    cards.remove(user_card)
    user_hand.append(user_card)

    # pull a card for computer
    computer_card = random.choice(cards)
    cards.remove(computer_card)
    computer_hand.append(computer_card)

user_score = sum(user_hand)
computer_score = sum(computer_hand)

print(f"Your cards: {user_hand}, current score: {user_score}\n"
      f"Computer's first card: {computer_hand[0]}")
