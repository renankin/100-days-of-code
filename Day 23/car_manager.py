from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.goto((280, randint(-250, 250)))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
