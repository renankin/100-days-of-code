import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# method 1
random_index = random.randint(0, 4)
print(friends[random_index])

# method 2
print(random.choice(friends))
