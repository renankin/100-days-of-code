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


# 4. Check resources sufficient?
def check_resources(order_ingredients):
    """Takes a dictionary of resources database and checks if there are
    available ingredients to make the coffee. Returns True if there are
    enough ingredients and false if not."""

    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


# 5. Process coins.
def process_coins():
    """ Returns the total number of money inserted in the machine"""

    print("Please insert coins")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


# 6. Check transaction successful?
def check_funds(money_received, coffee_cost):
    """Takes the inserted money and coffee choice and returns True if the
    money is enough and False if not."""

    if money_received >= coffee_cost:
        if money_received > coffee_cost:
            change = money_received - coffee_cost
            print(f"Here is ${change:.2f} in change.")
        resources["money"] += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# 7. Make coffee.
def make_coffee(coffee_choice, order_ingredients):
    """Takes the coffee choice and order ingredients and deduct the value from
    the
    resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {coffee_choice} ☕. Enjoy!")


def coffee_machine():

    user_choice = input(
        "What would like? (espresso/latte/cappuccino) ").lower()

    if user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffe: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
        coffee_machine()
    elif user_choice == "off":
        return
    else:
        coffee_ingredients = MENU[user_choice]["ingredients"]
        if check_resources(coffee_ingredients):
            payment = process_coins()
            coffe_cost = MENU[user_choice]["cost"]
            if check_funds(payment, coffe_cost):
                make_coffee(user_choice, coffee_ingredients)
        coffee_machine()


coffee_machine()
