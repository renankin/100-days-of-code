import turtle as t
import random


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


def draw_spirograph(angle_shift):
    for _ in range(int(360 / angle_shift)):
        tim.color(color_change())
        tim.circle(100)
        tim.right(angle_shift)


# Draw a spirograph
tim = t.Turtle()
t.colormode(255)
tim.shape("classic")
tim.pensize(1)
tim.speed("fastest")

draw_spirograph(90)

# Close screen
screen = t.Screen()
screen.exitonclick()
