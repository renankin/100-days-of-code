import random
import art

# 1: Create a way of pulling up cards for the user and computer in
#  sequence while removing cards from the deck and storing the cards in a list.

# 2: Asks the user if he wants to play again and iterate over the loop.

# 3: check if the score is above 21 and if so, let the user know he lost.

# 4: Calculate final scores if user don't want to play anymore.

# 5: Asks if the user wants to play a game of Blackjack initially.

# 6: Implement functions to simplify code.

# 7: Implement condition for using 11 if it is bust.


def draw_card(player_cards, n_cards, cards_available):

    for card in range(n_cards):
        card = random.choice(cards_available)
        cards_available.remove(card)
        player_cards.append(card)

    # substitute card if score above 21 and there is an ace
    player_score = sum(player_cards)
    if player_score > 21:
        for card in player_cards:
            if card == 11:
                player_cards.remove(card)
                player_cards.append(1)

    return player_cards, cards_available


def check_for_blackjack(user_cards, computer_cards):

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_score == 21 and computer_score == 21:
        display_results(user_cards, computer_cards)
        print("Both of you have a blackjack. You draw \U0001F643")
        play_blackjack()
    elif user_score == 21:
        display_results(user_cards, computer_cards)
        print("You have a blackjack. You win \U0001F601")
        play_blackjack()
    elif computer_score == 21:
        display_results(user_cards, computer_cards)
        print("Computer has a blackjack. You lose \U0001F62D")
        play_blackjack()


def find_winner(user_cards, computer_cards):

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_score <= 21 and computer_score <= 21:
        if user_score > computer_score:
            print("You have a higher score. You win \U0001F601")
        elif user_score == computer_score:
            print("You have the same score. You draw \U0001F643")
        else:
            print("You have a lower score. You lose \U0001F62D")
    else:
        if user_score > 21:
            print("You bust. You lose \U0001F62D")
        else:
            print("Computer bust. You win \U0001F601")


def display_results(user_cards, computer_cards):

    print(f"Your final hand: {user_cards},"
          f"final score: {sum(user_cards)}\n"
          f"Computer's final hand: {computer_cards}, "
          f"final score: {sum(computer_cards)}")


def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(20 * "\n" + art.logo)

    user_hand = []
    computer_hand = []
    # Draw 2 cards for pc and user
    draw_card(player_cards=user_hand, n_cards=2, cards_available=cards)
    draw_card(player_cards=computer_hand, n_cards=2, cards_available=cards)

    # Display score
    print(f"Your cards: {user_hand}, current score: {sum(user_hand)}\n"
          f"Computer's first card: {computer_hand[0]}")

    check_for_blackjack(user_hand, computer_hand)

    # Ask user if he wants new card
    keep_playing = True

    while keep_playing:
        wants_new_card = input("Type 'y' to get another card,"
                               "type 'n' to pass: ")

        if wants_new_card == "y":
            draw_card(user_hand, 1, cards)
            print(f"Your cards: {user_hand}, current score: {sum(user_hand)}\n"
                  f"Computer's first card: {computer_hand[0]}")

            if sum(user_hand) > 21:
                keep_playing = False

        else:
            while sum(computer_hand) < 17:
                draw_card(computer_hand, 1, cards)
            keep_playing = False

    display_results(user_hand, computer_hand)
    find_winner(user_hand, computer_hand)
    play_blackjack()


def play_blackjack():

    wants_to_play = input("Do you want to play a game of Blackjack: "
                          "Type 'y' or 'n': ")

    if wants_to_play == "y":
        blackjack()


play_blackjack()
