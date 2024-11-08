from turtle import Screen
import time
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
loops = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loops % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move()

        # Detect collision with car
        if player.distance(car) < 15:
            game_is_on = False

    # Detect if player reached

    loops += 1

screen.exitonclick()
