print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# work out how much they need to pay based on their size choice.
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("You typed a wrong input.")

# work out how much to add to their based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

# work out their final amount based on whether they want extra cheese.
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
