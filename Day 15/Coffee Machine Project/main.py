MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# 1. Prompt user by Asking "What would you like?".

# 2. Turn off the Coffee Machine by entering "off" to the prompt.


# 3. Print report.
def output_resources():
    """Takes a dictionary of resources database and prints the available
    resources"""

    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffe: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


# Check resources sufficient?
def check_resources(coffee_choice):
    """Takes a dictionary of resources database and checks if there are
    available ingredients to make the coffee. Returns True if there are
    enough ingredients and false if not."""

    recipe = MENU[coffee_choice]["ingredients"]

    for ingredient in recipe:
        if resources[ingredient] < recipe[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


# 5. Process coins.
def process_coins():
    """ Returns the total number of money inserted in the machine"""

    print("Please insert coins")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (+ 0.25 * quarters
             + 0.10 * dimes
             + 0.05 * nickles
             + 0.01 * pennies)

    return total


# 6. Check transaction successful?
def check_funds(inserted_coins, coffee_choice):
    """Takes the inserted money and coffee choice and returns True if the
    money is enough and False if not."""

    coffee_cost = MENU[coffee_choice]["cost"]

    if inserted_coins >= coffee_cost:
        resources["money"] += coffee_cost
        if inserted_coins > coffee_cost:
            change = inserted_coins - coffee_cost
            print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# 7. Make coffee.
def make_coffee(coffee_choice):
    """Takes the coffee choice and deduct the value from the resources"""

    recipe = MENU[coffee_choice]["ingredients"]

    for ingredient in recipe:
        resources[ingredient] -= recipe[ingredient]

    print(f"Here is your {coffee_choice}. Enjoy!")


def coffee_machine():
    user_choice = ""

    while user_choice != "off":

        user_choice = input(
            "What would like? (espresso/latte/cappuccino) ").lower()

        if user_choice == "report":
            output_resources()
        elif user_choice == "off":
            return
        else:
            if check_resources(user_choice):
                user_coins = process_coins()
                if check_funds(user_coins, user_choice):
                    make_coffee(user_choice)


coffee_machine()
