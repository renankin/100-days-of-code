import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 por Paper or "
                        "2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

# Find out if user wins
if user_choice == 0 and computer_choice == 2:
    print(f"You chose:\n {game_images[user_choice]}\n"
          f" Computer chose:\n {game_images[computer_choice]}\n You won!")
elif user_choice == 1 and computer_choice == 0:
    print(f"You chose:\n {game_images[user_choice]}\n"
          f" Computer chose:\n {game_images[computer_choice]}\n You won!")
elif user_choice == 2 and computer_choice == 1:
    print(f"You chose:\n {game_images[user_choice]}\n"
          f" Computer chose:\n {game_images[computer_choice]}\n You won!")
elif user_choice == computer_choice:
    print(f"You chose:\n {game_images[user_choice]}\n"
          f" Computer chose:\n {game_images[computer_choice]}\n It's a draw!")
elif user_choice >= 3 or user_choice < 0:
    print("You typed a wrong number. You lose!")
else:
    print(f"You chose:\n {game_images[user_choice]}\n"
          f" Computer chose:\n {game_images[computer_choice]}\n You lose!")
