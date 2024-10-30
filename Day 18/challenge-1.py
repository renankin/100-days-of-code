from turtle import Turtle, Screen

t = Turtle()
t.shape("classic")
t.color("blue")

# Draw a square with the turtle
for _ in range(4):
    t.right(90)
    t.forward(100)

# Close screen
screen = Screen()
screen.exitonclick()
