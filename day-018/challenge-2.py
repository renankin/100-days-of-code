from turtle import Turtle, Screen

t = Turtle()
t.shape("classic")
t.color("blue")

# Draw a dashed line
for _ in range(15):
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)

# Close screen
screen = Screen()
screen.exitonclick()
