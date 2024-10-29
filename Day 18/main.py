from turtle import Turtle, Screen
from random import random

t = Turtle()
t.shape("classic")

# Draw a square with the turtle
# for _ in range(4):
#     t.right(90)
#     t.forward(100)

# Draw a dashed line
# for _ in range(15):
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.forward(10)


def color_change():
    r = random()
    g = random()
    b = random()
    print(r)

    t.pencolor(r, g, b)


# Draw multiple sides
n_sides = 3
while n_sides <= 10:
    color_change()
    angle = 360 / n_sides
    for side in range(n_sides):
        t.forward(100)
        t.right(angle)
    n_sides += 1




# Close screen
screen = Screen()
screen.exitonclick()