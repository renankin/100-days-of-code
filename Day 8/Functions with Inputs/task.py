# Function without input
def greet():
    print(f"Hey!")
    print("How are you doing?")
    print("Do you have any news?")


# Function with input -> name is the parameter
def greet_with_name(name):
    print(f"Hey {name}!")
    print(f"How are you doing {name}?")
    print("Do you have any news?")


greet()
greet_with_name("Angela")  # Angela is the argument
