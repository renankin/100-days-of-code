import random

WINNING_SEQUENCES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def display_board(pc_positions, player_positions):
    board = [" " for _ in range(1, 10)]

    for position in pc_positions:
        board[position - 1] = "X"

    for position in player_positions:
        board[position - 1] = "O"

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def find_winning_sequence(position_sequences):
    for winning_sequence in WINNING_SEQUENCES:
        matching_positions = []
        for position in position_sequences:
            if position in winning_sequence:
                matching_positions.append(position)

        if len(matching_positions) > 1:
            return winning_sequence


def find_winner(position_sequences):
    for winning_sequence in WINNING_SEQUENCES:
        if all(pos in position_sequences for pos in winning_sequence):
            return True

    return False


available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_positions = []
pc_positions = []

game_is_on = True

while game_is_on:

    # player move
    player_choice = int(input(f"Pick one number from {available_positions}: "))
    player_positions.append(player_choice)
    available_positions.remove(player_choice)
    print(f"Player plays {player_choice}")
    display_board(pc_positions, player_positions)

    # check if player won
    if find_winner(player_positions):
        print("Player wins")
        game_is_on = False
    # check if it's a draw
    elif not available_positions:
        print("It is a draw!")
        game_is_on = False
    else:
        # pc moves randomly
        pc_choice = random.choice(available_positions)

        # check if PC can win next time
        pc_winning_sequence = find_winning_sequence(pc_positions)
        if pc_winning_sequence:
            for position in available_positions:
                if position in pc_winning_sequence:
                    # pc tries to win
                    pc_choice = position

        # check if player will win next time
        player_winning_sequence = find_winning_sequence(player_positions)
        if player_winning_sequence:
            for position in available_positions:
                if position in player_winning_sequence:
                    # pc blocks
                    pc_choice = position

        pc_positions.append(pc_choice)
        available_positions.remove(pc_choice)

        print(f"PC plays {pc_choice}")
        display_board(pc_positions, player_positions)

        if find_winner(pc_positions):
            print("PC wins")
            game_is_on = False
