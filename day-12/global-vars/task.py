# Modifying Global Scope

enemies = 1
print(enemies)


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# A better way of doing this would be:
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
