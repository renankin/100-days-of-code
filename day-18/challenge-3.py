from turtle import Turtle, Screen
from random import random


def color_change():
    r = random()
    g = random()
    b = random()

    t.pencolor(r, g, b)


def draw_shape(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        t.forward(100)
        t.right(angle)
    n_sides += 1


# Drawing different shapes
t = Turtle()
t.shape("classic")

for side in range(3, 11):
    color_change()
    draw_shape(side)


# Close screen
screen = Screen()
screen.exitonclick()