import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO-1: Create a way of pulling up cards for the user and computer in
#  sequence while removing cards from the deck and storing the cards in a list.

# TODO-2: Asks the user if he wants to play again and iterate over the loop.

# TODO-3: check if the score is above 21 and if so, let the user know he lost.

# TODO-4: Calculate final scores if user don't want to play anymore.

# TODO-5: Asks if the user wants to play a game of Blackjack initially.

# TODO-6: Implement functions to simplify code.

play_blackjack = True

while play_blackjack:
    wants_to_play = input("Do you want to play a game of Blackjack: "
                          "Type 'y' or 'n': ")

    if wants_to_play == 'n':
        play_blackjack = False

    print(art.logo)

    user_hand = []
    computer_hand = []
    turn = 0
    keep_playing = True

    while keep_playing:
        # pull a card for user
        user_card = random.choice(cards)
        cards.remove(user_card)
        user_hand.append(user_card)

        # pull a card for computer
        computer_card = random.choice(cards)
        cards.remove(computer_card)
        computer_hand.append(computer_card)

        turn += 1

        if turn > 1:
            # calculate score
            user_score = sum(user_hand)
            computer_score = sum(computer_hand)

            print(f"Your cards: {user_hand}, current score: {user_score}\n"
                  f"Computer's first card: {computer_hand[0]}")

            # condition for going above 21
            if user_score > 21:
                print(f"Your final hand: {user_hand}, "
                      f"final score: {user_score}\n"
                      f"Computer's final hand: {computer_hand}, "
                      f"final score: {computer_score}\n"
                      "You went over. You lose \U0001F62D")

                keep_playing = False

            question = input("Type 'y' to get another card, type 'n' to pass: ")

            # condition for finding who wins
            if question == 'n':

                # complete computer's hand
                while computer_score < 21:
                    computer_card = random.choice(cards)
                    cards.remove(computer_card)
                    computer_hand.append(computer_card)
                    computer_score = sum(computer_hand)

                print(f"Your final hand: {user_hand}, "
                      f"final score: {user_score}\n"
                      f"Computer's final hand: {computer_hand}, "
                      f"final score: {computer_score}\n")

                if computer_score > user_score:
                    if computer_score > 21:
                        print("You win \U0001F601")
                    else:
                        print("You lose \U0001F624")
                elif computer_score == user_score:
                    print("You draw \U0001F643")
                else:
                    print("You win \U0001F601")

                keep_playing = False
