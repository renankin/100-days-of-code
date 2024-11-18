def add(*args):
    sum_result = 0
    for n in args:
        sum_result += n
    return sum_result
    # return result_sum(args)


my_function = add(2, 3, 4, 5, 6)
print(my_function)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # Use get method to try to get the value
        # in case it doesn't exist
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
