import turtle as t
import random


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)

    return new_color


# Generate a random walk
tim = t.Turtle()
t.colormode(255)
tim.shape("classic")
tim.pensize(10)
tim.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(color_change())
    tim.forward(20)
    tim.setheading(random.choice(directions))


# Close screen
screen = t.Screen()
screen.exitonclick()
