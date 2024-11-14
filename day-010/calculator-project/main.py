import art


def add(n1, n2):
    return n1 + n2


# Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Add these 4 functions into a dictionary as the values. Keys = "+",
#  "-", "*", "/".
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    should_accumulate = True
    number_1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        number_2 = float(input("What is the next number: "))

        result = operations[operation_symbol](number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {result}")

        choice = input(f"Type 'y' to continue calculation with {result},"
                       f" or type 'n' to start a new calculation: ")

        if choice == "y":
            number_1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
