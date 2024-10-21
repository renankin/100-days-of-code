from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffee_machine():

    choice = input(f"What would like {menu.get_items()}? ")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        return
    else:
        drink = menu.find_drink(choice)  # returns menu item object
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    run_coffee_machine()


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
run_coffee_machine()
