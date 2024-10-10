# There is no Block Scope in Python!
# That means the variable is always global when created inside loops
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
