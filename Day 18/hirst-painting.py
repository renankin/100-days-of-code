import colorgram
import turtle as t
import random

# Extract color from image
colors = colorgram.extract("image.jpg", 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if abs(r - g) >= 10:
        rgb_colors.append((r, g, b))


def draw_points(size):
    for row in range(size):
        for column in range(size):
            start_shift = -250
            jump = 50
            x = start_shift + (jump * column)
            y = start_shift + (jump * row)
            tim.teleport(x, y)
            tim.dot(20, random.choice(rgb_colors))


# Create dot pattern
tim = t.Turtle()
t.colormode(255)
tim.shape("classic")
tim.speed("fastest")
tim.hideturtle()
draw_points(10)

# Close screen
screen = t.Screen()
screen.exitonclick()